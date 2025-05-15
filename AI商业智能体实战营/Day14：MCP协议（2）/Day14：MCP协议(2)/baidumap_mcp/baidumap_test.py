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
    await mcp_client.connect_to_server("./baidumap_server.py")
    print(mcp_client.tools)
    while 1:
        query = input("请输入命令：")
        if not query: continue
        await agent_run(
            appbuilder_client,
            mcp_client,
            query,
        )
    await appbuilder_client.http_client.session.close()


if __name__ == "__main__":
    import certifi
    import os

    os.environ['SSL_CERT_FILE'] = certifi.where()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
