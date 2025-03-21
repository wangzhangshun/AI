# (1) 无限循环嵌套
# import random
#
# coin = 100
# exp = 100
# blood = 100
# chest = []
#
# while True:
#     room = input("请输入房间名:")
#     if room == "怪物房":
#         print("遇到了史莱姆")
#         choice = input("【1.攻击/2.逃跑】")
#         if choice == "1":
#             # 选择攻击
#             print("选择干史莱姆！")
#             is_success = random.choice([100, 200])  # 100:成功  200:失败
#             if is_success == 100:
#                 print("战胜史莱姆！")
#                 coin += 20
#                 exp += 20
#             else:
#                 print("没打过史莱姆！")
#                 coin -= 20
#                 exp -= 20
#                 blood -= 20
#         elif choice == "2":
#             # 逃跑的逻辑
#             print("逃跑ing")
#             coin -= 20
#         else:
#             print("无效输入！")
#
#         print("离开怪物房")
#     elif room == "宝箱房":
#         print("你打开了宝箱，获得了钥匙")
#         chest.append("钥匙")
#         print("当前宝贝:", chest)
#     elif room == "陷阱房":
#         print("你触发了陷阱，受到了毒箭的伤害")
#         blood -= 10
#     elif room == "商店":
#         print(f"玩家的金币:{coin},血值:{blood}")
#         print("一个金币买一个药水对应10个血值")
#         is_buy = input("是否购买药水【Y/N】")
#         if is_buy == "Y":
#             num = int(input("购买几瓶药水?"))
#             coin -= 1 * num
#             blood += 10 * num
#             print(f"当前玩家的金币:{coin},血值:{blood}")
#         elif is_buy == "N":
#             print("退出商店!")
#         else:
#             print("无效输入!")
#     print(f"""
#     玩家信息:
#        金币：{coin}
#        经验值：{exp}
#        血值: {blood}
#     """)
#
# # print("游戏结束")


####################################################################################


import random

coin = 100
exp = 100
blood = 100
chest = []

for i in range(3):
    room = input("请输入房间名:")
    if room == "怪物房":
        print("遇到了史莱姆")
        choice = input("【1.攻击/2.逃跑】")
        if choice == "1":
            # 选择攻击
            print("选择干史莱姆！")
            is_success = random.choice([100, 200])  # 100:成功  200:失败
            if is_success == 100:
                print("战胜史莱姆！")
                coin += 20
                exp += 20
            else:
                print("没打过史莱姆！")
                coin -= 20
                exp -= 20
                blood -= 20
        elif choice == "2":
            # 逃跑的逻辑
            print("逃跑ing")
            coin -= 20
        else:
            print("无效输入！")

        print("离开怪物房")
    elif room == "宝箱房":
        print("你打开了宝箱，获得了钥匙")
        chest.append("钥匙")
        print("当前宝贝:", chest)
    elif room == "陷阱房":
        print("你触发了陷阱，受到了毒箭的伤害")
        blood -= 10
    elif room == "商店":
        print(f"玩家的金币:{coin},血值:{blood}")
        print("一个金币买一个药水对应10个血值")
        is_buy = input("是否购买药水【Y/N】")
        if is_buy == "Y":
            num = int(input("购买几瓶药水?"))
            coin -= 1 * num
            blood += 10 * num
            print(f"当前玩家的金币:{coin},血值:{blood}")
        elif is_buy == "N":
            print("退出商店!")
        else:
            print("无效输入!")
    print(f"""
       玩家信息:
          金币：{coin}
          经验值：{exp}
          血值: {blood}
       """)

print("游戏结束")
