# 案例1： 不可变数据类型的存储方式
x = 1
print(x)
x = 2
print(x)
# 案例2
s = "yuan"
print(id(s))
s = "Yuan"
print(s)
print(id(s))

# 案例3：可变数据类型的存储方式
l = [1, 2, 3]
print(l)
print(id(l))
l[2] = 300
print(l)
print(id(l))
l = [4, 5, 6]
print(l)
print(id(l))
