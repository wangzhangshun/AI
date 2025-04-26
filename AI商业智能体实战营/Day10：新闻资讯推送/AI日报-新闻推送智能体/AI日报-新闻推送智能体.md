# AI日报-新闻推送智能体



## 一、新闻推送

### 【1】抓取新闻插件

![image-20250425下午55913641](./assets/image-20250425%E4%B8%8B%E5%8D%8855913641.png)

![image-20250425下午55935415](./assets/image-20250425%E4%B8%8B%E5%8D%8855935415-5575176.png)

![image-20250425下午60012675](./assets/image-20250425%E4%B8%8B%E5%8D%8860012675-5575213.png)

### 【2】数据调整

![image-20250425下午60222596](./assets/image-20250425%E4%B8%8B%E5%8D%8860222596-5575343.png)

代码1:

```python
async def main(args: Args) -> Output:
    params = args.params

    ret = []
    for item in params["input"]:
        ret.append(
            {
                "title":item["title"],
                 "url":item["url"],
                  "desc":item["summary"],
            }
        )


    # 构建输出对象
    ret: Output = {
        "key0": ret
       
    }
    return ret
```

代码2:

```python
async def main(args: Args) -> Output:
    params = args.params

    ret = []
    for item in params["input"]:
        ret.append(
            {
                "title":item["name"],
                 "url":item["url"],
                  "desc":item["snippet"],
            }
        )


    # 构建输出对象
    ret: Output = {
        "key0": ret
       
    }
    return ret
```

### 【3】数据汇总

![image-20250425下午60347662](./assets/image-20250425%E4%B8%8B%E5%8D%8860347662-5575428.png)

汇总节点：

```python
async def main(args: Args) -> Output:
    params = args.params
    input1 = params['input1']
    input2 = params['input2']
    # 构建输出对象
    ret: Output = {
        "key0":input1+ input2[:3]
      
    }
    return ret
```

### 【4】大模型

![image-20250425下午60446685](./assets/image-20250425%E4%B8%8B%E5%8D%8860446685-5575488.png)

提示词：

```apl
# 角色
你是一名关于新闻消息的总结专家，擅长将用户信息搜索出来的desc进行提炼汇总并展示给用户，附上地址

# 技能
1. 仔细阅读数据中的desc
2. 提炼概要
3. 找出源地址

== 示例 ==
- 新闻简介： 具体提炼的内容
- [来源网站](url)

输入数据{{data}}
```

### 【5】卡片

![image-20250425下午60654174](./assets/image-20250425%E4%B8%8B%E5%8D%8860654174-5575615.png)

![image-20250425下午60726355](./assets/image-20250425%E4%B8%8B%E5%8D%8860726355-5575647.png)

> 更改了工作流记得发布后再测试

![image-20250425下午60816208](./assets/image-20250425%E4%B8%8B%E5%8D%8860816208-5575697.png)

### 【6】触发器（定时推送）

![image-20250425下午61024977](./assets/image-20250425%E4%B8%8B%E5%8D%8861024977-5575826.png)

![image-20250425下午60939743](./assets/image-20250425%E4%B8%8B%E5%8D%8860939743-5575780.png)

## 二、AI咨询日报

### 【1】主页链接提取

![image-20250425下午61309349](./assets/image-20250425%E4%B8%8B%E5%8D%8861309349.png)

```apl
https://fisherdaddy.com/
```

![image-20250425下午61342583](./assets/image-20250425%E4%B8%8B%E5%8D%8861342583-5576023.png)

### 【2】数据清洗

![image-20250425下午61432899](./assets/image-20250425%E4%B8%8B%E5%8D%8861432899-5576073.png)

```python
import json
async def main(args: Args) -> Output:
    params = args.params
    # 构建输出对象
   # filter(lambda i:len(i["title"])>10,params["input"])
    r = []
    for i in params["links"]:

        if i.get("href").find("https://fisherdaddy.com/posts/") != -1:
        
            r.append(i.get("href"))


    ret: Output = {
        "key0":r[:3]
    }
    return ret
```

### 【3】循环提取链接文章信息

![image-20250425下午61633373](./assets/image-20250425%E4%B8%8B%E5%8D%8861633373-5576194.png)

![image-20250425下午61820895](./assets/image-20250425%E4%B8%8B%E5%8D%8861820895-5576301.png)

![image-20250425下午61657548](./assets/image-20250425%E4%B8%8B%E5%8D%8861657548-5576218.png)

![image-20250425下午61743985](./assets/image-20250425%E4%B8%8B%E5%8D%8861743985-5576264.png)

```apl
# 角色
你是一位文章凝练专家，能够准确地提炼文章的核心信息

# 技能
1. 接收网页内容：{{content}}
2. 根据内容进行提炼，字数不要超过200字
3. 如果英文的内容，也要用中文总结
4. 严格按着的示例格式返回

# 限制
保证url一定存在

== 示例 == 
标题：{{title}}
地址：{{url}}
提炼：总结的内容
== 示例结束 == 
```

### 【4】数据集成

![image-20250425下午62100583](./assets/image-20250425%E4%B8%8B%E5%8D%8862100583-5576461.png)

提示词：

```apl
# 角色
你是一位专业的排版专家，擅长将各种数据信息进行结构化排版后并返回，使内容呈现出清晰、美观的效果
# 技能
## 1. 对文本进行排版
1. 这是输入的信息：{{input}}
2. 对文本中的标题进行加粗处理
3. 对本文中的总结部分进行加粗并换行显示
4. 合理运用换行和缩紧，使排版更加清晰

== 回复示例 ==
**标题:** <标题内容>
**地址:** <地址>
**总结:** <总结>
== 示例结束 ==
```

### 【5】多平台AI咨询

![image-20250425下午62341251](./assets/image-20250425%E4%B8%8B%E5%8D%8862341251-5576622.png)

![image-20250425下午62504679](./assets/image-20250425%E4%B8%8B%E5%8D%8862504679-5576705.png)

