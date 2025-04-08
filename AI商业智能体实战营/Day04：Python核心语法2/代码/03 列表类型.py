# 编程本质就是对数据做各种操作
# 基本数据基本操作
# 高级数据（容器数据）增删改查操作
# s = "北京 天津 哈尔滨 乌鲁木齐"
# 这里面有几个城市
# print(len(s))
# 列表语法：[元素1,元素2,元素3,...]
# 元素个数理论上没有限制
# 元素值可以是任意类型，包括数字、字符串、列表、字典
# 元素是从左到右有序存储
# l = ["北京","天津","哈尔滨","乌鲁木齐"]
# print(len(l))


# 一、查（基本语法实现）
# (1) 索引操作：获取元素值： l[索引]
# print(l[1])
# print(l[-1])
# (2) 切片操作 l[开始索引:结束索引]  顾头不顾尾
# print(l[0:3])
# print(l[-3:])

# 二、改（基本语法实现）
# l = ["北京","天津","哈尔滨","乌鲁木齐"]
# print(l[2])
# l[2] = "沈阳"
# print(l)
# 增：内置方法  列表对象.方法()  ：append insert extend
# gf_list = ["范冰冰","刘亦菲","波多野结衣"]
# print(len(gf_list))
# gf_list.append("赵丽颖")
# print(gf_list)
# gf_list.insert(0,"章若楠")
# print(gf_list)

# 删：内置方法：remove pop clear

# gf_list = ["章若楠","范冰冰","刘亦菲","波多野结衣"]
# gf_list.remove("范冰冰") # 按元素值删除
# print(gf_list)
# gf_list.pop(-1)
# print(gf_list)
# gf_list.clear()
# print(gf_list)

# 列表与for循环


# gf_list = ["章若楠", "范冰冰", "刘亦菲", "波多野结衣"]

# for循环：遍历循环
# for gf in gf_list:
#     data = f"我的宝贝：{gf},我太爱你了"
#     print(data)

# l = [23, 14, 2, 11, 5]
#
# l2 = []
# for i in l:
#     print(i*i)
#     l2.append(i*i)
# print(l2)


# range()函数

# for i in [1,1,1,1,1]:
#     print("hello yuan")
# for i in range(1, 100):
#     print(i)
# for i in range(100):
#     print(i)
