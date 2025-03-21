# 案例1: 计算1-100的和
# while版本
# count = 1
# s = 0
# while count <= 1000:
#     # 逻辑代码块开始
#     s += count
#     # 逻辑代码块结束
#     count += 1
# print(s)

# for 版本：

# s = 0
# for i in range(1,101):
#     s += i
# print(s)

# 案例2:
import random
import string

# while版本
# count = 0
# s = ""
# while count < 100:
#     # 逻辑代码块开始
#     char = random.choice(string.digits+string.ascii_letters)
#     # print(char)
#     s += char
#     # 逻辑代码块结束
#     count += 1
#
# print("s:::",s)

# for版本


s = ""
for i in range(100):
    char = random.choice(string.digits + string.ascii_letters)
    # print(char)
    s += char
print("s:::", s)
