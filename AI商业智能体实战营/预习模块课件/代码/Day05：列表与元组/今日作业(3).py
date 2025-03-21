# (11) 给定一个嵌套列表，表示学生的成绩数据，数据结构如下
# scores = [[80, 90, 78], [80, 82, 88], [80, 92, 86], [80, 72, 80], [80, 88, 90]]
# 计算每个学生的平均分。

# stu_average_list = []
# for stu_score_list in scores:
#     # 方式1
#     # val = (stu_score[0]+stu_score[1]+stu_score[2])/3
#     # 方式2
#     stu_total = 0
#     for stu_subject_score in stu_score_list:
#         # print(stu_subject_score)
#         stu_total += stu_subject_score
#
#     stu_average = round(stu_total / len(stu_score_list), 2)
#     print("stu_average:", stu_average)
#     stu_average_list.append(stu_average)

# 计算每科的平均分
# 计算第一个学科的平均成绩

# 方式1
# subject_total = 0
# for stu_score_list in scores:
#     subject_total += stu_score_list[0]
#
# subject_average = round(subject_total / len(scores), 2)
# print("subject_average",subject_average)
#
# # 计算第二个学科的平均成绩
#
# subject_total = 0
# for stu_score_list in scores:
#     subject_total += stu_score_list[1]
#
# subject_average = round(subject_total / len(scores), 2)
# print("subject_average",subject_average)
#
# # 计算第三个学科的平均成绩
#
# subject_total = 0
# for stu_score_list in scores:
#     subject_total += stu_score_list[2]
#
# subject_average = round(subject_total / len(scores), 2)
# print("subject_average",subject_average)

# 方式2:
# 计算第二个学科的平均成绩
# subject_average_list = []
# subject_num = 3
# for i in range(subject_num):
#     subject_total = 0
#     for stu_score_list in scores:
#         subject_total += stu_score_list[i]
#
#     subject_average = round(subject_total / len(scores), 2)
#     print("subject_average", subject_average)
#     subject_average_list.append(subject_average)
#
# print(subject_average_list)


# (12) 引导用户输入页数（每页获取3条数据），实现对作品列表的切片获取,并进行格式化打印
# 假设您有一个作品列表
works = ["作品1", "作品2", "作品3", "作品4", "作品5", "作品6", "作品7", "作品8", "作品9", "作品10", "作品11", "作品12",
         "作品13"]

per_page_num = 3
while 1:
    page_num = int(input("请输入查询的页数："))

    # 分页
    total_page, b = divmod(len(works), per_page_num)
    if b != 0:
        total_page += 1

    if page_num > total_page:
        print("已经超过最大页数")
        continue

    # print(works[0:3])
    start_index = (page_num - 1) * per_page_num
    end_index = start_index + per_page_num

    work_list = works[start_index:end_index]

    for work in work_list:
        print(work)
