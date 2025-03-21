# 选课系统代码提示

# 学生信息字典
students = {
    "1001": {"user": "yuan", "pwd": "123"}
}

# 课程信息字典
courses = {
    "CS101": "计算机科学导论",
    "ENG201": "高级英语写作",
    "MATH301": "线性代数",
    "PHYS401": "物理学原理",
    "HIST501": "世界历史概论"
}

# 学生选课字典
student_courses = {
    # "1001": [],

}

is_login = False
student_id = None

while True:
    print("欢迎使用选课系统！")
    print("1. 注册学生")
    print("2. 登录")
    print("3. 选课")
    print("4. 退课")
    print("5. 查看已选课程")
    print("6. 退出系统")

    choice = input("请输入您的选项：")

    if choice == "1":
        stu_id = input("请输入学生的学号")
        user = input("请输入学生的姓名")
        pwd = input("请输入学生的密码")
        students[stu_id] = {"user": user, "pwd": pwd}
        print(f"学生{user}注册成功！")

    elif choice == "2":
        stu_id = input("请输入学生学号:")
        if stu_id in students:
            # 获取用户名和密码，然后比对认证
            stu_pwd = input("请输入学生密码：")
            if stu_pwd == students[stu_id]["pwd"]:
                print(f"欢迎回来，{students[stu_id]['user']}")
                is_login = True
                student_id = stu_id
            else:
                print("账号或密码错误！")
        else:
            print(f"{stu_id}学号不存在，请先注册")

    elif choice == "3":
        if not is_login:
            # 未登录状态
            print("请先登录！")
            continue
        # 选课
        print("当前登陆人：", student_id)
        print("展示可以选修课程：")
        print("*" * 50)
        for course_code, course_name in courses.items():
            print(f"课程ID：{course_code}，课程名称：{course_name}")
        print("*" * 50)
        course_code = input("请输入选修课程ID")
        # 方式1:
        # if student_id in student_courses:
        #     if course_code in student_courses[student_id]:
        #         print(f"{course_code}已经选修了，不能重复选！")
        #     else:
        #         student_courses[student_id].append(course_code)
        #         print(f"再次选课：{student_id}选修{course_code}课程成功！")
        # else:
        #     student_courses[student_id] = [course_code]
        #     print(f"选课初始化：{student_id}选修{course_code}课程成功！")

        # 方式2(推荐方式):
        if student_id not in student_courses:
            student_courses[student_id] = []

        # 每一个学生id在student_courses大字典中都有一个一个初始化的列表
        if course_code in student_courses[student_id]:
            print(f"{course_code}已经选修了，不能重复选！")
        else:
            student_courses[student_id].append(course_code)
            print(f"{student_id}选修{course_code}课程成功！")

        print("student_courses:", student_courses)

    elif choice == "4":
        if not is_login:
            # 未登录状态
            print("请先登录！")
            continue

        if student_id in student_courses:
            print("该账号已经选修课程：")
            print("-" * 50)
            for course_code in student_courses[student_id]:
                print(f"课程ID：{course_code}，课程名称：{courses.get(course_code)}")
            print("-" * 50)

            course_code = input("请输入您要退的课程ID：")
            if course_code in student_courses[student_id]:
                student_courses[student_id].remove(course_code)
                print(f"成功退课：{courses[course_code]}")
                print("student_courses:", student_courses)
            else:
                print("您未选修该课程")
        else:
            print("您未选修过任何课程！")

    elif choice == "5":
        if not is_login:
            # 未登录状态
            print("请先登录！")
            continue

        if student_id in student_courses:
            print("-" * 50)
            for course_code in student_courses[student_id]:
                print(f"课程ID：{course_code}，课程名称：{courses.get(course_code)}")
            print("-" * 50)
        else:
            print("您未选修过任何课程！")

    elif choice == "6":
        print("感谢您使用我们的选课系统,欢迎下次再来!")
        break
    else:
        print("请您输入有效的选项")
