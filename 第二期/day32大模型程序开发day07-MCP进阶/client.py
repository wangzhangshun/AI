import asyncio
import os
import json
from typing import Optional
from contextlib import AsyncExitStack

from openai import OpenAI  
from dotenv import load_dotenv

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 加载 .env 文件，确保 API Key 受到保护
load_dotenv()

class MCPClient:
    def __init__(self):
        """初始化 MCP 客户端"""
        self.exit_stack = AsyncExitStack()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")  # 读取 OpenAI API Key
        self.base_url = os.getenv("BASE_URL")  # 读取 BASE YRL
        self.model = os.getenv("MODEL")  # 读取 model
        if not self.openai_api_key:
            raise ValueError("❌ 未找到 OpenAI API Key，请在 .env 文件中设置 OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.base_url) # 创建OpenAI client
        #用于保存 MCP 的客户端会话，默认是 None，稍后通过 connect_to_server 进行连接。
        self.session: Optional[ClientSession] = None
	
    #连接指定server端，参数为server端文件路径
    async def connect_to_server(self, server_script_path: str):
        #判断服务器脚本是 Python 还是 Node.js，选择对应的运行命令。
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("服务器脚本必须是 .py 或 .js 文件")

        command = "python" if is_python else "node"
        
        #告诉 MCP 客户端如何启动服务器。
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        # 启动服务器进程，并建立 标准 I/O 通信管道
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        
        #拿到读写流。
        self.stdio, self.write = stdio_transport
        
        #创建 MCP 客户端会话，与服务器交互。
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))
		
        #发送初始化消息给服务器，等待服务器就绪。
        await self.session.initialize()

        # 向 MCP 服务器请求所有已注册的工具（用 @mcp.tool() 标记）。
        response = await self.session.list_tools()
        tools = response.tools
        print("\n已连接到服务器，支持以下工具:", [tool.name for tool in tools])     
        
    #使用大模型处理查询并调用可用的 MCP 工具 (Function Calling)
    async def process_query(self, query: str) -> str:
       
        #收到用户输入后，先把它组装进一个 messages 列表，目前只包含用户信息（{"role": "user", "content": query}）。
        messages = [{"role": "user", "content": query}]
        
        # 向 MCP 服务器请求所有已注册的工具（用 @mcp.tool() 标记）。
        response = await self.session.list_tools()
        
        #获取服务器上的工具，再转换成 available_tools 的格式。方便后面发给模型，告诉它：可以调用这些工具。
        available_tools = [{
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema
            }
        } for tool in response.tools]
        # print(available_tools)
        
        #模型调用first response
        response = self.client.chat.completions.create(
            model=self.model,            
            messages=messages,
            tools=available_tools     
        )
        
        # 处理返回的内容
        content = response.choices[0]
        if content.finish_reason == "tool_calls":
            # 如何是需要使用工具，就解析工具
            tool_call = content.message.tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)
            
            # 执行工具（手动调用外部工具函数）
            result = await self.session.call_tool(tool_name, tool_args)
            print(f"\n\n[Calling tool {tool_name} with args {tool_args}]\n\n")
            
            # 将模型返回的调用哪个工具数据和工具执行完成后的数据都存入messages中
            messages.append(content.message.model_dump())
            messages.append({
                "role": "tool",
                "content": result.content[0].text,
                "tool_call_id": tool_call.id,
            })
            
            # 将上面的结果再返回给大模型用于生产最终的结果
            #second response
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            return response.choices[0].message.content
            
        return content.message.content
    
    #多轮对话
    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\n🤖 MCP 客户端已启动！输入 'quit' 退出")

        while True:
            try:
                query = input("\n你: ").strip()
                if query.lower() == 'quit':
                    break
                
                response = await self.process_query(query)  # 发送用户输入到 OpenAI API
                print(f"\n🤖 OpenAI: {response}")

            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")
   
	#清理资源
    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()

async def main():
    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())