# gf_name_list = ['高圆圆', '刘亦菲', '赵丽颖', '范冰冰', '李嘉欣']

# 一、索引操作：
# (1) 查看元素: 列表对象[索引] ,获取元素,重点是获取的只有一个元素值
# print(gf_name_list[2])
# print(gf_name_list[4])
# print(gf_name_list[-1])

# (2) 修改元素：列表对象[索引] = 值
# gf_name_list[3] = "佟丽娅"
# print(gf_name_list)

# 二、切片操作
# (1) 查看多个元素：列表对象[开始索引:结束索引:步长=1], 获取多个值的子列表
# print("hello"[1:4])  # 子字符串
# print(gf_name_list[1:4])  # 子列表 ['刘亦菲', '赵丽颖', '范冰冰']
# print(gf_name_list[0:3])
# print(gf_name_list[:3])  # 缺省0
# print(gf_name_list[2:5])
# print(gf_name_list[2:])  # 缺省最后一个值
# print(gf_name_list[:])  # 缺省最后一个值
# print(gf_name_list[-3:])  # 缺省最后一个值

# 步长=1
# 步长是正数：从小向大切(从左向右)
# 步长是负数：从大向小切(从右向左)
# print(gf_name_list[1:4])
# print(gf_name_list[4:1])  # []
# print(gf_name_list[3:0:-1])  # []
# print(gf_name_list[3:0:-1])  # []

# print(gf_name_list[-4:-2])
# print(gf_name_list[-2:-4:-1])
# print(gf_name_list[::1])
# print(gf_name_list[::2])
# print(gf_name_list[::3])
# print(gf_name_list[::-1])
# print(gf_name_list[::-2])

# (2) 修改多个元素：
# gf_name_list = ['高圆圆', '刘亦菲', '赵丽颖', '范冰冰', '李嘉欣']
# gf_name_list[1:4] = 100, 200, 300
# gf_name_list[1:4] = [100, 200, 300]
# gf_name_list[1:4] = ["霹雳狐", "小允", "小苏菲"]
# print(gf_name_list)


# 扩展面试题：将字符串的倒数第二个字符改为大写
s = "hello yuan"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# s[-2] = "A"
ret = list(s)
print(ret)  # ['h', 'e', 'l', 'l', 'o', ' ', 'y', 'u', 'a', 'n']
ret[-2] = "A"
print(ret)
ret2 = "".join(ret)
print(ret2)
