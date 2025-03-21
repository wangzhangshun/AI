import random

"""
#  场景：
# （1）怪物房： 遇到了史莱姆，并打败了它，金币加5，经验加10！
#  (2) 宝箱房: 你打开了宝箱，获得了钥匙
#  (3) 陷阱房: 你触发了陷阱，受到了毒箭的伤害,血值减10
#  (4) 商店:   你来到了商店，购买了药水,金币减5，血值加20
"""
# room = random.choice(["怪物房", "宝箱房", "陷阱房", "商店"])
# print("房间:", room)

coin = 100
exp = 100
blood = 100
chest = []


room = input("请输入房间名:")

if room == "怪物房":
    print("遇到了史莱姆，并打败了它")
    coin += 5
    exp += 10
elif room == "宝箱房":
    print("你打开了宝箱，获得了钥匙")
    chest.append("钥匙")
    print("当前宝贝:", chest)
elif room == "陷阱房":
    print("你触发了陷阱，受到了毒箭的伤害")
    blood -= 10
elif room == "商店":
    print("你来到了商店，购买了药水")
    coin -= 5
    blood += 20

print(f"""
玩家信息:
   金币：{coin}
   经验值：{exp}
   血值: {blood}
""")

print("游戏结束")
