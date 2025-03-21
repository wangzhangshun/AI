# 初始化客户信息列表
customers = {
    1001: {
        "name": "Alice",
        "age": 25,
        "email": "alice@example.com"
    },
    1002: {
        "name": "Bob",
        "age": 28,
        "email": "bob@example.com"
    },
}

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

        id = int(input("请输入添加客户的ID:"))

        if id in customers:  # "1001" in {1001:...}
            print("该ID已经存在！")
        else:

            name = input("请输入添加客户的姓名:")
            age = input("请输入添加客户的年龄:")
            email = input("请输入添加客户的邮箱:")

            new_customer = {
                "name": name,
                "age": age,
                "email": email
            }
            # customers[id] = new_customer
            customers.update({id: new_customer})

            print(f"添加客户{name}成功！")
            print("当前客户:", customers)
    elif choice == "2":
        # (2) 删除客户
        del_customer_id = int(input("请输入删除客户的ID:"))
        if del_customer_id in customers:

            customers.pop(del_customer_id)
            print(f"删除{del_customer_id}客户成功!")
            print("当前客户:", customers)
        else:
            print("该ID不存在！")
    elif choice == "3":
        # (3) 修改客户

        update_customer_id = int(input("请输入修改客户的ID:"))

        if update_customer_id in customers:

            name = input("请输入修改客户新的姓名:")
            age = input("请输入修改客户新的年龄:")
            email = input("请输入修改客户新的邮箱:")

            # 方式1:
            # customers[update_customer_id]["name"] = name
            # customers[update_customer_id]["age"] = age
            # customers[update_customer_id]["email"] = email
            # 方式2:
            customers[update_customer_id].update({"name": name, "age": age, "email": email})

            # 方式3:

            # customers[update_customer_id] = {
            #     "name": name,
            #     "age": age,
            #     "email": email,
            # }

            print(f"{update_customer_id}客户修改成功！")
            print("当前客户:", customers)
        else:
            print("该ID不存在！")
    elif choice == "4":
        # (4) 查看某一个客户
        query_customer_id = int(input("请输入查看客户的ID:"))
        if query_customer_id in customers:
            customerD = customers[query_customer_id]
            print(f"姓名:{customerD.get('name')},年龄：{customerD.get('age')},邮箱:{customerD.get('email')}")
        else:
            print("该客户ID不存在！")
    elif choice == "5":
        # (5) 遍历每一个一个客户信息
        # if len(customers) == 0:
        if customers:
            for key,customerDict in customers.items():
                print(f"客户ID：{key},姓名:{customerDict.get('name'):10},年龄：{customerDict.get('age')},邮箱:{customerDict.get('email')}")
        else:
            print("当前没有任何客户信息！")
    elif choice == "6":
        print("退出程序！")
        break
    else:
        print("输入内容格式不对！")
