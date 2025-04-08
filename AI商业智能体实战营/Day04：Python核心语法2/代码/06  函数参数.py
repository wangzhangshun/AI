# 函数：组织代码
# 功能：解耦和去重
"""
def poke():
   功能代码块

"""


def cal(m, n):
    ret = 0

    for i in range(m, n + 1):
        # print(i)
        ret += i  # ret = ret +i

    return ret


cal(666, 888)
# ret = cal(666, 888)
# print(ret)
