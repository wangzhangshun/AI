# (1) % 占位符
# name = "yuan"
# age = 18
# height = 185.123
#
# s = "姓名：%s，年龄：%s，身高：%scm" % (name, age, height)
# print(s)

# (2) format-string  {表达式}

name = "yuan"
age = 18
height = 185.123456

s = f"姓名：{name:*^15}，年龄：{age}，身高：{height:12.6} cm 其他：{type(1 + 1 > 2)}"
print(s)

name = "abcdefg"
age = 45
height = 185.123456

s = f"姓名：{name:*^15}，年龄：{age}，身高：{height:<.6} cm 其他：{type(1 + 1 > 2)}"
print(s)
