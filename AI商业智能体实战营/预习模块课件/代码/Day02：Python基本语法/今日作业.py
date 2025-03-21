# 2. 解析`x=1;x=x+1`执行过程

# x = 1
# x = x + 1
# x += 1
# print(x)

# 3. `1+"1"`的结果是?
# print(1 + "1")

# 4. `bool("2<1")`的结果是？
# print(bool(2 < 1))
# print(bool("False"))
# print(bool("-1"))
# print(bool("0"))
# print(bool(""))
# print(bool("2<1"))

# 5.  浅述目前学过的Python的内置函数以及功能
# print("hello world")
# data = input("")

# print(id(100))
# x = 100
# print(id(x))
# type(100)
# print(type(100))

# print(bool(100))
# print(bool(0))
# int("100")
# str(100)

# 6.分析下面程序的执行过程以及结果

# a = 1
# b = a
# c = b
# a, d = c + 1, b + 2
# a += 1
# print(a, d)
# print(id(a))
# print(id(d))

# 7.  获取用户输入圆的半径。使用圆的周长和面积公式计算并打印出输入半径的圆的周长和面积。
# pai = 3.1415926
# r = int(input("请输入圆的半径"))
#
# area = round(pai * r * r, 5)
# perimeter = round(2 * pai * r, 5)
#
# print("面积：", area)
# print("周长：", perimeter)

# 8.  假设有一个变量count的初始值为0，将count增加5次，每次增加值分别为1，2，3，4，5，然后打印count的值。

# count = 0
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# # print(a + b + c + d + e)
# count = count + a
# print("count 吃进a后的结果",count)
# count = count + b
# print("count 吃进b后的结果",count)
# count = count + c
# print("count 吃进c后的结果",count)
# count = count + d
# print("count 吃进d后的结果",count)
# count = count + e
# print("count 吃进e后的结果",count)

# 9.  判断一个学生的考试成绩score是否在80到100之间（包括80和100）
# score = int(input("input a score:"))
# print(score >= 80 and score <= 100)
# 判断一个学生的考试成绩score是否小于80或大于100之间
# print(score < 80 or score > 100)
# print(not (score >= 80 and score <= 100))

# 10.  输入一个数字，判断是否是三位数且能被13整除
# num = input("input a num:")
# print(len(num) == 3 and int(num) % 13 == 0)

# 11.  判断用户名密码是否正确
# user = input("input a user:")
# pwd = input("input a pwd:")
#
# username = "root"
# password = "123"
# print(user == username and pwd == password)

# 12.  判断一个年份year是否是闰年，如果是，则打印"year是闰年"，否则打印"year不是闰年"。
# 闰年满足以下条件：能被4整除但不能被100整除，或者能被400整除。

# year = int(input("input a user:"))
# print(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
