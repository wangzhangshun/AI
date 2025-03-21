# (6) 从一个列表中移除重复的元素，`numbers = [1, 2, 3, 2, 4, 3, 5, 6, 5]`

#
# l = []
# for i in numbers:
#     if i not in l:
#         l.append(i)
# print(l)

# print(list(set(numbers)))

# (7) 编写一个程序，找到给定列表中的最大值和最小值。
# numbers = [23, 2, 5, 66, 76, 12, 88, 23, 65]
# max_value = numbers[0]
# min_value = numbers[0]
# for i in numbers:
#     if i > max_value:
#         max_value = i
#
#     if i < min_value:
#         min_value = i
#
# print("max value:", max_value)
# print("min value:", min_value)

# (8) 将二维列表中所有元素放在一个新列表中，`numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

# 方式1
# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# l = []
# for i in numbers:
#     for j in i:
#         l.append(j)
# print(l)

# 方式2
# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([j*j for i in numbers for j in i if j % 2 == 0])

# (9) 编写一个程序，计算给定列表中所有正数元素的平均值。
# numbers = [1, 2, -3, 4, -5, 6, 7, -8, 9]
# ret = 0
# n = 0
# for i in numbers:
#     if i >= 0:
#         # print(i)
#         ret += i
#         n += 1
# print(ret)
# print(n)
# print(round(ret/n,2))

# (10) 编写一个程序，找到给定列表中的所有大于平均值的元素并计算它们的总和

# numbers = [1, 2, -3, 4, -5, 6, 7, -8, 9]
# ret = 0
# for i in numbers:
#     ret += i
# print(ret)
#
# average = round(ret / len(numbers), 2)
#
# ret2 = 0
# for i in numbers:
#
#     if i > average:
#         ret2 += i
#
# print(ret2)
