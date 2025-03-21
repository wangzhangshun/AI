# 获取用户输入的身高和体重
height = float(input("请输入您的身高（单位：米）："))
weight = float(input("请输入您的体重（单位：千克）："))

bmi = weight / (height ** 2)

if bmi < 18.5:
    advise = f"您的BMI的值{bmi:.3}，体重过轻，建议多吃少动"
elif 18.5 <= bmi < 24:
    advise = f"您的BMI的值{bmi:.3}，体重正常，建议保持！"
elif 24 <= bmi < 28:
    advise = f"您的BMI的值{bmi:.3}，体重稍胖，建议多动少吃！"
else:
    advise = f"您的BMI的值{bmi:.3}，太肥胖，建议绝食！"
print("我们的建议：", advise)
