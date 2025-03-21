# (1) % 占位符

# name = "yuan"
# age = 18
# height = 185
#
# s = """
#      员工信息：
#      姓名：%s
#      年龄：%s
#      身高: %s
# """ % (name, age, height)
# print(s)


# (2) f-str

# name = "yuan"
# age = 18
# height = 185.123456
#
# s = f"姓名：{name:?^15}，年龄：{age:<20}，身高：{height:<20.5} "
# print(s)
#
# name = "abcdefg"
# age = 45
# height = 155.123456
#
# s = f"姓名：{name:-^15}，年龄：{age:<20}，身高：{height:<20.5} "
# print(s)


# 拓展 f-str  {表达式}

name = "yuan"
age = 18
height = 185

s = f"""
     员工信息：
     姓名：{name}
     年龄：{age}
     虚岁：{age + 1}
     身高: {height}
     其他：{type(1 + 1 > 2)}
"""
print(s)
