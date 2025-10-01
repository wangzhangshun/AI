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
    key = open('./ken_files/baichuan_API-Key.md').read().strip()
    embeddings = BaichuanTextEmbeddings(api_key=key)
    vectordb = Chroma.from_documents(splits, embeddings)

    # 创建文档检索器
    retriever = vectordb.as_retriever()
    #返回检索器对象
    return retriever