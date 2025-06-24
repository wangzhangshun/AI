# 1 Cursor介绍

## 1.1 Cursor 是什么

![image-20250622011059952](img/dday09-Cursor入门/image-20250622011059952.png)

```python
# 1 AI 代码编辑器
# 2 Cursor 旨在提高您的工作效率，是使用 AI 进行编码的最佳方式
# 3 Cursor 是一款基于人工智能技术的现代化代码编辑器，它基于 VSCode 开发，集成了 GPT-4 和 deepseek 等大模型，继承了 VSCode 的强大功能和扩展性，并在此基础上加入了 AI 辅助编程功能
```

## 1.2 Cursor的功能

```python
# 1 智能代码补全：
能根据上下文和开发者的输入，提供精准的代码补全建议，其补全功能基于深度学习模型，可理解代码语义，不仅是语法层面的补全。
# 2 代码生成：
支持通过自然语言描述生成代码，开发者输入简单描述，如 “创建一个函数，计算两个数的和”，Cursor 就能自动生成相应代码片段，适用于快速原型开发。
# 3 错误检测与修复：
内置强大的错误检测功能，可实时分析代码并指出潜在错误，还能提供修复建议，帮助开发者快速解决问题。
# 4 代码重构：
支持自动化代码重构功能，开发者可通过简单命令对代码进行优化和重构，如提取函数、重命名变量、优化代码结构等。
# 5 多语言支持：
支持多种编程语言，包括 Python、JavaScript、Java、C++、Go 等，无论是前端开发、后端开发还是数据科学，都能提供强大支持。
# 6 集成开发环境（IDE）功能：
具备完整的 IDE 功能，包括调试、版本控制、项目管理等，开发者可在一个工具中完成从编写代码到调试和部署的整个流程
```

## 1.3 常见AI代码编辑器

```python
# 1  Cursor：Anysphere 由几位麻省理工高材生在 2022 年创立，总部在纽约布法罗
	-2023年，Cursor发布
    -最初，Cursor 基于 Codemirror 构建，但为了专注于开发尖端 AI 功能，并打造一个原生支持 AI 配对编程的集成开发环境（AI-native IDE），Anysphere 将 Cursor 迁移至 VSCodium 的一个分支上，即微软 Visual Studio Code（VS Code）的开源版本
    -为了实现以更快的速度提供最前沿的 AI 功能，Cursor 引入了性能更优的 Claude/klɔːd/ 模型，将 Copilot++（智能代码补全等功能）的速度提高了大约两倍。此外，还引入了一个名为「Composer」的试验性功能（Beta 版），它使用户能够在单一编辑环境中操作多个文件
    -2025年3月，AI 编程神器 Cursor 新鲜出炉 Claude Max 模式（MAX 代表了最大智能），其核心优势在于处理大规模代码和复杂逻辑时表现出色，适合硬核开发者和大型项目。
	-Claude Max 是 Claude 3.7 的一种更强大配置，它以 Claude 3.7 Thinking 模型为基础。具有超强的创造力，能在其他模型失灵时脱颖而出，解决更复杂、更精妙的任务。
	-2025年6月17日，AI代码编辑器Cursor于宣布对其Pro计划进行重大升级，正式取消每月500次快速请求限制，推出备受期待的“无限使用”模式
    
# 2 Trae /treɪ/-字节跳动推出出
	-地址：https://www.trae.cn/
    -2025年1月19日，字节跳动发布了一款面向专业的开发者提供服务的全新AI Coding产品Trae。
    -Trae面向希望提高编程效率、减少重复性任务的开发者，无论是初学者还是经验丰富的开发人员均可使用。
	-2025年2月，该工具上线Windows版，3月3日，字节跳动发布AI编程工具Trae国内版，Trae本质上是AI原生集成开发环境工具，有一体化的原生AI体验。
    -新发布的Trae国内版模型搭载doubao-1.5-pro，支持切换满血版DeepSeek-R1&V3 
    -6月12日消息，TRAE的整体月活已超100万

    
# 3 Windsurf /ˈwɪndsɜːrf/
	- Windsurf是一家于2021年成立的企业，专注于人工智能驱动的编程工具。
	- 2025 年 5 月 6 日，OpenAI 以约 30 亿美元（218 亿元人民币）的价格收购 AI 辅助的编程工具 Windsurf
	-下载地址：https://windsurf.com/editor
    - 有IDE和plugins
   

# 4 Copilot /ˈkoʊ.pɪ.lɑːt/
	-官网：https://github.com/features/copilot
	-Copilot是2023年5月24日微软在Windows 11中加入的AI助手，该AI助手是一个集成了在操作系统中的侧边栏工具，可以帮助用户完成各种任务。Copilot依托于底层大语言模型（LLM），用户只需说几句话，做出指示，它就可以创建类似人类撰写的文本和其他内容。
```

![image-20250622134943564](img/day09-Cursor入门/image-20250622134943564.png)

![image-20250622133838485](img/day09-Cursor入门/image-20250622133838485.png)

![image-20250622135022082](img/day09-Cursor入门/image-20250622135022082.png)

## 1.4 Trae 使用

>目前免费，最像cursor的AI编辑器，未来可期

![image-20250622135513537](img/day09-Cursor入门/image-20250622135513537.png)

![image-20250622135610262](img/day09-Cursor入门/image-20250622135610262.png)

# 2 注册并下载安装Cursor

## 2.1 注册-下载

```python
# 1 因为cursor在使用过程中，需要跟服务器交互，必须注册账号
# 2 https://authenticator.cursor.sh/sign-up
# 3 邮箱注册后，需要邮箱验证【国内邮箱即可】
# 4 个人信息--如下图
# 5 购买账号：个人计划和团队计划
	https://www.cursor.com/pricing
        
# 6 不同账号介绍
## 6.1 个人计划免费版：
	-AI 模型选择：仅支持 GPT-3.5  模型，而无法使用 GPT-4 等更高级的模型。
	-每日请求额度：每天仅可使用 20 次 AI 辅助功能（如代码生成、解释、修复等），超出后需等待次日重置。
	-高级功能缺失：无法使用如 AI 驱动的代码重构、复杂代码解释、多文件分析等高级功能。
	-适用场景：适合初学者体验 AI 辅助编程，或仅用于简单项目的轻量级开发
## 6.2 个人计划Pro版：
    -AI 模型选择：支持 GPT-4、deepseek 等高级模型，可根据任务复杂度选择更适合的模型。
    -无限请求额度：取消每日请求次数限制，可无限制使用 AI 辅助功能。
    -高级功能解锁：包含代码重构建议、长文本解释（如论文级代码分析）、团队协作功能（如共享项目 AI 分析）等。
    -优先支持：享受优先客服响应，更快解决使用中的问题。
    -价格：通常为订阅制，如每月$20（具体以官方定价为准）。
    -适用场景：适合专业开发者、高频使用 AI 辅助的场景，或需要处理复杂项目的团队
## 6.3 个人计划旗舰版：
	-顶级 AI 模型优先使用权：率先接入 最新版 GPT-4 Turbo、Claude 4 等前沿模型（例如 GPT-4 Turbo 支持 128K 上下文窗口，可处理更复杂的代码）。
	-享受模型参数调优的专属权限（如调整温度值以控制 AI 生成代码的创造性）。
	-极致性能与稳定性：AI 响应速度提升 50%（通过优化模型调用链路实现），高峰期无排队限制（Pro 版在高并发时可能需要等待）。
	-专属高级功能
		代码质量评估：AI 自动检查代码并生成评分报告（覆盖可读性、性能、安全等维度）。
		自定义 AI 工作流：支持创建个性化的 AI 指令模板（例如一键生成符合特定风格的文档注释）。
		跨项目知识图谱：自动关联和分析历史项目中的代码模式，提供跨项目的复用建议。
	-数据安全与隐私增强
		支持 本地模型部署（可选配 Cursor 私有部署版，敏感代码不传输至云端）。
		代码历史记录加密存储，提供 隐私模式（禁用 AI 对代码的学习功能）。
	-专属服务
		24/7 技术支持：通过邮件、工单或在线聊天获取即时帮助。
		专属客户经理：提供个性化使用建议和功能定制方案
## 6.4 团队版（Team）
	-功能扩展
		多用户管理：支持创建团队工作区，管理员可添加 / 管理多个成员账号。
		协作功能：团队共享代码片段库、AI 生成的最佳实践模板，支持多人同时编辑项目并查看彼此的 AI 辅助记录。
		统一账单：团队统一付费，简化财务管理。
		专属支持：提供专属客户经理和优先技术支持。
	-价格：基于团队规模计费，如每人每月 $40（具体以官方定价为准）。
	-适用场景：适合需要协同开发的小型 / 中型团队，或对代码质量和协作效率有较高要求的企业。
## 6.5 企业版（Enterprise）
	-定制化服务
		安全与合规：支持企业级安全需求，如 SSO（单点登录）集成、数据加密、合规审计等。
		定制化部署：可选择私有部署（On-premises）或与企业内部系统集成。
		高级 API 访问：提供更深度的 API 接口，允许企业开发自定义 AI 辅助工作流。
		专属培训：提供针对企业团队的定制化培训和最佳实践指导。
	-价格：需联系官方销售团队获取定制报价，通常基于企业规模和具体需求定价。
	-适用场景：适合大型企业、对数据安全有严格要求的行业（如金融、医疗），或需要深度定制 AI 辅助开发流程的组织

    

```

![image-20250622005911951](img/dday09-Cursor入门/image-20250622005911951.png)

![image-20250622010402057](img/dday09-Cursor入门/image-20250622010402057.png)

![image-20250622013736824](img/dday09-Cursor入门/image-20250622013736824.png)



## 2.2 安装

```python
# 1 下载：https://www.cursor.com/downloads


# 2 安装，一路下一步


# 3 登录账号，如下图
```





![image-20250622014002861](img/dday09-Cursor入门/image-20250622014002861.png)

![image-20250622014034378](img/dday09-Cursor入门/image-20250622014034378.png)

![image-20250622014059719](img/dday09-Cursor入门/image-20250622014059719.png)

![image-20250622014108500](img/dday09-Cursor入门/image-20250622014108500.png)

![image-20250622014119195](img/dday09-Cursor入门/image-20250622014119195.png)

![image-20250622014125714](img/dday09-Cursor入门/image-20250622014125714.png)

![image-20250622014137068](img/dday09-Cursor入门/image-20250622014137068.png)

![image-20250622014207061](img/dday09-Cursor入门/image-20250622014207061.png)

![image-20250622014240405](img/dday09-Cursor入门/image-20250622014240405.png)

![image-20250622014256468](img/dday09-Cursor入门/image-20250622014256468.png)

![image-20250622014358693](img/dday09-Cursor入门/image-20250622014358693.png)

![image-20250622014410129](img/dday09-Cursor入门/image-20250622014410129.png)

![image-20250622014436805](img/dday09-Cursor入门/image-20250622014436805.png)

![image-20250622014501892](img/dday09-Cursor入门/image-20250622014501892.png)

## 2.3 配置中文

```python
# 1 打开配置界面
	-方式一：右上角齿轮
    -方式二：ctrl + shift+J
    -方式三：ctrl + shift + P
    	-搜索 settings
        
# 2 安装中文插件
	- 左右分栏
    - 点击插件市场：搜索 中文插件
    - 下载中文插件
	-ctrl + shift + P
    	-搜索 language---》选择：config display language
    -选择中文即可
```

![image-20250622014854805](img/dday09-Cursor入门/image-20250622014854805.png)

![image-20250622014956231](img/dday09-Cursor入门/image-20250622014956231.png)

![image-20250622015042430](img/dday09-Cursor入门/image-20250622015042430.png)

![image-20250622015452642](img/dday09-Cursor入门/image-20250622015452642.png)

![image-20250622015659776](img/dday09-Cursor入门/image-20250622015659776.png)

![image-20250622015743593](img/dday09-Cursor入门/image-20250622015743593.png)

![image-20250622015250217](img/dday09-Cursor入门/image-20250622015250217.png)

![image-20250622015916696](img/dday09-Cursor入门/image-20250622015916696.png)

![image-20250622015950859](img/dday09-Cursor入门/image-20250622015950859.png)

![image-20250622020022461](img/dday09-Cursor入门/image-20250622020022461.png)

## 2.4 常用功能介绍

### 2.4.1 打开或新建项目

![image-20250622020443583](img/dday09-Cursor入门/image-20250622020443583.png)

### 2.4.2 新建文件

```python
# 1 方式一：如下图，点击新建文件图标
# 2 方式二：文件--》新建文本文件

# 3 ctrl+s保存：注意文件后缀名
	s1.py

# 4 会提示安装python插件：我们暂时先不安装
```

![image-20250622020723808](img/dday09-Cursor入门/image-20250622020723808.png)

![image-20250622020838174](img/dday09-Cursor入门/image-20250622020838174.png)

### 2.4.3 常用按钮

![image-20250622021313731](img/dday09-Cursor入门/image-20250622021313731.png)

### 2.4.4 打开多个项目

>再双击cursor图标，打开即可--》适用于同时开发多个项目
>
>比如开发前端+后端

### 2.4.5 左中右

```python
# 左侧：资源代码管理
# 中间：代码编写
# 右边：AI对话界面
	-1 点击右上角：如图
    -2 按： ctrl + alt + B
```

![image-20250622021645497](img/dday09-Cursor入门/image-20250622021645497.png)

## 2.5 配置之General

![image-20250622022320277](img/dday09-Cursor入门/image-20250622022320277.png)



## 2.6 配置之Chat

```python
# 1 Default Model：具有Agent（代理模式）、Ask（询问模式）、Manual（手动模式）等预定义模式
	-Agent:自主决策与执行：AI 会像 “开发者助手” 一样，基于用户指令和代码上下文，自主规划任务步骤并执行操作（如修改代码、创建文件、调试问题等），无需用户逐行确认,AI 可直接修改文件、创建新文件，甚至执行终端命令（需用户授权），操作结果会以 “代码差异” 形式展示，用户可选择接受或拒绝
    -Ask:用户提出具体问题或需求，AI 仅提供 “回答” 或 “代码片段”，不主动修改代码库，需用户手动将代码应用到项目中,AI 返回的代码需用户手动复制粘贴或通过 “应用代码块” 功能插入，不会自动执行操作
    -Manual:AI 完全基于用户输入的指令执行操作，不主动添加额外逻辑，适合需要精细控制的场景
        
复杂任务优先选代理模式：如需要 AI 帮你完成 “将项目从 Vue2 迁移到 Vue3”，代理模式会自动分析依赖、修改文件，效率更高。
日常提问用询问模式：遇到代码报错或技术疑问时，直接用询问模式获取解决方案，无需担心 AI 误改代码。
精细控制选手动模式：当需要严格按特定格式生成代码（如生成测试用例模板），或避免 AI 输出多余解释时，手动模式更灵活


# 2 Text Size ： 控制对话的字体大小

# 3 Auto-Clear Chat ：自动清除聊天记录
	-在一段时间不活动后，打开聊天面板到新聊天
    
# 4 scroll to new Message 滚动到新消息
	-如果有新消息，自动滚动到新消息处
    
# 5 completion Sound ：完成声音
	-Angent完成响应后，播放声音
# 6 自定义模式：测试版
	-创建具有特定模型，工具，快捷键和针对您工作流程定制的指令的自定义模式
    
# 7 Include Full-Folder context：包含完整文件夹上下文
	-允许讲所选文件夹的全部内容包含在上下文中
    
# 8 Web Search Tool ：网络搜索工具
	-允许Agnet 通过网络搜索相关信息
    
# 9Hierarchical Cursor Ignore：层次化忽略
	-应用 .cursorignore 文件到所有子文件夹，修改这个配置要重启
# 10 backspace removews context：退格键删除上下文
	-在输入开始时，按下退格键，移除 composer 中的最后一个上下文提示
    
# 11 out-of-context Edits in manual Mode：手动模式下的上下文外编辑
	-允许Agent 在手动模式下修改编辑选定之外的文件
    
# 12 auto-fix lints ：自动修复代码检查
	-自动修复聊天中的 lints错误
    
# 13 auto-accept on commit：自动接受提交
	-在文件提交且不再处于工作树中时，自动接受所有更改
    
# 14 auto-run mode：自动运行模式
	-允许Agent在响应时，搜索网络相关信息
# 15 Toolbar onselection：选择时，显示工具栏
	-选择代码时，显示添加到聊天和快捷编辑按钮
    
# 16 auto-parse links：自动解析连接
	-在粘贴到快速编辑输入时自动解析连接
    
 # 17 Auto-Select Code Regions for Quick Edit(ctrl+k):自动选择代码区域以进行快速编辑
	-自动选择区域进行内联代码编辑
    
 # 18 Themed Diff backgrounds:主题差异背景
	-使用主题背景颜色进行内连代码差异显示
    
 # 19 Character-Level Diffs：字符级差异
使用字符级差异进行内联代码差异

# 20 Terminal Hint：终端工具提示
	-使用终端中类似 添加到聊天 的工具提示
    
# 21 Preview Box for Terminal Ctrl+K ：终端 ctrl+k的预览框
	-使用预览框而不是将相应直接流式传输到外壳中
```





## 2.7 配置之Tab

```python
# 1 Cursor Tab:基于最近编辑的上下文感知多行建议
# 2 paartial Accepts：部分接受
	-通过Ctrl+右箭头接受建议的下一个单词
# 3 suggestions while commenting:注释时的建议
	允许在注释区域时，触发Tab键
    
# 4 whitespace-only suggestions：仅空白建议
	-建议编辑，如换行和缩进等进修改空白的编辑
    
# 5 Imports导入
	-自动导入TypeScript的模块
```



## 2.8 配置之Models

```python
# 1 max Mode ：New--最大模式-新版
	-获取最大上下文窗口和工具调用。适用于成本不敏感的高级用户
    -按api定价计费
#2 添加或搜索模式
	-查看所有模型
    -claude 模型写代码最好
    
# 3 API秘钥：可以添加 OpenAI，谷歌APIkey，亚马逊APIKey，awsKey等
```



## 2.9 配置之 Background Agents[配置之后台代理【新】]

```python
# 后台代理：测试版
	-在云服务中运行代理，处于测试预览中
    -后台代理仅在具有git存储库的文件夹中工作，请打开包含git存储库的文件夹以使用此功能
```



## 2.10 配置之Tools&Integrations【工具与集成】

```python
# 1 链接github以支持后台代理，bugBot和增加的代码库上下文
# 2 直接从slack与Cursor和后台代理一起工作
# 3 添加MCP 工具
```

## 2.11 配置之Rules-规则

```python
#1 记忆：在聊天中保存有用信息
	- 生成记忆：beta版
    	-根据聊天自动学习您的偏好
    -管理记忆：
    	-查看或删除单个记忆
# 2 用户规则：管理您的自定义用户规则和偏好设置
	-始终用简体中文回复
# 3 项目规则：帮助Agent理解此项目目录中的约定
	-包含 .cursorrules 文件：
    	-如果关闭，我们将不会在你的请求中包含.cursorrules文件
    -目前暂无项目规则，可以添加
```

## 2.12 配置之Indexing&Docs-索引与文档

```python
#1 codebase：代码库
	-代码库索引
    	-嵌入代码库以提高上下文理解和知识，嵌入和元数据存储在云端，但所有代码都本地存储
    -可以同步 和  删除索引
    
# 2 索引新文件：
	-自动索引任何包含少于50000个文件的新文件夹
# 3 忽略文件 在 .cursorignore
	-.cursorignore中的文件，将被排除在索引之外--》可以查看包含哪些文件
    
# 4 文档：爬取和索引自定义资源和开发文档
	-未添加任何文档：可以添加文档上下文或在聊天或编辑时，使用 @add来添加文档
```



## 2.13 配置之Network-网络

```python
# 1 Http兼容模式
	建议使用http/2 进行低延迟流媒体传输。在某些公司的代理或vpn环境中，可能需要降低兼容性模式

#2 网络诊断
	检测与后端ai服务的网络连接
```

![image-20250622164436701](img/day09-Cursor入门/image-20250622164436701.png)

## 2.14 配置之Beta功能

```python
# 1 更新访问权限
	-默认情况，获取稳定更新的通知，在抢先体验中，预发布版本可能不稳定，不适合生产环境
    
# 2 记事本
	-捕获项目笔记以自动包含在聊天上下文中
    
# 3 后台代理
	-后台代理在云中运行，处于测试阶段，可以开启关闭
```





## 2.6 配置执行Python

```python
# 1 安装python插件
# 2 安装完成后，ctrl+shift+p，输入select python interpreter：
# 3 选择本机安装的Python解释器即可
# 4 右下角显示

# 5 右键py文件，运行Python即可
```

![image-20250622130206276](img/day09-Cursor入门/image-20250622130206276.png)

![image-20250622130338057](img/day09-Cursor入门/image-20250622130338057.png)

![image-20250622130405923](img/day09-Cursor入门/image-20250622130405923.png)

![image-20250622130512026](img/day09-Cursor入门/image-20250622130512026.png)



![image-20250622130605056](img/day09-Cursor入门/image-20250622130605056.png)



# 3 IT公司人员职责及分配

```python
# 1 技术研发部门：负责产品的技术实现、架构设计、代码开发与维护
    架构师：设计系统架构（如微服务、分布式），制定技术选型和开发规范
	开发工程师（前端 / 后端 / 全栈）：实现功能代码，遵循架构规范开发模块（如前端负责页面交互，后端处理数据逻辑）
    测试工程师：设计测试用例，执行功能测试、性能测试，确保代码质量
    运维工程师（DevOps）：管理服务器、部署上线、监控系统稳定性，优化运维流程
    数据工程师 / 算法工程师：处理数据清洗、建模，开发 AI 算法（如推荐系统、机器学习模型）
    
# 2 产品部门：定义产品方向，收集用户需求，推动产品落地
    产品经理（PM）：调研市场需求，制定产品路线图，协调技术、设计、运营推进项目
    需求分析师：拆解业务需求，转化为技术可实现的功能规格说明书（PRD）
    项目经理（PM）：管理项目进度，协调资源，确保按时交付（部分公司由产品经理兼任
    
# 4 设计与用户体验：优化产品界面与用户体验，提升用户留存和转化率
    UI 设计师：设计产品界面视觉（如配色、布局、图标），输出高保真原型。
    UX 设计师：研究用户行为，优化交互流程（如按钮点击逻辑、页面跳转路径）。
    交互设计师：细化界面动效和操作反馈，提升使用流畅度。
    
# 5 运营与市场部：推广产品、运营用户、提升品牌影响力
    运营团队：
        用户运营：维护用户社群，策划活动提升活跃度（如签到奖励、用户分层运营）。
        内容运营：生产图文、视频等内容（如公众号推文、产品教程），吸引流量。
        活动运营：策划促销活动（如电商大促、裂变拉新），制定转化目标。
    市场团队：
        品牌市场：制定品牌策略（如 Slogan、视觉 VI），投放广告（如社交媒体、搜索引擎）。
        增长营销：通过 SEO/SEM、信息流广告等渠道获取新用户，优化获客成本。
        
# 6  销售与客户服务部：获取客户、完成交易、提供售后支持
    销售团队：
        客户经理：对接企业客户，制定销售方案，完成签单目标。
        渠道销售：拓展代理商、合作伙伴，扩大市场覆盖。
    客服团队：
        客服专员：通过电话 / 在线聊天解决用户问题，收集反馈优化产品。
        售后工程师：为企业客户提供技术支持（如部署培训、故障排查）
        
# 7 行政、人力、财务:保障公司日常运转，管理人才与资源
	人力资源（HR）：招聘、培训、绩效考核，搭建团队架构。
    行政部门：办公场地管理、采购、后勤支持。
    财务部门：财务核算、税务申报、预算管理。
```



# 4 开发常见项目

```python
# 1 前台项目-前端项目:
## 1.1 定义：
	负责用户可见的界面展示与交互逻辑，直接影响用户体验。
## 1.2 技术栈：
	Web 前端：HTML/CSS/JavaScript、框架（React/Vue/Angular）、构建工具（Webpack/Vite）。
	移动端前端：Flutter、React Native、原生 iOS（Swift）/Android（Kotlin）。
## 1.3 应用场景：
	企业官网、电商平台（如淘宝 PC 端）、管理后台（如 OA 系统界面）。
	移动端 H5 页面（如微信公众号内嵌页面）。
## 1.4 特点：
	注重 UI 设计、响应式布局、动画效果和性能优化
    
    
# 2 后台项目（后端项目）:
## 2.1 定义：
	处理数据逻辑、业务规则和服务器交互，不直接面向用户。
## 2.2 技术栈：
	编程语言：Java/Python/Go/PHP/.NET/C# 等。
	框架：Spring Boot（Java）、Django（Python）、Express（Node.js）。
	数据库：MySQL/Oracle/PostgreSQL（关系型）、MongoDB（非关系型）。
## 2.3 应用场景：
	电商平台的订单处理、用户数据管理、支付系统。
	云计算服务的 API 接口（如阿里云 API）。
## 2.4 特点：
	注重业务逻辑复杂度、数据安全性、并发处理和服务器性能。
    
# 3 小程序项目
## 3.1 定义：
	运行在第三方平台（如微信、支付宝）内的轻量化应用，无需下载安装。
## 3.2 技术栈：
	微信小程序：WXML（类似 HTML）、WXSS（类似 CSS）、JavaScript，或使用框架（Taro/uni-app 跨平台开发）。
	支付宝 / 抖音小程序：各平台专属语法或兼容 Web 技术。
## 3.3 应用场景：
	餐饮点单（如星巴克微信小程序）、共享单车扫码（如美团单车）、小游戏。
## 3.2 特点：
	依赖平台生态，开发周期短，流量入口丰富（如微信社交裂变）。
    
    
# 4 App 项目（移动端原生 / 混合应用）
## 4.1 定义：
	安装在移动端设备的独立应用，分为原生 App 和混合 App。
## 4.2 技术栈：
	原生 App：
		iOS：Swift/Objective-C + Xcode。
		Android：Kotlin/Java + Android Studio。
	混合 App：React Native/Flutter/Cordova（Web 技术封装）。
## 4.3 应用场景：
    社交软件（微信、抖音）、工具类（支付宝、高德地图）、游戏（王者荣耀）。
## 4.4 特点：
	可调用设备原生功能（相机、定位），性能优于小程序，但开发成本较高。
    
    
# 5 微服务项目
## 5.1 定义：
	将复杂系统拆分为独立部署的小型服务，通过 API 通信。
## 5.2 技术栈：
    服务注册与发现：Consul/Nacos。
    网关：Spring Cloud Gateway/APISIX。
    容器化：Docker/Kubernetes。
## 5.3 应用场景：
大型互联网平台（如京东、拼多多），需处理高并发和海量数据。


# 6 大数据项目
## 6.1 定义：
	处理海量数据的采集、存储、分析与可视化。
## 6.2 技术栈：
    数据采集：Flume/Sqoop。
    存储：Hadoop/HDFS、Spark。
    分析：Hive/Presto。
## 6.3 应用场景：
	用户行为分析（如抖音推荐算法）、金融风控数据建模。
    
# 7 物联网（IoT）项目
## 7.1 定义：
	连接硬件设备与云端的系统，实现数据交互与设备控制。
## 7,2 技术栈：
    硬件开发：Arduino/Raspberry Pi。
    云端：MQTT 协议、AWS IoT/Azure IoT。
## 7.3 应用场景：
	智能家居（如小米米家）、工业设备监控。
```

# 5 Cursor 自动编写贪食蛇小游戏

```python
# 1 输入：使用Python生成一个贪食蛇程序，并运行
# 2 自动生成代码，并运行，运行过程中出错，会自动修复
```

![image-20250622172308131](img/day09-Cursor入门/image-20250622172308131.png)

![image-20250622172321279](img/day09-Cursor入门/image-20250622172321279.png)

# 6 Cursor自动编写订单管理系统

```python
使用Flask框架，生成一个订单管理系统，有登录注册功能，创建，修改，查看，删除订单功能
```

![image-20250622174148357](img/day09-Cursor入门/image-20250622174148357.png)

# 补充

# 1 Cursor无法安装插件

```python
# 根本原因是因为cursor 商店源不对   可以更换下面的商店源

## 1.在cursor 目录中找到product.json文件（位置在D:\soft\cursor\resources\app\product.json）
	-注意是在自己的安装目录下
## 2.将下面的商店源进行更换可以直接复制下面的代码进行更换。
#### 修改https://marketplace.cursorapi.com为https://marketplace.visualstudio.com 
## 原来：
"extensionsGallery": {
    "galleryId": "cursor",
    "serviceUrl": "https://marketplace.cursorapi.com/_apis/public/gallery",
    "itemUrl": "https://marketplace.cursorapi.com/items",
    "resourceUrlTemplate": "https://marketplace.cursorapi.com/{publisher}/{name}/{version}/{path}",
    "controlUrl": "https://api2.cursor.sh/extensions-control",
    "recommendationsUrl": "",
    "nlsBaseUrl": "",
    "publisherUrl": ""
},
## 替换为：
"extensionsGallery": {
		"galleryId": "cursor",
		"serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
		"itemUrl": "https://marketplace.visualstudio.com/items",
		"resourceUrlTemplate": "https://marketplace.visualstudio.com/{publisher}/{name}/{version}/{path}",
		"controlUrl": "https://api2.cursor.sh/extensions-control",
		"extensionUrlTemplate": "https://www.vscode-unpkg.net/_gallery/{publisher}/{name}/latest",
		"recommendationsUrl": "",
		"nlsBaseUrl": "",
		"publisherUrl": ""
	},
## 3.重启cursor即可正常安装插件了
```




