import base64
import json

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

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
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'portal-sign': 'a56891e739cdb7563faf1740f9aa77b4',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'pageNo': 3,
    'pageSize': 20,
    'total': 2798,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2024-09-29 00:00:00',
    'EndTime': '2025-03-29 23:59:59',
    'createTime': '',
    'ts': 1743239013232,
}

response = requests.post('https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo', headers=headers, json=json_data)

# print(response.text)

# 基于Python做出AES的解密
# (1) base64解码
base64_encrypt_data = response.json().get("Data")
# print(base64_encrypt_data)

encrypt_data = base64.b64decode(base64_encrypt_data)
# print(encrypt_data)

# (2) aes解密
k = 'EB444973714E4A40876CE66BE45D5930'.encode()
i = 'B5A8904209931867'.encode()
aes = AES.new(key=k, mode=AES.MODE_CBC, iv=i)
data = aes.decrypt(encrypt_data)
data = unpad(data, 16)
data = json.loads(data)
print(data)

for i in data["Table"]:
     print(i.get("NAME"))
