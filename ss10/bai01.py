cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n===== SHOPEE CART MANAGEMENT =====")
    print("1. Xem chi tiết giỏ hàng và tổng tiền")
    print("2. Thêm sản phẩm mới hoặc tăng số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    match choice:
        case "1":
            if len(cart_items) == 0:
                print("Giỏ hàng đang trống.")
            else:
                print("\n===== CHI TIẾT GIỎ HÀNG =====")
                print("Mã SP\tTên sản phẩm\t\t\tSố lượng\tĐơn giá\t\tThành tiền")
                total_quantity = 0
                total_price = 0
                for item in cart_items:
                    product_id = item[0]
                    product_name = item[1]
                    quantity = item[2]
                    price = item[3]
                    amount = quantity * price
                    total_quantity += quantity
                    total_price += amount
                    print( product_id,"\t",product_name,"\t",quantity,"\t\t",price,"\t",amount)
                print("\nTổng số lượng:", total_quantity)
                print("Tổng tiền:", total_price, "VND")
        case "2":
            product_id = input("Nhập mã sản phẩm: ").strip().upper()
            product_name = input("Nhập tên sản phẩm: ").strip()
            quantity = input("Nhập số lượng: ").strip()
            price = input("Nhập đơn giá: ").strip()
            if quantity.isdigit() and price.isdigit():
                quantity = int(quantity)
                price = int(price)
                if quantity <= 0 or price < 0:
                    print("Số lượng hoặc đơn giá không hợp lệ!")
                else:
                    found = False
                    for item in cart_items:
                        if item[0] == product_id:
                            item[2] += quantity
                            found = True
                            print("Sản phẩm đã tồn tại, đã cộng dồn số lượng!")
                            break
                    if found == False:
                        cart_items.append([
                            product_id,
                            product_name,
                            quantity,
                            price
                        ])
                        print("Thêm sản phẩm thành công!")
            else:
                print("Số lượng và đơn giá phải là số!")
        case "3":
            product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
            new_quantity = input("Nhập số lượng mới: ").strip()
            if new_quantity.isdigit():
                new_quantity = int(new_quantity)
                if new_quantity <= 0:
                    print("Số lượng không hợp lệ!")
                else:
                    found = False
                    for item in cart_items:
                        if item[0] == product_id:
                            item[2] = new_quantity
                            found = True
                            print("Cập nhật số lượng thành công!")
                            break
                    if found == False:
                        print("Mã sản phẩm không tồn tại trong giỏ hàng.")
            else:
                print("Số lượng phải là số!")
        case "4":
            product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
            found = False
            for item in cart_items:
                if item[0] == product_id:
                    cart_items.remove(item)
                    found = True
                    print("Xóa sản phẩm thành công!")
                    break
            if found == False:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
        case "5":
            print("Thoát chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")