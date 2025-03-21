# 四、逻辑运算符

# 案例1
# # 语文成绩大于100分同时(并且)数学成绩大于100分
# chinese = 140
# math = 125
# # 与运算：and
# # 真与真 结果为真
# # 真与假 结果为假
# # 假与真 结果为假
# # 假与假 结果为假
# ret = chinese > 100 and math > 100
# print(ret)
#
# if chinese > 100 and math > 100:
#     print("买礼物")
# else:
#     print("小小惩罚！")


# 案例2
# 语文成绩大于100分或数学成绩大于100分
# chinese = 40
# math = 25
# # 或运算：or
# # 假或假为假
# # 真或假为真
# # 假或真为真
# # 真或真为真
#
# ret = chinese > 100 or math > 100
# print(ret)
#
# if ret:
#     print("买礼物")
# else:
#     print("小小惩罚！")


# print(not 3 > 2)
# print(not 3 == 2)


# 案例3：
# 用户输入一个年龄，判断是否符合20-35
# age = int(input("年龄："))

# if age > 20 and age < 35:
#     print("符合要求")
# else:
#     print("不符合要求")

# if 20 < age < 35:
#     print("符合要求")
# else:
#     print("不符合要求")


# 成员运算符： in 返回布尔值
# print("rain" in "yuan rain alvin eric")
# print("rai" in "yuan rain alvin eric")
# print("rains" in "yuan rain alvin eric")
# print("rain al" in "yuan rain alvin eric")
# print("yuan" in ["123", "yuan", "真假"])


