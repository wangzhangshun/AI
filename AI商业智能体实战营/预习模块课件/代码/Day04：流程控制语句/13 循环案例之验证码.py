"""
s1 = "hello"
s2 = "yuan"
print(s1 + s2)

s = ""
a = "aaa"
s += a  # s = s+a
print(s)
b = "bbb"
s += b  # s = s+"bbb"
print(s)
c = "ccc"
s += c
print(s)

# s = "aaabbbccc"

"""

import random
import string


# print(string.digits+string.ascii_lowercase+string.ascii_uppercase)
# print(string.digits+string.ascii_letters)

count = 0

s = ""
while count < 100:
    # 逻辑代码块开始
    char = random.choice(string.digits+string.ascii_letters)
    # print(char)
    s += char
    # 逻辑代码块结束
    count += 1

print("s:::",s)