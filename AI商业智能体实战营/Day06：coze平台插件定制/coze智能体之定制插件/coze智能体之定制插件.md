# coze智能体之定制插件



Coze 是一种灵活的 AI 平台，允许开发者通过自定义插件扩展其功能。这些插件可以通过特定的工作流工具进行集成和管理，从而实现复杂的业务逻辑编排。

插件节点主要用于在工作流中调用插件，运行指定的工具。插件就像是一个工具百宝箱，里面的每个工具都是可以调用的 API 哦。不管是商店里上架的插件，还是自己或者团队创建的插件，都能以节点的形式集成到工作流中，大大拓展了智能体的能力。

## 一 已有服务API插件

![image-20250410下午70118971](./assets/image-20250410%E4%B8%8B%E5%8D%8870118971.png)

```apl
https://www.coze.cn/open/docs/developer_guides/list_workspace
```

![image-20250410下午70256566](./assets/image-20250410%E4%B8%8B%E5%8D%8870256566-4282977.png)

![image-20250410下午70333227](./assets/image-20250410%E4%B8%8B%E5%8D%8870333227-4283014.png)

授权方式：有三种授权方式可供选择——不需要授权、Service 和 OAuth。

不需要授权：无需任何认证环节，直接请求接口并获取返回值。
Service：服务认证，API通过密钥或令牌校验合法性。需要向接口传递令牌信息，后端验证成功后才能获取返回值。
OAuth：一种常用于用户代理身份验证的标准，允许第三方应用程序在不共享用户密码的情况下访问用户下的特定资源。

![image-20250410下午70425439](./assets/image-20250410%E4%B8%8B%E5%8D%8870425439-4283066.png)

![image-20250410下午70526975](./assets/image-20250410%E4%B8%8B%E5%8D%8870526975-4283127.png)

![image-20250410下午70554155](./assets/image-20250410%E4%B8%8B%E5%8D%8870554155-4283155.png)

![image-20250410下午70630306](./assets/image-20250410%E4%B8%8B%E5%8D%8870630306-4283191.png)

API插件练习：

```apl
https://api.vvhan.com/
https://api.oick.cn/
```

![image-20250410下午74223275](./assets/image-20250410%E4%B8%8B%E5%8D%8874223275-4285344.png)

## 二 编程插件

![image-20250410下午73022989](./assets/image-20250410%E4%B8%8B%E5%8D%8873022989-4284623.png)

![image-20250410下午73051367](./assets/image-20250410%E4%B8%8B%E5%8D%8873051367-4284652.png)

![image-20250410下午73603600](./assets/image-20250410%E4%B8%8B%E5%8D%8873603600-4284964.png)

```python
from runtime import Args
from typings.get_url_list.get_url_list import Input, Output

"""
Each file needs to export a function named `handler`. This function is the entrance to the Tool.

Parameters:
args: parameters of the entry function.
args.input - input parameters, you can get test input value by args.input.xxx.
args.logger - logger instance used to print logs, injected by runtime.

Remember to fill in input/output in Metadata, it helps LLM to recognize and use tool.

Return:
The return data of the function, which should match the declared output parameters.
"""
import re


def handler(args: Args[Input])->Output:
    text = args.input.text
     # 正则表达式匹配URL
    url_pattern = r'https?://[^\s]+'
    urls = re.findall(url_pattern, text)
    return {
        "urls":urls,
        "count":len(urls)
    }

```

![image-20250410下午74122870](./assets/image-20250410%E4%B8%8B%E5%8D%8874122870-4285283.png)

![image-20250410下午73844459](./assets/image-20250410%E4%B8%8B%E5%8D%8873844459-4285125-4285179.png)

![image-20250410下午73900388](./assets/image-20250410%E4%B8%8B%E5%8D%8873844459-4285125-4285179.png)





