

```python
# 1 dify对接大模型报错问题
## 1.1 对接硅基流动
## 1.2 对接deepseek
## 1.3 对接本地ollama
## 1.4 对接火山方舟

# 2 应用发布
## 2.1 创建应该
## 2.2 填入提示词
## 2.3 选择模型
## 2.4 测试
## 2.5 发布
### 2.5.1 发布为应用
### 2.5.2 发布api

# 3 聊天助手，Agent，文本生成应用，ChatFlow和工作流
# 4 图像识别案例
## 4.1 创建应用
## 4.2 配置开始
## 4.3 添加llm
## 4.4 添加关键词
## 4.5 结束节点
## 4.6 发布
## 4.7 在线图片识别问题解决
## 4.8 api测试

```



# 1 关于dify对接大模型报错问题

```python
# 1 新版本dify，源码有bug,处理方案
	- 降级版本
    - 多次尝试：测试发现，只要有一个添加成功，后面都会成功
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

![image-20250615170455977](img/day07-Dify高级案例01/image-20250615170455977.png)

![image-20250615170525699](img/day07-Dify高级案例01/image-20250615170525699.png)

![image-20250615172953916](img/day07-Dify高级案例01/image-20250615172953916.png)

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

![image-20250615173106447](img/day07-Dify高级案例01/image-20250615173106447.png)

## 1.3 对接本地ollama

```python
deepseek-r1:1.5b
http://192.168.23.133:11434/
```

![image-20250615173452101](img/day07-Dify高级案例01/image-20250615173452101.png)

## 1.4 对接火山方舟

```python
# Doubao-1.5-thinking-vision-pro
# 219570fc-2a42-487d-9b2c-ffc04934935f
# ep-20250605011034-mfvj6
```

![image-20250615173309245](img/day07-Dify高级案例01/image-20250615173309245.png)

![image-20250615173334696](img/day07-Dify高级案例01/image-20250615173334696.png)

# 2 应用发布

## 2.1 创建应用

![image-20250612163716255](img/day07-Dify高级案例01/image-20250612163716255.png)

## 2.2 填入提示词

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

## 2.3 选择模型

![image-20250612163752553](img/day07-Dify高级案例01/image-20250612163752553.png)

## 2.4 测试



## 2.5 发布

### 2.5.1 发布为应用

### 2.5.2 供其它程序调用(python)

![image-20250612164120849](img/day07-Dify高级案例01/image-20250612164120849.png)

```python
# 1 秘钥
app-pQ16rwk2hX4wV3Z31pMOeQXk
```



**阻塞模式**

```python
import requests
import json
import re

class DifyClient:
    def __init__(self, api_key):
        """初始化Dify客户端，设置应用ID和API密钥"""
        self.api_key = api_key
        self.base_url = "http://192.168.23.133/v1/chat-messages"
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
        # 替换为你的APP_ID和API_KEY
        API_KEY = "app-pQ16rwk2hX4wV3Z31pMOeQXk"
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

**sse模式**

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
    API_KEY = "app-RdLzvBrDU9pqFcp06fVL3rtN"
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



# 2 **聊天助手**、**Agent**、**文本生成应用**、**ChatFlow** 和 工作流

## 2.1 区别

> 在 Dify 平台中，**聊天助手**、**Agent**、**文本生成应用**、**ChatFlow** 和 **工作流** 是构建 AI 应用的不同组件或模式，它们各自有特定的功能和适用场景。

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

## 2.2 对比表格

| 组件         | 核心功能             | 交互方式             | 工具调用能力 | 适用场景                         |
| ------------ | -------------------- | -------------------- | ------------ | -------------------------------- |
| 聊天助手     | 自然语言对话         | 文本交互             | 无           | 客服、问答、闲聊                 |
| Agent        | 调用工具解决复杂任务 | 文本或工具输出       | 有           | 数据分析、API 集成、多工具协同   |
| 文本生成应用 | 内容创作             | 输入提示词，输出文本 | 无           | 文案生成、报告撰写、内容批量生产 |
| ChatFlow     | 可视化编排对话逻辑   | 预设流程化交互       | 可选         | 表单填写、业务流程引导、游戏     |
| 工作流       | 跨系统自动化任务     | 事件触发或定时执行   | 有           | 企业流程自动化、数据同步、审批流 |

## 2.3 如何选择

- **简单问答**：选择 **聊天助手**。
- **需调用工具**：选择 **Agent**。
- **内容创作**：选择 **文本生成应用**。
- **复杂对话流程**：选择 **ChatFlow**。
- **跨系统自动化**：选择 **工作流**。

在实际应用中，这些组件可以组合使用。例如，通过 **ChatFlow** 定义对话流程，在关键节点调用 **Agent** 执行工具操作，最终通过 **工作流** 将结果同步到企业系统中





![image-20250615170455977](img/day07-Dify高级案例01/image-20250615170455977.png)



![image-20250615170525699](img/day07-Dify高级案例01/image-20250615170525699.png)



# 3 图像识别工作流

## 3.1 创建应用

## 3.2 配置开始

![image-20250615175919496](img/day07-Dify高级案例01/image-20250615175919496.png)

## 3.3 添加llm

```python
# 1 选择使用火山 豆包模型
# 2 上下文开始变量接收用户传入图片
# 3 写入 提示词
# 4 开启视觉
# 5 输出变量，结构化输出
```

![image-20250615180744060](img/day07-Dify高级案例01/image-20250615180744060.png)

## 3.4 添加LLM关键词

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

## 3.5 结束节点

![image-20250615180916553](img/day07-Dify高级案例01/image-20250615180916553.png)

## 3.6 发布

![image-20250615180930272](img/day07-Dify高级案例01/image-20250615180930272.png)



## 3.7 在线图片识别问题修改

```python
# 1 修改 .env文件，修改FILES_URL变量如下
FILES_URL=http://192.168.23.133

# 2 重启dify服务
docker compose down
docker compose up

```

## 3.8 api测试

### 3.8.1 上传图片

![image-20250615192053095](img/day07-Dify高级案例01/image-20250615192053095.png)

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

### 3.8.2 执行工作流

```python
# Authorization 需要使用浏览器中拿到的token
# 请求体：
{
    "inputs": {
        "image": {
            "type": "image",
            "transfer_method": "local_file",
            "upload_file_id": "7f23d4e4-e053-40d8-8332-65112917cc14"
        }
    },
    "response_mode": "streaming",
    "user":"demo"
}
```



![image-20250615192144289](img/day07-Dify高级案例01/image-20250615192144289.png)



```python
import requests
def run_workflow(file_id, user='demo', response_mode="blocking"):
    workflow_url = "http://192.168.23.133/v1/workflows/run"
    headers = {
        "Authorization": "Bearer app-pQ16rwk2hX4wV3Z31pMOeQXk",
        "Content-Type": "application/json"
    }
    data = {
        "inputs": {
            "image": [
                {
                    "transfer_method": "local_file",
                    "upload_file_id": file_id,
                    "type": "document"
                }
            ]
        },
        "response_mode": response_mode,
        "user": user
    }
 
    try:
        print("运行工作流...")
        response = requests.post(workflow_url, headers=headers, json=data)
        if response.status_code == 200:
            print("工作流执行成功")
            return response.json()
        else:
            print(f"工作流执行失败，状态码: {response.status_code}")
            print("错误详情：", response.text)  # 打印错误详情
            return {"status": "error", "message": f"Failed to execute workflow, status code: {response.status_code}"}
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return {"status": "error", "message": str(e)}
```













# 补充

## 1 Windows 上 DockerDestop和VMware冲突

### 1.1 冲突原因

```python
Docker Desktop 在 Windows 系统上运行通常依赖 Hyper-V 或 WSL 2，而 WSL 2 又基于 Hyper-V 的轻量级虚拟机技术。Hyper-V 是微软的虚拟化平台，它与 VMware 的虚拟化技术存在冲突。当 Hyper-V 启用时，会占用一些底层硬件资源和系统功能，导致 VMware Workstation 等软件无法正常使用，VMware 会提示 “VMware Workstation 与 Device/Credential Guard 不兼容” 等错误信息
```

### 1.2 几种解决方法

#### 【方式一】禁用Hyper-V

```python
# 禁用Hyper-V
在系统中禁用Hyper-V，这将允许VMware正常运行而不会与Docker冲突。

## 通过以下步骤来禁用Hyper-V：
1 打开“控制面板” > “程序” > “启用或关闭Windows功能”。
2 找到并取消勾选“Hyper-V”选项。
3 点击“确定”并重启计算机。
```

#### 【方式二】启用WSL 2

```python
如果主要使用Docker，可以考虑使用WSL 2来运行Linux容器，而不是依赖于Hyper-V。WSL 2在Windows 10和Windows 11上提供了轻量级的Linux环境，可以直接与Docker结合使用。
## 方式一：命令
启用WSL 2：打开PowerShell作为管理员。
运行命令 wsl --set-default-version 2 来设置WSL版本为2。
安装Linux发行版（如Ubuntu） wsl.exe --set-version Ubuntu 2
#方式二：软件
双击安装软件：wsl_update_x64.msi
	-软件包中提供

安装Docker Desktop并确保其配置为使用WSL 2。
```

#### 【方式三】使用Docker Desktop for Windows的WSL 2后端

```python
Docker Desktop for Windows也可以配置为使用WSL 2作为后端，这样可以绕过Hyper-V的限制。

在Docker Desktop的设置中，启用“Use the WSL 2 based engine”。

重启Docker Desktop。
```

#### 【方式四】同时使用VMware和Docker

```python
如果需要同时使用VMware和Docker，可以考虑以下方案：

使用嵌套虚拟化：在某些情况下，你可以在支持嵌套虚拟化的硬件上启用嵌套虚拟化功能，但这通常需要BIOS/UEFI设置中的特定配置。

使用桥接网络：确保你的虚拟机网络设置为桥接模式，这样可以避免与Docker容器网络冲突。
```

#### 【方式五】使用虚拟机软件的其他版本

```python
考虑使用其他虚拟机软件，如VirtualBox，它通常与Docker和Windows Hyper-V兼容性更好。
```

#### 【方式六】更新最新版本

```python
确保VMware Workstation、Docker Desktop和Windows系统都是最新版本，软件更新会解决兼容性问题。
```

![image-20250608164048907](img/day07-Dify高级案例01/image-20250608164048907.png)

![image-20250608163827887](img/day07-Dify高级案例01/image-20250608163827887.png)

![image-20250608164011100](img/day07-Dify高级案例01/image-20250608164011100.png)

## 2 Docker Desktop 安装在其他盘符

```python
# 0 开启WSL2
	打开“控制面板” -> 程序 -> 启用或关闭Windows功能->勾选“适用于Linux的Windows子系统”和“虚拟机平台”。
# 1 在D盘新建文件夹   D:\Docker      D:\Docker\data
# 2 把下载的Docker Desktop Installer.exe 放在该目录下
########### 一定使用管理员身份运行 安装####################
# 3 执行命令(使用软连接-这种不可控，因为不同用户路径不一样：存放容器的路径)
mklink /j "C:\Program Files\Docker" "D:\Docker"
mklink /j "C:\Users\Administrator\AppData\Local\Docker" "D:\Docker\data" 
# C:\Users\Administrator\AppData\Local 这个路径可能不同人不尽相同

# 4 方式二：命令方式
start /w "" "D:\Docker\Docker Desktop Installer.exe" install -accept-license --wsl-default-data-root="D:\Docker\data" --installation-dir="D:\Docker\"

########### 一定使用管理员身份运行 安装####################


# 5 开启后，看到装在了D盘 

```

![image-20250608160228893](img/day07-Dify高级案例01/image-20250608160228893.png)![image-20250608162333182](img/day07-Dify高级案例01/image-20250608162333182.png)

![image-20250608162612991](img/day07-Dify高级案例01/image-20250608162612991.png)

![image-20250608162837462](img/day07-Dify高级案例01/image-20250608162837462.png)

![image-20250608162856581](img/day07-Dify高级案例01/image-20250608162856581.png)

![image-20250608162921570](img/day07-Dify高级案例01/image-20250608162921570.png)

![image-20250608162944071](img/day07-Dify高级案例01/image-20250608162944071.png)

![image-20250608163023304](img/day07-Dify高级案例01/image-20250608163023304.png)

![image-20250608163355033](img/day07-Dify高级案例01/image-20250608163355033.png)



## 3 Mac安装虚拟机

```python
# 1 mac上虚拟机软件选择
VMware 公司为 Mac 用户开发了专门的虚拟化软件 ——VMware Fusion   免费
Parallels desktop(个人建议)                                收费

# 3 mac 破解软件下载：
https://macwk.cn/
https://www.macat.vip/
https://xclient.info/
https://appstorrent.ru/programs/ # 需要翻墙
    
    
# 4 下载后，正常安装软件，破解看相关下载网站


# 5 创建系统，并安装centos9如下图

# 使用可以参照：https://www.macat.vip/25088.html
```

![image-20250608175432209](img/day07-Dify高级案例01/image-20250608175432209.png)

![e3fa0d8baec99e3857d81d91359e5b01](img/day07-Dify高级案例01/e3fa0d8baec99e3857d81d91359e5b01.jpg)

![c0a0877ad5eaa68564910084fef6449f](img/day07-Dify高级案例01/c0a0877ad5eaa68564910084fef6449f.jpg)

![f7e0e5d42c3d0c2a7fc5d35ec4e3008d](img/day07-Dify高级案例01/f7e0e5d42c3d0c2a7fc5d35ec4e3008d.jpg)

![5b3008e774ce01567418b114d80ca26e](img/day07-Dify高级案例01/5b3008e774ce01567418b114d80ca26e.jpg)

![bca6276a0b3538875a8c7cfffc365562](img/day07-Dify高级案例01/bca6276a0b3538875a8c7cfffc365562.jpg)

