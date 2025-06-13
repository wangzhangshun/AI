import re
import os


def main(text):

    text = get_file_data(text)

    result = [[num, "待处理", ""] for num in re.findall(r'\d+', text)]
    print(result)
    return result

 # 格式化文件中单号
def get_file_data(input_data):
    # 去除字符串两端的空格和逗号
    cleaned = input_data.strip(' ,')
    # 使用正则表达式提取所有连续数字
    numbers = re.findall(r'\d+', cleaned)
    # 将数字列表用逗号连接成字符串
    return','.join(numbers)



# 测试示例
if __name__ == "__main__":
    # 测试文件数据
    file_example1 = "20250506-1.txt\r\n16B"
    file_example2 = "20250506-1 .xlsx\r\n16B"

    print(main(file_example1))  # 输出: 20250506-1.txt
    print(main(file_example2))  # 输出: 20250506-1 .xlsx