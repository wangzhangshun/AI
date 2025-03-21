# # 字典存储原理
# info_dict = {"name": "yuan", "age": 18, "height": 185, "weight": 70}

# print(hash("apple"))
# print(bin(4))  # 十进制转换二进制
# print(bin(5))  # 十进制转换二进制
# print(bin(6))  # 十进制转换二进制
# print(bin(hash("apple")))
# print(bin(hash("name")))
# print(bin(hash("age")))
# print(bin(hash("height")))

# 键的要求: 必须是可变数据类型对象且唯一
# {[]:"123"}
# {{}:"123"}

# {(1,2,3):100}
# {True:100}
#
# {"":"yuan"}
# {1001:"yuan"}

# 补充： 3.7+ 版本 默认有序字典
info_dict = {"name": "yuan", "age": 18, "height": 185, "weight": 70}
print(info_dict)














