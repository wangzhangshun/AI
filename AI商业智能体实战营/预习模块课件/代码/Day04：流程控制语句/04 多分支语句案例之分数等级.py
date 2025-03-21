# 案例1:
"""

多分支语句语法

if 表达式1:
    语句块1
elif 表达式2:
    语句块1
elif 表达式3:
    语句块3
elif 表达式4:
    语句块4
elif 表达式5:
    语句块5
else:
    语句块6

# 案例1:根据用户输入的成绩判断其等级。
# 如果成绩[90，100]，则输出"优秀"
# 如果成绩[80，90]，则输出"良好"
# 如果成绩[60，80]，则输出"及格"
# 如果成绩小于60，则输出"不及格"
# 如果成绩小于0或大于100，则输出"成绩有误"

"""
# 版本1
# score = float(input("请输入成绩:"))
#
# if 90 <= score <= 100:
#     print("成绩优秀！")
# elif 80 <= score < 90:
#     print("成绩良好！")
# elif 60 <= score < 80:
#     print("成绩及格！")
# elif 0 <= score < 60:
#     print("成绩不及格！")
# else:
#     print("非法输入!")


# 版本2:
score = float(input("请输入成绩:"))

if score > 100 or score < 0:
    print("非法输入！")
elif score >= 90:
    print("成绩优秀!")
elif score > 80:
    print("成绩良好!")
elif score >= 60:
    print("成绩及格!")
elif score > 0:
    print("成绩不及格!")
