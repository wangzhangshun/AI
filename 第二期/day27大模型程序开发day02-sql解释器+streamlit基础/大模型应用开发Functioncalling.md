## 自我介绍

张晓波：bobo老师

- 工信部认聘的数据分析和人工智能专家组专家，2024参与数字化人才《岗位能力标准》的制订工作。

- 华为认证AI大模型专家讲师

<img src="imgs/image-20250515161541997.png" alt="image-20250515161541997" style="zoom: 50%;" />

​																		**专业的事交给专业的人去做**



### 有言在先

- 授课风格：
  - 没有鸡汤、没有段子。有认真负责的态度、有传道受业解惑的**育人之志**和**启智之能**。
- 学习方法
  - 课上动脑听、课下用心练、笔记常翻译、消化在心中
- 授课相关：``好的授课过程就好比是谈一场恋爱，从来都不是一个人的事``
  - 节奏快慢
  - 内容动态补充
  - 授课内容+顺序
  - ......
- Finally：
  - 人无完人，每个人都有不同的短板和不足之处。互相理解、互相适应、搞定AI、成就大计！

### 核心内容

- Functioncalling技术实现
- Streamlit+大模型应用
- RAG+Agent+Streamlit项目实战
- MCP深度应用
- OpenAI Agents SDK（openai在25年推出的企业级Multi-Agent开发框架）
  - Agents SDK接入MCP
- 模型本地部署+调用（ollama+企业级）
- 模型微调
- 微软-GraphRAG应用开发

## 4、Function Calling

### 4.2 Function Calling简介

#### 4.2.1 背景和定义

我们都知道大语言模型的知识储量是巨大，并且它具备非常强大的原生能力，但是有时候我们在实际使用大模型时会感受到大模型能力上的某些局限，比如大模型无法回答超过大模型知识库截止日期之后发生的相关信息和知识，并且大模型只能给出文字的建议但无法直接帮我们解决某些实际操作性的问题（如自动进行邮件收发、自动预定车票等）。因此，这些问题的存在会极大程度上限制了大模型的实际应用价值。

在这一基本背景下，Function calling功能应运而生。该功能的本质是让大模型具有调用外部函数的能力。也就是说，当大模型遇到超出自身能力范围的需求时，可以通过访问相应的外部函数寻求解决方案。这样，大模型就可以不再仅仅根据自身的知识库进行回答，还可以额外挂载一个外部函数库，然后根据用户提问进行外部函数的检索，根据实际需求调用外部函数并获取函数运行结果，再基于函数运行结果进行回答。

毫无疑问，有了外部函数库的功能加持，大模型的处理和解决问题的能力也必将再上一个台阶。

#### 4.2.2 **核心原理**

<img src="imgs\Snipaste_2025-02-21_09-18-50.jpg" alt="Snipaste_2025-02-21_09-18-50" style="zoom:67%;" />

#### **在Agent中的应用**：

<img src="imgs\Snipaste_2025-02-21_09-20-27.jpg" alt="Snipaste_2025-02-21_09-20-27" style="zoom: 80%;" />

### 4.3 实时气象查询Agent开发

#### 4.3.1 项目背景

OpenWeather是一家提供全球范围内的气象数据服务的公司，该公司的服务包括实时天气信息、天气预报、历史天气数据以及各种气象相关的报告等，并且OpenWeather开放了一定使用限度内完全免费的API，即我们可以在代码环境中通过调用OpenWeather API来进行实时天气查询、天气预报等功能，这意味着开发者可以将OpenWeather的天气预报功能加入到他们自己的应用或网站中。

#### 4.3.2 OpenWeather注册及API key获取方法

为了能够调用OpenWeather服务，和OpenAI的API使用过程类似，我们首先需要先注册OpenWeather账号，并获取OpenWeather API Key。这里需要注意的是，对于大多数在线服务的API来说，都需要通过API key来进行身份验证，尽管OpenWeather相对更加Open，有非常多的免费使用的次数，但身份验证仍然是必要的防止API被滥用的有效手段。OpenWeather API key获取流程如下：

- Step 1.登录OpenWeather官网并点击Sign—>create account完成注册。该网站无需魔法即可直接登录，可以使用国内邮箱或者QQ邮箱均可进行注册，官网地址为：https://openweathermap.org/

  <img src="imgs\Snipaste_2025-02-21_09-26-52.jpg" alt="Snipaste_2025-02-21_09-26-52" style="zoom:80%;" />

  <img src="imgs\Snipaste_2025-02-21_09-26-59.jpg" alt="Snipaste_2025-02-21_09-26-59" style="zoom:80%;" />

  

- Step 2.获取API-key：注册完成后，即可在API keys页面查看当前账户的API key：

  <img src="imgs\Snipaste_2025-02-21_09-27-08.jpg" alt="Snipaste_2025-02-21_09-27-08" style="zoom:80%;" />

  <img src="imgs\Snipaste_2025-02-21_09-27-15.jpg" alt="Snipaste_2025-02-21_09-27-15" style="zoom:80%;" />

  一般来说完成注册后，就会有一个已经激活的API-key。和OpenAI一样，OpenWeather的API key也可以创建多个。

- Step 3.将其设置为环境变量：和OpenAI API key类似，为了方便后续调用，我们也可以直接将OpenWeather API key设置为环境变量，变量名为OPENWEATHER_API_KEY。具体设置环境变量的方法参考Ch.1中OpenAI APkey设置环境变量流程，此处不再赘述。

  <img src="imgs\Snipaste_2025-02-21_09-27-22.jpg" alt="Snipaste_2025-02-21_09-27-22" style="zoom:80%;" />

  设置完了环境变量之后，接下来即可按照如下方式创建OpenWeather API key变量：

  ```python
  open_weather_key = os.getenv("OPENWEATHER_API_KEY")
  ```

  

#### 4.3.3 获取实时天气信息API

```python
import requests

# Step 1.构建请求
url = "https://api.openweathermap.org/data/2.5/weather"

# Step 2.设置查询参数
params = {
    "q": "Beijing",               # 查询北京实时天气
    "appid": "xxx",    # 输入API key
    "units": "metric",            # 使用摄氏度而不是华氏度
    "lang":"zh_cn"                # 输出语言为简体中文
}

# Step 3.发送GET请求
response = requests.get(url, params=params)

# Step 4.解析响应
data = response.json()
print(data)

# 即时温度最高、最低气温
data['main']['temp_min'], data['main']['temp_max']
# 天气状况
data['weather'][0]['description']
```

这里需要注意的是，城市名必须输入英文名，否则无法正确识别。

**外部函数创建：**我们尝试编写一个通过OpenWeather API实时获取天气信息的API，并作为模型可调用的外部函数之一。很明显，为了确保和大语言模型之间的顺畅通信，此时要求函数的输入和输出都是字符串格式。具体函数编写如下：

**这里需要注意函数说明和参数解释的书写风格**

```python
def get_weather(loc):
    """
    查询即时天气函数
    :param loc: 必要参数，字符串类型，用于表示查询天气的具体城市名称，\
    注意，中国的城市需要用对应城市的英文名称代替，例如如果需要查询北京市天气，则loc参数需要输入'Beijing'；
    :return：OpenWeather API查询即时天气的结果，具体URL请求地址为：https://api.openweathermap.org/data/2.5/weather\
    返回结果对象类型为解析之后的JSON格式对象，并用字符串形式进行表示，其中包含了全部重要的天气信息
    """
    # Step 1.构建请求
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Step 2.设置查询参数
    params = {
        "q": loc,               
        "appid": 'xxx',    # 输入API key
        "units": "metric",            # 使用摄氏度而不是华氏度
        "lang":"zh_cn"                # 输出语言为简体中文
    }

    # Step 3.发送GET请求
    response = requests.get(url, params=params)
    
    # Step 4.解析响应
    data = response.json()
    return json.dumps(data)
```

函数测试：

```python
#测试函数是否可用
import json
get_weather('GuangZhou')
```

邮件发送外部函数：

```python
def send_mail(msg):
    """
    该函数是用于进行指定邮件发送的。
    :param msg: 必要参数，字符串类型，该参数表示要发送的邮件内容
    :return：邮件发送成功后的状态信息
    """
    return '邮件已经成功发送，邮件内容是:'+msg
```



#### 4.3.4 tools参数解释与定义

在准备好外部函数之后，接下来非常重要的一步就是需要将外部函数的信息以某种形式传输给模型。此时就需要使用到create函数的tools参数.从参数的具体形式来看，tools参数是一个可以包含多个字典的list，每个字典都需要包含两个键值对，分别是 **{type:function，function:外部函数的完整描述}**。因此每个字典都代表一个外部函数的相关信息。在大语言模型实际进行问答时，会根据tools参数提供的信息对各外部函数进行检索。

```python
tools = [
    {
        "type": "function", 
        "function":'外部函数的完整描述'
    }
]
```

#### 4.3.5 外部函数完整描述

外部函数的完整描述对于Function calling功能的实现至关重要。因为在大模型进行实际问答时，会根据对外部函数的完整描述信息的语义理解进行外部函数的检索和调用。

接下来我们详细解释外部函数完整描述的指定写法。总的来说，我们会使用一个字典来对其进行完整描述，每个字典都有三个参数（三组键值对），各参数（Key）名称及解释如下：

- name：代表函数函数名称字的符串，必选参数。
- description：用于描述函数功能的字符串，虽然是可选参数，但该参数传递的信息实际上是Chat模型对函数功能识别的核心依据。即Chat函数实际上是通过每个函数的description来判断当前函数的实际功能的。
- parameters：函数的参数说明，必选参数，要求遵照JSON Schema格式进行输入，JSON Schema是一种特殊的JSON对象，专门用于验证JSON数据格式是否满足要求。

例如，对于get_weather函数，我们需要创建如下字典来对其进行完整描述：

```python
get_weather_function = {
    'name': 'get_weather',
    'description': '查询即时天气函数，根据输入的城市名称，查询对应城市的实时天气',
    'parameters': {
        'type': 'object', #json对象类型
        'properties': { #参数成员描述
            'loc': {
                'description': "城市名称，注意，中国的城市需要用对应城市的英文名称代替，例如如果需要查询北京市天气，则loc参数需要输入'Beijing'",
                'type': 'string'
            }
        },
        'required': ['loc']
    }
}

send_mail_function = {
    'name': 'send_mail',
    'description': '该函数是用于进行指定邮件发送的',
    'parameters': {
        'type': 'object', #json对象类型
        'properties': { #参数成员描述
            'msg': {
                'description': "必要参数，字符串类型，该参数表示要发送的邮件内容",
                'type': 'string'
            }
        },
        'required': ['msg']
    }
}
```

因此修改tool参数值为：

```python
tools = [
    {
        "type":'function',
        'function':get_weather_function
    },
    {
        "type":'function',
        'function':send_mail_function
    }
]
```

同时还需要封装外部函数库，用于关联外部函数名称和外部函数对象

```python
available_functions = {
            "get_weather": get_weather,
            "send_mail":send_mail
        }
```

#### 4.3.6 Function calling实现

##### First response

在进行了一系列基础准备工作之后，接下来我们尝试在Chat模型对话执行Function calling功能。首先我们测试模型本身能否知道如何查询天气：

```python
from openai import OpenAI
#硅基流动API
ds_api_key = "sk-atisrxxxriejlfxlvnymvfxoesps"
client = OpenAI(api_key=ds_api_key, 
                base_url="https://api.siliconflow.cn/v1")
```

```python
messages = [
        {"role": "user", "content": "请帮我查询上海地区今日天气情况"}
    ]
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V2.5",  
     messages=messages, 
    )
        
response.choices[0].message.content
```

很明显，模型无法进行回答。接下来我们尝试将函数库相关信息输入给Chat模型

```python
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V2.5",  
    messages=[
        {"role": "user", "content": "请帮我查询北京地区今日天气情况"}
    ],
    tools=tools,
)

        
response_message = response.choices[0].message
response_message
```

返回结果：

```python
ChatCompletionMessage(content='', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='0195279d5095aab2d4ac52760de27c04', function=Function(arguments='{"loc":"Beijing"}', name='get_weather'), type='function')])
```

能够发现，此时返回的message中content为空，而增了一个"tool_calls"的list，该list就包含了当前调用外部函数的全部信息：

```python
response_message.tool_calls[0]
```

返回结果：

```python
ChatCompletionMessageToolCall(id='0195279d5095aab2d4ac52760de27c04', function=Function(arguments='{"loc":"Beijing"}', name='get_weather'), type='function')
```

对于当前CompletionMessageToolCall对象，id为外部函数调用发起请求id，function则表示调用外部函数基本信息，而type则代表了当前当前调用外部函数类型，function代表调用自定义的外部函数。

我们可以在此基础上分别提取调用外部函数名称信息和参数信息，分别保存为function_name和function_args对象：

```python
# 完成对话需要调用的函数名称
function_name = response_message.tool_calls[0].function.name
function_name

# 基于外部函数库获取具体的函数对象
fuction_to_call = available_functions[function_name]
fuction_to_call

'''
        available_functions = {
                    "get_weather": get_weather,
                }
'''

# 执行该函数所需要的参数，将其反序列化成字典对象，便于下一步函数调用时进行传输传递
function_args = json.loads(response_message.tool_calls[0].function.arguments)
function_args
```

需要注意的是，外部函数的计算过程仍然是在本地执行，即Chat模型并不会将代码读取到服务器上再进行在线计算，因此接下来我们需要根据模型返回的函数和函数参数，在本地完成函数计算，然后再将计算过程和结果保存为message并追加到messages后面，并第二次调用Chat模型分析函数的计算结果，并最终根据函数计算结果输出用户问题的答案。

##### Second response

```python
function_response  = fuction_to_call(**function_args) #get_weather(loc="Beijing")
function_response  #获取函数调用结果
```

能够发现，模型已经顺利完成计算。接下来我们在messages对象中追加两条消息，第一条消息是第一次模型返回的结果（即调用模型的assistant message），第二条消息则是外部函数计算结果，该条消息的role为function，且name为函数名称。这也是我们首次接触function message，和user、system、assistant message不同，function message必须要输入关键词name，且function message的内容源于外部函数执行的计算结果，并且需要手动进行输入。具体添加过程如下：

- 追加第一条消息：模型返回的结果

  ```python
  #将模型第一次返回的结果转换成字典类型，目的是为了将其追加到messages列表中
  response_message.model_dump()
  # 向messages追加第一次模型返回结果消息
  messages.append(response_message.model_dump())  
  #查看追加后的messages
  print(messages)
  ```
  
- 追加第二条消息：外部函数计算结果

  ```python
  # 追加function返回消息
  messages.append({
              "role": "tool",
              "content": function_response,
              "tool_call_id":response_message.tool_calls[0].id
          })
  ```

接下来，再次调用Chat模型来围绕messages进行回答。需要注意的是，此时我们不再需要向模型重复提问，只需要简单的将我们已经准备好的messages传入Chat模型即可：

```python
second_response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V2.5",
    messages=messages)

second_response.choices[0].message.content
```

能够发现，模型最终做出了准确回答。

##### 完整封装

```python
def run_conv(messages, 
             api_key,
             tools=None, 
             functions_list=None,
             model="deepseek-ai/DeepSeek-V2.5"):
    """
    能够自动执行外部函数调用的Chat对话模型
    :param messages: 必要参数，输入到Chat模型的messages参数对象
    :param api_key: 必要参数，调用模型的API-KEY
    :param tools: 可选参数，默认为None，可以设置为包含全部外部函数的列表对象
    :param model: Chat模型，可选参数，默认模型为deepseek-chat
    :return：Chat模型输出结果
    """
    user_messages = messages
    #基于硅基流动API
    client = OpenAI(api_key=api_key, 
                base_url="https://api.siliconflow.cn/v1")

    # 如果没有外部函数库，则执行普通的对话任务
    if tools == None:
        response = client.chat.completions.create(
            model=model,  
            messages=user_messages
        )
        final_response = response.choices[0].message.content

    # 若存在外部函数库，则需要灵活选取外部函数并进行回答
    else:
        # 创建外部函数库字典
        available_functions = {func.__name__: func for func in functions_list}

        # 创建包含用户问题的message
        messages = user_messages

        # first response
        response = client.chat.completions.create(
            model=model,  
            messages=user_messages,
            tools=tools,
        )
        response_message = response.choices[0].message

        # 获取函数名
        function_name = response_message.tool_calls[0].function.name
        # 获取函数对象
        fuction_to_call = available_functions[function_name]
        # 获取函数参数
        function_args = json.loads(response_message.tool_calls[0].function.arguments)

        # 将函数参数输入到函数中，获取函数计算结果
        function_response = fuction_to_call(**function_args)

        # messages中拼接first response消息
        user_messages.append(response_message.model_dump())  

        # messages中拼接外部函数输出结果
        user_messages.append(
            {
                "role": "tool",
                "content": function_response,
                "tool_call_id":response_message.tool_calls[0].id
            }
        )

        # 第二次调用模型
        second_response = client.chat.completions.create(
            model=model,
            messages=user_messages)

        # 获取最终结果
        final_response = second_response.choices[0].message.content

    return final_response
```

无需外部函数加持的情况：

```python
messages = [{"role": "user", "content": "请问什么是机器学习？"}]
run_conv(messages=messages, 
         api_key = ds_api_key)
```

需要外部函数加持的情况：

```python
messages = [{"role": "user", "content": "请问北京今天天气如何？"}]
run_conv(messages=messages, 
         api_key = ds_api_key,
         tools=tools, 
         functions_list=[get_weather])
```

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
        
        api_key = "sk-4b79f3axxx366ebb425b3"
        client = OpenAI(api_key=ds_api_key, 
                base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-reasoner",  
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
