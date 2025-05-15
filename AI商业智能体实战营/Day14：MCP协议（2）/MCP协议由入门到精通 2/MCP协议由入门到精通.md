# MCP协议由入门到精通2

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
mcp = FastMCP("NewsServer")

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

大模型分析文本：

```python
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

```

#### 【4】发送邮件

```python

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
```

### 4. MCP Client

```python
import asyncio
import os
import json
from typing import Optional, List
from contextlib import AsyncExitStack
from datetime import datetime
import re
from openai import OpenAI
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from loguru import logger

load_dotenv()


class MCPClient:

    def __init__(self):
        self.exit_stack = AsyncExitStack()
        self.session: Optional[ClientSession] = None
        self.base_url = os.getenv("BASE_URL")
        self.model = os.getenv("MODEL")
        self.tools = []
        self.openai_api_key = os.getenv("DASHSCOPE_API_KEY")
        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.base_url)

    async def connect_to_server(self, server_script_path):

        # 构造 MCP 所需的服务器参数，包含启动命令、脚本路径参数、环境变量（为 None 表示默认）
        server_params = StdioServerParameters(command="python3.12", args=[server_script_path], env=None)

        # 启动 MCP 工具服务进程（并建立 stdio 通信）
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))

        # 拆包通信通道，读取服务端返回的数据，并向服务端发送请求
        self.stdio, self.write = stdio_transport

        # 创建 MCP 客户端会话对象
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        # 初始化会话
        await self.session.initialize()
        # 获取工具列表并打印
        response = await self.session.list_tools()

        self.tools = response.tools
        logger.info("服务器支持的工具列表（tool/list）", self.tools)

    async def get_usage_tool_list(self, query: str) -> List[dict]:

        usage_tools_info = "\n".join([
            f"【{tool.name}】 {tool.description}"
            for tool in self.tools
        ])
        logger.info("usage_tools_info:::", usage_tools_info)
        system_prompt = {
            "role": "system",
            "content": f"""
            你是一个任务（函数）调度专家，用户会发出一句自然语言的请求。
            你必须从{usage_tools_info}中选择合适且应该调用的工具函数
            -- 限制
            1. 严格使用工具名
            2. 如果是多个功能，一定按照逻辑上的执行顺序返回
            3. 返回格式：JSON 数组，每个对象包含 name 和 arguments 字段。
            4. 如果多个工具需要串联编排，通过{{上一步函数名（工具名）}}
            """
        }

        # 将系统提示和用户的自然语言一起作为消息输入，并选用当前的模型。
        planning_messages = [
            system_prompt,
            {"role": "user", "content": query}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=planning_messages,
            # tools=self.response_tools,
            tool_choice="none"
        )

        # 提取出模型返回的 JSON 内容
        content = response.choices[0].message.content.strip()

        # 在解析 JSON 之后返回调用计划
        try:
            plan = json.loads(content.replace("json", "").replace("```", ""))
            return plan if isinstance(plan, list) else []
        except Exception as e:
            logger.error(f"❌❌❌ 工具链调用失败: {e}\n原始返回: {content}")
            return []

    async def call_tools_func(self, usage_tool_list, messages):
        # 缓存每一个工具以及对应结果的字典
        tool_outputs = {}
        # 依次执行工具调用，并收集结果
        for tool in usage_tool_list:
            tool_name = tool["name"]
            tool_args = tool["arguments"]

            for key, val in tool_args.items():
                # "text": "{search_google_news}",
                if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
                    tool_args[key] = tool_outputs.get(val.strip("{}"))

            logger.info(f"{tool_name}正在调用，参数为{tool_args}")
            result = await self.session.call_tool(tool_name, tool_args)

            # 写入缓存：tool_outputs
            tool_outputs[tool_name] = result.content[0].text
            messages.append({
                "role": "tool",
                "tool_call_id": tool_name,
                "content": result.content[0].text
            })

        return messages

    async def process_query(self, query: str):

        query = f"""
        用户要求：{query.strip()}
        """

        usage_tool_list = await self.get_usage_tool_list(query)

        logger.info("usage_tool_list:::", usage_tool_list)
        messages = [{"role": "user", "content": query}]
        messages = await self.call_tools_func(usage_tool_list, messages)
        logger.info("messages:::", messages)
        # 调用大模型生成回复信息，并输出保存结果
        final_response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        final_result = final_response.choices[0].message.content

        print("命令执行结果:::\n\n\033[1;35m", final_result.replace("```", "").replace("plaintext", ""))

    async def chat_loop(self):
        logger.info("MCP Client已经启动")

        while 1:
            try:
                query = input("\033[1;33m请输入您的要求：").strip()
                if not query: continue
                # 处理用户的提问，并返回结果
                await self.process_query(query)
                logger.info(f"✅✅✅ 命令{query}执行成功！")
            except Exception as e:
                print(f"❌❌❌ 异常报错，错误原因: {str(e)}")


async def main():
    server_script_path = "./server.py"
    client = MCPClient()

    await client.connect_to_server(server_script_path)
    await client.chat_loop()


if __name__ == "__main__":
    asyncio.run(main())

```

.env文件：

```bash
BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL=qwen2.5-vl-32b-instruct
DASHSCOPE_API_KEY="sk-xxxxx"


NEWS_API_KEY = 4e00a2737ff2496d9bb0aa3bc72b8dbe

SMTP_SERVER=smtp.163.com
SMTP_PORT=465
EMAIL_USER=17300138736@163.com
EMAIL_PASS=xxxxx
```

## 三、百度地图

### 1 MCP客户端：百度千帆

1. 进入千帆AppBuilder主页，https://qianfan.cloud.baidu.com/appbuilder/

2. 注册登录

3. 试用

   ![image-20250513下午72137168](./assets/image-20250513%E4%B8%8B%E5%8D%8872137168-7135298.png)

4. 创建

   ![image-20250513下午62809435](./assets/image-20250513%E4%B8%8B%E5%8D%8862809435-7132090.png)

5. 创建自主Agent

   ![image-20250513下午72252655](./assets/image-20250513%E4%B8%8B%E5%8D%8872252655-7135373.png)

6. 模型配置

   ![image-20250513下午72451841](./assets/image-20250513%E4%B8%8B%E5%8D%8872451841-7135492.png)

7. appid

   ![image-20250513下午72604165](./assets/image-20250513%E4%B8%8B%E5%8D%8872604165-7135565.png)

8. 获取客户端模板代码

   ![image-20250513下午72746102](./assets/image-20250513%E4%B8%8B%E5%8D%8872746102.png)

   ![image-20250513下午72853688](./assets/image-20250513%E4%B8%8B%E5%8D%8872853688-7135734.png)

   ```python
   import os
   import asyncio
   import appbuilder
   from appbuilder.core.console.appbuilder_client.async_event_handler import (
       AsyncAppBuilderEventHandler,
   )
   from appbuilder.mcp_server.client import MCPClient
   
   
   class MyEventHandler(AsyncAppBuilderEventHandler):
       def __init__(self, mcp_client):
           super().__init__()
           self.mcp_client = mcp_client
   
       def get_current_weather(self, location=None, unit="摄氏度"):
           return "{} 的温度是 {} {}".format(location, 20, unit)
   
       async def interrupt(self, run_context, run_response):
           thought = run_context.current_thought
           # 绿色打印
           print("\033[1;31m", "-> Agent 中间思考: ", thought, "\033[0m")
           tool_output = []
           for tool_call in run_context.current_tool_calls:
               tool_res = ""
               if tool_call.function.name == "get_current_weather":
                   tool_res = self.get_current_weather(**tool_call.function.arguments)
               else:
                   print(
                       "\033[1;32m",
                       "MCP工具名称: {}, MCP参数:{}".format(tool_call.function.name, tool_call.function.arguments),
                       "\033[0m",
                   )
                   mcp_server_result = await self.mcp_client.call_tool(
                       tool_call.function.name, tool_call.function.arguments
                   )
                   print("\033[1;33m", "MCP结果: {}\033[0m".format(mcp_server_result))
                   for i, content in enumerate(mcp_server_result.content):
                       if content.type == "text":
                           tool_res += mcp_server_result.content[i].text
               tool_output.append(
                   {
                       "tool_call_id": tool_call.id,
                       "output": tool_res,
                   }
               )
           return tool_output
   
       async def success(self, run_context, run_response):
           print("\033[1;34m", "-> Agent 非流式回答: ", run_response.answer, "\033[0m")
   
   
   async def agent_run(client, mcp_client, query):
       tools = mcp_client.tools
       conversation_id = await client.create_conversation()
       with await client.run_with_handler(
               conversation_id=conversation_id,
               query=query,
               tools=tools,
               event_handler=MyEventHandler(mcp_client),
       ) as run:
           await run.until_done()
   
   
   ### 用户Token
   os.environ["APPBUILDER_TOKEN"] = ()
   
   
   async def main():
       appbuilder.logger.setLoglevel("DEBUG")
       ### 发布的应用ID
       app_id = ""
       appbuilder_client = appbuilder.AsyncAppBuilderClient(app_id)
       mcp_client = MCPClient()
   
       ### 注意这里的路径为MCP Server文件在本地的相对路径
       await mcp_client.connect_to_server("./map2.py")
       print(mcp_client.tools)
       await agent_run(
           appbuilder_client,
           mcp_client,
           '现在开车从北京市昌平区回龙观东大街昌发展AI加速中心A座门口到北京首都国际机场A2航站楼8号门',
       )
       await appbuilder_client.http_client.session.close()
   
   
   if __name__ == "__main__":
       import certifi
       import os
       os.environ['SSL_CERT_FILE'] = certifi.where()
       loop = asyncio.get_event_loop()
       loop.run_until_complete(main())
   ```

**AppBuilder** 是百度智能云推出的一款 **低代码/零代码 AI 原生应用开发平台**，旨在帮助开发者、企业甚至非技术人员快速构建基于大语言模型（如百度文心大模型）的 AI 应用，无需复杂编程即可实现智能化功能。

依赖安装：

```python
pip install mcp
pip install --upgrade appbuilder-sdk
```

### 2. MCP服务端：百度地图MCP服务

1. 百度首页

   ![image-20250513下午73541518](./assets/image-20250513%E4%B8%8B%E5%8D%8873541518-7136142.png)

2. 地图开发平台

   ![image-20250513下午73511715](./assets/image-20250513%E4%B8%8B%E5%8D%8873511715-7136113.png)

3. 注册登录，进入MCP Server

   ![image-20250513下午73708616](./assets/image-20250513%E4%B8%8B%E5%8D%8873708616-7136230.png)

4. 试用准备

   ![image-20250513下午73815144](./assets/image-20250513%E4%B8%8B%E5%8D%8873815144-7136296.png)

5. 创建应用

   ![image-20250513下午73859719](./assets/image-20250513%E4%B8%8B%E5%8D%8873859719-7136340.png)

6. 获取AK

   ![image-20250513下午74005926](./assets/image-20250513%E4%B8%8B%E5%8D%8874005926-7136406.png)

7. 获取map.py：MCP Server源码

   ![image-20250513下午74125879](./assets/image-20250513%E4%B8%8B%E5%8D%8874125879-7136487.png)

   ![image-20250513下午74239112](./assets/image-20250513%E4%B8%8B%E5%8D%8874239112-7136560.png)

   ```python
   # map.py
   import os
   import copy
   import httpx
   from asyncio import sleep
    
   from mcp.server.fastmcp import FastMCP, Context
    
   # 创建MCP服务器实例
   mcp = FastMCP("mcp-server-baidu-maps")
   '''
   
   获取环境变量中的API密钥, 用于调用百度地图API
   环境变量名为: BAIDU_MAPS_API_KEY, 在客户端侧通过配置文件进行设置传入
   获取方式请参考: https://lbsyun.baidu.com/apiconsole/key; 
   
   '''
   
   api_key = os.getenv('BAIDU_MAPS_API_KEY')
   api_url = "https://api.map.baidu.com"
    
    
   def filter_result(data) -> dict:
       """
       过滤路径规划结果，用于剔除冗余字段信息，保证输出给模型的数据更简洁，避免长距离路径规划场景下chat中断
       """
       
       # 创建输入数据的深拷贝以避免修改原始数据
       processed_data = copy.deepcopy(data)
       
       # 检查是否存在'result'键
       if 'result' in processed_data:
           result = processed_data['result']
           
           # 检查'result'中是否存在'routes'键
           if 'routes' in result:
               for route in result['routes']:
                   # 检查每个'route'中是否存在'steps'键
                   if 'steps' in route:
                       new_steps = []
                       for step in route['steps']:
                           # 提取'instruction'字段，若不存在则设为空字符串
                           new_step = {
                               'distance': step.get('distance', ''),
                               'duration': step.get('duration', ''),
                               'instruction': step.get('instruction', '')
                           }
                           new_steps.append(new_step)
                       # 替换原steps为仅含instruction的新列表
                       route['steps'] = new_steps
       
       return processed_data
   
   
   @mcp.tool()
   async def map_geocode(
       address: str,
       ctx: Context
   ) -> dict:
       """
       Name:
           地理编码服务
           
       Description:
           将地址解析为对应的位置坐标。地址结构越完整，地址内容越准确，解析的坐标精度越高。
           
       Args:
           address: 待解析的地址。最多支持84个字节。可以输入两种样式的值，分别是：
           1、标准的结构化地址信息，如北京市海淀区上地十街十号【推荐，地址结构越完整，解析精度越高】
           2、支持“*路与*路交叉口”描述方式，如北一环路和阜阳路的交叉路口
           第二种方式并不总是有返回结果，只有当地址库中存在该地址描述时才有返回。
           
       """
       try:
           # 获取API密钥
           if not api_key:
               raise Exception("Can not found API key.")
    
           # 调用百度API
           url = f"{api_url}/geocoding/v3/"
           
           # 设置请求参数
           # 更多参数信息请参考:https://lbsyun.baidu.com/faq/api?title=webapi/guide/webservice-geocoding
           params = {
               "ak": f"{api_key}",
               "output": "json",
               "address": f"{address}",
               "from": "py_mcp"
           }
           
           async with httpx.AsyncClient() as client:
               response = await client.get(url, params=params)
               response.raise_for_status()
               result = response.json()
    
           if result.get("status") != 0:
               error_msg = result.get("message", "unkown error")
               raise Exception(f"API response error: {error_msg}")
    
           return result
    
       except httpx.HTTPError as e:
           raise Exception(f"HTTP request failed: {str(e)}") from e
       except KeyError as e:
           raise Exception(f"Failed to parse reponse: {str(e)}") from e
   
    
   @mcp.tool()
   async def map_reverse_geocode(
       latitude: float,
       longitude: float,
       ctx: Context
   ) -> dict:
       """
       Name:
           逆地理编码服务
           
       Description:
           根据纬经度坐标, 获取对应位置的地址描述, 所在行政区划, 道路以及相关POI等信息
           
       Args:
           latitude: 纬度 (gcj02ll)
           longitude: 经度 (gcj02ll)
           
       """
       try:
           # 获取API密钥
           if not api_key:
               raise Exception("There")
    
           # 调用百度API
           url = f"{api_url}/reverse_geocoding/v3/"
           
           # 设置请求参数
           # 更多参数信息请参考:https://lbsyun.baidu.com/faq/api?title=webapi/guide/webservice-geocoding-abroad
           params = {
               "ak": f"{api_key}",
               "output": "json",
               "coordtype": "gcj02ll",
               "location": f"{latitude},{longitude}",
               "extensions_road": "true",
               "extensions_poi": "1",
               "entire_poi": "1",# 返回周边全量poi信息
               "from": "py_mcp"
           }
    
           async with httpx.AsyncClient() as client:
               response = await client.get(url, params=params)
               response.raise_for_status()
               result = response.json()
    
           if result.get("status") != 0:
               error_msg = result.get("message", "unkown error")
               raise Exception(f"API response error: {error_msg}")
    
           return result
    
       except httpx.HTTPError as e:
           raise Exception(f"HTTP request failed: {str(e)}") from e
       except KeyError as e:
           raise Exception(f"Failed to parse reponse: {str(e)}") from e
    
   
   @mcp.tool()
   async def map_search_places(
       query: str,
       tag: str,
       region: str,
       location: str,
       radius: int,
       ctx: Context
   ) -> dict:
       """
       Name:
           地点检索服务
       
       Description:
           支持检索城市内的地点信息(最小到city级别), 也可支持圆形区域内的周边地点信息检索
           城市内检索: 检索某一城市内（目前最细到城市级别）的地点信息。
           周边检索: 设置圆心和半径，检索圆形区域内的地点信息（常用于周边检索场景）。
       
       Args:
           query: 检索关键字, 可直接使用名称或类型, 如'query=天安门', 且可以至多10个关键字, 用英文逗号隔开
           tag: 检索分类, 以中文字符输入: 如'tag=美食', 多个分类用英文逗号隔开, 如'tag=美食,购物'
           region: 检索的行政区划, 可为行政区划名或citycode, 格式为'region=cityname'或'region=citycode' 
           location: 圆形区域检索的中心点纬经度坐标, 格式为location=lat,lng
           radius: 圆形区域检索半径，单位：米
           
       """
       try:
           # 获取API密钥
           if not api_key:
               raise Exception("Can not found API key.")
    
           # 调用百度API
           url = f"{api_url}/place/v2/search"
           
           # 设置请求参数
           # 更多参数信息请参考:https://lbsyun.baidu.com/faq/api?title=webapi/guide/webservice-placeapi
           params = {
               "ak": f"{api_key}",
               "output": "json",
               "query": f"{query}",
               "tag": f"{tag}",
               "from": "py_mcp"
           }
           if location:
               params["location"] = f"{location}"
               params["radius"] = f"{radius}"
           else:
               params["region"] = f"{region}"
    
           async with httpx.AsyncClient() as client:
               response = await client.get(url, params=params)
               response.raise_for_status()
               result = response.json()
    
           if result.get("status") != 0:
               error_msg = result.get("message", "unkown error")
               raise Exception(f"API response error: {error_msg}")
    
           return result
    
       except httpx.HTTPError as e:
           raise Exception(f"HTTP request failed: {str(e)}") from e
       except KeyError as e:
           raise Exception(f"Failed to parse reponse: {str(e)}") from e
    
   @mcp.tool()
   async def map_place_details(
       uid: str,
       ctx: Context
   ) -> dict:
       """
       Name:
           地点详情检索服务
           
       Description:
           地点详情检索: 地点详情检索针对指定POI，检索其相关的详情信息。
           通地点检索服务获取POI uid。使用“地点详情检索”功能，传入uid，即可检索POI详情信息，如评分、营业时间等（不同类型POI对应不同类别详情数据）。
           
       Args:
           uid: poi的唯一标识
       """
       try:
           # 获取API密钥
           if not api_key:
               raise Exception("Can not found API key.")
    
           # 调用百度API
           url = f"{api_url}/place/v2/detail"
           
           # 设置请求参数
           # 更多参数信息请参考:https://lbsyun.baidu.com/faq/api?title=webapi/guide/webservice-placeapi/detail
           params = {
               "ak": f"{api_key}",
               "output": "json",
               "uid": f"{uid}",
               # Agent入参不可控，这里给定scope为2
               "scope": 2,
               "from": "py_mcp"
           }
           
           async with httpx.AsyncClient() as client:
               response = await client.get(url, params=params)
               response.raise_for_status()
               result = response.json()
    
           if result.get("status") != 0:
               error_msg = result.get("message", "unkown error")
               raise Exception(f"API response error: {error_msg}")
    
           return result
    
       except httpx.HTTPError as e:
           raise Exception(f"HTTP request failed: {str(e)}") from e
       except KeyError as e:
           raise Exception(f"Failed to parse reponse: {str(e)}") from e
    
   @mcp.tool()
   async def map_distance_matrix(
       origins: str,
       destinations: str,
       mode: str,
       ctx: Context
   ) -> dict:
       """
       Name:
           批量算路服务
           
       Description:
           根据起点和终点坐标计算路线规划距离和行驶时间
           批量算路目前支持驾车、骑行、步行
           步行时任意起终点之间的距离不得超过200KM，超过此限制会返回参数错误
           驾车批量算路一次最多计算100条路线，起终点个数之积不能超过100
           
       Args:
           origins: 多个起点纬经度坐标，纬度在前，经度在后，多个起点用|分隔。示例：40.056878,116.30815|40.063597,116.364973【骑行】【步行】支持传入起点uid提升绑路准确性，格式为：纬度,经度;POI的uid|纬度,经度;POI的uid。示例：40.056878,116.30815;xxxxx|40.063597,116.364973;xxxxx
           destinations: 多个终点纬经度坐标，纬度在前，经度在后，多个终点用|分隔。示例：40.056878,116.30815|40.063597,116.364973【【骑行】【步行】支持传入终点uid提升绑路准确性，格式为：纬度,经度;POI的uid|纬度,经度;POI的uid。示例：40.056878,116.30815;xxxxx|40.063597,116.364973;xxxxx
           mode: 批量算路类型(driving, riding, walking)
           
       """
       try:
           # 获取API密钥
           if not api_key:
               raise Exception("Can not found API key.")
    
           # 调用百度API
           url = f"{api_url}/routematrix/v2/{mode}"
           
           # 设置请求参数
           # 更多参数信息请参考:https://lbsyun.baidu.com/faq/api?title=webapi/routchtout
           params = {
               "ak": f"{api_key}",
               "output": "json",
               "origins": f"{origins}",
               "destinations": f"{destinations}",
               "from": "py_mcp"
           }
    
           async with httpx.AsyncClient() as client:
               response = await client.get(url, params=params)
               response.raise_for_status()
               result = response.json()
    
           if result.get("status") != 0:
               error_msg = result.get("message", "unkown error")
               raise Exception(f"API response error: {error_msg}")
    
           return result
    
       except httpx.HTTPError as e:
           raise Exception(f"HTTP request failed: {str(e)}") from e
       except KeyError as e:
           raise Exception(f"Failed to parse reponse: {str(e)}") from e
    
   @mcp.tool()
   async def map_directions(
       model: str,
       origin: str,
       destination: str,
       ctx: Context
   ) -> dict:
       """
       Name:
           路线规划服务
           
       Description:
           驾车路线规划: 根据起终点`纬经度坐标`规划驾车出行路线
           骑行路线规划: 根据起终点`纬经度坐标`规划骑行出行路线
           步行路线规划: 根据起终点`纬经度坐标`规划步行出行路线
           公交路线规划: 根据起终点`纬经度坐标`规划公共交通出行路线
           
       Args:
           model: 路线规划类型(driving, riding, walking, transit)
           origin: 起点纬经度坐标，纬度在前，经度在后，当用户只有起点名称时，需要先通过地理编码服务或地点地点检索服务确定起点的坐标
           destination: 终点纬经度坐标，纬度在前，经度在后，当用户只有起点名称时，需要先通过地理编码服务或地点检索服务确定起点的坐标
    
       """
       try:
           # 获取API密钥
           if not api_key:
               raise Exception("Can not found API key.")
    
           # 调用百度API
           url = f"{api_url}/directionlite/v1/{model}"
           
           # 设置请求参数
           # 更多参数信息请参考:https://lbs.baidu.com/faq/api?title=webapi/direction-api-v2
           params = {
               "ak": f"{api_key}",
               "output": "json",
               "origin": f"{origin}",
               "destination": f"{destination}",
               "from": "py_mcp"
           }
    
           async with httpx.AsyncClient() as client:
               response = await client.get(url, params=params)
               response.raise_for_status()
               result = response.json()
    
           if result.get("status") != 0:
               error_msg = result.get("message", "unkown error")
               raise Exception(f"API response error: {error_msg}")
    
           '''
           过滤非公交的导航结果，防止返回的结果中包含大量冗余坐标信息，影响大模型的响应速度，或是导致chat崩溃。
           当前只保留导航结果每一步的距离、耗时和语义化信息。
           公交路线规划情况比较多，尽量全部保留。
               
           '''
           if model == 'transit':
               return result
           else:
               return filter_result(result)
    
       except httpx.HTTPError as e:
           raise Exception(f"HTTP request failed: {str(e)}") from e
       except KeyError as e:
           raise Exception(f"Failed to parse reponse: {str(e)}") from e
    
    
   @mcp.tool()
   async def map_weather(
       location: str,
       district_id: int,
       ctx: Context
   ) -> dict:
       """
       Name:
           天气查询服务
           
       Description:
           用户可通过行政区划或是经纬度坐标查询实时天气信息及未来5天天气预报(注意: 使用经纬度坐标需要高级权限)。
           
       Args:
           location: 经纬度，经度在前纬度在后，逗号分隔 (需要高级权限, 例如: 116.30815,40.056878)
           district_id: 行政区划代码, 需保证为6位无符号整数 (例如: 1101010)
       """
       try:
           # 获取API密钥
           if not api_key:
               raise Exception("Can not found API key.")
    
           # 调用百度API
           url = f"{api_url}/weather/v1/?"
           
           # 设置请求参数
           # 更多参数信息请参考:https://lbs.baidu.com/faq/api?title=webapi/weather
           params = {
               "ak": f"{api_key}",
               "data_type": "all",
               "from": "py_mcp"
           }
           
           # 核心入参，二选一
           if not location:
               params["district_id"] = f"{district_id}"
           else :
               params["location"] = f"{location}"
    
           async with httpx.AsyncClient() as client:
               response = await client.get(url, params=params)
               response.raise_for_status()
               result = response.json()
    
           if result.get("status") != 0:
               error_msg = result.get("message", "unkown error")
               raise Exception(f"API response error: {error_msg}")
    
           return result
    
       except httpx.HTTPError as e:
           raise Exception(f"HTTP request failed: {str(e)}") from e
       except KeyError as e:
           raise Exception(f"Failed to parse reponse: {str(e)}") from e
    
    
   @mcp.tool()
   async def map_ip_location(
       # ip: str,
       ctx: Context
   ) -> dict:
       """
       Name:
           IP定位服务
           
       Description:
           根据用户请求的IP获取当前的位置，当需要知道用户当前位置、所在城市时可以调用该工具获取
           
       Args:
       """
       try:
           # 获取API密钥
           if not api_key:
               raise Exception("Can not found API key.")
    
           # 调用百度API
           url = f"{api_url}/location/ip"
           
           # 设置请求参数
           # 更多参数信息请参考:https://lbs.baidu.com/faq/api?title=webapi/ip-api
           params = {
               "ak": f"{api_key}",
               "from": "py_mcp"
           }
    
           async with httpx.AsyncClient() as client:
               response = await client.get(url, params=params)
               response.raise_for_status()
               result = response.json()
    
           if result.get("status") != 0:
               error_msg = result.get("message", "unkown error")
               raise Exception(f"API response error: {error_msg}")
    
           return result
    
       except httpx.HTTPError as e:
           raise Exception(f"HTTP request failed: {str(e)}") from e
       except KeyError as e:
           raise Exception(f"Failed to parse reponse: {str(e)}") from e
       
   
   @mcp.tool()
   async def map_road_traffic(
       model: str,
       road_name: str,
       city: str,
       bounds: str,
       vertexes: str,
       center: str,
       radius: int,
       ctx: Context
   ) -> dict:
       """
       Name:
           实时路况查询服务
           
       Description:
           查询实时交通拥堵情况, 可通过指定道路名和区域形状(矩形, 多边形, 圆形)进行实时路况查询。
           
           道路实时路况查询: 查询具体道路的实时拥堵评价和拥堵路段、拥堵距离、拥堵趋势等信息
           矩形区域实时路况查询: 查询指定矩形地理范围的实时拥堵情况和各拥堵路段信息
           多边形区域实时路况查询: 查询指定多边形地理范围的实时拥堵情况和各拥堵路段信息
           圆形区域(周边)实时路况查询: 查询某中心点周边半径范围内的实时拥堵情况和各拥堵路段信息
   
           
       Args:
           model:      路况查询类型(road, bound, polygon, around)
           road_name:  道路名称和道路方向, model=road时必传 (如:朝阳路南向北)
           city:       城市名称或城市adcode, model=road时必传 (如:北京市)
           bounds:     区域左下角和右上角的纬经度坐标,纬度在前,经度在后, model=bound时必传 (如:39.912078,116.464303;39.918276,116.475442)
           vertexes:   多边形区域的顶点纬经度坐标,纬度在前,经度在后, model=polygon时必传 (如:39.910528,116.472926;39.918276,116.475442;39.916671,116.459056;39.912078,116.464303)
           center:     圆形区域的中心点纬经度坐标,纬度在前,经度在后, model=around时必传 (如:39.912078,116.464303)
           radius:     圆形区域的半径(米), 取值[1,1000], model=around时必传 (如:200)
    
       """
       try:
           # 获取API密钥
           if not api_key:
               raise Exception("Can not found API key.")
    
           # 调用百度API
           url = f"{api_url}/traffic/v1/{model}?"
           
           # 设置请求参数
           # 更多参数信息请参考:https://lbs.baidu.com/faq/api?title=webapi/traffic
           params = {
               "ak": f"{api_key}",
               "output": "json",
               "from": "py_mcp"
           }
           
           # 核心入参，根据model选择
           match model:
               case 'bound': 
                   params['bounds'] = f'{bounds}'
               case 'polygon': 
                   params['vertexes'] = f'{vertexes}'
               case 'around': 
                   params['center'] = f'{center}'
                   params['radius'] = f'{radius}'
               case 'road':
                   params['road_name'] = f'{road_name}'
                   params['city'] = f'{city}'
               case _:             
                   pass
           
           async with httpx.AsyncClient() as client:
               response = await client.get(url, params=params)
               response.raise_for_status()
               result = response.json()
    
           if result.get("status") != 0:
               error_msg = result.get("message", "unkown error")
               raise Exception(f"API response error: {error_msg}")
    
           return result
    
       except httpx.HTTPError as e:
           raise Exception(f"HTTP request failed: {str(e)}") from e
       except KeyError as e:
           raise Exception(f"Failed to parse reponse: {str(e)}") from e
       
       
   @mcp.tool()
   async def map_poi_extract(
       text_content: str,
       ctx: Context
   ) -> dict:
       """
       Name:
           POI智能提取
           
       Description:
           根据用户提供的文本描述信息, 智能提取出文本中所提及的POI相关信息. (注意: 使用该服务, api_key需要拥有对应的高级权限, 否则会报错)
           
       Args:
           text_content: 用于提取POI的文本描述信息 (完整的旅游路线，行程规划，景点推荐描述等文本内容, 例如: 新疆独库公路和塔里木湖太美了, 从独山子大峡谷到天山神秘大峡谷也是很不错的体验)
       """
       
       # 关于高级权限使用的相关问题，请联系我们: https://lbsyun.baidu.com/apiconsole/fankui?typeOne=%E4%BA%A7%E5%93%81%E9%9C%80%E6%B1%82&typeTwo=%E9%AB%98%E7%BA%A7%E6%9C%8D%E5%8A%A1
       
       try:
           # 获取API密钥
           if not api_key:
               raise Exception("Can not found API key.")
    
           # 调用POI智能提取的提交接口
           headers = {"Content-Type": "application/x-www-form-urlencoded"}
           submit_url = f"{api_url}/api_mark/v1/submit"
           result_url = f"{api_url}/api_mark/v1/result"
           
           # 设置上传用户描述的请求体
           submit_body = {
               "ak": f"{api_key}",
               "id": 0,
               "msg_type": "text",
               "text_content": f"{text_content}",
               "from": "py_mcp"
           }
   
           # 异步请求
           async with httpx.AsyncClient() as client:
               # 提交任务
               submit_resp = await client.post(
                   submit_url, data=submit_body, headers=headers, timeout=10.0
               )
               submit_resp.raise_for_status()
               submit_result = submit_resp.json()
   
               if submit_result.get("status") != 0:
                   error_msg = submit_result.get("message", "unkown error")
                   raise Exception(f"API response error: {error_msg}")
               
   
               map_id = submit_result.get("result", {}).get("map_id")
               if not map_id:
                   raise Exception("Can not found map_id")
   
               # 轮询获取结果（最多5次，间隔2秒）
               result_body = {"ak": api_key, "id": 0, "map_id": map_id, "from": "py_mcp"}
               max_retries = 5
               for attempt in range(max_retries):
                   result_resp = await client.post(
                       result_url, data=result_body, headers=headers, timeout=10.0
                   )
                   result_resp.raise_for_status()
                   result = result_resp.json()
   
                   if result.get("status") == 0 and result.get("result"):
                       return result
                   elif attempt < max_retries - 1:
                       await sleep(2)
               
               else:
                   raise Exception("Timeout to get the result")
                   
           if result.get("status") != 0:
               error_msg = result.get("message", "unkown error")
               raise Exception(f"API response error: {error_msg}")
   
       except httpx.HTTPError as e:
           raise Exception(f"HTTP request failed: {str(e)}") from e
       except KeyError as e:
           raise Exception(f"Failed to parse reponse: {str(e)}") from e
    
   if __name__ == "__main__":
       mcp.run()
   ```

   



​        

```python
import os
import asyncio
import appbuilder
from appbuilder.core.console.appbuilder_client.async_event_handler import (
    AsyncAppBuilderEventHandler,
)
from appbuilder.mcp_server.client import MCPClient
class MyEventHandler(AsyncAppBuilderEventHandler):
    def __init__(self, mcp_client):
        super().__init__()
        self.mcp_client = mcp_client
    def get_current_weather(self, location=None, unit="摄氏度"):
        return "{} 的温度是 {} {}".format(location, 20, unit)
    async def interrupt(self, run_context, run_response):
        thought = run_context.current_thought
        # 绿色打印
        print("\033[1;31m", "-> Agent 中间思考: ", thought, "\033[0m")
        tool_output = []
        for tool_call in run_context.current_tool_calls:
            tool_res = ""
            if tool_call.function.name == "get_current_weather":
                tool_res = self.get_current_weather(**tool_call.function.arguments)
            else:
                print(
                    "\033[1;32m",
                    "MCP工具名称: {}, MCP参数:{}
".format(tool_call.function.name, tool_call.function.arguments),
                    "\033[0m",
                )
                mcp_server_result = await self.mcp_client.call_tool(
                    tool_call.function.name, tool_call.function.arguments
                )
                print("\033[1;33m", "MCP结果: {}\033[0m".format(mcp_server_result))
                for i, content in enumerate(mcp_server_result.content):
                    if content.type == "text":
                        tool_res += mcp_server_result.content[i].text
            tool_output.append(
                {
                    "tool_call_id": tool_call.id,
                    "output": tool_res,
                }
            )
        return tool_output
    async def success(self, run_context, run_response):
        print("\033[1;34m", "-> Agent 非流式回答: ", run_response.answer, "\033[0m")
async def agent_run(client, mcp_client, query):
    tools = mcp_client.tools
    conversation_id = await client.create_conversation()
    with await client.run_with_handler(
        conversation_id=conversation_id,
        query=query,
        tools=tools,
        event_handler=MyEventHandler(mcp_client),
    ) as run:
        await run.until_done()
### 用户Token
os.environ["APPBUILDER_TOKEN"] = (
    ""
)
async def main():
    appbuilder.logger.setLoglevel("DEBUG")
    ### 发布的应用ID
    app_id = ""
    appbuilder_client = appbuilder.AsyncAppBuilderClient(app_id)
    mcp_client = MCPClient()
    
    ### 注意这里的路径为MCP Server文件在本地的相对路径
    await mcp_client.connect_to_server("./<YOUR_FILE_PATH>/map.py")
    print(mcp_client.tools)
    await agent_run(
        appbuilder_client,
        mcp_client,
        '开车导航从北京到上海',
    )
    await appbuilder_client.http_client.session.close()
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```











