import streamlit as st
import tempfile #创建临时文件和目录，并提供了自动清理这些临时文件和目录的机制，以避免占用不必要的磁盘空间
import os
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import BaichuanTextEmbeddings

# 启动：streamlit run 项目代码.py
# 设置Streamlit应⽤的⻚⾯标题和布局
st.set_page_config(page_title="Rag Agent", layout="wide")

# 设置应⽤的标题
st.title("Rag Agent")

#上传txt⽂件，允许上传多个⽂件
uploaded_files = st.sidebar.file_uploader(
    label="上传txt⽂件", type=["txt"], accept_multiple_files=True
)
# 如果没有上传⽂件，提示⽤户上传⽂件并停⽌运⾏
if not uploaded_files:
    st.info("请先上传按TXT⽂档。")
    st.stop()
    
#实现检索器函数封装：文件读取、分块、向量转换、向量数据库、MMR信息检索
'''
@st.cache_resource(ttl="1h") 是 Streamlit 框架中的一个装饰器，用于缓存资源（如数据文件、数据库连接等）以提高性能和效率。具体来说，这个装饰器会将函数的返回值缓存一段时间（在这里是1小时），以避免在每次调用时都重新加载或计算相同的资源。
'''
@st.cache_resource(ttl="1h")
def configure_retriever(uploaded_files):
    docs = [] #存储用户上传文件的文件内容（字符串）
    #创建临时文件和目录
    temp_dir = tempfile.TemporaryDirectory(dir=r"D:\\")
    for file in uploaded_files:
        temp_filepath = os.path.join(temp_dir.name, file.name)
        with open(temp_filepath, "wb") as f:
            f.write(file.getvalue())
        # 使用TextLoader加载文本文件
        loader = TextLoader(temp_filepath, encoding="utf-8")
        docs.extend(loader.load())
    # 进行文档分割
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)

    # 使用BaichuanTextEmbeddings向量模型生成文档的向量表示
    key = "sk-83cd52xxxca6f57952d76f95d"
    embeddings = BaichuanTextEmbeddings(api_key=key)
    vectordb = Chroma.from_documents(splits, embeddings)

    # 创建文档检索器
    retriever = vectordb.as_retriever()
    #返回检索器对象
    return retriever

# 配置检索器：调用检索器函数，返回MMR检索器对象
retriever = configure_retriever(uploaded_files)

# 如果session_state中没有消息记录或用户点击了清空聊天记录按钮，则初始化消息记录
if "messages" not in st.session_state or st.sidebar.button("清空聊天记录"):
    st.session_state["messages"] = [{"role": "assistant", "content": "您好，我是AI智能助手，我可以查询文档"}]

# 加载历史聊天记录
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

    
# 下一步工作就是将文档检索作用在Agent对象中。创建Agent时需要让其对多轮对话具备上下文记忆能力
# 创建用于文档检索的工具
'''
    create_retriever_tool:
        功能：创建具体的检索工具实例
        用途：从文档库中检索信息
        典型场景：问答系统、文档搜索

    langchain.agents.Tool:
        功能：定义工具的通用接口
        用途：自定义工具或扩展工具功能
        典型场景：创建自定义工具或扩展现有工具 
'''
from langchain.tools.retriever import create_retriever_tool
tool = create_retriever_tool(
    retriever = retriever,
    name = "文档检索",
    description = "用于检索用户提出的问题，并基于检索到的文档内容进行回复.",
)
tools = [tool]

# 创建聊天消息历史记录
'''
StreamlitChatMessageHistory 是一个专为 Streamlit 应用设计的聊天历史管理工具，适用于需要保存和管理对话上下文的场景。
支持实时更新聊天历史，并在界面上动态显示。和之前学过的ChatMessageHistory消息集工具对象类似。
'''
msgs = StreamlitChatMessageHistory()
# 创建对话缓冲区
'''
参数介绍：
    chat_memory：指定初始的对话历史记录。 用于加载已有的对话历史，以便在后续对话中参考之前的上下文。
    return_messages：控制是否在返回结果中包含消息对象。如果设置为 True，则在调用 memory.load_memory() 时，返回的结果中会包含完整的消息对象（包括角色、内容等）。如果设置为 False，则只返回字符串形式的消息的内容。
    memory_key：指定在内存中存储对话历史的键名。当从内存中加载或保存对话历史时，使用这个键名来标识对话历史。例如，如果内存中存储了多个键值对，可以通过 memory_key 来指定要加载的对话历史。
    output_key：指定在内存中存储模型输出的键名。当将模型的输出保存到内存中时，使用这个键名来标识输出内容。例如，如果内存中存储了多个键值对，可以通过 output_key 来指定要加载的模型输出。
'''
memory = ConversationBufferMemory(
    chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
)

# 指令模板
instructions = """你是一个设计用于查询文档来回答问题的代理对象。
你可以使用文档检索工具，并基于检索内容来回答问题
你可能不查询文档就知道答案，但是你仍然应该查询文档来获得答案。
如果你从文档中找不到任何信息用于回答问题，则只需返回“抱歉，这个问题我还不知道。”作为答案。
"""

# 基础提示模板-React提示词
base_prompt_template = """
{instructions}

TOOLS:
------

You have access to the following tools:

{tools}

To use a tool, please use the following format:

‍```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: {input}
Observation: the result of the action
‍```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

‍```
Thought: Do I need to use a tool? No 
Final Answer: [your response here]
‍```

Begin!

Previous conversation history:
{chat_history}

New input: {input}
{agent_scratchpad}"""


# 创建基础提示模板
base_prompt = PromptTemplate.from_template(base_prompt_template)
# 创建部分填充的提示模板
prompt = base_prompt.partial(instructions=instructions)

# 创建llm
API_KEY = "sk-4b79f3a3ff3xxx366ebb425b3"
llm = ChatOpenAI(model="deepseek-reasoner",
                   openai_api_key=API_KEY,
                   openai_api_base="https://api.deepseek.com")

# 创建react Agent
agent = create_react_agent(llm, tools, prompt)

# 创建Agent执行器
'''
memory：指定用于存储和管理对话历史的内存对象。
    用途:
        - 存储对话历史，包括用户输入和机器人回复。
        - 在多轮对话中提供上下文，帮助机器人更好地理解用户意图。

handle_parsing_errors：控制是否在解析用户输入时自动处理错误。
    用途:
        - 如果设置为 True，当用户输入无法被正确解析时，系统会自动尝试修复或忽略错误，而不是直接抛出异常。
        - 如果设置为 False，系统会在遇到解析错误时抛出异常，可能导致程序中断。
'''
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True, handle_parsing_errors=True)

# 创建聊天输入框
user_query = st.chat_input(placeholder="请开始提问吧!")

# 如果有用户输入的查询
if user_query:
    # 添加用户消息到session_state
    st.session_state.messages.append({"role": "user", "content": user_query})
    # 显示用户消息
    st.chat_message("user").write(user_query)
    
    #创建一个 Streamlit 的聊天消息块，用于显示助手（机器人）的回复。
    with st.chat_message("assistant"):
        # st.container(): 创建一个 Streamlit 的容器组件，用于动态更新内容。
        #StreamlitCallbackHandler 是 LangChain 的一个回调处理器，用于将模型的输出或日志信息显示在 Streamlit 界面中。通过将 st.container() 传递给 StreamlitCallbackHandler，可以将 LangChain 的输出直接渲染到 Streamlit 的容器中。
        st_cb = StreamlitCallbackHandler(st.container())
        
        # 配置 LangChain 的回调函数列表，将 StreamlitCallbackHandler 添加到回调中。通过配置回调函数，LangChain 可以在处理过程中调用StreamlitCallbackHandler，从而将输出或日志信息显示在 Streamlit 界面中。这种方式可以实现实时更新界面。
        config = {"callbacks": [st_cb]}
        
        # 执行Agent并获取响应
        response = agent_executor.invoke({"input": user_query}, config=config)
        # 添加助手消息到session_state
        st.session_state.messages.append({"role": "assistant", "content": response["output"]})
        # 显示助手响应
        st.write(response["output"])