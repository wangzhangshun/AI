# (1) 字符串索引切片练习

# s = "hello world"

# 操作1：通过正反索引切片world
# print(s[6:])
# print(s[-5:])
# 操作2: 获取world的翻转,即"dlrow"

# print(s[6:][::-1])

# (2) 有些程序经常需要引导用户输入"Y"或"N"，其中"Y"代表肯定，"N"代表否定。无论用户输入大写的"Y"还是小写的"y"，结果都被视为肯定。肯定打印True
# ret = input('[输入"Y"或"N"]')
# print(ret == "Y" or ret == "y")
# print(ret.upper() == "Y")


# (3)
# task_id = 1001
# task_name = "定时检测订单"
# task_date = "2012-12-12"
# task_cost_second = 15
#
# s = f"""<html>
# <head>
#    <meta charset="utf-8">
# </head>
# <body>
# Hello，定时任务出错了：
# <p style="font-size:16px;">任务执行详情：</p>
# <p style="display:block; padding:10px; background:#efefef;border:1px solid #e4e4e4">
#     任务 ID：{task_id}<br/>
#     任务名称：{task_name}<br/>
#     执行时间：{task_date}<br/>
#     执行耗时：{task_cost_second}秒<br/>
#     执行状态：开启
# </p>
# <br/>
# <p>-----------------------------------------------------------------<br/>
#     本邮件由CronJob定时系统自动发出，请勿回复<br/>
#     如果要取消邮件通知，请登录到系统进行设置<br/>
# </p>
# </body>
# </html>"""
#
# print(s)


# (4) 引导用户输入一个双值加法字符串，例如`3+5`或`3 + 5`，计算出两个数字的和，打印出来
# exp = input("双值加法表达式")
# ret = exp.split("+")
# num1 = int(ret[0].strip())
# num2 = int(ret[1].strip())
# print(num1 + num2)


# (5) 用户输入一个11位手机号，将第5位至第8位替换成`*`
# tel = "15100323329"
# print(tel[:4]+"****"+tel[-3:])

# (6) 编写一个Python程序，输入一个三位数。将其拆分为百位数，十位数和个位数，井输出它们的和
# ret = input("请输入一个三位数")
# ge = int(ret[0])
# shi = int(ret[1])
# bai = int(ret[2])
# print(ge + shi + bai)


# (7) 将`Unix/Linux`系统下的路径字符串`"/Users/yuan/npm/index.js"`转换为`Windows`系统下的路径字符串`"\Users\yuan\npm\index.js"`。请使用两种方式来实现路径转换

# path = "/Users/yuan/npm/index.js"
# 方式1
# print(path.replace("/","\\"))
# 方式2

# print(path.split("/"))
# ret = path.split("/")
# print("\\".join(ret))


# (9) 引导用户输入一个字符串，判断是否是回文字符串**
# s = "level"
# print(s == s[::-1])


# (10)
# data = input("请输入一个str")
# data += "=" * (4 - len(data) % 4)
# print(data)


# data = input("请输入一个str")
#
# if len(data) % 4 != 0:
#     data += "=" * (4 - len(data) % 4)
#
# print(data)


# (11) 引导用户输入一个手机号,通过一个逻辑表达式判断该字符串是否符合电信手机号格式，格式要求如下，是打印True，不是打印False

# tel = input("请输入一个手机号")
# print(len(tel) == 11 and tel.isdigit() and (tel.startswith("133") or tel.startswith("153")))


# (12) 引导用户输入一个邮箱格式字符串，比如`916852314@163.com`或`1052065088@qq.com`等，然后将邮箱号和邮箱类型名打印出来，比如邮箱号`916852314`和`163邮箱

# s = "1052065088@qq.com"
#
# ret = s.split("@")
# email_code = ret[0]
# others = ret[1]
#
# email_type = others.split(".")[0]
# print(email_code)
# print(email_type)

# (13) HTTP协议格式数据组装，引导用户分别输入请求方式，请求URL以及若干个请求头

"""
请输入 HTTP 请求方法：GET
请输入 URL：https://www.example.com/api/data
请输入 HTTP 协议：HTTP/1.1
请输入请求头信息（键值对用冒号分隔，多个键值对用逗号分隔）：User-Agent: MyClient/1.0,Authorization: Token abcdef123456

浏览器pack
GET /api/data HTTP/1.1
User-Agent: MyClient/1.0
Authorization: Token abcdef123456
"""

method = input("请输入 HTTP 请求方法")
url = input("请输入 URL")
proto_name = input("请输入 HTTP 协议")
headers = input("请输入请求头信息（键值对用冒号分隔，多个键值对用逗号分隔）")

path = url.split("com")[-1]
first_line = method + " " + path + " " + proto_name
# print("first_line:", first_line)

print(first_line + "\n" + "\n".join(headers.split(",")))
