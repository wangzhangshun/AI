import requests

url = "https://v1.yiketianqi.com/api?unescape=1&version=v91&appid=47284135&appsecret=jlmX3A6s&ext=&cityid=&city="
res = requests.get(url)
# res:响应首行，响应头，响应体
res = res.json()


for i in res.get("data"):
    print(i.get("day"),i.get("day"),i.get("tem2"),i.get("tem1"))


