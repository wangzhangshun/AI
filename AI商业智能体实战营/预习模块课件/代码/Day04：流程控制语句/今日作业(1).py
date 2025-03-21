# （1）编写一个程序，判断一个字符是否为元音字母（a、e、i、o、u，包括小写和大写）。如果是元音字母，则输出"是元音字母"，否则输出"不是元音字母"。

# 方案1
# char = input("请输入一个字符:")
# if char in "aeiouAEIOU":
#     print("是元音字母")
# else:
#     print("不是元音字母")

# 方案2

# char = input("请输入一个字符")
# if char not in "aeiou":
#     print("不是元音字母")
# else:
#     print("是元音字母")

# 方案3
# char = input("请输入一个字符:")
# char = char.lower()
# if char in "aeiou":
#     print("是元音字母")
# else:
#     print("不是元音字母")


# （2）统计元音字母：编写一个程序，接受用户输入的一段文本，统计其中元音字母（a、e、i、o、u）的个数，并输出结果。
# data = input("请输入一段文本:")
# count = 0
# for char in data:
#     if char.lower() in "aeiou":
#         count += 1
# print("元音字母出现次数：", count)


# （3） 计算1-2+3-4+......-1000最终的结果,能整除13的数不参与计算
# ret = 0
# for i in range(1, 1001):
#
#     if i % 13 == 0:
#         continue
#
#     if i % 2 == 0:
#         # ret += -i
#         ret -= i
#     else:
#         ret += i
# print(ret)

# （4）身份证号码的倒数第二位数字是奇数，表示性别为男性，否则为女性，引导用户输入身份证号，先判断是否为18位，再判断性别。


# uid = input("请输入您的身份证号：")
#
# if len(uid) == 18:
#     gender_val = int(uid[-2])
#     if gender_val % 2 == 0:
#         print("女性")
#     else:
#         print("男性")
# else:
#     print("输入格式不对，确保18位")

