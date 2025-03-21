import re

# 开发程序对 stock_data.txt 进行以下操作：
f = open("stock_data.txt")
headers = f.readline().strip().split(",")

stock_dic = {}
for line in f:
    line = line.strip()
    line = line.split(",")
    stock_dic[line[0]] = line
f.close()

# 程序启动后，给用户提供查询接口，允许用户重复查股票行情信息。
while True:
    # 输入
    cmd = input("请输入查询指令：")
    for s_id, s_data in stock_dic.items():
        s_name = s_data[1]

        # 允许用户通过模糊查询股票名，
        # 比如输入“啤酒”, 就把所有名称当中包含啤酒的股票都打印出来。
        if cmd in s_name:
            print(s_data)

    # 允许按 当前价、涨跌幅、换手率 这几列来筛选信息，
    # 比如输入“当前价>50”则把价格大于50的股票都打印，
    # 输入“涨跌幅<50“，则把涨跌幅小于50的股票都打印，不用判断等于。

    # 公式查询（健壮性）
    # 1. 判断公式的合法性(正则表达式)
    cmd_parser = re.split("[><]", cmd)
    print(cmd_parser)
    if len(cmd_parser) != 2:
        print("输入的公式不合法，请重新输入！")
        continue

    # 2. 判断列名的合法性
    filter_column, filter_val = cmd_parser
    if filter_column not in ['当前价', '涨跌幅', '换手率']:
        print("输入的列名不合法，请重新输入！")
        continue

    # 3. 判断数值的合法性
    try:  # 尝试
        filter_val = float(filter_val)
    except:
        print("输入的数值不合法，请重新输入！")
        continue

    # 4. 放心的去处理逻辑
    # 4.1 拿索引 ----   headers
    column_index = headers.index(filter_column)

    for s_id, s_data in stock_dic.items():
        if ">" in cmd:  # 大于
            if float(s_data[column_index].strip("%")) > filter_val:
                print(s_data)
        else:  # 小于
            if float(s_data[column_index].strip("%")) < filter_val:
                print(s_data)