# 案例1:
# l1 = [3, 4, 5]
# d1 = {"a": 1, "b": 2, "c": l1}

# print(id(l1))
# print(id(d1["c"]))
# 列表更新
# l1.append(6)
# print(d1)
# d1["c"][0] = 300
# print(l1)
# 变量重新赋值
# d1["c"] = 300
# print(l1)
# print(id(l1))
# print(id(d1["c"]))


# 案例2:

# d2 = {"x": 10, "y": 20}
# d3 = {"a": 1, "b": 2, "c": d2}

# d2["z"] = 30
# d2.update({"z": 30})
# print(d3)

# print(type(d3["c"]))
# d3["c"].pop("y")
# print(d2)
# d2 = 1000
# print(d3)


# 案例3
d4 = {"x": 10, "y": 20}
l2 = [1, 2, d4]
# d4["z"] = 30
# print(l2)

# print(type(l2[2]))
# l2[2]["y"] = 200
# print(d4)

l2[2] = [3, 4]
