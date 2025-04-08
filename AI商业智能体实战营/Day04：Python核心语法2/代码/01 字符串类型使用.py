# 字符串类型

#  有序存储
# s = "hello yuan"

# (1) 索引操作：获取字符： s[索引]
# print(s[1])
# print(s[4])
# print(s[9])
# print(s[-1])
# print(s[-2])

# (2) 切片操作 s[开始索引:结束索引]
# print(s[0:5])
# print(s[6:9])
# print(s[6:-1])
# print(s[6:])


# (3) f-str
name = "rain"
age = 28
s = f"敬爱的党组织：... 我是{name}，我今年{age}岁，我对党绝对忠诚..."
print(s)

# (4) 字符串内置方法  s.方法()
# i = 100
# s = "yuan"
# s2 = "alex"

# print(s.upper())
# print(s2.upper())
# print(i.upper())

s = "Hello Yuan"
print(s.upper())
print(s.lower())
name = "苑老师"
print(name.startswith("张")) # False
print(name.endswith("师")) # True
print(name.endswith("老师")) # True

s = "北京 天津 上海 深圳"
print(s.split(" ")) # ['北京', '天津', '上海', '深圳']

