# HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS

# (1) PHÂN TÍCH & THIẾT KẾ GIẢI PHÁP

# 1. INPUT / OUTPUT
# Input:
# - Lựa chọn menu chính (str)
# - Lựa chọn menu con (str)
# - Mã đơn hàng (str)
# - Trạng thái đơn hàng (str)
# - Vị trí cần sửa/xóa (str)

# Output:
# - Danh sách đơn hàng
# - Thông báo thêm/sửa/xóa thành công
# - Thống kê số lượng đơn hàng
# - Thông báo lỗi nếu nhập sai

# 2. GIẢI PHÁP
# - Dùng List lưu đơn hàng.
# - Dùng while True để chạy chương trình.
# - Dùng match case xử lý menu.
# - Dùng strip() để xóa khoảng trắng.
# - Dùng upper() để chuẩn hóa dữ liệu.
# - Dùng append() để thêm đơn hàng.
# - Dùng pop() để xóa đơn hàng.
# - Dùng split() để lấy trạng thái.
# - Dùng isdigit() kiểm tra vị trí có phải số hay không.

# 3. EDGE CASES

# - Nhập khoảng trắng hoặc chữ thường
# => chuẩn hóa bằng strip().upper()
# - Nhập sai vị trí
# => báo lỗi
# - Nhập chữ ở vị trí
# => báo "Vị trí không hợp lệ!"
# - Nhập sai menu
# => báo lỗi
# - Danh sách rỗng vẫn thống kê được

# 4. PSEUDOCODE
# Khởi tạo danh sách đơn hàng
# while True:
#     Hiển thị menu chính

#     match case:
#         case 1:
#             Hiển thị danh sách

#         case 2:
#             Hiển thị menu con

#         case 3:
#             Thống kê trạng thái

#         case 4:
#             Thoát

# (2) TRIỂN KHAI CODE

order_list = ["GE001 - PENDING","GE002 - DELIVERING","GE003 - CANCELLED"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    main_choice = input("Nhập lựa chọn: ").strip()

    match main_choice:
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
            while True:
                print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
                print("1. Thêm đơn hàng mới")
                print("2. Sửa đơn hàng theo vị trí")
                print("3. Xóa đơn hàng theo vị trí")
                print("4. Quay lại menu chính")
                sub_choice = input("Nhập lựa chọn: ").strip()
                match sub_choice:
                    case "1":
                        order_code = input("Nhập mã đơn hàng: ").strip().upper()
                        order_status = input("Nhập trạng thái: ").strip().upper()
                        new_order = (f"{order_code} - {order_status}")
                        order_list.append(new_order)
                        print("Thêm đơn hàng thành công!")
                    case "2":
                        position = input("Nhập vị trí cần sửa: ").strip()

                        if position.isdigit():
                            position = int(position)
                            index = position - 1
                            if 0 <= index < len(order_list):
                                order_code = input("Nhập mã mới: ").strip().upper()
                                order_status = input("Nhập trạng thái mới: ").strip().upper()
                                updated_order = (
                                    f"{order_code} - "
                                    f"{order_status}")
                                order_list[index] = updated_order
                                print("Cập nhật thành công!")
                            else:
                                print("Không tồn tại đơn hàng ở vị trí này!")
                        else:
                            print("Vị trí không hợp lệ!")
                    case "3":
                        position = input("Nhập vị trí cần xóa: ").strip()

                        if position.isdigit():
                            position = int(position)
                            index = position - 1
                            if 0 <= index < len(order_list):
                                deleted_order = (order_list.pop(index))
                                print("Đơn hàng vừa xóa:",deleted_order)
                            else:
                                print("Không tồn tại đơn hàng ở vị trí này!")
                        else:
                            print("Vị trí không hợp lệ!")
                    case "4":
                        break
                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        case "3":
            pending_count = 0
            delivering_count = 0
            completed_count = 0
            cancelled_count = 0
            for order in order_list:
                split_order = order.split(" - ")
                status = split_order[1]
                match status:
                    case "PENDING":
                        pending_count += 1
                    case "DELIVERING":
                        delivering_count += 1
                    case "COMPLETED":
                        completed_count += 1
                    case "CANCELLED":
                        cancelled_count += 1
            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            print(f"PENDING: {pending_count}")
            print(f"DELIVERING: {delivering_count}")
            print(f"COMPLETED: {completed_count}")
            print(f"CANCELLED: {cancelled_count}")
            print(f"Tổng số đơn hàng: {len(order_list)}")
        case "4":
            print("Thoát chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")