# (8) 猜数字游戏
"""

1.首先，程序使用random.randint函数产生一个1~10之间的随机数。
2.然后，程序通过for循环提示玩家输入一个猜测的数字，玩家可以输入一个1~10之间的整数。
3.如果玩家猜对了数字，程序输出恭喜玩家的信息并结束游戏；如果玩家猜错了，程序会根据玩家输入的数字与随机数之间的大小关系来提示玩家是否猜对，并在每次猜错后告诉玩家还剩下几次机会。
4.如果玩家在三次机会内猜对了数字，程序输出恭喜玩家的信息并结束游戏；否则程序输出很遗憾的信息并结束游戏。

"""
import random

# 案例1:
# secret_num = random.randint(1, 10)
#
# for i in range(3):
#     guess_num = int(input("请输入一个数字，范围【1-10】:"))
#
#     # 判断
#     if guess_num > secret_num:
#         print("猜大了")
#     elif guess_num < secret_num:
#         print("猜小了")
#     else:
#         print("恭喜您，猜对了，数字正是", guess_num)
#         break
# else:
#     print("很遗憾，三次机会已经用完！")

# 案例2:
# secret_num = random.randint(1, 10)
# max_guesses = 3
# for i in range(1, max_guesses + 1):
#     guess_num = int(input("请输入一个数字，范围【1-10】:"))
#
#     # 判断
#     if guess_num > secret_num:
#         print("猜大了")
#     elif guess_num < secret_num:
#         print("猜小了")
#     else:
#         print("恭喜您，猜对了，数字正是", guess_num)
#         break
#
#     # 提示
#     remaining_guesses = max_guesses - i
#     if remaining_guesses >0:
#         print(f"您还剩下{remaining_guesses}次机会，请珍惜!")
#     else:
#         print("很遗憾，三次机会已经用完！")
#         break

# (9)

# print("欢迎来到电影订票系统！")
# print("请选择您要进行的操作：")
# print("1. 查询电影场次")
# print("2. 选座购票")
# print("3. 查看订单信息")
#
# choice = int(input("请输入您的选择（1-3）："))
#
# if choice == 1:
#     print("正在查询电影场次...")
#     # 执行查询电影场次的代码
# elif choice == 2:
#     print("正在选座购票...")
#     # 普通票/学生票/老年票
#     ticket_type = input("""
#         1. 学生票
#         2. 老年票
#         3. 普通票
#     """)
#     if ticket_type == "1":
#         print("正在购买学生票")
#     elif ticket_type == "2":
#         print("正在购买老年票")
#     elif ticket_type == "3":
#         print("正在购买普通票")
#
#
#
# elif choice == 3:
#     print("正在查看订单信息...")
#     # 执行查看订单信息的代码
# else:
#     print("无效的选择！请重新运行程序并输入有效的选项。")


