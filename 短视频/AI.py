import pandas as pd
import os
import zipfile

def excel_to_srt_zip(input_excel, output_dir="output_srt", columns=None, seconds_per_line=5):
    """
    将 Excel 文案生成 SRT 字幕，并打包 ZIP
    :param input_excel: Excel 文件
    :param output_dir: 输出目录
    :param columns: 合并列名列表
    :param seconds_per_line: 每条字幕显示时长
    """
    df = pd.read_excel(input_excel)
    if columns is None:
        columns = ["文案内容"]

    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Excel里没有 {col} 列")

    os.makedirs(output_dir, exist_ok=True)
    srt_files = []

    for idx, row in df.iterrows():
        parts = [str(row[col]).strip() for col in columns if pd.notna(row[col])]
        if not parts:
            continue
        full_text = " ".join(parts)

        # 时间控制
        start_sec = 0
        end_sec = seconds_per_line
        srt_content = f"1\n00:00:00,000 --> 00:00:{seconds_per_line:02},000\n{full_text}\n"

        filename = os.path.join(output_dir, f"{idx+1}.srt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(srt_content)
        srt_files.append(filename)
        print(f"✅ 已生成 {filename}")

    # 打包 zip
    zip_filename = f"{output_dir}.zip"
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in srt_files:
            zipf.write(file, os.path.basename(file))

    print(f"\n🎉 所有 SRT 已生成并打包为 {zip_filename}")

# 使用示例
if __name__ == "__main__":
    excel_to_srt_zip("文案.xlsx", columns=["开头钩子","文案内容","结尾"])
