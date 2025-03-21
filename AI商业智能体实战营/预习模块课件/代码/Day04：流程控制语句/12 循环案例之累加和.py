"""
# 准备：
# 假设有一个变量s的初始值为0，将s增加5次，每次增加值分别为1，2，3，4，5，然后打印s的值。
"""
# s = 0
# s = 1 + 2 + 3 + 4 + 5
# print(s)

# s = 0
# a = 1
# s += a
# print(s)
# b = 2
# s += b
# print(s)
# c = 3
# s += c
# print(s)
# d = 4
# s += d
# print(s)
# e = 5
# s += e
# print(s)


# 计算1-100的和

count = 1
s = 0
while count <= 1000:
    # 逻辑代码块开始
    s += count
    # 逻辑代码块结束
    count += 1

print(s)
