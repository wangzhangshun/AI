# 预备知识点
# x = 1
# y = 2
# x, y = 1, 2
# a, b, c = [1, 2, 3]
# a, b, c = (1, 2, 3)
# print(a)
# print(b)
# print(c)


# gf = {"name": "高圆圆", "age": 32}

# 内置方法补充

# keys = list(gf.keys())
# print(keys,type(keys))
# print(keys[1])

# values = list(gf.values())
# print(values,type(values))
# print(values[0])

# items = list(gf.items())
# print(items) # [('name', '高圆圆'), ('age', 32)]

# gf = {"name": "高圆圆", "age": 32}

# for key in gf:
#     print(key, gf.get(key))

# for i in gf.items(): # [('name', '高圆圆'), ('age', 32)]
#     print(i[0],i[1])


# for key,val in gf.items(): # [('name', '高圆圆'), ('age', 32)]
#     print(val)

# 创建字典:
# courses = ["english", "math", "chinese"]
# # d = {"english": 0, "math": 0, "chinese": 0}
# ret = dict.fromkeys(courses,60)
# print(ret)
