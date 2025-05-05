from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import tempfile
import time
import logging
import gc
import sys
import uuid
from deepseek_python import RailwayPlanParser

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制上传文件大小为16MB


def safe_delete(file_path, is_dir=False):
    """安全删除文件或目录"""
    max_retries = 5
    for attempt in range(max_retries):
        try:
            if is_dir:
                if len(os.listdir(file_path)) == 0:
                    os.rmdir(file_path)
            else:
                if sys.platform == 'win32':
                    # Windows特殊处理
                    import ctypes
                    GENERIC_READ = 0x80000000
                    GENERIC_WRITE = 0x40000000
                    OPEN_EXISTING = 3
                    FILE_SHARE_DELETE = 0x00000004
                    handle = ctypes.windll.kernel32.CreateFileW(
                        str(file_path), GENERIC_READ | GENERIC_WRITE,
                        FILE_SHARE_DELETE, None, OPEN_EXISTING, 0, None)
                    if handle != -1:
                        ctypes.windll.kernel32.CloseHandle(handle)
                os.unlink(file_path)
            logger.debug("成功删除: %s", file_path)
            return True
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(0.5 * (attempt + 1))
                continue
            logger.warning("删除失败(最终尝试): %s - %s", file_path, str(e))
            return False


@app.route('/parse', methods=['POST'])
def parse_excel():
    start_time = time.time()
    logger.info("开始处理文件解析请求")

    if 'file' not in request.files:
        logger.error("未找到文件")
        return jsonify({"error": "未找到文件"}), 400

    file = request.files['file']
    if file.filename == '':
        logger.error("文件名为空")
        return jsonify({"error": "文件名为空"}), 400

    filename = secure_filename(file.filename)
    if not filename.endswith('.xlsx'):
        logger.error("不支持的文件类型: %s", filename)
        return jsonify({"error": "只支持 .xlsx 文件"}), 400

    # 使用本地Ollama服务和deepseek-r1:7b模型
    model = request.form.get('model', 'deepseek-r1:7b')
    ollama_url = request.form.get('ollama', 'http://localhost:11434')
    api_key = request.form.get('api_key', '')

    tmp_dir = None
    tmp_path = None
    parser = None

    try:
        # 创建临时目录和文件（使用UUID防止冲突）
        tmp_dir = tempfile.mkdtemp(prefix=f"railway_parser_{uuid.uuid4().hex}_")
        tmp_path = os.path.join(tmp_dir, f"upload_{uuid.uuid4().hex}.xlsx")
        file.save(tmp_path)

        # 验证文件
        if not os.path.exists(tmp_path) or os.path.getsize(tmp_path) == 0:
            raise ValueError("文件保存失败或为空")

        logger.info("文件保存成功，大小: %s bytes", os.path.getsize(tmp_path))

        # 初始化解析器
        parser = RailwayPlanParser(ollama_url=ollama_url, model=model, api_key=api_key)
        logger.info("解析器初始化完成，开始解析文件")

        # 解析文件
        try:
            result = parser.parse(tmp_path)
            logger.info("文件解析成功，共解析 %d 条记录", len(result))

            process_time = time.time() - start_time
            logger.info("总处理时间: %.2f 秒", process_time)

            return jsonify({
                "status": "success",
                "result": result,
                "process_time": f"{process_time:.2f}秒"
            })

        except Exception as e:
            logger.error("解析过程中出错: %s", str(e))
            return jsonify({"error": str(e)}), 500

    except Exception as e:
        logger.error("处理请求时出错: %s", str(e))
        return jsonify({"error": str(e)}), 500

    finally:
        # 强制释放资源
        if parser:
            del parser
        gc.collect()

        # 清理临时文件
        if tmp_path and os.path.exists(tmp_path):
            if not safe_delete(tmp_path):
                logger.error("无法删除临时文件: %s", tmp_path)

        if tmp_dir and os.path.exists(tmp_dir):
            if not safe_delete(tmp_dir, is_dir=True):
                logger.error("无法删除临时目录: %s", tmp_dir)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)