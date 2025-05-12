# MCP协议由入门到精通

## 一、MCP介绍

### 1 MCP是什么

MCP（Model Context Protocol，译作：模型上下文协议）是由Anthropic公司（Claude大模型的母公司）于2024年11月25日发布的一种开放通信标准协议，旨在解决目前AI大模型因为数据孤岛限制而无法充分发挥潜力的问题，统一大模型语言（LLM）与外界数据源和工具之间的通信协议，它就像 USB-C 接口一样，提供了一种标准化的方法，将 AI 模型连接到各种数据源和工具，为 AI 应用提供了连接万物的接口。

![image-20250511下午123536347](./assets/image-20250511%E4%B8%8B%E5%8D%88123536347-6938137.png)

### 2 MCP架构

![image-20250511下午55910651](./assets/image-20250511%E4%B8%8B%E5%8D%8855910651-6957551.png)

![image-20250511下午54535938](./assets/image-20250511%E4%B8%8B%E5%8D%8854535938-6956736.png)

![image-20250511下午60046158](./assets/image-20250511%E4%B8%8B%E5%8D%8860046158-6957647.png)

MCP采用简单的客户端-服务器架构模式：

| 架构组件               | 描述                                                         |
| ---------------------- | ------------------------------------------------------------ |
| **MCP Host**           | 通过 MCP 访问数据的 Claude Desktop、IDE 、 AI 工具或自己开发应用等程序 |
| **MCP Clients**        | 与服务器保持 1：1 连接的协议客户端                           |
| **MCP Servers**        | 轻量级程序，每个程序都通过标准化的 Model Context Protocol 公开特定功能 |
| **Local Data Sources** | MCP 服务器可以安全访问的计算机文件、数据库和服务             |
| **Remote Services**    | MCP 服务器可以连接到的 Internet 上可用的外部系统（例如，通过 API） |

`MCP` 大概的工作方式：`MCP Host`，比如 `Claude Desktop、Cursor` 这些工具，在内部实现了 `MCP Client`，然后`MCP Client` 通过标准的 MCP 协议和 `MCP Server` 进行交互，由各种三方开发者提供的 `MCP Server` 负责实现各种和三方资源交互的逻辑，比如访问数据库、浏览器、本地文件，最终再通过 标准的 MCP 协议返回给 `MCP Client`，最终在 `MCP Host` 上展示。

开发者按照 MCP 协议进行开发，无需为每个模型与不同资源的对接重复编写适配代码，可以大大节省开发工作量，另外已经开发出的 MCP Server，因为协议是通用的，能够直接开放出来给大家使用，这也大幅减少了开发者的重复劳动。

> 官网：https://modelcontextprotocol.io/introduction

### 3. MCP的通信模式

`MCP` 协议中的 `STDIO` 和 `SSE` 其实就是是两种不同的（`MCP Server` 与 `MCP Client`）通信模式：

- **STDIO（标准输入输出）**：像「面对面对话」：客户端和服务器通过本地进程的标准输入和标准输出直接通信。例如：本地开发时，你的代码脚本通过命令行启动，直接与 MCP 服务器交换数据，无需网络连接。
- **SSE（服务器推送事件）**：像「电话热线」：客户端通过 HTTP 协议连接到远程服务器，服务器可以主动推送数据（如实时消息）。例如：AI 助手通过网页请求调用远程天气 API，服务器持续推送最新的天气信息。

简单理解，STDIO 调用方式是将一个 `MCP Server` 下载到你的本地，直接调用这个工具，而 SSE 则是通过 HTTP 服务调用托管在远程服务器上的 `MCP Server`。

### 4 MCP服务

mcp发布后已经有大量的 McpServer提供使用，整个生态发展非常迅速，因此我们在掌握如何编写MCP的同时，也需要了解如何介入大量的第三方MCPServers帮助我们快速拓展AI业务。

**MCP 服务如雨后春笋般一下都涌了出来，MCP 市场也一下多了起来**

[mcp.so/zh/servers](https://link.juejin.cn?target=https%3A%2F%2Fmcp.so%2Fzh%2Fservers) MCP.so 上目前已经有9千多个MCP服务 ![image-20250420204038620](./assets/6895a2f33f0948a7b8dbb7c7a4cb208e~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5YyX54G16IGKQUk=:q75.awebp)

魔搭社区的MCP 广场。还可以在线调试你的MCP服务 [MCP 广场 · 魔搭社区](https://link.juejin.cn?target=https%3A%2F%2Fwww.modelscope.cn%2Fmcp) ![image-20250420211520036](./assets/559e6f80de434e41b1fe80ba2a1c8330~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5YyX54G16IGKQUk=:q75.awebp)

[mcpmarket.cn/](https://link.juejin.cn?target=https%3A%2F%2Fmcpmarket.cn%2F) ![image-20250420220011603](./assets/3d38fee40763427aa14226f76d926a81~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5YyX54G16IGKQUk=:q75.awebp)

| MCP平台                | 地址                                            |
| ---------------------- | ----------------------------------------------- |
| ModelContextProtocol   | https://github.com/modelcontextprotocol/servers |
| MCP Market             | https://mcpmarket.com/                          |
| MCP.so                 | https://mcp.so/zh                               |
| SmitheryAI             | https://smithery.ai/                            |
| PulseMCP               | https://www.pulsemcp.com/                       |
| GlamaAI                | https://glama.ai/mcp/servers                    |
| cursor.directory       | https://cursor.directory/mcp                    |
| Awesome MCP servers    | https://github.com/punkpeye/awesome-mcp-servers |
| MCP Servers            | https://mcpservers.org/                         |
| OpenTools              | https://opentools.com/registry                  |
| MCP Composio           | https://mcp.composio.dev/                       |
| MCP-Get                | https://mcp-get.com/                            |
| Gumloop                | https://www.gumloop.com/mcp                     |
| ClineMCPMarketplace    | https://cline.bot/mcp-marketplace               |
| 百度MCP平台（4月25日） | https://sai.baidu.com/ai/mcp                    |
| 魔塔MCP广场            | https://www.modelscope.cn/mcp                   |
| 百炼MCP广场            | https://bailian.console.aliyun.com/?tab=mcp     |
| 腾讯云MCP广场          | https://cloud.tencent.com/developer/mcp         |
| mcpservers             | https://www.mcpservers.cn/                      |
| MCP星球                | https://mcpmarket.cn/                           |

## 二、MCP实战案例

### 1. MCP实现：FastMCP

FastMCP是一个基于Python的高级框架，专为构建MCP服务器而设计。它极大简化了MCP服务器的开发流程，让开发者能够以最小的代码量创建功能强大的MCP服务器。

FastMCP的主要特点包括：

1. **简洁的API**：通过装饰器模式，简化MCP服务器的创建
2. **丰富的功能**：支持工具（Tools）、资源（Resources）、提示模板（Prompts）等MCP核心元素
3. **多种传输方式**：支持stdio和SSE等不同传输协议
4. **类型安全**：利用Python的类型提示，自动生成MCP协议所需的模式定义
5. **内置图像处理**：支持图像数据的自动格式转换和处理

使用FastMCP，开发者可以专注于业务逻辑，而不必过多关注底层协议细节。

### 2. MCP搭建

![image-20250511下午10012093](./assets/image-20250511%E4%B8%8B%E5%8D%8810012093-6939613.png)

https://github.com/ConardLi/mcp-client-nodejs

### 3. mcp server

#### 【1】搜索新闻

```python
# 加载环境变量
"""
load_dotenv() 是一个来自 python-dotenv 库的函数，用于加载环境变量。具体来说，它的作用包括
读取 .env 文件: 将位于项目根目录下的 .env 文件中的环境变量读取到程序中。这些环境变量通常用于存储敏感信息，如 API 密钥、数据库连接字符串等。
"""
load_dotenv()

# 初始化 MCP 服务器
mcp = FastMCP("AssistantServer")


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
```

#### 【2】查询天气

 ```python
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
 
 
 ```

#### 【3】大模型分析文本

Python调用大模型：openai

```python
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

```

#### 【4】发送邮件

```python
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
            email_message.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name+"!!!")
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
```

### 4. MCP Client

```python
import asyncio
import os
import json
from datetime import datetime
import re
from contextlib import AsyncExitStack
from typing import Optional, List
from openai import OpenAI
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()


class MCPClient:

    def __init__(self):
        self.async_context_manager = AsyncExitStack()
        self.api_key = os.getenv("DASHSCOPE_API_KEY")
        self.api_base_url = os.getenv("BASE_URL")
        self.model_name = os.getenv("MODEL")
        if not self.api_key:
            raise ValueError("未找到 OpenAI API Key，请在 .env 文件中设置DASHSCOPE_API_KEY")
        self.openai_client = OpenAI(api_key=self.api_key, base_url=self.api_base_url)
        self.client_session: Optional[ClientSession] = None
        self.available_tools = []

    async def connect_to_server(self):
        # 设置并启动 MCP 服务器进程，指定命令、脚本和环境变量
        server_parameters = StdioServerParameters(command="python3.12", args=["./server.py"], env=None)

        # 启动 MCP 服务并建立标准输入输出通信通道
        transport = await self.async_context_manager.enter_async_context(stdio_client(server_parameters))

        # 拆分通信通道以准备数据的读取和发送
        self.stdio, self.write_channel = transport

        # 创建会话对象以便与 MCP 进行交互
        self.client_session = await self.async_context_manager.enter_async_context(
            ClientSession(self.stdio, self.write_channel))

        # 初始化会话
        await self.client_session.initialize()

        # 获取并打印服务器支持的工具列表
        response = await self.client_session.list_tools()
        self.available_tools = response.tools
        print("服务器支持的工具列表（tool/list）", self.available_tools)

    async def process_query(self, query: str):

        # 测试1
        tool_name = "search_news"
        tool_args = {'wd': 'tesla'}
        result = await self.client_session.call_tool(tool_name, tool_args)
        print("结果:::", result)

        # 测试2
        # tool_name = "analyze_report"
        # tool_args = {'content': '分析下目前印巴冲突的国际影响',
        #              'output_filename': '印巴冲突的国际影响.md'}
        #
        # result = await self.client_session.call_tool(tool_name, tool_args)
        # print("结果:::", result)

        # 测试3
        # tool_name = "send_email"
        # tool_args = {'recipient': '916852314@qq.com',
        #              'email_subject': '国际黄金价格趋势分析报告2',
        #              'email_body': '请查收附件中的国际黄金价格趋势分析报告。',
        #              'attachment_filename': '国际黄金价格趋势分析报告_20250511_184022.md'}
        #
        # result = await self.client_session.call_tool(tool_name, tool_args)
        # print("结果:::", result)

    async def chat_loop(self):
        print("MCP-Client智能助手已启动...")
        while True:
            try:
                query = input("请输入您的要求：").strip()
                # 执行用户输入的指令并返回结果
                await self.process_query(query)
                print(f"命令{query}执行完成")

            except Exception as e:
                print(f"发生异常，具体原因: {str(e)}")


async def main():
    client = MCPClient()
    await client.connect_to_server()
    await client.chat_loop()


if __name__ == "__main__":
    asyncio.run(main())

```

