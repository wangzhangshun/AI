age = int(input("年龄:"))

if age > 18:
    print("成人电影!")

    choice = input("""
       1. 日韩区
       2. 欧美区
       3. 国产区 
    """)

    if choice == "1":
        print("《熔炉》")
        print("《千与千寻》")
        print("《龙猫》")
        print("《天空之城》")
    elif choice == "2":
        print("《肖申克的救赎》")
        print("《当幸福来敲门》")
        print("《阿甘正传》")
        print("《星际穿越》")
    elif choice == "3":
        print("《霸王别姬》")
        print("《大话西游》")
        print("《让子弹飞》")
        print("《无间道》")
    else:
        print("输入有误！")
    print("观看成人电影结束！")

else:
    print("少儿电影")
    print("科幻冒险类")
    print("益智早教类")
    print("科普记录类")

print("程序结束")



