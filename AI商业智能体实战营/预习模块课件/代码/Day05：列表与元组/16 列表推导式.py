# 构建列表:1-10的平方
# 方式1:基本方式
# ret = []
# for i in range(1, 11):
#     ret.append(i ** 2)
# print(ret)

# 方式2:列表表达式
# ret = [1 for i in range(1, 11)]
# print(ret)
# ret = [i for i in range(1, 11)]
# print(ret)

# ret = [i**2+1 for i in range(1, 11)]
# print(ret)

# ret = [i for i in range(1, 101) if i > 1000]
# print(ret)
# ret = [i for i in range(1, 101) if i % 13 == 0]
# print(ret)


# ret = [i**2 for i in range(1, 101) if i % 13 == 0]
# print(ret)

words = ["apple", "banana", "cherry", "date", "elderberry"]
ret = [i.upper() for i in words if len(i)>5]
print(ret)