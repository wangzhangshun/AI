# Python  八种基本的数据类型

# 集合  set  无序且不重复

# set1 = {1, 2, 3, 4, 5}
#
# # 输出
# print(set1)


five_men_fight_bg = {"ian", "Alex", "佩奇", "Old_Shang", "智哥", "black_girl"}

happy_day = {"唐艺昕", "李孝利", "black_girl", "刘诗诗", "李沁", "柳岩", "ian"}

# print(five_men_fight_bg[1])

# # 要找出，同时参演了，这两部电影的人，都有谁。（交集）
# print(five_men_fight_bg.intersection(happy_day))
#
# print(five_men_fight_bg & happy_day)
#
# # 这两部电影中，一共包含了有，哪些演员。(并集)
# print(five_men_fight_bg.union(happy_day))
#
# print(five_men_fight_bg | happy_day)
#
# # 参演了抗战片，五男大战黑姑娘的演员中，谁没有参演，开心的一天。(差集)
# print(five_men_fight_bg.difference(happy_day))
#
# print(five_men_fight_bg - happy_day)
#
# # 哪些演员，只参演了一部电影。(交叉补集)
# print(five_men_fight_bg.symmetric_difference(happy_day))
#
# print(five_men_fight_bg ^ happy_day)

# # set    个性
# set2 = {1, 2, 3, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7}
# # print(set2)
#
# # 八种基本数据类型2  列表  list   三好学生
# alex = [1, 2, 3, 4, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8]
# print(list(set(alex)))


# 流程控制结构
# 1. 顺序结构 --- 基本结构
# 2. 选择结构   分支结构  条件语句
# 3. 循环结构
# 3.1 循环嵌套


kaiGuan = True
# 第一层循环控制  楼层号
for floor in range(1, 6):
    print(f"欢迎来到第{floor}层")
    if floor == 3:
        print("Alex与狗禁止入内！")
        continue
    # 第二层循环控制  每层楼的房间号
    for room in range(1, 9):
        print(f"{floor} 0 {room}")
        if floor == 4 and room == 4:
            print("Alex:我的草原我的马呀，你咋****文明用语*****")
            kaiGuan = False
            break
    if kaiGuan == False:  # ！=
        print("ian：发筷子，开席吧~")
        break

    # 循环控制保留字：只能控制离它最近的【一层】循环
    # continue:(执行到我)跳过本次循环，直接开始下一次循环
    # break:(执行到我)直接跳出循环
