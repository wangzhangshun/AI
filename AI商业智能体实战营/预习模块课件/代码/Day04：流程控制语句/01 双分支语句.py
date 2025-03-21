"""
双分支语句的语法if-else
冒号+缩紧：标识语句块

if 表达式:
    语句1
    语句2
    语句3
else:
    语句4
    语句5
    语句6

C++,Java,JS语言：
if (表达式){
    语句1
    语句2
    语句3
}else{
    语句4
    语句5
    语句6
}


"""

# 案例1:
age = int(input("年龄:"))

if age > 18:
    print("成人电影!")
    print("日韩区")
    print("欧美区")
    print("国产区")
else:
    print("少儿电影")
    print("科幻冒险类")
    print("益智早教类")
    print("科普记录类")

print("程序结束")



