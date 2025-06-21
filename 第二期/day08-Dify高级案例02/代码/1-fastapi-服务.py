from fastapi import FastAPI
import aiomysql
import datetime


def get_previous_month(months: int) -> str:
    # 验证输入
    if not isinstance(months, int) or months < 0:
        raise ValueError("月份数必须是一个非负整数")
    # 获取当前日期
    current_date = datetime.datetime.now()
    current_year = current_date.year
    current_month = current_date.month
    # 计算前推指定月数后的年月
    # 先计算总月数
    total_months = current_year * 12 + current_month - months
    # 计算年份和月份
    target_year = total_months // 12
    target_month = total_months % 12
    # 处理月份为0的情况（表示12月）
    if target_month == 0:
        target_month = 12
        target_year -= 1
    # 格式化并返回年月信息
    return f"{target_year:04d}-{target_month:02d}"




app = FastAPI()

# 接口一：根据月份，获取没有每个人的销售额--》用户生成饼形图
# 后期改，只改 192.168.23.131  是你虚拟机地址，其他不改
@app.get('/get_01')  # 获取每个销售，月度销售额
async def get_01(month: str = '2025-02'):
    names = ''
    names_amount = ''
    async with aiomysql.connect(host='192.168.23.131', port=3307, user='lqz', password='lqz12345', db='lqz01') as conn:
        cur = await conn.cursor()
        await cur.execute("SELECT customer_name,total_amount FROM sales_orders where order_date=%s", month)
        result = await cur.fetchall()
        for item in result:
            names += item[0] + ';'
            names_amount += str(item[1]) + ';'
        return {'names': names[:-1], 'names_amount': names_amount[:-1]}

# 接口二：获取最近3个月的总销售额，用于生成折线图
@app.get('/get_02')  # 获取最近X个月总销售数据
async def get_02(month: int = 3):
    dates = ''
    total_amounts = ''
    # 格式化并返回年月信息
    real_month = get_previous_month(month)
    async with aiomysql.connect(host='192.168.23.131', port=3307, user='lqz', password='lqz12345', db='lqz01') as conn:
        cur = await conn.cursor()
        await cur.execute(
            "SELECT order_date,SUM(total_amount) as total FROM sales_orders GROUP BY  order_date HAVING order_date>=%s",
            real_month)
        result = await cur.fetchall()
        for item in result:
            dates += item[0] + ';'
            total_amounts += str(item[1]) + ';'
        return {'dates': dates[:-1], 'total_amounts': total_amounts[:-1]}

# 接口三：获取某月，销售额最高的前三个人--》柱状图
@app.get('/get_03')  # 获取  X 月份销售最高排名
async def get_03(month: str = '2025-02'):
    names = ''
    names_amount = ''
    async with aiomysql.connect(host='192.168.23.131', port=3307, user='lqz', password='lqz12345', db='lqz01') as conn:
        cur = await conn.cursor()
        await cur.execute(
            "SELECT customer_name,total_amount  FROM sales_orders where order_date=%s order by total_amount DESC LIMIT 5",
            month)
        result = await cur.fetchall()
        for item in result:
            names += item[0] + ';'
            names_amount += str(item[1]) + ';'
        return {'names': names[:-1], 'names_amount': names_amount[:-1]}



# 接口四：根据人名和月份，查询这个人这个月销售额是多少，不生成图表，只拿到文字
@app.get('/get_04')  # 获取 YY 的  X 月份销售数据
async def get_04(month: str = '2025-01', name: str = 'justin'):
    async with aiomysql.connect(host='192.168.23.131', port=3307, user='lqz', password='lqz12345', db='lqz01') as conn:
        cur = await conn.cursor()
        await cur.execute(
            "SELECT customer_name,total_amount FROM sales_orders where customer_name = %s and order_date=%s;",
            (name, month))
        result = await cur.fetchall()
        return f'{name}的第{month}个月，总销售额为：{result[0][1]}'


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('1-fastapi-服务:app', host='0.0.0.0', port=5000, reload=True)


'''
1 在浏览器中访问：(你们需要改成你们的ip地址)
    http://192.168.71.100:5000/get_01
    http://192.168.71.100:5000/get_02
    http://192.168.71.100:5000/get_03
    http://192.168.71.100:5000/get_04
2 使用postman访问
    http://192.168.71.100:5000/get_03
3 使用python代码访问
    看具体代码
    

'''

