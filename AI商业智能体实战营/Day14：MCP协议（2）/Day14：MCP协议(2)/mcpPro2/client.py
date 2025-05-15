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
        logger.info("服务器支持的工具列表（tool/list）")
        print(self.tools)

    async def get_usage_tool_list(self, query):
        """
        功能描述：通过大模型和适当的提示词将server注册的mcp函数中用得到智能提取
        :param query:
        :return:
        """
        # 一、获取服务器注册的所有的mcp工具函数
        usage_tools_info = "\n".join([
            f"【{tool.name}】 {tool.description}"
            for tool in self.tools
        ])
        print("usage_tools_info:::", usage_tools_info)
        # 二 通过大模型和适当的提示词将server注册的mcp函数中用得到智能提取
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
            5. 不要列出没有用到的工具
            """
        }

        # 将系统提示和用户的自然语言一起作为消息输入，并选用当前的模型。
        planning_messages = [
            system_prompt,
            {"role": "user", "content": query}
        ]
        # 北京的未来几天的天气哪一天适合出行
        response = self.client.chat.completions.create(
            model=self.model,
            messages=planning_messages,
            # tools=self.response_tools,
            tool_choice="none"
        )

        # 提取出模型返回的 JSON 内容
        content = response.choices[0].message.content.strip()
        print("content:::", content)

        # 在解析 JSON 之后返回调用计划
        try:
            plan = json.loads(content.replace("json", "").replace("```", ""))
            return plan if isinstance(plan, list) else []
        except Exception as e:
            logger.error(f"❌❌❌ 工具链调用失败: {e}\n原始返回: {content}")
            return []

    async def call_tools_func(self, usage_tool_list, messages):
        # 依次执行工具调用，并收集结果

        """
       [
                {
                    "name": "search_forecast",
                    "arguments": {
                        "city": "beijing"
                    }
                },
                {
                    "name": "analyze_report",
                    "arguments": {
                        "data": "{search_forecast}",
                        "query": "分析未来几天北京的天气，找出最适合出行的一天，并生成报告。"
                    }
                },
                {
                    "name": "send_email",
                    "arguments": {
                        "to": "916852314@qq.com",
                        "subject": "未来几天北京适合出行的天气预报",
                        "body": "请查看附件中的详细分析。",
                        "filename": "{analyze_report}"
                    }
                }
       ]
        """
        # 缓存每一个工具以及对应结果的字典
        tool_outputs = {}

        for tool in usage_tool_list:
            tool_name = tool["name"]
            tool_args = tool["arguments"]

            # 判断有没有依赖上一个工具的数据
            for key, val in tool_args.items():
                if val.startswith("{") and val.endswith("}"):
                    print("数据替换")
                    tool_args[key] = tool_outputs.get(val.strip("{}"))

            logger.info(f"{tool_name}正在调用，参数为{tool_args}")
            result = await self.session.call_tool(tool_name, tool_args)
            # 将工具函数名以及结果写入到缓存变量
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
    server_script_path = "./mcp_server.py"
    client = MCPClient()

    await client.connect_to_server(server_script_path)
    await client.chat_loop()


if __name__ == "__main__":
    asyncio.run(main())
