# 初始化客户信息列表
customers = [
    {
        "name": "Alice",
        "age": 25,
        "email": "alice@example.com"
    },
    {
        "name": "Bob",
        "age": 28,
        "email": "bob@example.com"
    },
]

while 1:

    print("""
           1. 添加客户
           2. 删除客户
           3. 修改客户
           4. 查询一个客户
           5. 查询所有客户
           6. 退出

        """)
    choice = input("请输入您的选择:")

    if choice == "1":
        # (1) 添加客户 append

        name = input("请输入添加客户的姓名:")
        age = input("请输入添加客户的年龄:")
        email = input("请输入添加客户的邮箱:")

        new_customer = {
            "name": name,
            "age": age,
            "email": email
        }

        customers.append(new_customer)
        print(f"添加客户{name}成功！")
        # print("当前客户:", customers)
    elif choice == "2":
        # (2) 删除客户
        del_customer_name = input("请输入删除客户的姓名:")

        flag = False
        for customerD in customers:
            # print(customerL)
            if customerD["name"] == del_customer_name:
                customers.remove(customerD)
                print(f"客户{del_customer_name}删除成功！")
                flag = True
                break

        if flag:
            print("当前客户列表:", customers)
        else:
            print(f"客户{del_customer_name}不存在！")

    elif choice == "3":
        # (3) 修改客户

        update_customer_name = input("请输入修改客户的姓名:")

        name = input("请输入修改客户新的姓名:")
        age = input("请输入修改客户新的年龄:")
        email = input("请输入修改客户新的邮箱:")

        for customerD in customers:
            if customerD["name"] == update_customer_name:
                # customerD["name"] = name
                # customerD["age"] = age
                # customerD["email"] = email

                customerD.update({"name": name, "age": age, "email": email})

                break

        print("当前客户列表:", customers)
    elif choice == "4":
        # (4) 查看某一个客户
        query_customer_name = input("请输入查看客户的姓名:")
        for customerD in customers:
            # print("customerL",customerL)
            if customerD["name"] == query_customer_name:
                print(f"姓名:{customerD.get('name')},年龄：{customerD.get('age')},邮箱:{customerD.get('email')}")
                break
    elif choice == "5":
        # (5) 遍历每一个一个客户信息
        # if len(customers) == 0:
        if customers:
            for customerD in customers:
                print(f"姓名:{customerD.get('name'):10},年龄：{customerD.get('age')},邮箱:{customerD.get('email')}")
        else:
            print("当前没有任何客户信息！")
    elif choice == "6":
        print("退出程序！")
        break
    else:
        print("输入内容格式不对！")
