import time
import base64
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import md5
import json

headers = {

}

# 生成sign值
def get_sign(data):
    # (1) 剔除空值
    new_data = {}
    for key, val in data.items():
        # print(key, val)
        if val == "" or val == 0:
            continue
        new_data[key] = val

    # print(new_data)

    # (2) 排序
    s = new_data.items()
    # print(s)
    ret = sorted(s, key=lambda item: item[0])
    # print(ret)
    s2 = ""
    for key, val in ret:
        s2 += key + str(val)

    # print(s2)
    ra = "B3978D054A72A7002063637CCDF6B2E5"

    n = ra + s2

    # (3) 生成md5值
    m = md5()
    m.update(n.encode())
    sign = m.hexdigest()
    # print(sign)  # 4145a19057c83fd6a99163d0bd2f5e88

    return sign


def decrypt(res):
    # 基于Python做出AES的解密
    # (1) base64解码
    base64_encrypt_data = res.json().get("Data")
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


def main():
    for i in range(1,10):
        json_data = {
            "ts": int(time.time() * 1000),
            "pageNo": i,
            "pageSize": 20,
            "total": 2798,
            "AREACODE": "",
            "M_PROJECT_TYPE": "",
            "KIND": "GCJS",
            "GGTYPE": "1",
            "PROTYPE": "",
            "timeType": "6",
            "BeginTime": "2024-09-29 00:00:00",
            "EndTime": "2025-03-29 23:59:59",
            "createTime": ""
        }
        sign = get_sign(json_data)

        headers["portal-sign"] = sign

        response = requests.post('https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo', headers=headers,
                                 json=json_data)
        # 解密
        decrypt(response)
        time.sleep(1)


if __name__ == '__main__':
    main()
