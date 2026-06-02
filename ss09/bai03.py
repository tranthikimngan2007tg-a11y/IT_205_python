# HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS

# (1) PHÂN TÍCH & THIẾT KẾ GIẢI PHÁP

# 1. INPUT / OUTPUT

# Input:
# - Người dùng nhập lựa chọn menu (str)
#     1 -> Hiển thị danh sách đơn hàng
#     2 -> Thêm đơn hàng mới
#     3 -> Xóa đơn hàng theo mã
#     4 -> Thoát chương trình

# - Người dùng nhập mã đơn hàng (str)
#     Có thể viết thường hoặc có khoảng trắng.

# Output:
# - Danh sách đơn hàng hiện tại
# - Thông báo thêm/xóa thành công
# - Thông báo lỗi nếu không tìm thấy mã
# - Thông báo lỗi khi nhập sai menu


# 2. GIẢI PHÁP
# - Sử dụng list để lưu đơn hàng.
# - Sử dụng while True để chạy menu liên tục.
# - Dùng strip() để xóa khoảng trắng.
# - Dùng upper() để chuyển thành chữ hoa.
# - Dùng append() để thêm đơn hàng.
# - Dùng remove() để xóa đơn hàng.
# - Sử dụng match case để xử lý menu.

# 3. EDGE CASES
# - Nhập khoảng trắng hoặc chữ thường:
#     "  ge004  "
# => Chuẩn hóa thành "GE004"

# - Xóa mã không tồn tại:
#     GE999
# => Báo lỗi

# - Nhập menu sai:
#     5, abc, @
# => Báo lỗi và hiển thị lại menu


# 4. THUẬT TOÁN
# B1: Tạo danh sách đơn hàng mẫu
# B2: Hiển thị menu liên tục
#     - Nhập lựa chọn
#     match case:
#         case "1":
#             Hiển thị danh sách

#         case "2":
#             Nhập mã mới
#             Chuẩn hóa
#             Thêm vào list

#         case "3":
#             Nhập mã cần xóa
#             Chuẩn hóa
#             Kiểm tra tồn tại
#             Nếu có -> xóa
#             Nếu không -> báo lỗi

#         case "4":
#             Thoát chương trình

#         case _:
#             Báo nhập sai menu

# (2) TRIỂN KHAI CODE

order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    match choice:
        case "1":
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("\nDanh sách đơn hàng hiện tại:")
                count = 1
                for order in order_list:
                    print(f"{count}. {order}")
                    count += 1
        case "2":
            new_order = input("Nhập mã đơn hàng mới: ")
            new_order = new_order.strip().upper()

            if new_order == "":
                print("Mã đơn hàng không được để trống!")
            else:
                order_list.append(new_order)

                print("Thêm đơn hàng thành công!")
                print("Danh sách hiện tại:", order_list)
        case "3":
            delete_code = input("Nhập mã đơn hàng cần xóa: ")
            delete_code = delete_code.strip().upper()

            if delete_code in order_list:
                order_list.remove(delete_code)
                print("Xóa đơn hàng thành công!")
            else:
                print("Không tìm thấy mã đơn hàng cần xóa!")
        case "4":
            print("Thoát chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")