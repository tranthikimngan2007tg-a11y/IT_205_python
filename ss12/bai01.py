cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]

while True:
    print("============================================")
    print("\tSHOPEE CART MANAGEMENT SYSTEM")
    print("============================================")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("============================================")

    choice = input("Mời bạn chọn chức năng (1-5): ")

    match choice:

        case "1":
            total_product = 0
            total_price = 0

            print("\n--- CHI TIẾT GIỎ HÀNG ---")
            print(f"{'STT':<5} | {'Mã SP':<10} | {'Tên Sản Phẩm':<25} | {'SL':<5} | {'Đơn Giá':<15} | {'Thành Tiền'}")

            for index, value in enumerate(cart_items, start=1):
                thanh_tien = value["number"] * value["price"]

                print(f"{index:<5} | {value['id']:<10} | {value['name']:<25} | {value['number']:<5} | {value['price']:<15} | {thanh_tien}")

                total_product += value["number"]
                total_price += thanh_tien

            print(f"\n=> Tổng số lượng sản phẩm: {total_product}")
            print(f"=> TỔNG TIỀN THANH TOÁN: {total_price:,}đ")

        case "2":
            new_id = input("Nhập mã sản phẩm: ")
            new_name = input("Nhập tên sản phẩm: ")

            while True:
                new_number = input("Nhập số lượng: ")
                if new_number.isdigit():
                    new_number = int(new_number)
                    break
                print("LỖI! Vui lòng nhập số.")

            while True:
                new_price = input("Nhập đơn giá: ")
                if new_price.isdigit():
                    new_price = int(new_price)
                    break
                print("LỖI! Vui lòng nhập số.")

            found = False

            for item in cart_items:
                if new_id == item["id"]:
                    item["number"] += new_number
                    print("Mã sản phẩm đã tồn tại! Đã cộng dồn số lượng.")
                    found = True
                    break

            if not found:
                new_product = {
                    "id": new_id,
                    "name": new_name,
                    "number": new_number,
                    "price": new_price
                }

                cart_items.append(new_product)
                print("Thêm sản phẩm thành công!")

        case "3":
            id_update = input("Nhập mã sản phẩm muốn cập nhật: ")

            while True:
                number_update = input("Nhập số lượng mới: ")
                if number_update.isdigit():
                    number_update = int(number_update)
                    break
                print("LỖI! Nhập lại.")

            found = False

            for item in cart_items:
                if id_update == item["id"]:
                    item["number"] = number_update
                    print("Cập nhật thành công!")
                    found = True
                    break

            if not found:
                print("Không tìm thấy mã sản phẩm!")

        case "4":
            del_id = input("Nhập mã sản phẩm muốn xóa: ")

            found = False

            for item in cart_items:
                if del_id == item["id"]:
                    cart_items.remove(item)
                    print("Xóa sản phẩm thành công!")
                    found = True
                    break

            if not found:
                print("Không tìm thấy mã sản phẩm!")

        case "5":
            print("Thoát chương trình...")
            break

        case _:
            print("Lựa chọn không hợp lệ!")