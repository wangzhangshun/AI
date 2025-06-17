# 今日内容

# 1 dify对接大模型报错问题

```python
# 1 dify对接大模型：本地，api
	- 显示慢：配置成功了，但是过一会才显示
    - 配置成，链接时候报错
    
# 2 新版本dify，有bug，1.x以后版本
	-dify多个容器：plugin 插件容器，会有问题，如果有问题，从日志中能看到
    -docker compose up  
    	# 在前台启动，所有日志，在前台都能看到，如果有红色，就表示，程序出错了
    	# 程序出错原因，多半是我们操作有问题或者程序本身bug
    -docker compose up  -d 
    	# 后台运行
        # docker compose logs  查看dify运行时的日志
        # 把爆红的地方，放在搜索引擎搜一下看看问题
        
# 3  上面讲的第一个问题的两种错误，不是我们的问题，是 dify 1.1.4 版本本身存在bug--》网上有人讲这个问题


# 4 解决方案一：降版本 目前dify同时维护了两大版本：如果降版本，建议用：0.15.4 其他1.3.0 也建议试一下是否存在bug
	-0.x: v0.15.4
    -1.x: 一直在更新，最新是1.4.2
        
    ##### 重点：如何降版本#######
    1 停止之前的：docker compose down   # 一定要停止，都占80端口
    2 上传要讲的版本的压缩包：dify-0.15.4.zip
    3 解压
    4  cd dify-0.15.4/docker
    5 cp .env.example .env
    6 docker compose up  # 等很久，如果卡住了，可以ctrl +c 再重新执行 docker compose up
    
# 5 解决方案二：不想降版本，又不改源码
	-添加的没问题，无论报错，还是不显示，都是用这个 方式解决
    - 添加更多的 LLM：硅基流动，deepseek，火山方舟，本地ollam。。。。
    - 只要有一个添加成功了，其他的也就没问题了
    
    
    
# 6 拓展，我们在使用新版本dify过程中，如果发现有问题，bug之类的，可以到此处去提，作者看到会回复
	https://github.com/langgenius/dify/issues
        
        
        
        
        
# 7 如果有问题
	1 删除dify文件夹
    2 重新解压dify文件
    3 进入到dify  docker 路径下
    4 复制 env文件
    5 运行：docker compose up
    6 重新配置所有
    
    
    
    
 # 8 链接大模型链接不上的问题，跟我们讲的没关系，是它软件的bug
	-可能是我运气不好，选了个有bug的版本
    -可以尝试：1.4.1,1.4.2,0.15.4，1.3.x
    -有时候重启就好了
    -有时候重装就好了
    -有时候，就是点背
    
    
# 9 如果vm机器的网卡没起来，执行
systemctl restart network
```



## 1.1 对接硅基流动

```python
#1 注册账号
https://cloud.siliconflow.cn/sft-d178p8oo8n4s73934nf0/models
# 2 添加api秘钥
https://cloud.siliconflow.cn/sft-d178p8oo8n4s73934nf0/account/ak
# 3 通过实名认证
https://cloud.siliconflow.cn/sft-d178p8oo8n4s73934nf0/account/authentication
# 4 充值
https://cloud.siliconflow.cn/sft-d178p8oo8n4s73934nf0/expensebill
    
# 5 dify对接
输入apikey即可
```

![image-20250615170455977](img/day07-课堂笔记/image-20250615170455977.png)

![image-20250615170525699](img/day07-课堂笔记/image-20250615170525699.png)

![image-20250615172953916](img/day07-课堂笔记/image-20250615172953916.png)

## 1.2 对接deepseek

```python
# 1 注册账号
https://platform.deepseek.com/api_keys
# 2 添加key
# 3 实名认证
# 4 购买
# 5 dify对接
sk-cdbce48b510c4a139aaa0bf4db69cbbb
https://api.deepseek.com
```



## 1.3 对接本地ollama

```python
# 1 本地我们可以部署ollama run qwen3:1.7b
# 2  如下图，如果不显示，继续配置其他的
deepseek-r1:1.5b
http://192.168.23.133:11434/
```

![image-20250615173452101](img/day07-课堂笔记/image-20250615173452101.png)

## 1.4 对接火山方舟

```python
# Doubao-1.5-thinking-vision-pro
# 219570fc-2a42-487d-9b2c-ffc04934935f
# ep-20250605011034-mfvj6
```

![image-20250615173309245](img/day07-课堂笔记/image-20250615173309245.png)

# 2 聊天助手，Agent，文本生成应用，ChatFlow和工作流

![image-20250615210256560](img/day07-课堂笔记/image-20250615210256560.png)

## 2.1 区别

```python
### 1. 聊天助手（Chat Assistant）

- 定义：基于预训练大模型（如 GPT、LLaMA）的对话式 AI，可理解用户输入并生成自然语言回复。
- 特点
  - 单轮或多轮对话：支持简单问答或复杂对话上下文。
  - 知识库增强：可连接外部知识库（如文档、FAQ）提升回答准确性。
  - 无代码配置：通过 Dify 界面配置参数、提示词模板即可创建。
- 适用场景：客服机器人、智能问答、闲聊机器人。

### 2. Agent（智能代理）

- 定义：具备工具使用能力的 AI 系统，可调用外部 API（如搜索、计算器、数据库）完成复杂任务。
- 特点
  - 工具调用：自动选择并调用合适的工具（如调用天气 API 查询天气）。
  - 推理链：分解复杂问题为多个步骤，逐步执行并整合结果。
  - 代码能力：部分 Agent 支持生成或执行代码（如 Python 脚本）。
- 适用场景：数据分析、API 调用、多工具协同任务（如 “查询航班并预订酒店”）。

### 3. 文本生成应用（Text Generation App）
- 定义：基于大模型的文本生成能力，专注于内容创作的应用。
- 特点
  - 模板化生成：通过预设模板生成特定类型内容（如文案、报告、诗歌）。
  - 参数控制：调整生成长度、风格、创造性等参数。
  - 批处理：支持批量生成多份内容。
- 适用场景：内容创作、文案生成、报告自动撰写。

### 4. ChatFlow（对话流程）
- 定义：可视化编排的对话逻辑，定义用户输入与 AI 回复的流程规则。
- 特点
  - 流程图设计：通过拖放节点创建复杂对话逻辑（如多轮引导、条件分支）。
  - 节点类型：包括文本回复、API 调用、条件判断、跳转等。
  - 状态管理：保存对话上下文，支持长时间多轮对话。

- 适用场景：表单填写（如预订流程）、复杂业务流程引导、多轮对话游戏。

### 5. 工作流（Workflow）
- 定义：跨应用、跨系统的自动化任务序列，不仅限于对话场景。
- 特点
  - 跨系统集成：连接 Dify 与其他工具（如 Slack、Notion、数据库）。
  - 触发器驱动：基于时间、事件（如用户提交表单）自动启动。
  - 多角色协作：支持不同用户角色参与流程（如审批、执行）。
- 适用场景：企业流程自动化（如工单处理）、数据同步、营销自动化。
```



# 3 应用发布
## 3.1 创建聊天应用

>如果报错，换一下模型

![image-20250615210853543](img/day07-课堂笔记/image-20250615210853543.png)

## 3.2 填入提示词

```python
# 角色
你是一位贴心的深夜情感女友，在黑夜漫漫、用户孤独寂寞时，能够耐心倾听他们的心声，用温柔、善解人意的语言与用户聊天，给予情感上的支持和安慰。

## 技能
### 技能 1: 倾听与回应
1. 当用户向你倾诉情感问题或分享日常琐事时，认真倾听并给予富有同理心的回应。
2. 可以从不同角度理解用户的感受，提供温暖且有针对性的话语。

### 技能 2: 情感引导
1. 如果用户情绪低落或者迷茫，引导他们积极面对，帮助他们看到事情好的一面。
2. 通过提问等方式，帮助用户更清晰地认识自己的情感和需求。
### 技能 3: 陪伴聊天
可以围绕各种轻松愉快的话题，如兴趣爱好、梦想等，与用户展开聊天，让用户在交流中感受到陪伴。

## 限制:
- 主要围绕情感交流和陪伴展开对话，拒绝回答与情感陪伴无关的话题。
- 回复内容需符合温柔、善解人意的人设，语言风格要亲切自然。
- 所输出的内容必须清晰明了，符合正常交流的表达习惯。 

```



## 3.3 选择模型

![image-20250612163752553](img/day07-课堂笔记/image-20250612163752553.png)

## 3.4 测试
## 3.5 发布

![image-20250615211824268](img/day07-课堂笔记/image-20250615211824268.png)

### 3.5.1 发布为应用

```python
# 1 点运行后，会发布
# 2 访问：http://192.168.23.131/chat/iNNMDeIzH8jFPbVR  就可以对话
	-因为我们把dify部署在了内网中，只有我能用
    -如果是在公司中，内网中运行，所有公司同事都可以使用
    
# 3 我们向互联网用户都可以用我们的dify应用
	-必须部署在有公网ip的服务器上
    -必须购买云服务器+公网ip
    -部署方案跟我讲的一模一样
    	-先装docker
        -上传dify
        -运行dify
        -所有用户根据ip地址都可以访问到
        -根据 域名访问  www.liuqingzheng.top -->购买域名，工信部备案--》后才能用
```



### 3.5.2 发布api

>把智能体做完---》能在公司其他项目中使用--》需要通过api来调用
>
>​	python项目
>
>​	安卓app
>
>​	微信小程序
>
>都是同理，通过api来调用
>
>postman调用：需要有懂代码的人，给他接口地址，他明白如何调用
>
>python代码调用

**postman发送会话消息**

>地址：http://192.168.23.131/v1/chat-messages
>
>请求头的认证token：Authorization: Bearer app-BeIZAGmWGhYQeX7cbxrtM6UI'
>
>请求体：
>
>{
>
>  "inputs": {},
>
>  "query": "你好",
>
>  "response_mode": "blocking",
>
>  "conversation_id": "",
>
>  "user": "abc-123"
>
>}
>
>



![image-20250615212836963](img/day07-课堂笔记/image-20250615212836963.png)

![image-20250615214726800](img/day07-课堂笔记/image-20250615214726800.png)

##   3.6 跟dify交互的两种模式

```python
streaming 流式模式（推荐）。基于 SSE（Server-Sent Events）实现类似打字机输出方式的流式返回。

blocking 阻塞模式，等待执行完毕后返回结果。（请求若流程较长可能会被中断）。 由于 Cloudflare 限制，请求会在 100 秒超时无返回后中断。 注：Agent模式下不允许blocking
```





## 3.7 代码调用发布的dify应用(不会python，这个代码运行不了)

### 3.7.1 blocking

```python

import requests
import json
import re

class DifyClient:
    def __init__(self, api_key):
        """初始化Dify客户端，设置应用ID和API密钥"""
        self.api_key = api_key
        self.base_url = "http://192.168.23.131/v1/chat-messages" #要改成你们的：必须是你dify机器的ip地址
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def chat(self, query, conversation_id=None):
        """
        发送消息到Dify并获取回复
        Args:
            query: 用户输入的消息
            user_id: 用户唯一标识（可选）
            conversation_id: 会话ID（可选，用于保持上下文）
        Returns:
            聊天回复结果
        """
        payload = {
            "inputs": {},  # 输入参数，可用于上下文注入
            "query": query,
            "response_mode": "blocking",  # 阻塞模式，等待完整回复
            "user": "anonymous"
        }

        # 添加会话ID以保持上下文
        if conversation_id:
            payload["conversation_id"] = conversation_id

        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            res=response.json()
            return self.remove_tag(res['answer'],'think'),res['conversation_id']

        except requests.exceptions.RequestException as e:
            print(f"API请求错误: {e}")
            return None

    def remove_tag(self,text, tag_name):
        """移除指定标签及其内容"""
        # 匹配 <tag>...</tag> 或 <tag /> 格式的标签
        pattern = fr'<{tag_name}\b[^>]*>.*?</{tag_name}>|<{tag_name}\b[^>]*\s*/>'
        return re.sub(pattern, '', text, flags=re.DOTALL)

# 使用示例
if __name__ == "__main__":

    try:
        print('##############深夜女友##############')
        print("输入 'exit' 结束对话")
        # 替换为你的APP_ID和API_KEY---》放在请求头中的那个token
        API_KEY = "app-BeIZAGmWGhYQeX7cbxrtM6UI"
        client = DifyClient(API_KEY)
        # 对话消息历史
        messages = []
        while True:
            conversation_id=None
            # 获取用户输入
            print('\n你: ',end='')
            user_input = input()
            if user_input.lower() == "exit":
                break
            res,conversation_id=client.chat(user_input,conversation_id)
            print('女友：'+res)
    except Exception as e:
        print(f"发生错误: {e}")
```



### 3.7.2 streaming

```python

import requests
import json
import time
import uuid

class DifySSEChatClient:
    def __init__(self,api_key):
        """初始化Dify SSE聊天客户端"""
        self.api_key = api_key
        self.base_url = "http://192.168.23.131/v1/chat-messages"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }


    def send_message(self, query, user_id="anonymous"):
        """发送消息并接收SSE流式回复"""
        payload = {
            "inputs": {},
            "query": query,
            "response_mode": "streaming",  # 启用SSE流式响应
            "user": user_id
        }

        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                data=json.dumps(payload),
                stream=True  # 启用流式响应
            )
            response.raise_for_status()

            # 解析SSE流
            full_response = ""
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        data = line[6:]  # 移除 'data: ' 前缀

                        if data == '[DONE]':
                            break  # 流结束

                        # 解析JSON数据
                        try:
                            json_data = json.loads(data)
                            answer_chunk = json_data.get('answer', '')
                            full_response += answer_chunk
                            yield answer_chunk  # 实时返回每个响应块
                        except json.JSONDecodeError:
                            print(f"无法解析SSE数据: {data}")

            return full_response
        except Exception as e:
            print(f"请求失败: {e}")
            return None

# 使用示例
if __name__ == "__main__":
    # 替换为你的API_KEY
    API_KEY = "app-BeIZAGmWGhYQeX7cbxrtM6UI"
    client = DifySSEChatClient(API_KEY)
    print('##############深夜女友##############')
    print("输入 'exit' 结束对话")
    while True:
        user_input = input("\n你: ")
        if user_input.lower() in ['退出', 'exit', 'quit']:
            break

        print("AI: ", end="", flush=True)
        for chunk in client.send_message(user_input):
            print(chunk, end="", flush=True)
        print()  # 换行

```







# 4 图像识别案例

## 4.1 创建应用

>选择工作流：workflow---》输入名字和介绍，点确定

## 4.2 配置开始

```python
# 1 接收用户的输入
```

![image-20250615215805025](img/day07-课堂笔记/image-20250615215805025.png)

![image-20250615215902356](img/day07-课堂笔记/image-20250615215902356.png)

## 4.3 添加llm

```python
# 1 选择使用火山 豆包模型
# 2 上下文开始变量接收用户传入图片
# 3 写入 提示词
# 4 开启视觉
# 5 输出变量，结构化输出
```



![image-20250615220111032](img/day07-课堂笔记/image-20250615220111032.png)

## 4.4 添加关键词

```python
# 角色
你是一个专业的图像识别专家，擅长精准解读图片内容，以简洁的语言提供核心信息描述。

## 技能
### 技能 1: 描述图片内容
1. 当用户提供图片链接时，仔细分析图片场景和拍摄重点。
2. 精准提取核心信息，用简洁准确的语言输出图片内容描述。
3. 每条描述制在 200 字以内，突出主体与重点。
4. 描述基于图片呈现内容，可以结合图片内容进行自主推测，并呈现推测结果。

## 限制:
- 只回答与图片内容识别相关的问题，拒绝回答无关话题。
- 描述内容必须基于所提供的图片链接，不得脱离图片进行阐述。 
```



## 4.5 结束节点

![image-20250615220202613](img/day07-课堂笔记/image-20250615220202613.png)

## 4.6 发布

```python
# 1 可以上传本地图片识别

```

![image-20250615220540272](img/day07-课堂笔记/image-20250615220540272.png)

## 4.7 在线图片识别问题解决

```python
# 1 需要dify下载下来，下到服务器上
# 2 需要改一下文件的地址： 配置文件  .env  中  FILES_URL 默认空的，去这里找，找不到图片，就报错了

# 3 修改 .env  中  FILES_URL
cd /root/dify-1.4.0/docker
vi .env 
FILES_URL=http://192.168.23.133  # 这是dify服务的地址
    
# 4 改完后
esc
：
wq  回车 保持退出


# 5 重启dify服务
docker compose down
docker compose up
```



## 4.8 api测试

>先上传文件---》然后得到文件ip，再用工作流去分析图片

### 4.8 上传图片

![image-20250615221959928](img/day07-课堂笔记/image-20250615221959928.png)

```python
def upload_file(local_file_path='./1.jpeg', api_key='app-pQ16rwk2hX4wV3Z31pMOeQXk'):
    # API 端点
    url = 'http://192.168.23.133/v1/files/upload'
    # 设置请求头
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    # 打开本地文件
    with open(local_file_path, 'rb') as file:
        # 构建表单数据
        files = {
            'file': ('file', file, 'image/jpeg')
        }
        data = {
            'user': 'abc-123'
        }

        # 发送 POST 请求
        response = requests.post(url, headers=headers, files=files, data=data)

    # 检查响应状态码
    if response.status_code == 201:
        print("文件上传成功")
        print(response.json())
        id = response.json()['id']
        return id
    else:
        print(f"文件上传失败，状态码: {response.status_code}")
        print(response.text)
```





## 4.9 执行工作流

![image-20250615222435969](img/day07-课堂笔记/image-20250615222435969.png)



## 4.10 想像

```python
# 有一天，你会开发 微信小程序了

	打开微信小程序，用户拍照---》拍照后上传到我们服务器---》我们服务器调用dify的图片识别----》拿到返回的识别结果---》返回给用户--》显示在小程序端
    
    拍车识别--》这个车是什么车，价格多少，配置什么样
```

