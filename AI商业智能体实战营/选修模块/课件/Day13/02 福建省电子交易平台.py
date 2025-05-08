import requests
import execjs

js_code = open("03 福建省电子交易平台.js").read()
js_compile = execjs.compile(js_code)

headers = {
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
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'pageNo': 5,
    'pageSize': 20,
    'total': 2813,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2024-10-09 00:00:00',
    'EndTime': '2025-04-09 23:59:59',
    'createTime': '',
    'ts': 1744203721471,
}

sign = js_compile.call("d", json_data)
print("sign:::", sign)

headers['portal-sign'] = sign

response = requests.post('https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo', headers=headers, json=json_data)
print(response.text)
data = response.json().get("Data")

# 响应解密
print(data)
data = js_compile.call("b", data)
print(data)
