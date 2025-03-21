# gf_name_list = ['高圆圆', '刘亦菲', '赵丽颖', '范冰冰', '李嘉欣']

# 一、增：append  insert  extend
# (1) append:向列表最后的位置添加元素
# gf_name_list.append("橘梨纱")
# print(gf_name_list)  # gf_name_list发生变化

# 错误写法
# l = gf_name_list.append("橘梨纱")
# print(l) # None

# (2) insert：插入
# l = gf_name_list.insert(1, "橘梨纱")
# print(l)  # None
# print(gf_name_list)

# (3) extend方法：扩展
gf_name_list = ['高圆圆', '刘亦菲', '赵丽颖', '范冰冰', '李嘉欣']
# gf_name_list.append(["橘梨纱", "波多野结衣"])
# print(len(gf_name_list))

# new_gf_list = ["橘梨纱", "波多野结衣"]
# print(gf_name_list.extend(new_gf_list))
# print(gf_name_list, len(gf_name_list))
# print(gf_name_list + new_gf_list)
