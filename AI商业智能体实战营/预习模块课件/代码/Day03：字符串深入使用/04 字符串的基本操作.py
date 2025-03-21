# (1) 字符串不能修改

# s1 = "yuan"
# s1 = "rain"
# print(s1)
# # s1[0] = "R"
# s1 = "Rain"

# (2) 内置函数：len
# s = "hello yuan"
# print(len(s))
# print(s[-1])
# print(s[len(s) - 1])
# print(len([1, 2, 3]))
# print(len({"k1": "v1"}))

# (3) 拼接 + *
# s1 = "hello"
# s2 = "yuan"
# print(1 + 2)
# print(s1 + " " + s2)

# 案例
# name_str = ""
# name1 = "rain"
# # name_str = name_str + name1  # name_str = "rain"
# name_str += " "+name1
# name2 = "eric"
# # name_str = name_str + name2  # name_str = "raineric"
# name_str += " "+name2
# name3 = "yuan"
# # name_str = name_str + name3  # name_str = "rainericyuan"
# name_str += " "+name3
# print(name_str)

# print("*" * 100)


# (4) in 返回布尔值
# print("rain" in "rain eric yuan")
# print("rai" in "rain eric yuan")
# print("rains" in "rain eric yuan")
# print("rains" not in "rain eric yuan")

# if "rain" in "rain eric yuan": # "rain eric yuan" 优秀名单
#     print("奖励他")
# else:
#     print("惩罚他")


# if "rain" not in "rain eric yuan":  # "rain eric yuan" 黑名单
#     print("奖励他")
# else:
#     print("惩罚他")
