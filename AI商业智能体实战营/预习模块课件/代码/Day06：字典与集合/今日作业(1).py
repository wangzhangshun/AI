# （1）给定两个字典，找到它们共有的键存放到一个列表中

# dict1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
# dict2 = {'B': 20, 'D': 40, 'E': 50}
#
# key_list = []
#
# for key in dict2:
#     if key in dict1:
#         key_list.append(key)
#
# print(key_list)

# (2) 给定一个字典，找到字典中值最大的键：`my_dict = {'A': 10, 'B': 5, 'C': 15, 'D': 20}`

# my_dict = {'A': 10, 'B': 5, 'C': 15, 'D': 20}
# max_val = 0
# max_val_key = None
# for key, val in my_dict.items():
#     if val > max_val:
#         max_val = val
#         max_val_key = key
#
# print(max_val)
# print(max_val_key)


# （3）字典值的乘积：编写一个程序，计算给定字典中所有值的乘积
# my_dict = {'A': 2, 'B': 3, 'C': 4, 'D': 5}
#
# ret = 1
# for val in my_dict.values():
#     ret *= val
# print(ret)


# （4）编写一个程序，统计给定列表中每个元素出现的次数，并将结果存储在一个字典中。
# my_list = [1, 2, 3, 2, 1, 3, 4, 5, 2, 1]
#
# count_dict = {}
#
# for i in my_list:
#     if i in count_dict:
#         # count_dict[i] +=1
#         count_dict[i] = count_dict[i] + 1
#     else:
#         count_dict[i] = 1
#
# print("count_dict:::",count_dict)


# （5）编写一个程序，将两个字典合并，并将相同键对应的值进行加法运算。

dict1 = {'A': 1, 'B': 2, 'C': 3}
dict2 = {'B': 10, 'D': 20, 'C': 30}
# dict1.update(dict2)
# print(dict1)
merger_dic = dict1.copy()

for key, val in dict2.items():
    if key in merger_dic:
        merger_dic[key] += val
    else:
        merger_dic[key] = val

print("合并的字典：",merger_dic)


