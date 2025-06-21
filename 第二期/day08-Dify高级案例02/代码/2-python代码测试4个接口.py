
# pip install requests

import requests
# 1 获取每个销售，2025-02月度销售额
res=requests.get('http://192.168.71.100:5000/get_01?month=2025-02')
print(res.json())

# 2  获取最近3个月,所有销售 总销售数据
res=requests.get('http://192.168.71.100:5000/get_02?month=3')
print(res.json())

# 3  获取  2025-04 月份销售最高排名
res=requests.get('http://192.168.71.100:5000/get_03?month=2025-04')
print(res.json())
# 4  获取  justin 2025-04 月份销售数据
res=requests.get('http://192.168.71.100:5000/get_04?month=2025-04&name=justin')
print(res.json())