import requests

# 发起一个HTTP协议包四要素：
# -- (1) url
# -- (2) 请求方式 get/post请求
# -- (3) 请求头
# -- (4) 请求载荷（get请求走查询参数或者post请求走请求体）

# http协议格式：
# 方式1
"""
get url?查询参数 http/1.1
请求头1
请求头2
...
请求头n

请求体         
"""
# 方式2
"""
post url http/1.1
请求头1
请求头2
...
contentType：form
请求头n

user=yuan&pwd=123 :form格式    
"""
# 方式3

"""
post url http/1.1
请求头1
请求头2
...
contentType：json
请求头n
 
{"user":"yuan","pwd":123}：json格式      
"""

my_headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://ggzyfw.fujian.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzyfw.fujian.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'portal-sign': '02f433c6b30db0154f54687b5438d7f1',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}
data = {
    'pageNo': 2,
    'pageSize': 20,
    'total': 2797,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2024-09-29 00:00:00',
    'EndTime': '2025-03-29 23:59:59',
    'createTime': '',
    'ts': 1743234193847,
}
url = "https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo"
# data:默认数据处理成form表单格式
# res = requests.post(url, headers=my_headers, data=data)
# data:数据处理成json格式
res = requests.post(url, headers=my_headers, json=data)
print(res.text)
