# 案例1: 打印10次hello world
# count = 0  # (1) 初始变量
# while count < 10:  # (2) 判断表达式
#     print("hello world")
#
#     count += 1  # (3) 步进语句 count = count+1

# 案例2: 打印1-100

# # 方式1:
# n = 0  # (1) 初始变量
# while n < 100:  # (2) 判断表达式
#     # 逻辑代码块开始
#     print(n + 1)
#     # 逻辑代码块结束
#     n += 1  # (3) 步进语句 count = count+1


# 方式2:
# n = 0  # (1) 初始变量
# while n < 100:  # (2) 判断表达式
#     n += 1  # (3) 步进语句 count = count+1
#     # 逻辑代码块开始
#     print(n)
#     # 逻辑代码块结束

# 方式3:
# n = 10  # (1) 初始变量
# while n < 111:  # (2) 判断表达式
#     print(n)
#     n += 1  # (3) 步进语句 count = count+1


# 案例3: 打印100-1

# 方式1
# n = 0  # (1) 初始变量
# while n < 100:  # (2) 判断表达式
#     # 逻辑代码块开始
#     print(100-n)
#     # 逻辑代码块结束
#     n += 1  # (3) 步进语句 count = count+1

# 方式2
n = 100  # n: 100-1地变化
while n >= 1:
    print(n)
    n -= 1
