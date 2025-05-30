## 3、Deepseek-R1的API调用指南

### 3.1 快速开始

DeepSeek-R1正式版已于2025年1月20号正式上线，其强大的模型推理能力可以让DeepSeek-R1在数学、代码、自然语言推理等任务上取得很好的结果，性能比肩 OpenAI o1 正式版。

DeepSeek-R1的API调用也是非常简单的，但是在调用API之前需要我们完成API Key的申请：

- 访问DeepSeek官网：https://www.deepseek.com/，进入到API开放平台中

  <img src="imgs\Snipaste_2025-02-20_18-55-11.jpg" alt="Snipaste_2025-02-20_18-55-11" style="zoom: 80%;" />

- 进行API Key的申请：

  - 新用户注册即赠送10元额度，约500万token额度。
  - 价格方面，DeepSeek R1价格约为OpenAI o1正式版模型的1/50：

  <img src="imgs\Snipaste_2025-02-20_18-58-23.jpg" alt="Snipaste_2025-02-20_18-58-23" style="zoom: 50%;" />

  <img src="imgs\Snipaste_2025-02-20_18-59-29.jpg" alt="Snipaste_2025-02-20_18-59-29" style="zoom: 50%;" />

- 注意：

  - 目前DeepSeek R1模型调用不限速

    <img src="imgs\Snipaste_2025-02-20_19-02-59.jpg" alt="Snipaste_2025-02-20_19-02-59" style="zoom:77%;" />

  - API调用风格和OpenAI完全一致，但是暂不支持多模态和Function calling功能。

### 3.2 API调用规范

在Deepseek官网中有如下内容：

<img src="imgs\Snipaste_2025-02-20_19-06-15.jpg" alt="Snipaste_2025-02-20_19-06-15" style="zoom:80%;" />

**OpenAI安装：**

``pip install openai``

**调用实例：**

```python
from openai import OpenAI

ds_api_key = "YOUR_DS_API_KEY"

# 实例化客户端
client = OpenAI(api_key=ds_api_key, 
                base_url="https://api.deepseek.com")

# 调用 deepseek-r1 模型
response = client.chat.completions.create(
    #model="deepseek-chat" 调用Deepseek-V3模型,不存在推理过程
    #model="deepseek-coder" 调用的是DeepSeek的Coder模型,不存在推理过程。这个模型是专为代码相关任务而训练的，具有较强的代码生成、理解、修改和调试能力，适用于编程问答、代码补全、代码错误检测与修复等场景
    model="deepseek-reasoner", #调用推理模型deepseek-r1 模型标识/名称，存在推理过程
    messages=[
        {"role": "user", "content": "请问，9.8和9.11哪个更大？"}
    ]
)

# 最终回复
response.choices[0].message.content

# 思考链
response.choices[0].message.reasoning_content
```

注意，在上述代码中，r1模型不光可以返回模型对于用户提问的回答，还可以返回对于用户提问问题的具体推理/思考过程，该过程就是r1模型的思考链。而思考链也是r1模型和GPT的o1模型主要的一个区别。

**关于返回思考链的深度思考**

如果我们可以看到r1模型的思考过程的话，那么就可以根据这个思考过程的内容去创建非常多高质量的问答数据。在问答数据中，不仅会包含问题和答案，还会包含对于问题的思考过程。这也是Deepseek可以基于r1模型蒸馏了很多小尺寸模型的主要原因。

**Message参数设置方法**

  时至今日，“多角色” 对话基本上已经成了顶尖大模型的标配。正是基于多角色对话这一基础技术架构，大模型才能非常灵活的实现各类对话需求。而实际执行多角色对话的过程中，其核心是依靠messages参数来实现的。

messages（必填）

- `messages` 参数是 DeepSeek模型 API 中必填的参数之一，用于定义聊天上下文，包括用户的输入、系统的指令、助手的回复等。通过 `messages` 数组，模型可以理解当前对话的背景，从而生成更加连贯的响应。根据不同的使用场景，`messages` 包含多种类型的消息，例如 `system message`、`user message` 和 `assistant message`。下面是对 `messages` 参数及其各个子类型的详细解释。

  - **`content`** (必填)：系统消息的内容，可以是字符串或数组。如果是数组，可能包含多个类型的内容（如文本、图像）。
  - **`role`** (必填)：此处角色为 `system`，表明这是系统发出的消息。
  - **`name`** (可选)：提供系统消息发送者的名称，尤其适用于区分多个具有相同角色的参与者。
  
  示例代码：

  ```python
  response = client.chat.completions.create(
      model="deepseek-reasoner",
      messages=[
          {'role':'system','content':"你是一位滑稽且幽默的小品演员。"},
          {"role": "user", "content": "请问，你如何理解人生呢？"}
      ]
  )
  display(Markdown(response.choices[0].message.content))
  
  
  
  response = client.chat.completions.create(
      model="deepseek-reasoner", 
      messages=[
          {"role": "system", "content": "你是一位大学数学系教授"},
          {"role": "user", "content": "请问，你如何理解人生呢？"}
      ]
  )
  display(Markdown(response.choices[0].message.content))
  ```
  
  - 还有一个非常常见的`system message`的使用方法，就是借助system消息进行聊天背景信息的设定，很多时候我们可以在system消息中输入一段长文本，这段长文本将在聊天开始之前输入到系统中，而在之后的聊天中，即可让assistant围绕这个长文本进行回答，这是一种最简单的实现大语言模型围绕本地知识库进行问答的方法。
  
  ```python
  text = '张三，男，1990年10月25日出生于中国台湾省高雄市。\
          2013年毕业于北京工业大学的信息工程专业，由于在校表现良好，毕业后被中科院信息技术部破格录取。'
  response = client.chat.completions.create(
      model="deepseek-reasoner",  
      messages=[
          {"role": "system", "content": text},
          #请问张三是什么星座的？请问张三毕业后去哪里了？
          {"role": "user", "content": '请问张三是哪一年毕业的？'}
    ]
  )
  response.choices[0].message.content
  ```
  
  - `user message` 表示用户发给模型的消息，是对话的核心部分之一。它定义了用户的输入内容，模型根据这些内容生成响应。
  
    - **`content`** (必填)：用户消息的内容，通常为文本或图像链接的数组。对于支持图像输入的模型，如 DeepSeek v2.5 ，还可以传递图像。
    - **`role`** (必填)：角色为 `user`，表示该消息来自用户。
    - **`name`** (可选)：可以为用户指定一个名称，用于区分多个具有相同角色的用户。
  
    示例代码：
  
    ```python
    # 创建用户消息
    user_message = {
        "role": "user",
        "content": "你好，请介绍下你自己。"
    }
    ```
  
  - `assistant message`表示助手消息，是模型根据用户消息生成的响应。
  
    - **content**：类型为字符串，表示助手消息的内容，这是助手对用户提问的回答或执行任务的结果等。
  
    - **role**：类型为字符串，固定为 “assistant”，表示消息的作者角色是助手。
  
    - **name**：类型为字符串，表示对话参与者的名称，一般用于区分不同身份的助手。
  
      

### 3.3 多轮对话

#### 3.3.1 基本原理

首先，任何一款大模型在原始状态下都不会存在和用户对话的长期记忆，也就是所谓的上下文或者多轮对话机制。但是正是由于message参数包含多种类型的消息，例如 `system message`、`user message` 和 `assistant message`就可以实现“多轮对话”机制，使得模型可以具备上下文或者和用户长期对话记忆的能力。

我们只需要将模型返回的``assistant message``消息+用户新的提问``usermessage``拼接到模型的messages参数中，并再次向模型进行提问，即可非常便捷的实现多轮对话。

#### 3.3.2 封装实现

```python
from openai import OpenAI

ds_api_key = "sk-f010301e7xxx5214d14c30cce1e"
# 实例化客户端
client = OpenAI(api_key=ds_api_key, 
                base_url="https://api.deepseek.com")

def multi_chat_with_model(msg): #msg表示用户提出的问题
    text = '张三，男，1990年10月25日出生于中国台湾省高雄市。\
        2013年毕业于北京工业大学的信息工程专业，由于在校表现良好，毕业后被中科院信息技术部破格录取。'
    
    messages=[
        {"role": "system", "content": text},
        {"role": "user", "content": msg}
    ]
    while True:
        response = client.chat.completions.create(
            model="deepseek-reasoner",  
            messages=messages
        )
        
        # 获取模型回答
        answer = response.choices[0].message.content
        print(f"模型回答: {answer}")


        # 询问用户是否还有其他问题
        user_input = input("您还有其他问题吗？(输入退出以结束对话): ")
        if user_input == "退出":
            break
            
        # 记录用户回答
        messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": user_input})

#多轮对话测试
multi_chat_with_model('张三哪一年毕业的？')
```

## 4、Agent智能体开发

### 4.1 Agent简介

Agent智能体是一个由人工智能驱动的系统或程序，能够在一定的环境中自主感知、决策和执行任务。它模拟或扩展了人类或其他生物的智能行为，旨在解决复杂问题或完成特定目标。可以广泛应用与自动驾驶、智能客服、游戏NPC、金融分析、医疗诊断等多个领域。

在Agent智能体的开发过程中，有一种实现机制，可以使得开发者可以定义、管理和调用各种函数来实现复杂的任务。这些函数可以封装具体的业务逻辑、算法或外部服务调用等。这种机制就是Function Calling！因此，**Function Calling是Agent智能体开发的基础**。  

同时，**Agent智能体利用Function Calling增强能力**。因为，Agent智能体通过调用外部函数或服务（即Function Calling），可以访问实时数据、执行特定算法或调用其他资源来完成其任务。这种能力使得Agent智能体能够更加灵活地适应不同的应用场景和需求。

因此，随着AI技术的不断发展，Agent智能体和Function Calling都在不断地演进和完善。两者相互促进、相互影响，共同推动了AI技术的创新和应用落地。

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
```

因此修改tool参数值为：

```python
tools = [
    {
        "type": "function", 
        "function":get_weather_function
    }
]
```

同时还需要封装外部函数库，用于关联外部函数名称和外部函数对象

```python
available_functions = {
            "get_weather": get_weather,
        }
```

#### 4.3.6 Function calling实现

##### First response

在进行了一系列基础准备工作之后，接下来我们尝试在Chat模型对话执行Function calling功能。首先我们测试模型本身能否知道如何查询天气：

```python
from openai import OpenAI
#硅基流动API
ds_api_key = "sk-atisrrfnrxsnuxxxkriejlfxlvnymvfxoesps"
client = OpenAI(api_key=ds_api_key, 
                base_url="https://api.siliconflow.cn/v1")
```

```python
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V2.5",  
     messages=[
        {"role": "user", "content": "请帮我查询北京地区今日天气情况"}
    ], 
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

这里我们只需要借助\**方法，直接将function_args对象传入fuction_to_call中，即可一次性传输全部参数，**方法的功能可以参考如下示例：

```python
def function_to_call_test(a, b, c):
    return a + b + c

function_args_test = {'a': 1, 'b': 2, 'c': 3}

result = function_to_call_test(**function_args_test)

print(result)
```

**方法其实是一种较为特殊、但同时也非常便捷的参数传递方法吗，该方法会将字典中的每个key对应的value传输到同名参数位中。接下来我们将function_args对象传入fuction_to_call中并完成计算：

```python
function_response  = fuction_to_call(**function_args) #get_weather(loc="Beijing")
function_response  #获取函数调用结果
```

能够发现，模型已经顺利完成计算。接下来我们在messages对象中追加两条消息，第一条消息是第一次模型返回的结果（即调用模型的assistant message），第二条消息则是外部函数计算结果，该条消息的role为function，且name为函数名称。这也是我们首次接触function message，和user、system、assistant message不同，function message必须要输入关键词name，且function message的内容源于外部函数执行的计算结果，并且需要手动进行输入。具体添加过程如下：

- 追加第一条消息：模型返回的结果

  ```python
  #展示目前messages内容
  print(messages)
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
