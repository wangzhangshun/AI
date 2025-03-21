# 一、计算运算符

# print(1 + 1)
# print(1 - 1)
# print(1 * 1)
# print(1 / 1)
#
# x = 5
# y = 2
# print(5 / 2)
# print(5 // 2)  # 商
# print(5 % 2)  # 余数：1
# print(5 % 3)  # 余数：2

# 应用1：计算某个变量值是否为偶数
# a = 135
# print(a % 2 == 0)

# 应用2
# a = int(input("please input an int num:"))
# # print(a % 2 == 0)
# if a % 2 == 0:
#     print("是偶数")
# else:
#     print("是奇数")


# 二、比较运算符： 返回值都是布尔值（True，False）

# print(2 >= 1)

# 三、赋值运算符

# (1) 普通赋值语句
# x = 1
# x = 1 + 2
# y = x + 3
# print(y)

# (2) 自加运算符

# 版本1
# exp = 85
# print("kill小妖怪,经验值+5")
# exp = exp+5
# print(exp)
# print("kill小妖怪,经验值+5")
# exp = exp+5
# print("kill小妖怪,经验值+5")
# exp = exp+5
# print("kill小妖怪,经验值+5")
# exp = exp+5
# print(exp)

# 版本2
# exp = 85
# print("kill小妖怪,经验值+5")
# exp += 5  # exp = exp + 5
# print(exp)
# print("kill小妖怪,经验值+5")
# exp += 5
# print("kill小妖怪,经验值+5")
# exp += 5
# print("kill小妖怪,经验值+5")
# exp += 5
# print(exp)

blood = 100
print("受到攻击,血值降低10")
blood -= 10  # blood = blood - 10
print(blood)
