# (4) strip方法

# 案例1:
# name = input("姓名：")
# print(name)
# ret = name.strip() # 去除两端的空格或者换行符
# print(ret)
# print(len(ret))

# 案例2:
# print("\nyuan\n")
# print("\nyuan\n".strip())

# 案例3:

# s = "##abcd#####"
# print(s.strip("#"))
# print(s.rstrip("#"))
# print(s.lstrip("#"))


# (5) isdigit：判断字符串是否为数字字符串

# print("apple".isdigit())
# print("123".isdigit())
# print("123元".isdigit())
# print("123.45".isdigit())

# age_str = input("age:::")
#
# if age_str.isdigit():
#     age = int(age_str)
#     print(age)
# else:
#     print("非法输入！")

# (6) split()和join()
# 案例1
# cities = "北京 哈尔冰 重庆 大连"
# ret = cities.split(" ")  # ['北京', '哈尔冰', '重庆', '大连']
# print(ret)
# print(len(ret))

# ret = ['北京', '哈尔冰', '重庆', '大连']
# # ret.join(",")
# print(",".join(ret))

# 案例2
# info = "yuan|19|185"
# ret = info.split("|")  # ['yuan', '19', '185']
# print(ret)
# print(ret[0])
# print(ret[1])
# print(ret[2])

# (7) replace(): 子字符串替换
# 案例1
# cities = "北京 哈尔冰 重庆 大连"
# ret = cities.replace(" ",",")
# print(cities)
# print(ret)

# 案例2
# sentence = "PHP is the best language.PHP...PHP...PHP..."
# ret = sentence.replace("PHP","JAVA")
# print(ret)

# 案例3
# comments = "这个产品真棒！我非常喜欢。服务很差，不推荐购买。这个餐厅的食物质量太差了，味道不好。我对这次旅行的体验非常满意。这个电影真糟糕，剧情一团糟。这个景点真糟糕，再也不来了！"

# ret = comments.replace("差", "***")
# print(ret)
#
# ret2 = ret.replace("糟", "***")
# print(ret2)
#
# ret3 = ret.replace("不推荐", "***")
# print(ret3)

# ret = comments.replace("差", "***").replace("糟", "***").replace("不推荐", "***")
# print(ret)


# (8) count:计算字符串中某个子字符串出现的次数

# sentence = "PHP is the best language.PHP...PHP...PHP..."
# print(sentence.count("PHP"))  # 4
