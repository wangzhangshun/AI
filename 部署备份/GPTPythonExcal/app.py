from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import tempfile
import time
from deepseek_python import RailwayPlanParser

app = Flask(__name__)


@app.route('/parse', methods=['POST'])
def parse_excel():
    if 'file' not in request.files:
        return jsonify({"error": "未找到文件"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "文件名为空"}), 400

    filename = secure_filename(file.filename)
    if not filename.endswith('.xlsx'):
        return jsonify({"error": "只支持 .xlsx 文件"}), 400

    model = request.form.get('model', 'deepseek-r1:7b')
    ollama_url = request.form.get('ollama', 'http://localhost:11434')
    api_key = request.form.get('api_key', None)

    tmp_path = None
    try:
        # 创建临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
            file.save(tmp.name)
            tmp_path = tmp.name

        # 确保文件写入完成
        time.sleep(0.5)

        # 初始化解析器
        parser = RailwayPlanParser(ollama_url=ollama_url, model=model, api_key=api_key)

        # 解析文件
        result = parser.parse(tmp_path)

        return jsonify({"status": "success", "result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # 确保文件被关闭后删除
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except Exception as e:
                print(f"删除临时文件失败: {str(e)}")
                # 尝试重试删除
                time.sleep(1)
                try:
                    os.unlink(tmp_path)
                except:
                    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)