# 方式1: 操作符 交集(&) 差集(-) 并集(|)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)  # {3, 4}
print(s2 & s1)  # {3, 4}
print(s1 - s2)  # {1, 2}
print(s2 - s1)  # {5, 6}
print(s1 | s2)  # {1, 2, 3, 4, 5, 6}
print(s2 | s1)  # {1, 2, 3, 4, 5, 6}
print(s1, s2)

# 方式2：集合的内置方法

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
# 交集
print(s1.intersection(s2))  # {3, 4}
print(s2.intersection(s1))  # {3, 4}

# 差集
print(s1.difference(s2))  # {1, 2}
print(s2.difference(s1))  # {5, 6}
print(s1.symmetric_difference(s2))  # {1, 2, 5, 6}
print(s2.symmetric_difference(s1))  # {1, 2, 5, 6}

# 并集
print(s1.union(s2))  # {1, 2, 3, 4, 5, 6}
print(s2.union(s1))  # {1, 2, 3, 4, 5, 6}
