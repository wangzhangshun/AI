# s = "hello yuan"

# (1) 索引的语法 字符串对象[索引],获取的一个字符
# print(s[6], type(s[6]))  # "y"
# print(s[0])
# print(s[-1])

# (2) 切片的语法：字符串对象[开始索引:结束索引]
# print(s[0:5])  # 左闭右开
# print(s[6:9])
# print(s[6:10])
# print(s[6:11])
# print(s[6:])  # 缺省
# print(s[:5])
# print(s[:])
# print(s[6:9])
# print(s[6:9])
# print(s[-4:-1])
# print(s[6:-1])

# 切片的语法扩展：字符串对象[开始索引:结束索引:步长=1]
# s = "hello yuan"
# print(s[::1])  # step=1: 从左向右一个个取
# print(s[::2])
# print(s[::3])
# print(s[::-1])  # step=-1: 从右向左一个个取
# print(s[::-2])  # step=-1: 从右向左一个个取

# print(s[0:3])
# print(s[3:0])
# print(s[3:0:-1])
# print(s[-2:-4:-1])
