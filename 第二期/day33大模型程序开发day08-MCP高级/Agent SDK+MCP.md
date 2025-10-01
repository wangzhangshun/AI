## Agents SDK+MCP智能体开发

### MCP入门介绍与接入Agents SDK基本流程

2025年3月27号，Agents SDK正式官宣支持MCP使用，这也使得Agents SDK的实际应用场景得到拓展：

<img src="Agent%20SDK+MCP.assets/image-20250807094033921.png" alt="image-20250807094033921" style="zoom:67%;" />

现在，我们仅需在创建Agent的时候，将MCP服务器视作为一项工具，即可顺利调用MCP服务器进行Agent开发。而实际在借助Agents SDK调用MCP的流程也非常简单，我们`只需将MCP视作tools`，即可进行调用。换而言之，就是如果使用Agents SDK作为Agent开发框架，则可以零门槛快速接入MCP海量服务器生态。

### MCP+Agents SDK基础调用流程

在新版的Agents SDK中，Agents SDK可以将某个对应的Agent封装为client与外部定义好的server进行通信。基本实现流程如下，还是查询天气的server.py，现在将其复制到jupyter运行主目录下，并修改名称为`weather_server.py`：(mcp的server端脚本程序)

<img src="Agent%20SDK+MCP.assets/image-20250807095508711.png" alt="image-20250807095508711" style="zoom:67%;" />



创建一个run_agent.py文件然后导入相关的库：

```Python
import asyncio
import os
import shutil
import subprocess
import time
from typing import Any

from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerStdio
from agents.model_settings import ModelSettings
```

同时定义Agent+MCP运行函数，要求带入MCPServer对象，且带入mcp_servers中，作为类似tools参数带入到当前Agent运行过程中：

```Python
async def run(mcp_server: MCPServer):
    
    agent = Agent(
        name="Assistant",
        instructions="你是一名助人为乐的助手",
        mcp_servers=[mcp_server],
        model=deepseek_model
    )

    message = "请帮我查询北京今天天气如何？"
    print(f"Running: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)
```

然后创建mcp_run函数，负责开启外部server并运行Agent：

```Python
async def mcp_run():
    async with MCPServerStdio(
        name="Weather Server",
        cache_tools_list=True,
        params = {"command": "uv","args": ["run", "weather_server.py"]} 
    ) as server:
        await run(server)
```

关键组件解释：

- `async with MCPServerStdio(...) as server:` 启动一个 MCP 工具服务器进程，使用标准输入输出（`stdio`）作为通信协议，并在上下文中运行（退出时会自动关闭）。
- `name="Weather Server"` 给这个 MCP Server 起名为“天气服务器”，这只是用于日志和识别用的标识符。
- `cache_tools_list=True` 意思是：首次加载工具时缓存工具列表，后续不需要重新请求工具元数据（提升效率）。
- `params = {"command": "uv", "args": ["run", "weather_server.py"]}` 这是启动 MCP 工具服务器的 **命令行参数**。

最后测试运行：

```Python
await mcp_run()
```

### Agents SDK接入多个MCP服务器流程

如何将Agents SDK同时接入多个MCP服务器，理论上，MCP一个服务器能同时运行多个外部函数，而一个MCP Client则可以连接多个MCP服务器。

<img src="Agent%20SDK+MCP.assets/image-20250807100559366.png" alt="image-20250807100559366" style="zoom: 67%;" />

这里我们尝试创建一个“写入本地文档”和“天气查询”的MCP服务器：`write_server.py和weather_server.py`，并将其放在Jupyter主目录下。代码如下：

```Python
#write_server.py
import json
import httpx
from typing import Any
from mcp.server.fastmcp import FastMCP

# 初始化 MCP 服务器
mcp = FastMCP("WriteServer")
USER_AGENT = "write-app/1.0"

@mcp.tool()
async def write_file(content: str) -> str:
    """
    将指定内容写入本地文件。
    :param content: 必要参数，字符串类型，用于表示需要写入文档的具体内容。
    :return：是否成功写入
    """
    return "已成功写入本地文件。"

if __name__ == "__main__":
    # 以标准 I/O 方式运行 MCP 服务器
    mcp.run(transport='stdio')
```

```python
#weather_server.py
import json
import httpx
from typing import Any
from mcp.server.fastmcp import FastMCP

# 初始化 MCP 服务器
mcp = FastMCP("WeatherServer")

# OpenWeather API 配置
OPENWEATHER_API_BASE = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "YOUR_API_KEY"  # 请替换为你自己的 OpenWeather API Key
USER_AGENT = "weather-app/1.0"

async def fetch_weather(city: str) -> dict[str, Any] | None:
    """
    从 OpenWeather API 获取天气信息。
    :param city: 城市名称（需使用英文，如 Beijing）
    :return: 天气数据字典；若出错返回包含 error 信息的字典
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "zh_cn"
    }
    headers = {"User-Agent": USER_AGENT}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(OPENWEATHER_API_BASE, params=params, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()  # 返回字典类型
        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP 错误: {e.response.status_code}"}
        except Exception as e:
            return {"error": f"请求失败: {str(e)}"}

def format_weather(data: dict[str, Any] | str) -> str:
    """
    将天气数据格式化为易读文本。
    :param data: 天气数据（可以是字典或 JSON 字符串）
    :return: 格式化后的天气信息字符串
    """
    # 如果传入的是字符串，则先转换为字典
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception as e:
            return f"无法解析天气数据: {e}"

    # 如果数据中包含错误信息，直接返回错误提示
    if "error" in data:
        return f"⚠️ {data['error']}"

    # 提取数据时做容错处理
    city = data.get("name", "未知")
    country = data.get("sys", {}).get("country", "未知")
    temp = data.get("main", {}).get("temp", "N/A")
    humidity = data.get("main", {}).get("humidity", "N/A")
    wind_speed = data.get("wind", {}).get("speed", "N/A")
    # weather 可能为空列表，因此用 [0] 前先提供默认字典
    weather_list = data.get("weather", [{}])
    description = weather_list[0].get("description", "未知")

    return (
        f"🌍 {city}, {country}\n"
        f"🌡 温度: {temp}°C\n"
        f"💧 湿度: {humidity}%\n"
        f"🌬 风速: {wind_speed} m/s\n"
        f"🌤 天气: {description}\n"
    )

@mcp.tool()
async def query_weather(city: str) -> str:
    """
    输入指定城市的英文名称，返回今日天气查询结果。
    :param city: 城市名称（需使用英文）
    :return: 格式化后的天气信息
    """
    data = await fetch_weather(city)
    return format_weather(data)

if __name__ == "__main__":
    # 以标准 I/O 方式运行 MCP 服务器
    mcp.run(transport='stdio')
```

同时调用多个server：

```Python
async def mcp_run_multi(servers_params, message):
    # 使用 AsyncExitStack 自动管理多个上下文退出
    async with AsyncExitStack() as stack:
        servers = []
        # 创建并进入所有 server 上下文
        for p in servers_params:
            server = MCPServerStdio(
                name=p.get("name", "Unnamed Server"),
                cache_tools_list=True,
                params={
                    "command": "uv",
                    "args": ["run", p["script"]],
                },
            )
            entered_server = await stack.enter_async_context(server)
            servers.append(entered_server)
        
        # 构造 agent，传入多个 server
        agent = Agent(
            name="Assistant",
            instructions="你是一名助人为乐的助手",
            mcp_servers=servers,
            model_settings=ModelSettings(tool_choice="required"),
            model=deepseek_model
        )
        
        print(f"Running: {message}")
        result = await Runner.run(starting_agent=agent, input=message)
        print(result.final_output)

        return result
```

```Python
# 示例调用：传入多个 server 的配置
result = await mcp_run_multi(
    servers_params=[
        {"name": "Weather Server", "script": "weather_server.py"},
        {"name": "Writer Server", "script": "write_server.py"}
    ],
    message="请帮我查询北京天气，并写入本地文档。"
)
```



