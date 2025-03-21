shopping_cart = [
    {
        "name": "mac",
        "price": 14999,
        "quantity": 1
    },
    {
        "name": "iphone15",
        "price": 9980,
        "quantity": 1
    }
]

inventory = {
    1: {
        "name": "苹果",
        "price": 122,
        "quantity": 100
    },
    2: {
        "name": "橘子",
        "price": 32,
        "quantity": 1000
    },
    3: {
        "name": "香蕉",
        "price": 12,
        "quantity": 1500
    },

}

while 1:
    print("""
       请选择操作：
           1. 添加商品
           2. 删除商品
           3. 打印购物车
           4. 退出
    """)

    choice = input("请输入您的选择：")

    if choice == "1":
        name = input("请输入上商品的名称：")
        price = float(input("请输入上商品的价格："))
        quantity = int(input("请输入上商品的数量："))

        shopping_cart.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        print("添加商品成功", shopping_cart)

    elif choice == "2":
        num = int(input("请输入删除商品的序号"))
        index = num - 1
        del_goods = shopping_cart.pop(index)
        print(f"商品{del_goods.get('name')}删除成功")

    elif choice == "3":
        print("当前购物车展示:")
        print("-" * 40)
        total = 0
        for i, goods in enumerate(shopping_cart, 1):
            name = goods.get("name")
            price = goods.get("price")
            quantity = goods.get("quantity")
            print(f"{i}.{name:10} 价格-{price:5} 数量-{quantity:5}")
            total += price * quantity
        print("-" * 40)
        print("总价格：", total)
    elif choice == "4":
        print("感谢使用购物车!")
        break
    else:
        print("无效输入，请重新选择!")
