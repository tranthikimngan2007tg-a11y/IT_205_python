# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

# 1. Phân tích Input / Output

# Input:
# - Người dùng nhập lựa chọn menu (1 - 5)
# - Người dùng nhập:
#   + Mã sản phẩm (str)
#   + Số lượng mua (int)
#   + Số lượng nhập kho (int)

# Output:
# - Hiển thị danh sách sản phẩm và trạng thái tồn kho
# - Bán sản phẩm thành công hoặc báo lỗi
# - Nhập thêm hàng thành công hoặc báo lỗi
# - Hiển thị báo cáo doanh thu
# - Thông báo thoát chương trình

# 2. Đề xuất giải pháp

# - Sử dụng list để lưu danh sách sản phẩm
# - Mỗi sản phẩm được lưu bằng dictionary gồm:
#   + product_id
#   + product_name
#   + price
#   + quantity
#   + sold
# - Sử dụng vòng lặp while True để hiển thị menu liên tục
# - Chức năng hiển thị sản phẩm:
#   + Duyệt list bằng for
#   + Kiểm tra tồn kho:
#       quantity == 0 -> Hết hàng
#       quantity <= 5 -> Sắp hết hàng
#       quantity > 5 -> Còn hàng
# - Chức năng bán sản phẩm:
#   + Chuẩn hóa mã sản phẩm bằng strip() và upper()
#   + Kiểm tra sản phẩm có tồn tại không
#   + Kiểm tra số lượng mua là số nguyên dương
#   + Kiểm tra tồn kho có đủ không
#   + Nếu hợp lệ:
#       Trừ số lượng tồn kho
#       Tăng số lượng đã bán
#       Tính tiền khách cần thanh toán
# - Chức năng nhập kho:
#   + Chuẩn hóa mã sản phẩm
#   + Kiểm tra sản phẩm tồn tại
#   + Kiểm tra số lượng nhập hợp lệ
#   + Nếu hợp lệ -> cộng thêm tồn kho
# - Chức năng báo cáo doanh thu:
#   + Tính doanh thu từng sản phẩm
#   + Tính tổng doanh thu cửa hàng
#   + Tìm sản phẩm bán chạy nhất
#   + Nếu chưa bán sản phẩm nào -> thông báo
# - Kiểm tra edge cases:
#   + Mã sản phẩm dư khoảng trắng hoặc viết thường
#   + Mã sản phẩm không tồn tại
#   + Số lượng mua/nhập không hợp lệ
#   + Số lượng mua vượt tồn kho
#   + Nhập sai menu

# 3. Thiết kế thuật toán (Pseudocode)

# B1: Khởi tạo danh sách sản phẩm
# B2: Lặp menu vô hạn
#     Hiển thị menu
# B3: Nhập lựa chọn

#     Nếu chọn 1:
#         Hiển thị danh sách sản phẩm
#         Kiểm tra trạng thái tồn kho
#     Nếu chọn 2:
#         Nhập mã sản phẩm
#         Chuẩn hóa mã
#         Kiểm tra tồn tại
#         Nhập số lượng mua
#         Kiểm tra hợp lệ
#         Kiểm tra tồn kho
#         Cập nhật tồn kho và số lượng bán
#         Tính tiền thanh toán
#     Nếu chọn 3:
#         Nhập mã sản phẩm
#         Chuẩn hóa mã
#         Kiểm tra tồn tại
#         Nhập số lượng nhập
#         Kiểm tra hợp lệ
#         Cộng thêm tồn kho
#     Nếu chọn 4:
#         Tính doanh thu từng sản phẩm
#         Tính tổng doanh thu
#         Tìm sản phẩm bán chạy nhất
#     Nếu chọn 5:
#         Thoát chương trình
#     Ngược lại:
#         Báo lỗi lựa chọn không hợp lệ

# (2) TRIỂN KHAI CODE

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    match choice:

        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("\nDanh sách sản phẩm hiện tại:")
                for index, product in enumerate(product_list, start=1):
                    if product["quantity"] == 0:
                        status = "Hết hàng"
                    elif product["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                    print(
                        f"{index}. "
                        f"Mã SP: {product['product_id']} | "
                        f"Tên: {product['product_name']} | "
                        f"Giá: {product['price']} | "
                        f"Tồn kho: {product['quantity']} | "
                        f"Đã bán: {product['sold']} | "
                        f"Trạng thái: {status}"
                    )
        case "2":
            product_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
            found_product = None
            for product in product_list:
                if product["product_id"] == product_id:
                    found_product = product
                    break
            if found_product is None:
                print("Không tìm thấy sản phẩm cần bán")
                continue
            quantity_buy = input("Nhập số lượng khách mua: ").strip()
            if not quantity_buy.isdigit():
                print("Số lượng mua không hợp lệ")
                continue
            quantity_buy = int(quantity_buy)
            if quantity_buy <= 0:
                print("Số lượng mua không hợp lệ")
                continue
            if quantity_buy > found_product["quantity"]:
                print("Số lượng trong kho không đủ để bán")
                continue
            found_product["quantity"] -= quantity_buy
            found_product["sold"] += quantity_buy
            total_price = (found_product["price"] * quantity_buy)
            print("Bán sản phẩm thành công")
            print(f"Khách cần thanh toán: {total_price}")
        case "3":
            product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
            found_product = None
            for product in product_list:
                if product["product_id"] == product_id:
                    found_product = product
                    break
            if found_product is None:
                print("Không tìm thấy sản phẩm cần nhập kho")
                continue

            import_quantity = input("Nhập số lượng nhập thêm: ").strip()

            if not import_quantity.isdigit():
                print("Số lượng nhập kho không hợp lệ")
                continue
            import_quantity = int(import_quantity)
            if import_quantity <= 0:
                print("Số lượng nhập kho không hợp lệ")
                continue
            found_product["quantity"] += import_quantity
            print("Nhập hàng thành công")
        case "4":
            total_revenue = 0
            best_seller = None
            max_sold = 0
            has_revenue = False
            print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")

            for index, product in enumerate(product_list,start=1):
                revenue = (product["price"]* product["sold"])
                if product["sold"] > 0:
                    has_revenue = True
                total_revenue += revenue
                print(
                    f"{index}. "
                    f"{product['product_name']} | "
                    f"Đã bán: {product['sold']} | "
                    f"Doanh thu: {revenue}"
                )
                if product["sold"] > max_sold:
                    max_sold = product["sold"]
                    best_seller = (
                        product["product_name"]
                    )
            if not has_revenue:
                print("Chưa có doanh thu phát sinh.")
            else:
                print(
                    f"\nTổng doanh thu: "
                    f"{total_revenue}"
                )
                print(
                    f"Sản phẩm bán chạy nhất: "
                    f"{best_seller}"
                )
        case "5":
            print("Thoát chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ vui lòng nhập lại!")