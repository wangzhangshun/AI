# (1) 反转列表中的元素顺序，`numbers = [5, 2, 9, 1, 7, 6]`

# numbers = [5, 2, 9, 1, 7, 6]
# print(numbers[:])
# print(numbers[::-1])
# print(numbers[::-2])


# (2) 给定一个列表，筛选出列表中大于等于 5 的元素，并存储在一个新的列表中。

# 方案1
# numbers = [5, 2, 9, 1, 7, 6]
# l = []
# for i in numbers:
#     if i >= 5:
#         print(i)
#         l.append(i)
# print(l)

# 方案2
# numbers = [5, 2, 9, 1, 7, 6]
# print([i for i in numbers if i >= 5])


# (3) `l=[23,4,5,66,76,12,88,23,65]`,l保留所有的偶数

# 方式1
# l = [23, 4, 5, 66, 76, 12, 88, 23, 65]
#
# l2 = []
# for i in l:
#     if i % 2 == 0:
#         l2.append(i)
# print(l2)
# l = l2
# print(l)

# 方式2

# l = [23, 4, 5, 66, 76, 12, 88, 23, 65]
# l = [i for i in l if i % 2 == 0]
# print(l)

# 方式3
# l = [23, 4, 5, 23, 76, 12, 88, 23, 65]
# l = [1, 3, 5, 7]
# for i in l[:]:
#     print("i:::",i)
#     if i % 2 != 0:
#         l.remove(i)
#         print(f"l删除了{i},现在的l{l}")
# print(l)

# (4) 计算给定列表中所有元素的和，但要跳过列表中的负数，`numbers = [1, 2, -3, 4, -5, 6, 7, -8, 9]`
# numbers = [1, 2, -3, 4, -5, 6, 7, -8, 9]
#
# ret = 0
# for i in numbers:
#     if i >= 0:
#         # print(i)
#         ret += i
# print(ret)


# (5) 编写一个程序，将列表中的所有字符串元素反转
# 方式1
# data = ["yuan", "alex", "rain", "eric"]
# print(data[::-1])
#
# l = []
# for i in data:
#     print(i[::-1])
#     l.append(i[::-1])
# print(l)
# data = l

# 方式2
# data = ["yuan", "alex", "rain", "eric"]
#
# print([name[::-1] for name in data])
