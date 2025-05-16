from openai import OpenAI
import os

def open_ai(text):
    # 获取大模型以及API-KEY
    openai_key = "sk-7c617e3f9945432593dea80cc5530037"
    model =  "qwen2.5-vl-32b-instruct"
    client = OpenAI(api_key=openai_key, base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

    # 构造情感分析的提示词
    prompt = f"请对以下内容进行综合分析：\n\n{text}"

    # 向模型发送请求，并处理返回的结果
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content.strip()
    return result

print(open_ai("生成一个MCP(Model Context Protocol)的介绍文档"))
