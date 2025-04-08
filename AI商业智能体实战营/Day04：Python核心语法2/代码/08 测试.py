import re


def extract_url(text):
    # 正则表达式匹配 URL
    url_pattern = r'(https?://[^\s]+)'
    match = re.search(url_pattern, text)
    return match.group(0) if match else None


# 示例文本
text = "清脂无负担，百年老字号科学护航 https://v.douyin.com/4Qu3qOS0Hcw/ 复制此链接，打开【抖音短视频】，直接观看视频！"

# 提取 URL
url = extract_url(text)
print(url)
