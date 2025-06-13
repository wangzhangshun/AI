### 4.4 sql解释器Agent开发

#### 4.4.1 项目背景

在平常的工作中，会经常对数据库中的数据进行相关的读写操作，这是一些繁杂的sql语句的编写就会尤为的麻烦也非常容易出错。尤其是在数据分析的一些业务场景中，更是需要频繁的进行数据库的相关操作且高频的编写一些对应的sql代码。

那么我们是否可以利用大模型本身的编码能力帮我们根据相关的自然语言的指令自动进行sql的编写和运行呢？

这一小节，我们就一起来学习，如何将大模型接入到本地数据库中，让大模型帮我们生成对应的sql且在本地数据库环境中进行sql的运行，将结果再次经过大模型的语义理解能力和文字生成能力进行润色后返回！

#### 4.4.2 数据字典

对于大多数企业来说，都会围绕各关键数据集制作数据字典。所谓数据字典，指的是一份记录了每个数据集详细信息的文档，有的时候数据字典也可以以表格形式呈现。借助数据字典，开发/数据分析人员能够快速了解数据表中的各项关键信息。

那么，为了让大模型可以更好的理解数据库中的数据，我们也可以给大模型制作一个数据字典，让大模型可以更好的理解数据，返回更加具有针对性的结果。

```python
import os
from openai import OpenAI
from IPython.display import display, Code, Markdown

#硅基流动API
ds_api_key = "sk-atisrejlfxlvnymvfxoesps"
client = OpenAI(api_key=ds_api_key, 
                base_url="https://api.siliconflow.cn/v1")
```

```python
# 打开并读取Markdown文件
with open('./data/LC数据字典.md', 'r', encoding='utf-8') as f:
    md_content = f.read()
    
len(md_content)
```

```python
#基于md_content作为模型背景信息，向模型进行相关提问
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V2.5", 
    messages=[
        {"role": "system", "content": md_content}, 
        # "content": '请帮我统计下LC数据表一共有哪些字段？共计多少个？'
        {"role": "user", "content": '请帮我介绍下LC数据表'}
    ],
)
display(Markdown(response.choices[0].message.content))
```

#### 4.4.3 Function calling实现

##### 创建生成SQL语句的外部函数

```python
def get_sql_result(sql_query):
    """
    查询数据库相关数据的函数
    :param sql_query: 必要参数，字符串类型，用于表示查询数据的sql语句；
    :return：sql_query表示的sql语句查询到的结果;
    """
    connection = pymysql.connect(
            host='localhost',  # 数据库地址
            user='root',  # 数据库用户名
            passwd='boboadmin',  # 数据库密码
            db='testdb',  # 数据库名
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
```

##### 自动生成外部函数描述信息

```python
import inspect
import json
import os
from openai import OpenAI
import pymysql
from IPython.display import display, Code, Markdown

#用于自动生成外部函数描述信息
def auto_function_desc(function): #参数为外部函数对象
    #定义一个内部函数用于生成外部函数的完整描述信息
    def inner(function):
        function_description = inspect.getdoc(function)#外部函数的函数说明
        function_name = function.__name__ #外部函数名
        
        system_prompt = '以下是某的函数说明：%s' % function_description
        
        user_prompt = '根据这个函数的函数说明，请帮我创建一个JSON格式的字典，这个字典有如下5点要求,请你仔细阅读，并且务必遵从所有要求：\
                       1.字典总共有三个键值对；\
                       2.第一个键值对的Key是字符串name，value是该函数的名字：%s，也是字符串；\
                       3.第二个键值对的Key是字符串description，value是该函数的函数的功能说明，也是字符串；\
                       4.第三个键值对的Key是字符串parameters，value是一个JSON Schema对象，用于说明该函数的参数输入规范。\
                       5.输出结果必须是一个JSON格式的字典，并且一定不要任何前后修饰语句,务必参按照如下格式进行输出:%s' % (function_name,'{key:value}')
        
        api_key = "xxx"
        client = OpenAI(api_key=ds_api_key, 
                base_url="https://api.siliconflow.cn/v1")
        response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V2.5",  
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}

             ]
        )

        return json.loads(response.choices[0].message.content)
    #由于模型根据提示信息生成的外部函数完整信息可能会有问题，因此，如果出现问题则loads环节会报错，则要求模型重新进行生成
    max_try_count = 5 #模型调用的最大次数
    count = 0 #当前调用模型的次数
    while count < max_try_count:
        try:
            function_desc = inner(function)
            break
        except Exception as e:
            count += 1
            print('something error:',e)
            if count == max_try_count:
                print('模型达到最大尝试次数，程序停止！')
                raise
            else:
                print('模型重新生成中......')
    tools = [
    {
        "type": "function", 
        "function":function_desc
    }
]
    return tools
```

测试：

```python
auto_function_desc(get_sql_result)
```

输出：

```python
[
    {
        'type': 'function',
        'function': {
            'name': 'get_sql_result',
  		   'description': '查询数据库相关数据的函数',
           'parameters': {
               'type': 'object',
               'properties': {
                   'sql_query': {
                       'type': 'string',
                       'description': '用于表示查询数据的sql语句'
                   }
               },
         'required': ['sql_query']}}}
]
```

##### sql解释器封装

```python
#available_functions表示外部函数库
def auto_run_conversation(messages,available_functions=None):
    api_key = "sk-atisrrfnrxsnulmuvlzqnvuvcglkriejlfxlvnymvfxoesps"
    client = OpenAI(api_key=ds_api_key, 
                base_url="https://api.siliconflow.cn/v1")
    
    # 如果没有外部函数库，则执行普通的对话任务
    if available_functions == None:
        print('模型原生能力解决该提问.........')
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V2.5",  
            messages=messages
        )
        final_response = response.choices[0].message.content
    else:
        #外部函数库定义
        available_functions = available_functions
        
       #step_3:外部函数完整描述定义 + #step_4:tools参数值定义
        tools = auto_function_desc(available_functions['function'])

        #step_5:第一次模型调用
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V2.5",  
            messages=messages,
            tools=tools,
        )
        response_message = response.choices[0].message
        
        #判断返回结果是否存在tool_calls，即判断是否需要调用外部函数来回答问题
        if response_message.tool_calls:
            print('function_calling解决该提问.........')
            sql = response_message.tool_calls[0].function.arguments
            print('生成的sql为：:',sql)
            choose = input('是否执行上述sql? y/n')
            if choose == 'n':
                print("您选择不执行sql语句，再见！")
                return
            #step_6:外部函数手动调用且获取调用结果
            fuction_to_call = available_functions['function'] #函数对象
            function_args = json.loads(response_message.tool_calls[0].function.arguments)#函数参数

            function_response = fuction_to_call(**function_args)#函数手动调用

            #step_7:向messages进行两次消息追加
            messages.append(response_message.model_dump())  
            messages.append({
                        "role": "tool",
                        "content": function_response,
                        "tool_call_id":response_message.tool_calls[0].id
                    })

            #step_8: 再次调用大模型
            second_response = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V2.5",
                messages=messages)
            final_response = second_response.choices[0].message.content
        else:
            final_response = response_message.content
    return Markdown(final_response)
```

测试：

```python
messages = [
    {"role": "system", "content": md_content},
    {"role": "user", "content": "请问LC数据表有多少男性用户？"}
]
#定义外部函数库
available_functions = {
            "function": get_sql_result,
        }
auto_run_conversation(messages,available_functions)
```
