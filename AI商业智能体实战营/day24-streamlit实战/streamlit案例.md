### 模型对话示例：

```python
import streamlit as st  
from openai import OpenAI  
  
# 设置页面标题  
st.title("💬 DeepSeek Chatbot")  
  
# 在侧边栏添加配置选项  
with st.sidebar:  
    # 提供一个文本输入框让用户可以手动输入API Key（可选）  
    openai_api_key = st.text_input("DeepSeek API Key", key="chatbot_api_key", type="password")  
    
    "[获取 DeepSeek API key](https://platform.deepseek.com/api_keys)"  
    
    if st.button("开启新对话"):  
        st.session_state.messages = [{"role": "assistant", "content": "欢迎使用对话机器人，你想知道什么?"}] 
  
#检查API Key是否已提供  
if not openai_api_key:  
    st.info("请添加新的API Key")  
else:  
    base_url = "https://api.deepseek.com"  
    client = OpenAI(api_key=openai_api_key, base_url=base_url)  
  
    # 初始化对话历史记录  
    if "messages" not in st.session_state:  
        st.session_state.messages = [{"role": "assistant", "content": "欢迎使用对话机器人，你想知道什么?"}]  
  
    # 显示对话历史  
    for msg in st.session_state.messages:  
        st.chat_message(msg["role"]).write(msg["content"])  
  
    # 获取用户输入  
    if prompt := st.chat_input():  
        st.session_state.messages.append({"role": "user", "content": prompt})  
        st.chat_message("user").write(prompt)  
  
        # 调用DeepSeek API  
        response = client.chat.completions.create(  
            model="deepseek-chat",  
            messages=st.session_state.messages,  
            stream=False  
        )  
        #追加聊天记录
        assistant_reply = response.choices[0].message.content  
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})  
        st.chat_message("assistant").write(assistant_reply)

```

### sql解释器-1：

上传数据字典，围绕数据字典进行问答

```python
import streamlit as st  
from openai import OpenAI  
# 设置页面标题  
st.title("💬 DeepSeek Chatbot")  

# 在侧边栏添加配置选项  
with st.sidebar:  
    data_dic = ""
    # 提供一个文本输入框让用户可以手动输入API Key（可选）  
    openai_api_key = st.text_input("DeepSeek API Key", key="chatbot_api_key", type="password")  
    "[获取 DeepSeek API key](https://platform.deepseek.com/api_keys)"  
    
        
    #上传数据字典文件:创建文件上传组件，如果上传失败则返回None
    upload_file = st.file_uploader(
        label = "上传数据字典文件" 
    )
    #判断上传文件是否成功
    #Streamlit 会将文件内容作为字节流 (BytesIO) 对象返回给你。
    if upload_file is not None:
        #读取上传文件数据
        data_dic = upload_file.read().decode("utf-8")
        st.success("上传文件成功！")
    else:
        st.stop() # 退出
    
    #开启对话按钮
    if st.button("开启新对话"):  
        st.session_state.messages = [{"role": "system", "content": data_dic}] 
        
#检查API Key是否已提供  
if not openai_api_key:  
    st.info("请添加新的API Key")  
else:  
    base_url = "https://api.deepseek.com"  
    client = OpenAI(api_key=openai_api_key, base_url=base_url)  
  
    # 初始化对话历史记录  
    if "messages" not in st.session_state:  
        st.session_state.messages = [{"role": "assistant", "content": "欢迎使用对话机器人，你想知道什么?"}]  
  
    # 显示对话历史  
    for msg in st.session_state.messages:  
        if msg["role"] != 'system':
            st.chat_message(msg["role"]).write(msg["content"])  
  
    # 获取用户输入  
    if prompt := st.chat_input():  
        st.session_state.messages.append({"role": "user", "content": prompt})  
        st.chat_message("user").write(prompt)  
  
        # 调用DeepSeek API  
        response = client.chat.completions.create(  
            model="deepseek-chat",  
            messages=st.session_state.messages,  
            stream=False  
        )  
        #追加聊天记录
        assistant_reply = response.choices[0].message.content  
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})  
        st.chat_message("assistant").write(assistant_reply)
```

### sql解释器-2

sk-4b79f3a3ff334a15a1935366ebb425b3

```python
import streamlit as st  
from openai import OpenAI  
import os
import sys  
import pymysql
import json
sys.path.append('./swarm-main')

from swarm import Swarm, Agent
from IPython.display import Markdown, display

#外部函数定义
def get_sql_result(sql_query):
    """
    查询数据库相关数据的函数
    :param sql_query: 必要参数，字符串类型，用于表示查询数据的sql语句；
    :return：sql_query表示的sql语句查询到的结果;
    """
    connection = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,
            user='root',  # 数据库用户名
            passwd='boboadmin',  # 数据库密码
            db='guanghuan',  # 数据库名
            charset='utf8'  # 字符集选择utf8
        )
    
    try:
        with connection.cursor() as cursor:
            # SQL查询语句
            sql = sql_query
            cursor.execute(sql)

            # 获取查询结果
            results = cursor.fetchall()
    finally:
        connection.close()
    return json.dumps(results)


# 设置页面标题  
st.title("💬 DeepSeek Chatbot")  
# 在侧边栏添加配置选项  
with st.sidebar:  
    data_dic = ""
    # 提供一个文本输入框让用户可以手动输入API Key（可选）  
    openai_api_key = st.text_input("DeepSeek API Key", key="chatbot_api_key", type="password")  
    "[获取 DeepSeek API key](https://platform.deepseek.com/api_keys)"  
    
        
    #上传数据字典文件:创建文件上传组件，如果上传失败则返回None
    upload_file = st.file_uploader(
        label = "上传数据字典文件" 
    )
    #判断上传文件是否成功
    #Streamlit 会将文件内容作为字节流 (BytesIO) 对象返回给你。
    if upload_file is not None:
        #读取上传文件数据
        data_dic = upload_file.read().decode("utf-8")
        st.success("上传文件成功！")
    else:
        st.stop() # 退出
    
    #开启对话按钮
    if st.button("开启新对话"):  
        st.session_state.messages = [{"role": "system", "content": data_dic}] 
swarm_client = ""
sql_agent = ""
#检查API Key是否已提供  
if not openai_api_key:  
    st.info("请添加新的API Key")  
else:  
    base_url = "https://api.deepseek.com"  
    client = OpenAI(api_key=openai_api_key, base_url=base_url)  
    #创建swarm客户端
    swarm_client = Swarm(client)
    #创建Agent
    sql_agent = Agent(
        name = "sql执行智能体",
        model="deepseek-chat",
        instructions="你用来接收一组指定的sql语句，然后可以在指定的数据库环境中执行该sql语句，返回sql查询到的结果，并对结果进行合理的理解进行内容输出",
        functions=[get_sql_result]
)

# 初始化对话历史记录  
if "messages" not in st.session_state:  
    st.session_state.messages = [{"role": "assistant", "content": "欢迎使用对话机器人，你想知道什么?"}]  

# 显示对话历史  
for msg in st.session_state.messages:  
    if msg["role"] != 'system':
        st.chat_message(msg["role"]).write(msg["content"])  

# 获取用户输入  
if prompt := st.chat_input():  
    st.session_state.messages.append({"role": "user", "content": prompt})  
    st.chat_message("user").write(prompt)  

    # 调用DeepSeek API  
    response = swarm_client.run(
                       agent=sql_agent,
                       messages=st.session_state.messages,
                    )
    #追加聊天记录
    assistant_reply = response.messages[-1]["content"]  
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})  
    st.chat_message("assistant").write(assistant_reply)
```

