import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'i',
    'range': 'bytes=0-',
    'referer': 'https://v95-zjb-a.douyinvod.com/4a6dc8117794abe976b81ffe4aba0130/6807c58b/video/tos/cn/tos-cn-ve-15c001-alinc2/oYZGiK8ig6eLQEhIoBi0A5QBghCLBAO9f2AAi2/?a=1128&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1046&bt=1046&cs=0&ds=4&ft=VJbLr3TIRR0sWrC12D12Nc.xBiGNbLlb19dU_4n3eTxJNv7TGW&mime_type=video_mp4&qs=0&rc=M2dnaWQ8OWc4Z2k0M2Q4NUBpanNoaHA5cmtnMzMzNGkzM0A2MGEtNDU1XjQxYC5iMzQwYSNkMWUyMmRjcDBhLS1kLS9zcw%3D%3D&btag=c0000e0008d200&cquery=100y&dy_q=1745336176&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=202504222336169B618D1EA3F42931502F',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'video',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

params = {
    'a': '1128',
    'ch': '0',
    'cr': '0',
    'dr': '0',
    'er': '0',
    'cd': '0|0|0|0',
    'cv': '1',
    'br': '1046',
    'bt': '1046',
    'cs': '0',
    'ds': '4',
    'ft': 'VJbLr3TIRR0sWrC12D12Nc.xBiGNbLlb19dU_4n3eTxJNv7TGW',
    'mime_type': 'video_mp4',
    'qs': '0',
    'rc': 'M2dnaWQ8OWc4Z2k0M2Q4NUBpanNoaHA5cmtnMzMzNGkzM0A2MGEtNDU1XjQxYC5iMzQwYSNkMWUyMmRjcDBhLS1kLS9zcw==',
    'btag': 'c0000e0008d200',
    'cquery': '100y',
    'dy_q': '1745336176',
    'feature_id': '46a7bb47b4fd1280f3d3825bf2b29388',
    'l': '202504222336169B618D1EA3F42931502F',
}

response = requests.get(
    'https://v95-zjb-a.douyinvod.com/4a6dc8117794abe976b81ffe4aba0130/6807c58b/video/tos/cn/tos-cn-ve-15c001-alinc2/oYZGiK8ig6eLQEhIoBi0A5QBghCLBAO9f2AAi2/',
    params=params,
    headers=headers,
)

print(response.content)


# 将数据写入一个

with open("a.mp4","wb") as f:
    f.write(response.content)