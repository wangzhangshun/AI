"""


while 表达式:
    循环语句块

"""

# (1) 无限循环
# while True:
#     print("hello world")

# (2) 有限循环(三要素循环)

# 案例1: 打印10次hello world
count = 0  # 初始变量
while count < 10:  # 判断表达式
    print("hello world")

    count += 1  # 步进语句 count = count+1
