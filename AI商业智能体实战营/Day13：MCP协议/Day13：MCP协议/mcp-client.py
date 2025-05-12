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
        server_parameters = StdioServerParameters(command="python3.12", args=["./mcp_server.py"], env=None)

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
        # tool_name = "search_news"
        # tool_args = {'wd': 'tesla'}
        # result = await self.client_session.call_tool(tool_name, tool_args)
        # print("结果:::", result)

        # 测试2
        # tool_name = "analyze_report"
        # tool_args = {'content': '分析下目前印巴冲突的国际影响',
        #              'output_filename': '印巴冲突的国际影响.md'}
        #
        # result = await self.client_session.call_tool(tool_name, tool_args)
        # print("结果:::", result)

        # 测试3
        tool_name = "send_email"
        tool_args = {'recipient': '916852314@qq.com',
                     'email_subject': '国际黄金价格趋势分析报告2',
                     'email_body': '请查收附件中的国际黄金价格趋势分析报告。',
                     'attachment_filename': '国际黄金价格趋势分析报告_20250511_184022.md'}

        result = await self.client_session.call_tool(tool_name, tool_args)
        print("结果:::", result)

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
