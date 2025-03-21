# 案例1:
# for i in range(1, 101):
#     if i == 88:
#         break
#     print(i)

# 案例2: 打印除了88以外的1-100所有值
# for i in range(1, 101):
#     if i == 88:
#         continue  # 退出当次循环，当次continue下面的代码不再执行
#     print(i)

# for i in range(1, 101):
#     if i == 88:
#         continue  # 退出当次循环，当次continue下面的代码不再执行
#     print(i)

# for i in range(1, 101):
#     if i != 88:
#         print(i)

# 案例3: 计算1-100中所有能整除13的的值累加和
# ret = 0
# for i in range(1, 101):
#     if i % 13 == 0:
#         ret += i
# print(ret)


# ret = 0
# for i in range(1, 101):
#     if i % 13 != 0:
#         continue
#     ret += i
#
# print(ret)


