from decimal import Decimal

x = 1
y = 2
print(1 + 2)

a = 3.14
b = 1.11
print(a + b)
print(a - b)
# ret = round(a - b)  # 四舍五入精度限制
# print(ret)
# print(round(a - b, 2))

c = Decimal("3.14")
d = Decimal("1.11")
print(c - d)

# type(): 打印数据对象的类型名
# x,y,a,b分别是类型数据
print(type(x))  # "<class 'int'>"
print(type(y))  # "<class 'int'>"
print(type(a))  # "<class 'float'>"
print(type(b))  # "<class 'float'>"
