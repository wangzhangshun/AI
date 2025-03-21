# （5）计算初始本金为1万，年利率为0.0325的情况下，需要多少年才能将本金和利息翻倍，即本金和利息的总和达到原来的两倍。
# base = 10000
# rate = 0.0325
# total = base
# 存一年后：total = 10000+ 10000*0.0325  # 10325
# 存两年后：total = 10325+ 10325*0.0325  # 10660
# 存三年后：total = 10660+ 10660*0.0325  #
# 存n年后: total = total+ total * rate

# base = 10000
# rate = 0.0325
# total = base
#
# year = 0
# while total < 2 * base:
#     total = total + total * rate
#     print(total)
#     year += 1
#
# print(year)


# （6） 编写一个程序，生成斐波那契数列的第20个数字（斐波那契数列是指从0和1开始，后面的每一项都是前两项的和）

# pre = 0
# current = 1
#
# for _ in range(100):
#     next_num = pre + current
#     print("next:", next_num)
#     pre = current
#     current = next_num


# (7) 编写一个程序，接受用户输入的一个整数，判断该数是否是素数（只能被1和自身整除的数）。注意，素数的定义是大于1的自然数，只能被1和自身整除，没有其他的正因数。
# 方案1
# num = int(input("请输入一个大于1的整数："))
# flag = True
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
#         break
# if flag:
#     print(f"{num}是素数")
# else:
#     print(f"{num}不是素数")

# 方案2: for-else
"""
for item in sequence:
    # 迭代操作
    if condition:
        # 满足条件时执行的操作
        break
else:
    # 在循环结束后执行的操作
"""
# num = int(input("请输入一个大于1的整数："))
#
# for i in range(2, num):
#     if num % i == 0:
#         print(f"{num}不是素数")
#         break
# else:
#     print(f"{num}是素数")



