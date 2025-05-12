from fastmcp import FastMCP
import os
import httpx
from datetime import datetime
import json
from dotenv import load_dotenv
from typing import Dict,Any

# 初始化 MCP 服务器
mcp = FastMCP("AssistantServer")

# 加载环境变量
"""
load_dotenv() 是一个来自 python-dotenv 库的函数，用于加载环境变量。具体来说，它的作用包括
读取 .env 文件: 将位于项目根目录下的 .env 文件中的环境变量读取到程序中。这些环境变量通常用于存储敏感信息，如 API 密钥、数据库连接字符串等。
"""
load_dotenv()


@mcp.tool()
async def search_news(wd: str) -> str:
    """
    描述：根据关键词搜索新闻数据
    参数:
        wd (str): 关键词
    返回:
        str: 字符串，包含查询json字符在内
    """

    try:
        API_KEY = os.getenv("NEWS_API_KEY")
        if not API_KEY:
            return "NEWS_API_KEY需要配置"
        # (1) 异步爬虫请求，爬取新闻
        # 设置请求参数并发送请求
        url = f"https://newsapi.org/v2/everything"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params={
                "q": wd,
                "from": "2025-05-10",
                "sortBy": "publishedAt",
                "apiKey": API_KEY
            })
            data = response.json()
        # (2) 处理数据
        news = [
            {
                "title": item.get("title"),
                "description": item.get("description"),
                "url": item.get("url")
            } for item in data["articles"][:15] if item.get("description")
        ]

        # 将新闻结果以带有时间戳命名后的 JSON 格式文件的形式保存在本地指定的路径
        output_dir = "./search_news"
        os.makedirs(output_dir, exist_ok=True)
        filename = f"news_{wd}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        file_path = os.path.join(output_dir, filename)

        with open(file_path, "w") as f:
            json.dump(news, f, ensure_ascii=False, indent=4)

        return json.dumps(news, ensure_ascii=False)

    except Exception as e:
        return "search news error:" + str(e)


WEATHER_TOKEN = "SI876Lq1AhSR70Unn"


async def make_nws_request(url: str, params: dict | None = None) -> Dict[str, Any] | None:
    """
    发起http请求，获取响应数据
    """
    async with httpx.AsyncClient() as client:
        headers: dict = {
            "User-Agent": "weather-app/1.0",
            "Accept": "application/geo+json",
        }
        try:
            response: httpx.Response = await client.get(url, params=params or {}, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print(f"HTTP请求失败: {e}")
            return None

@mcp.tool()
async def search_forecast(city: str) -> str:
    """Get weather forecast for pinyin of the city.

    Args:
        city: pinyin of the city
    """
    api_url = f"https://api.seniverse.com/v3/weather/daily.json"
    api_params = {
        "key": WEATHER_TOKEN,
        "location": city,
        "language": "zh-Hans",
        "unit": "c",
        "start": 0,
        "days": 5
    }
    response_data = await make_nws_request(api_url, api_params)

    if not response_data:
        return "Unable to fetch detailed forecast data for pinyin of the city."

    location = response_data["results"][0]["location"]
    daily = response_data["results"][0]["daily"]
    forecasts = []
    for period in daily:
        forecast = f"""
{location['name']}:
日期: {period['date']}
白天: {period['text_day']}
夜间: {period['text_night']}
温度: {period['low']}° ~ {period['high']}°
风力: {period['wind_direction']}{period['wind_scale']}级 {period['wind_speed']}km/h
"""
        forecasts.append(forecast)
    return "\n---\n".join(forecasts)


import os
import smtplib
from email.message import EmailMessage


@mcp.tool()
async def send_email(recipient: str, email_subject: str, email_body: str, attachment_filename: str) -> str:
    """
    发送包含附件的电子邮件。

    参数:
        recipient: 收件人邮箱地址
        email_subject: 邮件主题
        email_body: 邮件正文内容
        attachment_filename: 附件文件名（MD文件）

    返回:
        邮件发送结果的描述
    """

    # 读取SMTP配置
    smtp_host = os.getenv("SMTP_SERVER")  # 例如 smtp.qq.com
    smtp_port = int(os.getenv("SMTP_PORT", 465))
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")

    # 生成附件的完整路径并检查文件是否存在
    attachment_path = os.path.abspath(os.path.join("./reports", attachment_filename))
    if not os.path.exists(attachment_path):
        return f"附件路径 {attachment_path} 不存在"

    # 创建邮件消息并设置基本信息
    email_message = EmailMessage()
    email_message["Subject"] = email_subject
    email_message["From"] = sender_email
    email_message["To"] = recipient
    email_message.set_content(email_body)

    # 添加附件到邮件消息
    try:
        with open(attachment_path, "rb") as file:
            file_data = file.read()
            file_name = os.path.basename(attachment_path)
            email_message.add_attachment(file_data, maintype="application", subtype="octet-stream",
                                         filename=file_name)
    except Exception as file_error:
        return f"附件文件操作失败: {str(file_error)}"

    # 发送邮件
    try:
        with smtplib.SMTP_SSL(smtp_host, smtp_port) as smtp_server:
            smtp_server.login(sender_email, sender_password)
            smtp_server.send_message(email_message)
        return f"邮件成功发送至 {recipient}，附件路径: {attachment_path}"
    except Exception as send_error:
        return f"邮件发送失败: {str(send_error)}"


if __name__ == '__main__':
    mcp.run(transport="stdio")
