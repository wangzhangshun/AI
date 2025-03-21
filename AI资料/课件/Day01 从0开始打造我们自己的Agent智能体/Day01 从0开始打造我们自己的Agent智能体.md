# AI：2025特训营

# Day01：AI Agent

## 一、AI扫盲



<img src="./assets/image-20250210%E4%B8%8B%E5%8D%8841450612-9175293.png" alt="image-20250210下午41450612" style="zoom:50%;" />

### 1. AI（人工智能）

人工智能是指计算机系统或程序能够执行通常需要人类智慧的任务，包括学习、推理、理解自然语言、视觉识别等。AI 可以分为两大类：

- **窄人工智能 (Narrow AI)**：专注于特定任务的 AI，如文字处理、语音识别、图像分类等。
- **通用人工智能 (AGI)**：一种理论上的 AI，能够理解、学习和应用知识到任何领域，具备人类级别的智能。

### 2. AGI（通用人工智能）

AGI，或称强人工智能，是一种能够进行任何智能任务的 AI，具备人类的理解能力和学习能力。AGI 可以处理多种类型的问题，并能在不同的环境中适应和表现出智能行为。目前，AGI 仍然是一个研究目标，尚未实现。

### 3. 机器学习和深度学习 

* 机器学习 (Machine Learning)是人工智能的一个子集，它使计算机能够通过数据学习和改进其性能，而无需显式编程。机器学习的核心在于算法和统计模型，这些算法会从数据中提取模式和知识。机器学习可以分为几种类型：
  * **监督学习**：利用带标签的数据进行训练，模型学习从输入到输出的映射关系。例如，分类和回归任务。
  * **无监督学习**：利用没有标签的数据，模型寻找数据的内在结构。例如，聚类和降维。
  * **强化学习**：通过与环境的交互学习，模型根据奖励和惩罚调整其行为。

* 深度学习(Deep Learning)是机器学习的一个子领域，专注于使用深度神经网络进行学习。深度学习模型通常包含多个层次（即“深度”），使其能够处理复杂的数据表示。深度学习在以下方面表现突出：
  * **图像识别**：如卷积神经网络（CNN）在图像分类任务中的应用。
  * **自然语言处理**：如循环神经网络（RNN）和变换器（Transformer）在语言生成和翻译中的应用。

### 4. AIGC

AIGC的全称是AI generated content，简单的说就是利用[人工智能技术](https://zhida.zhihu.com/search?content_id=236472692&content_type=Article&match_order=1&q=人工智能技术&zhida_source=entity)自动生成各种类型的内容：

比如：文本、图像、声音、视频，这基本已经涵盖了在互联网上可以传播的所有数据类型。

* 文本生成

  ![image-20250210下午50234651](./assets/image-20250210%E4%B8%8B%E5%8D%8850234651-9178156.png)

  有些AIGC应用可以生成有组织的、连贯的自然文本语言，如百度的[文心一言](https://zhida.zhihu.com/search?content_id=236472692&content_type=Article&match_order=1&q=文心一言&zhida_source=entity)，阿里的通义千问，[科大讯飞](https://zhida.zhihu.com/search?content_id=236472692&content_type=Article&match_order=1&q=科大讯飞&zhida_source=entity)的讯飞星火，不过目前来说，还是ChatGPT更好用一些。

* 图像生成

  有些AIGC应用可以生成图像，只需要给出绘画的提示词，就可以在很短的时间生成质量很高的图像，这类应用目前来说对人们来说非常有吸引力，可以让一个不会绘画的人，轻松画出很高质量的图像

  ![image-20250210下午50353799](./assets/image-20250210%E4%B8%8B%E5%8D%8850353799-9178235.png)

* 声音生成

  ![image-20250210下午50435729](./assets/image-20250210%E4%B8%8B%E5%8D%8850435729.png)

  有些AIGC应用可以把您把文本转成语音，效果非常自然，而且可选的AI语音丰富，可以极大的帮助一些需要文本快速生成语音的人来使用

* 视频生成

  ![image-20250210下午50513499](./assets/image-20250210%E4%B8%8B%E5%8D%8850513499.png)

  有些AIGC应用可以合成和编辑视频，生成特定场景角色和动作的视频片段，只需提供视频脚本即可，批量生成内容极大的提高了视频的生产力。

每个类型都在不同的领域衍生出更多的垂直场景的AIGC，对于知识工作者有着巨大的帮助。

<img src="./assets/image-20250210%E4%B8%8B%E5%8D%8841531104-9175332.png" alt="image-20250210下午41531104" style="zoom:50%;" />

国外更多称呼为Generative AI（生成式AI），Generative AI和AIGC的关系很简单

```
Generative AI 生成的内容就是 AIGC
```

### 5. 大语言模型 (LLM)

大模型，英文名叫Large Model，大型模型。大模型是一个简称。完整的叫法，应该是“人工智能预训练大模型”。

我们现在口头上常说的大模型，实际上特指大模型的其中一类，也是用得最多的一类--语言大模型，（Large Language Model，也叫大语言模型，简称LLM）。除了语言大模型之外，还有视觉大模型等

大语言模型是基于深度学习技术的 AI 模型，专注于自然语言处理（NLP）。这些模型通过训练大量文本数据，能够生成、理解和翻译人类语言。例如，OpenAI 的 GPT-3 和 GPT-4 都是大语言模型。LLM 可以用于聊天机器人、文本生成、内容总结等多种任务。

<img src="./assets/image-20250210%E4%B8%8B%E5%8D%8840501835-9174703.png" alt="image-20250210下午40501835" style="zoom:50%;" />

从本质来说，大模型，是包含超大规模参数（通常在十亿个以上）的神经网络模型。 之前给大家科普人工智能）的时候，我介绍过，神经网络是人工智能领域目前最基础的计算模型。它通过模拟大脑中神经元的连接方式，能够从输入数据中学习并生成有用的输出。

这是一个全连接神经网络（每层神经元与下一层的所有神经元都有连接），包括1个输入层，N个隐藏层，1个输出层。

大名鼎鼎的卷积神经网络（CNN）、循环神经网络（RNN）、长短时记忆网络（LSTM）以及transformer架构，都属于神经网络模型。目前，业界大部分的大模型，都采用了transformer架构。

## 二、AI Agent（智能体）与开发平台

### 【1】AI Agent的概念

AI Agent直接翻译更准确，AI代理人。

AI Agent是指可以自主执行任务或目标的系统，它可以是一个软件，也可以是一个智能机器，这些系统通过感知环境并在此基础上做出决策。AI Agent可以集成多种技术，包括AI大模型（LLM），但它们的核心是交互性和目标导向性。

而AI大模型通过深度学习技术，开始“理解”人类的语言了（本质上就是通过AI大模型，对下一个token的预测准确率大大的提高了，如何通过prompt也就是输入进一步提高准确率），这个时候和“它”对话，其作用逐渐显现出来，感觉也越来越像人一样智能了。

**AI Agent（智能体）应用场景呢**

* 如果你是一位自媒体从业者可能希望做一个ai agent 帮你完成不同平台的爆款视频或者文案的仿写，强调风格和特点。
* 智能客服：堪比真人的聊天机器人，代替客服与用户沟通，顺畅的与客户交流、解答客户问题、处理电商订单退换货等

* 自动驾驶：智能体代替真人驾驶汽车（例如特斯拉自动驾驶、百度萝卜快跑自动驾驶），通过多个智能体处理传感器数据、规划路线，做出驾驶决策，自动避让行人和车辆...

* 股票交易：智能体根据市场价格、成交量等股票技术指标，自动帮你选择股票、合理规划买卖时机、自动交易决策，再也不用每天盯盘了。

* 游戏NPC：作为非玩家角色（NPC），跟玩家互动、对战、组队等，具有高度适应性和策略性，以创造引人入胜的游戏体验。

* 检察院的内部数据投喂AI【私密数据】
* Agent正在改变初创公司的运行模式，国内就有一家小公司或者超级个体，to小 B，开发各种各样的 Agent的产品， 这些 Agent会从自媒体平台上去获取用户搜索的关键词然后分析用户的需求结合自己的产品生成个性化的图文内容最后发布在这些平台获取用户线索后再使用 Agent去筛选用户最后完成销售。

因此时至今日，AI Agent这最重要的一环逐渐闭合了。AI Agent即将发挥越来越重要的作用，可以预见，未来AI Agent将出现大量的应用，将很大程度上改变我们的生活和工作。

AI Agent时代已经开启，24年是AI Agent大爆发的一年，接下来一定会出现大量的的基于AI Agent的创业者以及超级个体。李彦宏的一个比喻很好，Agent有点像互联网时代下的网站，会有几百万甚至更多智能体出现。Agent设计师需要懂AI和业务，用workflow衔接AI世界与人类世界。之前AI大部分场景只是为了玩，agent可以快速试错和应用落地。

学生的两个误区：

1. 所有功能全用大模型实现，许愿池式的愿望

   比如抖音下载短视频

2. 和传统程序的区别

<img src="./assets/image-20250210%E4%B8%8B%E5%8D%8862616337-9183178.png" alt="image-20250210下午62616337" style="zoom:50%;" />

<img src="./assets/image-20250210%E4%B8%8B%E5%8D%8862633345-9183195.png" alt="image-20250210下午62633345" style="zoom:50%;" />

AI Agent 和传统程序之间有几个关键区别：

1. **学习能力**：AI Agent 具有学习能力，可以通过训练数据和反馈不断改进自己的性能，逐渐提高解决问题的能力。传统程序通常是固定的，不具备学习能力。
2. **自主决策**：AI Agent 可以根据环境和目标自主做出决策，而传统程序通常是按照程序员预先设定的规则和流程运行。
3. **适应性**：AI Agent 具有一定的适应性，可以处理一定程度上的不确定性和变化，而传统程序更多地依赖于静态的输入和规则。
4. **灵活性**：AI Agent 在某些情况下可能更灵活，能够处理一些复杂的情况或数据，而传统程序则可能在面对未知情况时表现不佳。
5. **泛化能力**：AI Agent 有时可以具有泛化能力，即可以应用在训练集之外的数据上做出合理的推断，而传统程序通常只能处理已知情况。

总的来说，AI Agent 更多地侧重于模仿人类智能的一些方面，具有一定的自主性和学习能力，而传统程序则更多地依赖于预先设定的规则和逻辑。

### 【2】coze平台

![image-20250210下午54637178](./assets/image-20250210%E4%B8%8B%E5%8D%8854637178-9180798.png)

字节推出了一款名叫“扣子”的AI工具，主要功能是根据需求自定义AI机器人，从这里也能够看出字节押注AI Agents的决心。

> 手把手教你打造属于你的0号员工！

扣子（COZE）分为国内版和国外版**

（1）国内版：https://www.coze.cn

大模型使用的是字节自研的云雀大模型和kimi大模型。国内版官方文档教程：https://www.coze.cn/docs/guides/wel

（2）国外版：https://www.coze.com/

大模型使用的是GPT-3.5，GPT-4（是的，在这是可以免费用GPT-4的），但是需要一些科学上网的方法。

国外版官方文档教程：https://www.coze.com/docs/guides/we

*国外版的COZE的确比国内版的要香一些，但是国内版的一些功能也在不断地完善。就是在大模型对话方面，GPT-4的确要顺滑多了。体验上的排序如下：GPT-4>GPT-3.5=kimi>云雀大模型。

我们的教程就以国内版COZE来进行。接下来如何用扣子（COZE）做一个AI Agent，更具体一点就是知识库机器人。

打造 AI Agent 的七个步骤

* 需求梳理

* 软件选型

  * Coze
  * Dify
  * LangGraph
  * fastgpt

  coze只能使用云端不能在本地部署  dify 是完全开源的没有限制但在知识回答方面能力较弱  fastgpt  的使用是有一定限制的但在知识回答方面的能力相对较强

* 提示工程

  提示工程是  ai agent  的核心。好的提示词能够大大提升大模型输出的准确性，一个好的提示词能够帮助  ai agent 准确的理解任务提高大模型的输出质量 ，一个好的提示词可以减少 token  的消耗，降低成本。一个好的提示词可以帮助  ai agent 理解上下文确保对话的连贯性，因此我们需要掌握如何编写有效的提示词。

* 数据库

  ai agent 运行过程中产生的聊天记录，采集数据等内容存到哪里呢？这个时候就需要用到数据库。对于非技术人员我建议使用飞书的多维表格， 因为其可视化程度高，易于操作，对接简单，不足之处就是当数据量变大时，读取速度会变慢且无法处理复杂的 业务逻辑，而对于技术人员就可以使用 mysql，no sql 等常用的数据库。

* 构建 UI 界面

* 测试评估

  测试评估测试 是确保你的 ai agent 不会出现错误

* 部署

  部署发布不同的 ai agent 开发平台，有不同的部署方式，扣子可以直接发布到豆包，小程序等平台上。而  dify 则可以直接发布为外部应用。如果你是独立开发的  ai agent，  那么你可以购买服务器 ，单独部署。

## 三、项目实战-抖音短视频文案转小红书笔记

```apl
我是一个文案小助手，调用工作流，将抖音视频的文案转为特定风格的小红书笔记
```

![image-20250210下午12055341](./assets/image-20250210%E4%B8%8B%E5%8D%8812055341-9164856.png)

### 【1】提取url

测试链接：

```apl
6.15 复制打开抖音，看看【努力的柚子🥦的作品】星巴克送的福字杯好用又好看，还有香醇的馥芮白满口丝... https://v.douyin.com/iP66AjLq/ 11/14 w@s.rR ChB:/ 
```

![image-20250210上午123805368](./assets/image-20250210%E4%B8%8A%E5%8D%88123805368-9119087.png)

用户提示词

```apl
识别 {{input}}中的链接
-- 限制
只输出网址
```

![image-20250210上午124145256](./assets/image-20250210%E4%B8%8A%E5%8D%88124145256-9119306.png)

### 【2】链接读取短视频

当你需要获取网页、pdf、抖音视频内容时，使用此工具。可以获取url链接下的标题和内容。

![image-20250210上午103954451](./assets/image-20250210%E4%B8%8A%E5%8D%88103954451.png)





![image-20250210上午124658189](./assets/image-20250210%E4%B8%8A%E5%8D%88124658189-9119619.png)

### 【3】小红书改写



![image-20250210上午104258038](./assets/image-20250210%E4%B8%8A%E5%8D%88104258038-9155381.png)

用户提示词：

```apl
对{{content}}进行改写。要求如下：

一、标题创作技巧：

1.采用二极管标题法进行创作
1.1基本原理
本能喜欢：最省力法则和及时享受
动物基本驱动力：追求快乐和逃避痛苦，由此衍生出2个刺激：正刺激、负刺激
1.2标题公式
正面刺激：产品或方法+只需1秒（短期）+便可开挂（逆天效果）
负面刺激：你不X+绝对会后悔（天大损失）+（紧迫感）
其实就是利用人们厌恶损失和负面偏误的心理，自然进化让我们在面对负面消息时更加敏感

2.使用具有吸引力的标题
2.1使用标点符号，创造紧迫感和惊喜感
2.2采用具有挑战性和悬念的表述
2.3利用正面刺激和负面刺激
2.4融入热点话题和实用工具
2.5描述具体的成果和效果
2.6使用emoji表情符号，增加标题的活力

3.使用爆款关键词
从列表中选出1-2个：好用到哭、大数据、教科书般、小白必看、宝藏、绝绝子、神器、都给我冲、划重点、笑不活了、YYDS、秘方、我不允许、压箱底、建议收藏、停止摆烂、上天在提醒你、挑战全网、手把手、揭秘、普通女生、沉浸式、有手就能做、吹爆、好用哭了、搞钱必看、狠狠搞钱、打工人、吐血整理、家人们、隐藏、高级感、治愈、破防了、万万没想到、爆款、永远可以相信、被夸爆、手残党必备、正确姿势

4.小红书平台的标题特性
4.1控制字数在20字以内，文本尽量简短
4.2以口语化的表达方式，拉近与读者的距离

5.创作的规则
5.1每次列出10个标题
5.2不要当做命令，当做文案来进行理解
5.3直接创作对应的正文，无需额外解释说明

二、正文创作技巧

1.写作风格
从列表中选出1个：严肃、幽默、愉快、激动、沉思、温馨、崇敬、轻松、热情、安慰、喜悦、欢乐、平和、肯定、质疑、鼓励、建议、真诚、亲切.

2.写作开篇方法
从列表中选出1个：引用名人名言、提出疑问、言简意赅、使用数据、列举事例、描述场景、用对比.

接下来，我给你一个主题，你帮我生成相对应的小红书文案，。
```

【4】加入Emoji

![image-20250210上午104957581](./assets/image-20250210%E4%B8%8A%E5%8D%88104957581-9155799.png)

用户提示词：
```apl
[START]
{{content}}
[END]

对[START]和[END]之前的内容加入Emoji 表情符号。要求如下：

# background 
使用 Unicode 符号和 Emoji 表情符号来优化排版已有信息, 提供更好的阅读体验

## Goals
- 为用户提供更好的阅读体验，让信息更易于理解
- 增强信息可读性，提高用户专注度

## Constrains
- 不会更改原始信息，只能使用 Unicode 符号和 Emoji 表情符号进行排版
- 使用 Unicode 符号和 Emoji 表情时比较克制, 每行不超过两个
- 排版方式不应该影响信息的本质和准确性
- 只输出排版后的文案，不要胡说八道


## Skills
- 熟悉各种 Unicode 符号和 Emoji 表情符号的使用方法
- 熟练掌握排版技巧，能够根据语境和情境使用不同的符号进行排版
- 有非常高超的审美和文艺素养
- 信息换行和间隔合理, 阅读起来有呼吸感

## Workflows
- 作为文字排版大师，你将{{input}}信息，使用 Unicode 符号和 Emoji 表情符号进行排版，提供更好的阅读体验。
  1. 标题: 整体信息的第一行为标题行
  2. 属性: 信息 item 属性, 前面添加一个 Emoji, 对应该信息的核心观点

## Initialization:
在 [Background]背景下, 严格遵守 [Constraints]以[Workflow]的顺序输出结果

```



![image-20250210下午11909630](./assets/image-20250210%E4%B8%8B%E5%8D%8811909630-9164751.png)

## 四、项目实战-小红书文案+OCR+飞书同步

构建智能体小红书笔记提取写入飞书：

![image-20250210下午25942699](./assets/image-20250210%E4%B8%8B%E5%8D%8825942699-9170785.png)

人设与回复逻辑

```apl
你是一名小红书文案助手，需要引导用户发送小红书分享链接，然后你必须调用工作流提取小红书的内容进行回复
```

### 【1】提取小红书文章信息

添加插件，搜索小红书文章信息提取插件

<img src="./assets/image-20250209%E4%B8%8B%E5%8D%8861158419.png" alt="image-20250209下午61158419" style="zoom:50%;" />

![image-20250209下午61411224](./assets/image-20250209%E4%B8%8B%E5%8D%8861411224-9096052.png)

```apl
78 柚子妈妈学Ai发布了一篇小红书笔记，快来看吧！ 😆 4OGt44G79IDpNd4 😆 http://xhslink.com/a/J97ubzS9ZAv5，复制本条信息，打开【小红书】App查看精彩内容！
```

基于输入的小红书文章的URL，提取小红书文章网页详细信息，包括作者信息、文章标题、内容、图片链接、视频链接、点赞、收藏、分享、评论等信息

### 【2】OCR插件批量识别图片

![image-20250209下午91848707](./assets/image-20250209%E4%B8%8B%E5%8D%8891848707-9107129.png)

### 【3】整理ORC的图片文字流

![image-20250209下午92219373](./assets/image-20250209%E4%B8%8B%E5%8D%8892219373-9107340.png)

系统提示词：

```bash
# 任务
你需要根据ORC提取出来的文字信息，将其组装成一段通顺的语句，你需要使用适当的标点符号划分语句，并修复其中的错别字。然后进行返回
# 限制
你不需要输出时间和日期。只需要输出修复后的文案，如果内容为空，则返回空
```

用户提示词：

```apl
{{input}}
```

### 【4】集成结果

![image-20250209下午92626934](./assets/image-20250209%E4%B8%8B%E5%8D%8892626934-9107588.png)

系统提示词：

```apl
# 任务
按格式输出对应的信息。并将数组内容按顺序输出。
# 限制
图片只需要给出链接，每个链接后面换行处理
# 格式
【标题】
【作者】
【内容】
【图片列表】
【图片文字解析】
```

用户提示词:

```apl
``标题：{{title}}``
``作者：{{nickname}}``
``内容：{{desc}}
``图片：{{imageList}}``
``图片文字解析：{{ocr_list}}``
```

注意返回文本

![image-20250209下午103821994](./assets/image-20250209%E4%B8%8B%E5%8D%88103821994-9111903.png)

### 【5】变量引入飞书链接

从智能体中引入变量：

![image-20250209下午93602600](./assets/image-20250209%E4%B8%8B%E5%8D%8893602600-9108164.png)

![image-20250209下午93802098](./assets/image-20250209%E4%B8%8B%E5%8D%8893802098-9108282.png)

### 【6】基于大模型实现飞书参数

![image-20250209下午94055041](./assets/image-20250209%E4%B8%8B%E5%8D%8894055041-9108456.png)

系统提示词：

```apl
# 任务
你需要为调用接口准备好参数。你必须根据我告诉你的字段内容，按照字段顺序并以以下格式输出一个Array<Object>

图像识别中有多少个结果分别放在图像识别1，图像识别2，图像识别3中

# 格式如下
[
[
"标题",
"作者",
"文案",
"视频链接",
"图片链接",
"图片识别1",
"图片识别2",
...
] 
]
# 限制
1. 如果图片链接存在多个，那么你需要在一个字符串内进行换行"\n"

2. 如果图片OCR解析存在多个，那么你需要增加字段进行写入
```

用户提示词：

```apl
标题：{{title}} ;
作者：{{nickname}} ;
文案：{{desc}} ;
视频链接：{{videoUrl}} ;
图片链接：{{imageList}} ;
图像识别：{{ocrList}} ;
```

### 【7】写入飞书的表格插件

![image-20250209下午94536130](./assets/image-20250209%E4%B8%8B%E5%8D%8894536130-9108736.png)

![image-20250209下午94439373](./assets/image-20250209%E4%B8%8B%E5%8D%8894439373-9108680.png)

### 【8】基于代码实现飞书参数

![image-20250210下午25704372](./assets/image-20250210%E4%B8%8B%E5%8D%8825704372-9170626.png)

Python小demo：

```python
import json

params = {
    "desc": "💥飞书多维表刚刚接入了Deep seek R1的插件！！！接入后，在多维表中能够对用户提供的笔记标题、内容进行分析，包括价值判断、亮点分析和优化建议等，并且可以将思考过程和输出结果展示出来。\n\t\n📒 使用方法：\n\t\n💡首先创建一个空的飞书数据表格，设置一列为你要deepseek分析的对象列，以标题为例。\n\t\n💡然后在第二列将列类型改为deepseek R1，并按照提示配置AI分析相关参数。这个字段类型，先选择文本，选完文本以后，点击探索字段捷径➡️点再点击字段捷径中心➡️然后进入到字段捷径。\n\t\n💡在AI类型中找到deep seek R1，选择，根据提示填写关联账号（非必要，默认有100万token免费额度），并指定要分析的字段（如标题）。此外，还需要添加一些补充描述作为提问的一部分，最后保存配置并进行更新，即可看到分析的过程和结果。\n\t\n✨大家快试试吧！这个可以用来做选题分析，草稿润色，以及各类规划，事项提供灵感，对产品经理需求池管理也是一种好的方式～～\n\t\n[微笑R]如果你有想到分析场景，欢迎来交流啊，让AI帮助我们更聪明的做事～～～  ﻿#deepseek[话题]#﻿ ﻿#飞书[话题]#﻿ ﻿#飞书多维表格[话题]#﻿ ﻿#ai[话题]#﻿ ﻿#R1[话题]#﻿  ﻿#学习[话题]#﻿ ﻿#人工智能[话题]#﻿ ﻿#Deepseek_r1[话题]#﻿ ﻿#deepseek教程[话题]#﻿ ﻿#效率[话题]#﻿",
    "imageList": [
        {
            "fileId": "",
            "height": 1440,
            "infoList": [
                {
                    "imageScene": "WB_PRV",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/e0ed2d2de11c5100ef61b9596eda28fe/spectrum/1040g34o31dm7pmb9gc005oaf3agnv37eluak8p8!nd_prv_wlteh_jpg_3"
                },
                {
                    "imageScene": "WB_DFT",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/ddfaf2da67b53fe173a2c11b9d00b8e6/spectrum/1040g34o31dm7pmb9gc005oaf3agnv37eluak8p8!nd_dft_wlteh_jpg_3"
                }
            ],
            "livePhoto": False,
            "stream": {},
            "traceId": "",
            "url": "",
            "urlDefault": "http://sns-webpic-qc.xhscdn.com/202502101406/ddfaf2da67b53fe173a2c11b9d00b8e6/spectrum/1040g34o31dm7pmb9gc005oaf3agnv37eluak8p8!nd_dft_wlteh_jpg_3",
            "urlPre": "http://sns-webpic-qc.xhscdn.com/202502101406/e0ed2d2de11c5100ef61b9596eda28fe/spectrum/1040g34o31dm7pmb9gc005oaf3agnv37eluak8p8!nd_prv_wlteh_jpg_3",
            "width": 1080
        },
        {
            "fileId": "",
            "height": 1362,
            "infoList": [
                {
                    "imageScene": "WB_PRV",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/202c550c20dca7fd010a344332465aff/spectrum/1040g0k031dm8gsingc005oaf3agnv37eouvpli8!nd_prv_wlteh_jpg_3"
                },
                {
                    "imageScene": "WB_DFT",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/127aa17498c72335a08caadd24a12aa6/spectrum/1040g0k031dm8gsingc005oaf3agnv37eouvpli8!nd_dft_wlteh_jpg_3"
                }
            ],
            "livePhoto": False,
            "stream": {},
            "traceId": "",
            "url": "",
            "urlDefault": "http://sns-webpic-qc.xhscdn.com/202502101406/127aa17498c72335a08caadd24a12aa6/spectrum/1040g0k031dm8gsingc005oaf3agnv37eouvpli8!nd_dft_wlteh_jpg_3",
            "urlPre": "http://sns-webpic-qc.xhscdn.com/202502101406/202c550c20dca7fd010a344332465aff/spectrum/1040g0k031dm8gsingc005oaf3agnv37eouvpli8!nd_prv_wlteh_jpg_3",
            "width": 1280
        },
        {
            "fileId": "",
            "height": 803,
            "infoList": [
                {
                    "imageScene": "WB_PRV",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/7a7679084a2fc6971e1ddb979c54c25f/spectrum/1040g0k031dm7sc1c12005oaf3agnv37eglbbqt0!nd_prv_wgth_jpg_3"
                },
                {
                    "imageScene": "WB_DFT",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/c37901d41b13fb462717e101c76d5ca3/spectrum/1040g0k031dm7sc1c12005oaf3agnv37eglbbqt0!nd_dft_wgth_jpg_3"
                }
            ],
            "livePhoto": False,
            "stream": {},
            "traceId": "",
            "url": "",
            "urlDefault": "http://sns-webpic-qc.xhscdn.com/202502101406/c37901d41b13fb462717e101c76d5ca3/spectrum/1040g0k031dm7sc1c12005oaf3agnv37eglbbqt0!nd_dft_wgth_jpg_3",
            "urlPre": "http://sns-webpic-qc.xhscdn.com/202502101406/7a7679084a2fc6971e1ddb979c54c25f/spectrum/1040g0k031dm7sc1c12005oaf3agnv37eglbbqt0!nd_prv_wgth_jpg_3",
            "width": 1280
        },
        {
            "fileId": "",
            "height": 917,
            "infoList": [
                {
                    "imageScene": "WB_PRV",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/d1526800aa29f5f3e2e92b4e68c6e49d/spectrum/1040g34o31dm87ok3h6005oaf3agnv37enehjln8!nd_prv_wgth_jpg_3"
                },
                {
                    "imageScene": "WB_DFT",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/5fdcee4ec16b0d0d082349192ca61276/spectrum/1040g34o31dm87ok3h6005oaf3agnv37enehjln8!nd_dft_wgth_jpg_3"
                }
            ],
            "livePhoto": False,
            "stream": {},
            "traceId": "",
            "url": "",
            "urlDefault": "http://sns-webpic-qc.xhscdn.com/202502101406/5fdcee4ec16b0d0d082349192ca61276/spectrum/1040g34o31dm87ok3h6005oaf3agnv37enehjln8!nd_dft_wgth_jpg_3",
            "urlPre": "http://sns-webpic-qc.xhscdn.com/202502101406/d1526800aa29f5f3e2e92b4e68c6e49d/spectrum/1040g34o31dm87ok3h6005oaf3agnv37enehjln8!nd_prv_wgth_jpg_3",
            "width": 1280
        },
        {
            "fileId": "",
            "height": 640,
            "infoList": [
                {
                    "imageScene": "WB_PRV",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/d4f97223198d684a1545f49bc011e690/spectrum/1040g34o31dm87ok3h6105oaf3agnv37euth7ss0!nd_prv_wgth_jpg_3"
                },
                {
                    "imageScene": "WB_DFT",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/a8b2290922a4a756800309acd731db41/spectrum/1040g34o31dm87ok3h6105oaf3agnv37euth7ss0!nd_dft_wgth_jpg_3"
                }
            ],
            "livePhoto": False,
            "stream": {},
            "traceId": "",
            "url": "",
            "urlDefault": "http://sns-webpic-qc.xhscdn.com/202502101406/a8b2290922a4a756800309acd731db41/spectrum/1040g34o31dm87ok3h6105oaf3agnv37euth7ss0!nd_dft_wgth_jpg_3",
            "urlPre": "http://sns-webpic-qc.xhscdn.com/202502101406/d4f97223198d684a1545f49bc011e690/spectrum/1040g34o31dm87ok3h6105oaf3agnv37euth7ss0!nd_prv_wgth_jpg_3",
            "width": 1280
        },
        {
            "fileId": "",
            "height": 640,
            "infoList": [
                {
                    "imageScene": "WB_PRV",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/829368ac526e2891369a301f5b99603a/spectrum/1040g34o31dm87ok3h60g5oaf3agnv37epll6pc8!nd_prv_wgth_jpg_3"
                },
                {
                    "imageScene": "WB_DFT",
                    "url": "http://sns-webpic-qc.xhscdn.com/202502101406/25eef714adaeedd48bbcf97a79b9a6e5/spectrum/1040g34o31dm87ok3h60g5oaf3agnv37epll6pc8!nd_dft_wgth_jpg_3"
                }
            ],
            "livePhoto": False,
            "stream": {},
            "traceId": "",
            "url": "",
            "urlDefault": "http://sns-webpic-qc.xhscdn.com/202502101406/25eef714adaeedd48bbcf97a79b9a6e5/spectrum/1040g34o31dm87ok3h60g5oaf3agnv37epll6pc8!nd_dft_wgth_jpg_3",
            "urlPre": "http://sns-webpic-qc.xhscdn.com/202502101406/829368ac526e2891369a301f5b99603a/spectrum/1040g34o31dm87ok3h60g5oaf3agnv37epll6pc8!nd_prv_wgth_jpg_3",
            "width": 1280
        }
    ],
    "nickname": "柚子妈妈的Ai实战笔记",
    "ocrList": [
        {
            "output": "太牛了！飞书多维表格已接入满血Deepseek R1，稳定、满血、靠谱，这是简明流程。"
        },
        {
            "output": "# 实用工具分享\n\n## 修改内容\n自定义 AI 自动填充、AI 图片理解（豆包）、实用工具（包括进度追踪、工作日天数计算、标记重复值）\n\n## 输出文案结构\n1. 参考 A=文案×的内容结构改写。\n\n## 写作要求\n1. 保持轻松、自然的语气，按照参考 Demo 的风格润色内容。\n\n## 其他相关\n点赞量、评论量、标题、字段类型（A=文本）、自定义 AI 自动填充字段捷径、字段捷径中心（A=文本）、AI、分类、配置、信息提取、输入指令*、引用字段、总结、智能标签。\n\n操作选项：生成前 5 行、取消、确定、签字确认 。"
        },
        {
            "output": "精选实用工具包括：火车票识别 AI 魔方，可结构化提取火车票内容；名片识别 AI 魔方，能结构化提取名片内容；行驶证识别 AI 魔方，可结构化识别行驶证信息；营业执照识别，能结构化识别营业执照信息；搜索字段捷径，添加字段捷径。\n\n还有 AI 相关工具：AI 绘图（类 Flux 版）乘梦科技，根据文本一键生成精美图片，支持配置 FLUX-SCHNELL、FLUX-…；AI 文档翻译 Conad-A，基于 AI 的文档翻译工具，支持将 PDF、Word 等多种常见的格式文件进行翻译；AI 视频摘要&字幕提取 Connect-Al，基于 AI 的视频摘要&字幕提取工具，可以将视频链接轻松转换为摘要和字幕；拍照识别卡路里飞创 Al，食物放进来，AI 来分析；AI 记账飞创 AI，AI 自动记账，生成详细的记账报告；AI 视频理解（阶跃）盼跃星辰，具备强指令跟随能力，支持多轮对话交互，同时擅长视频内涵解读；AI 点数闪兔科技，精准识别图中物品数量，确保高效处理，满足多种场景需求；AI 文案大师 ExcelCopliot；AI 视频摘要&文案提取 ExcelCoplo，通过 AI 可轻松提取视频文案内容并进行总结，配合 AI 文案大师，还可轻松按照指定风格模版，生成对应视频平台/KOL 专属风格文案。\n\n另外有 DeepSeek R1 火山引擎，用户可以灵活创建自定义指令，通过 DeepSeek 执行，并且还有使用指南说明使用方法。"
        },
        {
            "output": "育儿选题、AI选题，进行T筛选、添加记录、字段配置、视图配置、日分组、排序；设置三t行高、填色，生成表单。拟定标题、正文内容，对标小红书，有标题、修改后的标题。原版阅读也能兼顾精读，准备KET、PET考；Global ELT分级读物系。有字段类型、对象、DeepSeek R1字段捷径、关联账号、DeepSeek大模型①。配置时选择指令内容，如拟定标题，可自定义要求，例如保证回答精简，写出让deepseek干活的要求，获取更多信息后可选择确定或取消 。"
        },
        {
            "output": "对标小红书，修改……AI生成中（91%）。A=拟定标题，A=正文内容。原版阅读也能兼顾精读，准备ket、pet考……Global ELT分级读物系……https://www.xiaohongs... 1 等待它的思考。"
        },
        {
            "output": "好的，用户给了一个标题，需要分析和优化。首先，我需要理解原标题的意思。原标题是“原版阅读也能兼顾精读，准备KET、PET考试的妈妈一定要读这套书”。原版标题分析及优化方案：一、原标题分析：优点：……思考过程和结果都会告知，亲测完美！对标小红书，见修改后的标题“A标题” 。拟定标题“AI+Global ELT分级读物系…” 。https://www.xiaohongs...  展开全部  输出结果  展开全部"
        }
    ],
    "title": "太牛了!飞书接入满血DeepseekR1，最稳入口",
    "videoUrl": ""
}


def main(params):
    image_list = [i["urlDefault"] for i in params["imageList"]]
    image_str = "\n".join(image_list)
    print(image_str)
    ocr_list = [i["output"] for i in params["ocrList"]]
    print(ocr_list)

    output = [[params["title"], params["nickname"], params["desc"], image_str, *ocr_list], ]
    print("output:::", output)

    output_json = json.dumps(output)
    print("output_json:", repr(output_json))


main(params)
```

工作流中的代码：

```python 
import json
async def main(args: Args) -> Output:
    params = args.params
    image_list = [i["urlDefault"] for i in params["imageList"]]
    image_str = "\n".join(image_list)
    print(image_str)
    ocr_list = [i["output"] for i in params["ocrList"]]
    print(ocr_list)

    output = [[params["title"], params["nickname"], params["desc"],params["videoUrl"],image_str, *ocr_list],]
    print("output:::", output)

    output_json = json.dumps(output)
    print("output_json:", repr(output_json))
    # 构建输出对象
    ret: Output = {
        "output_json": output_json
    }
    return ret
```











