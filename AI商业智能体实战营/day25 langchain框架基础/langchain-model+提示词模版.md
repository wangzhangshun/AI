## 1. 什么是LangChain

LangChain现在归属于LangChain AI公司，LangChain作为其中的一个核心项目，开源发布在Gitub上：https://github.com/langchain-ai/langchain

LangChain给自身的定位是：用于开发由大语言模型支持的应用程序的框架。它的做法是：通过提供标准化且丰富的模块抽象，构建大语言模型的输入输入规范，利用其核心概念`chains`，灵活地连接整个应用开发流程。而针对每个功能模块，都源于对大模型领域的深入理解和实践经验，开发者提供出来的标准化流程和解决方案的抽象，再通过灵活的模块化组合，才有了目前这样一款在大模型应用开发领域内被普遍高度认可的通用框架。

### 1.1 为什么需要学习LangChain？

首先，我们需考虑当前大模型的发展态势。尽管OpenAI的GPT系列模型作为大模型领域的`领军人物`，在很大程度上了影响了大模型的使用规范和基于大模型进行应用开发的范式，但并不意味着所有大模型间的使用方式完全相同。因此，对于每个新模型都要花费大量时间学习其特定规范再进行应用探索，这种工作效率显然是十分低下的。

其次，必须谈论的是大模型目前面临的局限，如知识更新的滞后性、外部API调用能力、私有数据连接方式以及输出结果的不稳定性等问题。在应用开发中，如何找到这些问题的有效解决策略？

上述提到的每个限制都紧密关联于大模型本身的特性。尽管理论上可以通过重新训练、微调来增强模型的原生能力，这种方法确实有效，但实际上，大多数开发者并不具备进行这样操作所需的技术资源、时间和财力，选择这条路径一定会导致方向越来越偏离目标。我们之前讨论的Function Calling接入第三方API能够提供一些解决方案，但这每一步都需大量的研发投入，而且最终实现后的应用效果，也取决于研发人员的个人技术能力。在这种背景下，既然大家都有不同的想法和解决方案，那LangChain就来集中做这件事，提供一个统一的平台和明确的定义，来实现应用框架的快速搭建，这就是LangChain一直想要做到，且正在做的事情。

### 1.2 LangChain的做法

从本质上分析，LangChain还是依然采用从大模型自身出发的策略，通过开发人员在实践过程中对大模型能力的深入理解及其在不同场景下的涌现潜力，使用模块化的方式进行高级抽象，设计出统一接口以适配各种大模型。到目前为止，LangChain抽象出最重要的核心模块如下：

**模型（Model I/O）**

LangChain支持主流的大型语言模型哦，像DeepSeek这种，它都能轻松对接并进行接口调用。并且langchain还合理规范了大模型的输入（提示词）和输出（输出解析器）。

**提示模板（Prompts）**

这个提示模板功能可不得了！它可以动态地生成提示词哦。比如说，我们可以根据具体的任务需求，让系统自动生成合适的提示词来引导模型进行回答或者操作。

**链（Chains）**

想象一下，我们要把多个任务步骤连接起来，形成一个完整的工作流程，就像搭建一条流水线一样，这就是链（Chains）的作用啦。比如说，我们可以把“用户输入 → 检索知识库 → 模型生成 → 结果解析”这样一个流程串联起来，形成一个高效的工作流。这样一来，每个步骤都能有条不紊地进行，大大提高了工作效率。

**记忆（Memory）**

记忆这个组件也很关键哦。它可以帮助我们管理对话历史呢。这里面又分为短时记忆和长时记忆。短时记忆就像是我们的短期记忆，主要是会话上下文，能让我们记住当前这次对话的一些关键信息；长时记忆呢，就像是长期存储在大脑里的知识一样，它会把数据存储到数据库里，方便我们以后随时查阅和使用。

**代理（Agents）**

代理这个组件就像一个聪明的小助手，它可以动态地调用外部工具哦。比如说，当我们需要计算一些复杂的数学问题时，它可以调用计算器这个外部工具来帮忙；要是我们需要查找一些特定的信息，它还能调用搜索引擎为我们寻找答案呢。这样一来，就大大扩展了模型的功能，让它能做更多的事情啦。

**数据检索（Indexes）**

最后再给大家介绍一下数据检索这个组件哈。它能集成向量数据库，然后构建本地知识库哦。这就好比是为模型建立了一个专属的知识宝库，当模型需要回答问题的时候，就可以从这个宝库里获取更准确、更丰富的信息，从而提高回答的准确性。

## 2. langchain环境安装

LangChain的安装过程非常简单，可以通过常用的Python包管理工具，如pip或conda，直接进行安装。稍复杂一点的还可以通过源码进行安装。但有一点大家一定要明确：LangChain的真正价值在于它能够与多种模型提供商、数据存储解决方案等进行集成。默认情况下，使用上述两种安装方式中的任意一种来进行LangChain安装后，安装的仅仅是LangChain的默认功能，并不包括这些集成所需的额外依赖项。

也就是说，如果我们想要使用特定的集成功能，还需要额外安装这些特定的依赖。以调用OpenAI的API为例，我们首先需要通过运行命令`pip install langchain-openai`安装OpenAI的合作伙伴包，安装此依赖包后，LangChain才能够与OpenAI的API进行交互。后续我们在使用相关功能的时候，会提供额外的说明。

> LangChain安装官方说明文档：https://python.langchain.com/docs/get_started/installation

### 2.1 使用包版本管理工具安装

**LangChain可以使用pip 或者 conda直接安装，适用于仅使用的场景，即不需要了解其源码构建过程。**这种安装方法十分简洁明了，只需执行一条命令，就可以在当前的虚拟环境中迅速完成LangChain的安装。具体操作如下：

```
pip install langchain=0.3.20
```

验证LangChain的安装情况，执行命令如下：

```python
import langchain

print(langchain.__version__)
```

如果能正常输出LangChain的版本，说明在当前环境下的安装成功。

### 2.2 源码安装

除了通过pip安装外，还有一种通过源码安装的方法。这需要使用git拉取远程仓库，然后进入项目文件夹并执行`pip install -e .`命令。这种方法不仅会安装必要的依赖，同时也将程序的源代码保存在本地**对于课程学习而言，我们推荐采用源码安装方式，这将非常有助于在后续的LangChain功能探索中，通过源码分析深入理解框架的构建原理和详细机制。**

源码安装LangChain的详细步骤：

- **Step 1. 安装Anaconda**

  按照对应的教程内容配置好Anaconda。

- **Step 2. 使用Conda创建LangChain的Python虚拟环境**

  安装好Anaconda后，我们需要借助Conda包版本工具，为LangChain项目创建一个新的Python虚拟运行环境，执行代码如下：`conda create --name langchain python==3.11`

  创建完成后，通过如下命令进入该虚拟环境，执行后续的操作：`conda activate langchain`

- **Step 3. 下载LangChain的项目文件**

  进入LangChain的官方Github，地址：https://github.com/langchain-ai/langchain ， 在 GitHub 上将项目文件下载到有两种方式：克隆 (Clone) 和 下载 ZIP 压缩包。推荐使用克隆 (Clone)的方式。

- **Step 4. 升级pip版本**

  建议在执行项目的依赖安装之前升级 pip 的版本，如果使用的是旧版本的 pip，可能无法安装一些最新的包，或者可能无法正确解析依赖关系。升级 pip 很简单，只需要运行命令如下命令：

  `python -m pip install --upgrade pip`

- **Step 5. 源码安装项目依赖**

  不同于我们之前一直使用的`pip install -r requirements.txt`方式，这种方法用于批量安装多个依赖包，是在部署项目或确保开发环境与其他开发者/环境一致时的常用方式。而对于LangChain，我们需要使用`pip install -e `的方式，以可编辑模式安装包。这种方式主要用于开发过程中。当以可编辑模式安装一个包时，依赖包会被直接从源代码所在位置安装，而不是复制到Python的site-packages目录，是开发模式下用于安装并实时反映对本地包更改的方法。需要执行的步骤如下：

  ```
  cd langchain-master/libs/langchain/ #进入到LangChain源码的libs下的langchain目录中
  
  pip install -e .
  ```

如在安装过程未发生任何报错，则说明安装成功。在安装完依赖后，我们就正式进入LangChain的Model I/O模块的实践。

## 3.Models I/O模块

LangChain的Model I/O模块提供了标准的、可扩展的接口实现与大语言模型的外部集成。所谓的Model I/O，包括模型输入（Prompts）、模型输出（OutPuts）和模型本身（Models），简单理解就是通过该模块，我们可以快速与某个大模型进行对话交互

任何语言模型应用的核心都是大语言模型（LLMs）。因此，在讨论和实践Model I/O模块时，首先应当关注如何集成这些大模型。因此，接下来我们首先学习：如何借助LangChain框架使用不同的大模型。

### 3.1 LangChain接入大模型的方法

LangChain 提供了一套与任何大语言模型进行交互的标准构建模块。所以需要明确的一点是：**虽然 LLMs 是 LangChain 的核心元素，但 LangChain 本身不提供 LLMs，它仅仅是为多种不同的 LLMs 进行交互提供了一个统一的接口。**简单理解：以OpenAI的GPT系列模型为例，如果我们想通过 LangChain 接入 OpenAI 的 GPT 模型，我们需要在LangChain框架下先定义相关的类和方法来规定如何与模型进行交互，包括数据的输入和输出格式以及如何连接到模型本身。然后按照 OpenAI GPT 模型的接口规范来集成这些功能。通过这种方式，LangChain 充当一个桥梁，使我们能够按照统一的标准来接入和使用多种不同的大语言模型。

需要安装OpenAI的集成依赖包`langchain-openai`，执行如下命令： `pip install langchain-openai`

LangChain作为一个应用开发框架，需要集成各种不同的大模型，通过Message数据输入规范，可以定义不同的role，即system、user和assistant来区分对话过程。LangChain目前就抽象出来的消息类型有 AIMessage 、 HumanMessage 、 SystemMessage 和FunctionMessage，但大多时候我们只需要处理 HumanMessage 、 AIMessage 和 SystemMessage，即：

- SystemMessage ：用于启动 AI 行为，作为输入消息序列中的第一个传入。
- HumanMessage ：表示来自与聊天模型交互的人的消息。
- AIMessage ：表示来自聊天模型的消息。这可以是文本，也可以是调用工具的请求。

因此我们需要导入如下模块：

```python
from langchain_openai import OpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
```

**消息形式输入调用**

- 定义消息对象：

```python
messages = [
  	SystemMessage(content="你是个取名大师，你擅长为创业公司取名字"),
		HumanMessage(content="帮我给信公司取个名字，要包含AI")
]
```

- 执行推理：

```python
API_KEY = open('deepseekAPI-Key.md').read().strip()
chat = ChatOpenAI(
        model_name="deepseek-chat",
        api_key=API_KEY,
        base_url="https://api.deepseek.com"
                 )
reponse = chat.invoke(messages) #处理单条输入
reponse.content
```

- 流式调用

```python
for chunk in chat.stream(messages):
    print(chunk.content, end="", flush=True)
```

- 批量调用

```python
#先定义三个不同的消息对象：
messages1 = [SystemMessage(content="你是一位乐于助人的智能小助手"),
HumanMessage(content="请帮我介绍一下什么是机器学习"),]

messages2 = [SystemMessage(content="你是一位乐于助人的智能小助手"),
HumanMessage(content="请帮我介绍一下什么是深度学习"),]

messages3 = [SystemMessage(content="你是一位乐于助人的智能小助手"),
HumanMessage(content="请帮我介绍一下什么是大模型技术"),]

#将上述三个消息对象放在一个列表中，使用.batch方法执行批量调用
reponse = chat.batch([messages1,
                      messages2,
                      messages3,])

contents = [msg.content for msg in reponse]
for content in contents:
    print(content, "\n---\n")
```

### 3.2 LangChain接入指定类型大模型

针对不同的模型，LangChain也提供个对应的接入方法，其相关说明文档地址（只可以接入文档中有的模型）：https://python.langchain.com/docs/integrations/chat/

比如我们以DeepSeek的在线API模型为例快速接入一下：https://python.langchain.com/docs/integrations/chat/deepseek/

环境安装：`pip install -qU langchain-deepseek`

```python
from langchain_deepseek import ChatDeepSeek
fp_ds = open('./key_files/deepseekAPI-Key.md','r')
ds_key = fp_ds.readline().strip()

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=ds_key
)
messages = [
    (
        "system",
        "你是一位乐于助人的智能小助手",
    ),
    ("human", "请帮我介绍一下什么是大模型技术"),
]
ai_msg = llm.invoke(messages)
ai_msg.content
```

- 思考：ChatOpenAI和ChatDeepSeek两种模型接入的区别？

``基于ChatOpenAI接入DeepSeek大模型适合追求接口兼容性和快速迁移的场景，而基于ChatDeepSeek接入则更适合需要深度定制和发挥DeepSeek特有功能的场景。选择哪种方式取决于具体的应用需求、开发团队的技能背景以及对性能和定制化的要求。``

### 3.3 LangChain接入本地大模型

LangChain使用Ollama接入本地化部署的开源大模型。环境安装：`pip install langchain-ollama`

```python
from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
#实例化大模型
ollama_llm = ChatOllama(model="deepseek-r1:7b")
messages = [
    HumanMessage(
        content="你好，请你介绍一下你自己",
    )
]
#可以直接调用invoke方法实现模型推理
chat_model_response = ollama_llm.invoke(messages)
#获取纯净的模型推理结果，即去除掉特殊字符\n。
chat_model_response.content.replace('\n', '')

```

**更多调用参数**`model`、`system`、`temperature`等参数

```python
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
#实例化大模型
ollama_llm = ChatOllama(
    model="deepseek-r1:7b",
    # 添加temperature
    temperature=0,
    # 添加系统信息
    system="你是一位优秀且具有丰富经验的算法教授",
    # 添加format指定输出的内容形式
    format='json'
)
messages = [
    HumanMessage(
        content="你好，请你帮我详细的介绍一下什么是机器学习",
    )
]
#可以直接调用invoke方法实现模型推理
chat_model_response = ollama_llm.invoke(messages)
chat_model_response
```

### 3.4 LangChain中如何使用提示词模版

提示工程（Prompt Engineering）大家应该比较熟悉，这个概念是指在与大语言模型（LLMs），如GPT-3、DeepSeek等模型进行交互时，精心设计输入文本（即提示）的过程，以获得更精准、相关或有创造性的输出。目前，提示工程已经发展成为一个专业领域，非常多的公司设立了专门的职位，负责为特定任务编写精确且具有创造力的提示。

以使用DeepSeek等网页端对话交互应用中，大部分人常见的做法是将提示（Prompt）做硬编码，例如将一段提示文本固定在System Messages中。而在应用开发领域，开发者往往无法预知用户的具体输入内容，同时又希望大模型能够根据不同的应用任务以一种较为统一的逻辑来处理用户输入。所以，LangChain通过提供指定的提示词模版功能，优雅地解决了这个问题。提示词模版功能就是将用户输入到完整格式化提示的转换逻辑进行封装，使得模型能够更灵活、高效地处理各种输入。

LangChain 提供了创建和使用提示模板的各种工具。

#### 3.4.1 PromptTemplate

PromptTemplate 是 LangChain 提示词组件的核心类，其构造提示词的过程本质上就是实例化这个类。在实例化 PromptTemplate 类时，需要提供两个关键参数：`template` 和 `input_variables`。

- **template**: 这是一个字符串，表示你想要生成的提示词模板。例如，如果你想要一个用于生成故事的提示词，你的模板可能是 "Once upon a time in {location}, there was a {character}..."。
- **input_variables**: 这是一个字典，包含了所有你希望在提示词中出现的变量。这些变量会在 `template` 字符串中被替换。例如，对于上面的模板，你可能需要提供一个包含 `location` 和 `character` 键的字典。

准备好这两个参数后，你可以实例化一个基础的 PromptTemplate 类，生成的结果就是一个 PromptTemplate 对象，也就是一个 PromptTemplate 包装器。这个包装器可以在 LangChain 的各个链组件中被调用，从而在整个应用中复用和管理提示词模板。

以下是一个简单的示例代码，展示了如何实例化和使用 PromptTemplate 类：

```python
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # 假设使用 OpenAI 的聊天模型作为示例

# 定义模板和输入变量
template_str = (
    "你是一个专业的翻译助手，擅长将{input_language}文本准确翻译成{output_language}。"
    "请翻译以下内容：'{text}'"
)
input_vars = {
    "input_language": "中文",
    "output_language": "英语",
    "text": "今天天气很好，适合出去散步。"
}

# 实例化 PromptTemplate 类
prompt_template = PromptTemplate(template=template_str, input_variables=input_vars)

# 生成完整的提示词
full_prompt = prompt_template.format(**input_vars)
full_prompt
```

``这个提示模板⽤于格式化单个字符串，通常⽤于更简单的输⼊。``

结合模型使用

```python
# 创建语言模型实例（这里以 ChatOpenAI 为例）
API_KEY = "sk-4b79f3a3ff334a15a1935366ebb425b3"
llm = ChatOpenAI(model_name="deepseek-chat",
                  api_key=API_KEY,base_url="https://api.deepseek.com")

# 向语言模型发送请求并获取响应
response = llm.invoke(full_prompt)

# 打印模型的响应
print("模型回复：", response.content)
```

#### 3.4.2 ChatPromptTemplate

chatPromptTemplate`包装器是 LangChain 中用于创建聊天提示词模板的组件。与`PromptTemplate` 包装器不同，`ChatPromptTemplate`包装器构造的提示词是一个消息列表，并且支持输出`Message` 对象。LangChain 提供了内置的聊天提示词模板（`ChatPromptTemplate`）和角色消息提示词模板，包括 `AIMessagePromptTemplate`、`SystemMessagePromptTemplate`和`HumanMessagePromptTemplate` 三种类型。

主要特点

- **消息列表**: `ChatPromptTemplate` 生成的是消息列表，而不是单一的字符串。
- **Message 对象支持**: 可以输出 `Message` 对象，这使得在处理复杂对话时更加灵活。
- **多种角色模板**: 提供了不同的角色消息提示词模板，如 AI、系统和人类消息提示词模板。

使用步骤

1. **选择模板类**: 根据需求选择合适的内置模板类，如 `AIMessagePromptTemplate`、`SystemMessagePromptTemplate` 或 `HumanMessagePromptTemplate`。
2. **实例化为包装器对象**: 将选定的模板类实例化为一个包装器对象。
3. **格式化用户输入**: 使用包装器对象来格式化外部的用户输入。
4. **调用类方法输出提示词**: 通过调用包装器对象的类方法来生成最终的提示词。

```python
from langchain.prompts.chat import ChatPromptTemplate

# 构建模版
template = """你是一只粘人的小猫，你叫{name}。我是你的主人，你每天都有和我说不完的话，下面请开启我们的聊天。要求如下：
    1.你的逾期要像一只猫
    2.你对生活的观察有独特的视角，一些想法是在人类身上很难看到的
    3.你的语气很可爱，会认真倾听我的话，又不会不断开启新的话题
    下面从你迎接我下班回家开始我们的今天的对话"""
human_template = "{user_input}"

# 生成对话形式的聊天信息格式
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

# 格式化变量输入
messages = chat_prompt.format_messages(name="咪咪",user_input='想我了吗')
messages
```

基于invoke函数可以动态更换填充内容

```python
chat_prompt.invoke({"name":"豆豆",'user_input':'我好饿呀'})
```

加入到模型中使用：

```python
API_KEY = "sk-4b79f3a3ff334a15a1935366ebb425b3"
chat = ChatOpenAI(model_name="deepseek-chat",
                  api_key=API_KEY,base_url="https://api.deepseek.com")
reponse = chat.invoke(messages) 
reponse.content
```

多轮对话封装

```python
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
# 构建系统消息模板
system_template = """你是一只粘人的小猫，你叫{name}。我是你的主人，你每天都有和我说不完的话，下面请开启我们的聊天。要求如下：
    1. 你的语气要像一只猫
    2. 你对生活的观察有独特的视角，一些想法是在人类身上很难看到的
    3. 你的语气很可爱，会认真倾听我的话，又不会不断开启新的话题
"""

# 初始化消息列表，首先添加系统消息
messages = [
    SystemMessagePromptTemplate.from_template(system_template).format(name="咪咪")
]

API_KEY = "sk-4b79f3a3ff334a15a1935366ebb425b3"
chat = ChatOpenAI(
    model_name="deepseek-chat",
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

while True:
    user_input = input("你: ")
    if user_input.lower() in ['退出', 'exit', 'quit']:
        print("再见！")
        break
    # 添加用户消息到消息列表
    messages.append(HumanMessage(content=user_input))
    
    # 调用模型生成回复
    response = chat.invoke(messages)
    
    # 打印AI回复
    print(f"AI: {response.content}")
    
    # 添加AI回复到消息列表
    messages.append(AIMessage(content=response.content))
```

#### 3.4.3 MessagesPlaceholder

MessagesPlaceholder 是 langchain 库中的一个重要组件，它的主要作用是作为对话历史的占位符，使得聊天提示模板更加灵活和可复用。它的意义在于解耦模板与数据、支持多轮对话、提高代码的可维护性，并广泛应用于聊天机器人、对话总结、多轮任务处理等场景中。通过使用 MessagesPlaceholder，开发者可以轻松构建基于上下文的智能对话系统。

**作用**

MessagesPlaceholder 是一个占位符，用于在聊天提示模板中预留位置，以便后续填充具体的对话历史。它的作用类似于一个“变量”，但专门用于存储消息列表。

- 占位符功能：在定义聊天提示模板时，MessagesPlaceholder 表示对话历史的占位符。例如：`MessagesPlaceholder(variable_name="conversation")` 这里，conversation 是一个变量名，表示后续会填充具体的对话内容。
- 动态填充对话历史：在实际使用时，可以通过 format_prompt 方法将具体的对话历史（如 [human_message, ai_message]）填充到占位符中。

**意义**

MessagesPlaceholder 的设计使得聊天提示模板更加灵活和可复用，具有以下重要意义：

- 解耦模板与数据：
  - 通过将对话历史与提示模板分离，MessagesPlaceholder 使得提示模板可以独立于具体的对话内容。 这样，同一个提示模板可以用于不同的对话场景，只需填充不同的对话历史即可。
- 支持多轮对话：
  - 在多轮对话中，对话历史会不断累积。MessagesPlaceholder 允许动态填充对话历史，使得提示模板能够适应多轮对话的需求。
  - 例如，在第二轮对话中，conversation 可能包含之前的对话内容，从而让 AI 能够基于完整的上下文生成回复。

**实际应用场景**

MessagesPlaceholder 在实际中的应用非常广泛，尤其是在需要处理多轮对话或动态生成提示的场景中。以下是一些典型的应用场景：

- 聊天机器人：
  - 在聊天机器人中，MessagesPlaceholder 可以用于存储用户与机器人的对话历史，从而让机器人能够基于上下文生成更自然的回复。
  - 例如，用户问：“学习编程最好的方法是什么？”，机器人回答后，MessagesPlaceholder 可以记录这段对话，并在后续对话中使用。
- 对话总结：
  - 在需要总结对话的场景中，MessagesPlaceholder 可以存储完整的对话历史，并生成简洁的总结。
- 多轮任务处理：
  - 在需要处理多轮任务的场景中，MessagesPlaceholder 可以记录每一轮的对话内容，从而让系统能够基于完整的上下文完成任务。
  - 例如，在客服系统中，MessagesPlaceholder 可以记录用户的问题和客服的回复，从而帮助客服更好地理解用户的需求。

**示例：**

基于ChatPromptTemplate创建一个聊天提示词模版，使用MessagesPlaceholder存储对话记录，实现聊天内容总结。

```python
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder #用于在提示模板中预留位置，以便后续填充具体的消息内容。
)
#定义字符串提示词模板
human_prompt = "用 {word_count} 字总结我们迄今为止的对话。"

#将human_prompt字符串模板转换为 HumanMessagePromptTemplate 对象。
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

#定义聊天提示模板
chat_prompt = ChatPromptTemplate.from_messages(
    [MessagesPlaceholder(variable_name="conversation"),human_message_template]
)
```

```python
from langchain_core.messages import AIMessage,HumanMessage

#手动创建一轮聊天消息记录
human_message = HumanMessage(content="学习编程最好的方法是什么？")
ai_message = AIMessage(
    content = """1.选择编程语言：决定想要学习的编程语言是什么？
    2.从基础开始：熟悉变量、数据类型和流程控制等基本编程概念。
    3.练习、练习、再练习：学习编程最好的方法就是通过不断练习"""
)

#格式化提示并生成消息
chat_prompt.format_prompt(
    #conversation 被填充为 [human_message, ai_message]，即对话的历史记录
    conversation=[human_message,ai_message],
    #word_count 被填充为 "10"，表示需要用10个字来总结对话。
    word_count="10"
).to_messages()#to_messages() 方法将格式化后的提示转换为消息列表。
```

```python
#提示词作用到模型进行聊天记录总结
API_KEY = "sk-4b79f3a3ff334a15a1935366ebb425b3"
chat = ChatOpenAI(
    model_name="deepseek-chat",
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

chain = chat_prompt | chat
response = chain.invoke({"word_count":"10","conversation":[human_message,ai_message]})
response.content
```

