import requests
# def main(month: str) -> dict:
#     res=requests.get(f'http://192.168.71.100:5000/get_01?month={month}').json()
#     return {
#         "names": res['names'],
#         'names_amount':res['names_amount']
#     }



def main(month: str) -> dict:
    res=requests.get(f'http://192.168.71.100:5000/get_02?month={month}').json()
    return {
        "dates": res['dates'],
        'total_amounts':res['total_amounts']
    }

if __name__ == '__main__':
    # 条件1 代码测试  每个销售人员，XX年Y月份销售记录占比
    # print(main('2025-04'))  # {'names': 'lqz;刘清政;justin;张三;李四;王五;赵六', 'names_amount': '35991.00;53994.00;6293.00;15992.00;39992.00;5196.00;53991.00'}

    # 条件2 代码测试  最近X个月总销售数据 ---写数字
    print(main(4))