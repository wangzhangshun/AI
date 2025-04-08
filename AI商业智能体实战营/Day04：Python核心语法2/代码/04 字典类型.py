# 编程本质就是对数据做各种操作
# 基本数据基本操作
# 高级数据（容器数据）增删改查操作

# 列表的灵魂是索引管理值
# info = ["yuan", 18, 185, 140]
# print(info[2])
# 字典的灵魂是键管理值
# info2 = {"name": "yuan", "age": 18, "height": 185, "weight": 140}
# 一、基本语法实现
# (1) 查
# print(info2["height"])
# (2) 添加和修改
# # info2["gender"] = "male"
# info2["age"] = 20
# print(info2)
# (3) 删除键值对
# del info2["name"]
# del info2
# print(info2)

# 二、内置函数实现（推荐）:字典对象.方法()
info2 = {"name": "yuan", "age": 18, "height": 185, "weight": 140}

# (1) 查
# print(info2["names"])
# print(info2.get("name"))
# (2) 添加和修改
# info2.update({"age": 22, "gender": "male"})
# print(info2)
# (3) 删除键值对
# info2.pop("weight")
# print(info2)


