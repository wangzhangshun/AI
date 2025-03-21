# peiQi_hobby = {"螺狮粉", "臭豆腐", "榴莲", "apple"}
#
# alex_hobby = {"螺狮粉", "臭豆腐", "榴莲", "💩","pizza"}
#
# yuan_hobby = {"pizza", "salad", "ice cream", "臭豆腐", "榴莲"}
#
# hobbies = [peiQi_hobby, yuan_hobby, alex_hobby]

#  给peiQi推荐商品
# 版本1:
# hobbies.remove(peiQi_hobby)
#
# peiQi_recommend_list = []
#
# for hobby in hobbies:
#     if len(peiQi_hobby.intersection(hobby)) >= 2:
#         # print(list(hobby - peiQi_hobby))
#         peiQi_recommend_list.extend(list(hobby - peiQi_hobby))
#
# print(list(set(peiQi_recommend_list)))


# 版本2:

# hobbies.remove(peiQi_hobby)
# peiQi_recommend_set = set()
# # print(type(peiQi_recommend_set))
# for hobby in hobbies:
#     if len(peiQi_hobby.intersection(hobby)) >= 2:
#         peiQi_recommend_set.update(hobby - peiQi_hobby)
#
#
# print(list(peiQi_recommend_set))






