# 函数：组织代码
# 功能：解耦和去重
"""
def poke():
   功能代码块


"""


# 声明函数
def print_poke():
    poke_types = ['♥️', '♦️', '♠️', '♣️']
    poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    for p_type in poke_types:
        for p_num in poke_nums:
            print(f"{p_type}{p_num}", sep="\t", end="")

        print()
        print()

# 调用函数
print_poke()
print("123")
print_poke()
print("456")
print_poke()



