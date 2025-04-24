"""
get/post

请求首行
请求头
请求体

一个get包：
get path?查询参数  协议
请求头1
请求头2
UA：浏览器

空

一个post包：
post path  协议
请求头1
请求头2
UA：浏览器

user=yuan&pwd=123
{"user":"yuan","pwd":"123"}



响应数据

协议 状态码 状态码解释文
响应头1
响应头2

响应体（响应数据）


"""

# 四要素：请求方法/url/载荷数据/请求头
import re
import requests

# requests.get()
# requests.post()
# requests.get(url,headers=,params=,data=)

# (1) 爬虫
url = "https://www.baidu.com/"
my_headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
res = requests.get(url=url, headers=my_headers)
res.encoding = "utf8"
# print(res.status_code)
# print(res.headers)
# print(res.text)  # res.content


# (2) 数据解析

# 使用正则表达式提取新闻标题
titles = re.findall(r'<span class="title-content-title">(.*?)<\/span>',res.text)

# 打印提取的标题
for title in titles:
    print(title)







