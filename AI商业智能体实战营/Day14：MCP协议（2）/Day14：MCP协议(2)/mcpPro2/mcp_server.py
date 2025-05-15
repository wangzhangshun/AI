import os
import json
import smtplib
from datetime import datetime
from email.message import EmailMessage
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from openai import OpenAI

from typing import *
import httpx

# 加载环境变量
load_dotenv()

# 初始化 MCP 服务器
mcp = FastMCP("mcpServer")

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

        news = [
            {
                "title": item.get("title"),
                "description": item.get("description"),
                "url": item.get("url")
            } for item in data["articles"][:10] if item.get("description")
        ]

        # 将新闻结果以带有时间戳命名后的 JSON 格式文件的形式保存在本地指定的路径
        output_dir = "./search_news"
        os.makedirs(output_dir, exist_ok=True)
        filename = f"news_{wd}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        file_path = os.path.join(output_dir, filename)

        with open(file_path, "w") as f:
            json.dump(news, f, ensure_ascii=False, indent=4)

        return f"""
        # 已搜索到【{wd}】 相关的新闻：
        {json.dumps(news, ensure_ascii=False, indent=2)}
        # 📃文件保存路径：{file_path}
        """

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


async def open_ai(text):
    openai_key = os.getenv("DASHSCOPE_API_KEY")
    model = os.getenv("MODEL")
    client = OpenAI(api_key=openai_key, base_url=os.getenv("BASE_URL"))

    # 构造情感分析的提示词
    prompt = f"请对以下内容进行综合分析：\n\n{text}"

    # 向模型发送请求，并处理返回的结果
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content.strip()
    return result


@mcp.tool()
async def analyze_report(query: str, data: str, ) -> str:
    """
    对传入的一段文本内容或者数据进行综合分析，并保存为指定名称的 Markdown 文件。

    参数:
        data (str): 上一个工具返回的数据文本
        query：提示词要求

    返回:
        str: 文件路径
    """

    # 按要求生成文案
    prompt = f"""
     数据：{data}
     要求：{query}
     """
    open_ai_res = await open_ai(prompt)
    print("result:::")
    # 生成 Markdown 格式的舆情分析报告，并存放进设置好的输出目录
    markdown = f"""# 综合分析报告

**分析时间：** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

------------------------
## 📃📃📃 原内容 📃📃📃 
{data}
------------------------
## 📚📚📚 分析结果 📚📚📚
{open_ai_res}
"""
    # 写文件操作
    output_dir = "./reports"
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = f"{query[:24]}_{timestamp}.md"

    file_path = output_dir + "/" + file_name
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    return file_name


@mcp.tool()
async def send_email(to: str, subject: str, body: str, filename: str) -> str:
    """
    将md文件作为附件发送给指定邮箱。

    参数:
        to: 收件人邮箱
        subject: 邮件主题
        body: 邮件内容
        filename: md文件名

    返回:
        邮件发送结果
    """

    # 获取并配置 SMTP 相关信息
    smtp_server = os.getenv("SMTP_SERVER")  # 例如 smtp.qq.com
    smtp_port = int(os.getenv("SMTP_PORT", 465))
    sender_email = os.getenv("EMAIL_USER")
    sender_pass = os.getenv("EMAIL_PASS")

    # 获取附件文件的路径，并进行检查是否存在
    full_path = os.path.abspath(os.path.join("./reports", filename))
    if not os.path.exists(full_path):
        return f"路径{full_path}不存在"

    # 创建邮件并设置内容
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to
    msg.set_content(body)

    # 添加附件并发送邮件
    try:
        with open(full_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(full_path)
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
    except Exception as e:
        return f"文件操作失败: {str(e)}"

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_pass)
            server.send_message(msg)
        return f"邮件已成功发送给 {to}，附件路径: {full_path}"
    except Exception as e:
        return f"邮件发送失败: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport='stdio')
