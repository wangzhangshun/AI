shopping_cart = []
while 1:

    print("--- 购物车清单 ---")
    print("1. 添加商品")
    print("2. 删除商品")
    print("3. 查看购物车")
    choice = input("请输入选项：")
    if choice == "1":
        add_item = input("请输入添加商品名称:")
        shopping_cart.append(add_item)
        print(f"已添加商品:{add_item}")
        print("\n")
    elif choice == "2":
        del_item = input("请输入删除商品名称:")

        if del_item in shopping_cart:
            shopping_cart.remove(del_item)
            print(f"已删除商品:{del_item}")
        else:
            print("该商品不存在在购物车中！")

    elif choice == "3":

        if len(shopping_cart) == 0:
            print("购物车为空")
        else:
            print("*" * 20)
            for i in shopping_cart:
                print(i)
            print("*" * 20)
    else:
        print("无效输入！")
