# gf = {"name": "高圆圆", "age": 32}
# 无序，属于容器类型
# print(len(gf))

# (1) 增或改: 字典对象[键] = 值
# gf["age"] = 27
# print(gf)
# gf["height"] = 175
# print(gf)

# (2) 删除
# l = [1, 2, 3]
# del l[2]
# print(l)
# del l
# print(l)
# del gf
# del gf["age"]
# print(gf)

# (3) 查看键值
# print(gf["name"])
# print(gf["names"]) # 键不存在，报错

# (4) 成员判断 in
# print("names" in gf)
# print("age" in gf)

# while 1:
#     key = input("查看的键：")
#     print(key)
#     if key in gf:
#         print(gf[key])
#     else:
#         print("键不存在！")

# (5) 遍历按字典所有的键值对
gf = {"name": "高圆圆", "age": 32, "height": 175}
for key in gf:
    print(key,gf[key])
