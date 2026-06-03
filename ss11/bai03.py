# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

# 1. Phân tích Input / Output

# Input:
# - Người dùng nhập lựa chọn menu (1 - 5)
# - Người dùng nhập:
#   + Mã sản phẩm (str)
#   + Tên sản phẩm (str)
#   + Giá sản phẩm (int)
#   + Số lượng sản phẩm (int)

# Output:
# - Hiển thị danh sách sản phẩm
# - Thêm sản phẩm mới thành công hoặc báo lỗi
# - Cập nhật thông tin sản phẩm thành công hoặc báo lỗi
# - Xóa sản phẩm thành công hoặc báo lỗi
# - Thông báo thoát chương trình

# 2. Đề xuất giải pháp

# - Sử dụng list để lưu danh sách sản phẩm
# - Mỗi sản phẩm được lưu bằng dictionary gồm:
#   + product_id
#   + product_name
#   + price
#   + quantity
# - Sử dụng vòng lặp while True để hiển thị menu liên tục
# - Chức năng hiển thị:
#   + Duyệt list bằng for
#   + Nếu list rỗng -> thông báo danh sách trống
# - Chức năng thêm sản phẩm
#   + Chuẩn hóa mã sản phẩm bằng strip() và upper()
#   + Kiểm tra mã sản phẩm bị trùng
#   + Kiểm tra giá và số lượng phải là số nguyên dương
#   + Nếu hợp lệ -> append() vào list
# - Chức năng cập nhật:
#   + Tìm sản phẩm theo product_id
#   + Nếu tìm thấy -> cập nhật tên, giá, số lượng
#   + Nếu không tìm thấy -> báo lỗi
# - Chức năng xóa:
#   + Tìm sản phẩm theo mã
#   + Nếu tồn tại -> remove()
#   + Nếu không tồn tại -> báo lỗi
# - Kiểm tra edge cases:
#   + Mã sản phẩm viết thường hoặc dư khoảng trắng
#   + Mã sản phẩm bị trùng
#   + Mã sản phẩm không tồn tại
#   + Giá hoặc số lượng không hợp lệ
#   + Nhập sai menu

# 3. Thiết kế thuật toán (Pseudocode)
# B1: Khởi tạo danh sách sản phẩm
# B2: Lặp menu vô hạn
#     Hiển thị menu
# B3: Nhập lựa chọn

#     Nếu chọn 1:
#         Hiển thị danh sách sản phẩm

#     Nếu chọn 2:
#         Nhập thông tin sản phẩm
#         Chuẩn hóa mã sản phẩm
#         Kiểm tra trùng mã
#         Kiểm tra dữ liệu hợp lệ
#         Thêm sản phẩm

#     Nếu chọn 3:
#         Nhập mã sản phẩm
#         Tìm sản phẩm
#         Nếu tồn tại -> cập nhật
#         Ngược lại -> báo lỗi

#     Nếu chọn 4:
#         Nhập mã sản phẩm
#         Tìm sản phẩm
#         Nếu tồn tại -> xóa
#         Ngược lại -> báo lỗi

#     Nếu chọn 5:
#         Thoát chương trình

#     Ngược lại:
#         Báo lựa chọn không hợp lệ

# (2) TRIỂN KHAI CODE

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    match choice:
        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("\nDanh sách sản phẩm hiện tại:")
                for index, product in enumerate(product_list, start=1):
                    print(
                        f"{index}. "
                        f"Mã SP: {product['product_id']} | "
                        f"Tên: {product['product_name']} | "
                        f"Giá: {product['price']} | "
                        f"Số lượng: {product['quantity']}"
                    )

        case "2":
            product_id = input("Nhập mã sản phẩm: ").strip().upper()
            is_duplicate = False
            for product in product_list:
                if product["product_id"] == product_id:
                    is_duplicate = True
                    break
            if is_duplicate:
                print("Mã sản phẩm bị trùng")
                continue
            product_name = input("Nhập tên sản phẩm: ").strip()
            price = input("Nhập giá sản phẩm: ").strip()
            quantity = input("Nhập số lượng sản phẩm: ").strip()

            if (
                not price.isdigit()
                or not quantity.isdigit()
            ):
                print("Giá/Số lượng không hợp lệ")
                continue
            price = int(price)
            quantity = int(quantity)
            if price <= 0 or quantity <= 0:
                print("Giá/Số lượng không hợp lệ")
                continue
            new_product = {
                "product_id": product_id,
                "product_name": product_name,
                "price": price,
                "quantity": quantity
            }
            product_list.append(new_product)
            print("Thêm sản phẩm thành công")
        case "3":
            update_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
            found_product = None
            for product in product_list:
                if product["product_id"] == update_id:
                    found_product = product
                    break

            if found_product is None:
                print("Không tìm thấy mã sản phẩm cần cập nhật!")
                continue

            new_name = input("Nhập tên mới: ").strip()
            new_price = input("Nhập giá mới: ").strip()
            new_quantity = input("Nhập số lượng mới: ").strip()

            if (
                not new_price.isdigit()
                or not new_quantity.isdigit()
            ):
                print("Giá/Số lượng không hợp lệ")
                continue

            new_price = int(new_price)
            new_quantity = int(new_quantity)

            if (
                new_price <= 0
                or new_quantity <= 0
            ):
                print("Giá/Số lượng không hợp lệ")
                continue
            found_product["product_name"] = new_name
            found_product["price"] = new_price
            found_product["quantity"] = new_quantity
            print("Cập nhật sản phẩm thành công")
        case "4":
            delete_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
            found_product = None
            for product in product_list:
                if product["product_id"] == delete_id:
                    found_product = product
                    break
            if found_product is None:
                print("Không tìm thấy mã sản phẩm cần xoá!")
            else:
                product_list.remove(found_product)
                print("Xóa sản phẩm thành công")
        case "5":
            print("Thoát chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
