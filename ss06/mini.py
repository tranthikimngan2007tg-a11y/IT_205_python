# (1) Phân tích và thiết kế giải pháp

# 1. Phân tích Input / Output

# Input (Dữ liệu đầu vào)
# - choice: lựa chọn menu (kiểu int)
# - product_choice: lựa chọn mặt hàng
#     1 = Laptop
#     2 = Phone
#     3 = Tablet
# - quantity: số lượng nhập hoặc xuất kho
#   (kiểu int, phải >= 0)
# Output (Dữ liệu đầu ra)
# Chức năng 1: Xem báo cáo tồn kho
# - Hiển thị số lượng tồn kho hiện tại
# - Hiển thị biểu đồ dấu *
# Ví dụ:
# Laptop (5): *****
# Chức năng 2: Nhập kho
# - Cộng thêm số lượng vào kho
# Chức năng 3: Xuất kho
# - Trừ số lượng khỏi kho
# - Nếu xuất lớn hơn tồn kho:
#   "Không đủ hàng"
# Chức năng 4: Cảnh báo tồn kho thấp
# - Nếu tồn kho < 10:
#   "[CẢNH BÁO] Mặt hàng ... sắp hết"
# Chức năng 5:
# - Hiển thị:
#   "Thoát chương trình"
# - Kết thúc hệ thống

# 2. Đề xuất giải pháp

# Bước 1:
# Khởi tạo 3 biến tồn kho:
# laptop_stock = 0
# phone_stock = 0
# tablet_stock = 0

# Bước 2:
# Dùng while True để tạo menu chạy liên tục.

# Bước 3:
# Kiểm tra lựa chọn menu bằng if/elif/else.
# Nếu nhập sai:
# Hiển thị lỗi và quay lại menu.
# Nếu chọn 5:
# Dùng break để thoát.

# Bước 4:
# Nhập kho
# - Chọn mặt hàng
# - Nhập số lượng
# Validation:
# Nếu quantity < 0:
# In:
# "Số lượng không hợp lệ,
# vui lòng nhập lại!"
# Sau đó hỏi lại bằng while.
# Dùng += để cộng kho.

# Bước 5:
# Xuất kho
# - Chọn mặt hàng
# - Nhập số lượng
# Validation số âm.
# Kiểm tra:
# Nếu xuất > tồn kho:
# In:
# "Không đủ hàng"
# Ngược lại:
# dùng -= để trừ kho.

# Bước 6:
# Xem báo cáo tồn kho
# - In số lượng từng mặt hàng
# - Dùng for để vẽ dấu *

# Bước 7:
# Cảnh báo tồn kho thấp
# Dùng if độc lập:
# Nếu mặt hàng < 10
# -> cảnh báo

# 3. Thiết kế thuật toán (Pseudocode)

# Khởi tạo tồn kho = 0
# Lặp menu vô hạn
#     Hiển thị menu
#     Nhập lựa chọn
#     Nếu chọn sai:
#         báo lỗi
#     Nếu chọn 1:
#         Hiển thị tồn kho
#         Vẽ dấu *
#     Nếu chọn 2:
#         Chọn mặt hàng
#         Nhập số lượng
#         Nếu số lượng âm:
#             nhập lại
#         Cộng kho
#     Nếu chọn 3:
#         Chọn mặt hàng
#         Nhập số lượng
#         Nếu số lượng âm:
#             nhập lại
#         Nếu không đủ hàng:
#             hủy giao dịch
#         Ngược lại:
#             trừ kho
#     Nếu chọn 4:
#         Kiểm tra tồn kho thấp
#     Nếu chọn 5:
#         Thoát chương trình


# (2) Triển khai code

laptop_stock = 0
phone_stock = 0
tablet_stock = 0

while True:
    print("\n===== MENU QUẢN LÝ KHO =====")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")

    choice = int(input("Nhập lựa chọn: "))
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ!")
        continue
    if choice == 1:
        print("\n===== BÁO CÁO TỒN KHO =====")
        print(f"Laptop ({laptop_stock}): ",end="")
        for i in range(laptop_stock):
            print("*", end="")
        print()

        print(f"Phone ({phone_stock}): ",end="")
        for i in range(phone_stock):
            print("*", end="")
        print()

        print(f"Tablet ({tablet_stock}): ",end="")
        for i in range(tablet_stock):
            print("*", end="")
        print()
    elif choice == 2:
        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")
        product_choice = int(input("Chọn mặt hàng: "))
        quantity = int(input("Nhập số lượng cần nhập: "))
        while quantity < 0:
            print(
                "Số lượng không hợp lệ, "
                "vui lòng nhập lại!")
            quantity = int(input("Nhập lại số lượng: "))
        if product_choice == 1:
            laptop_stock += quantity
        elif product_choice == 2:
            phone_stock += quantity
        elif product_choice == 3:
            tablet_stock += quantity
        else:
            print("Mặt hàng không hợp lệ")
    elif choice == 3:
        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")
        product_choice = int(input("Chọn mặt hàng: "))
        quantity = int(input("Nhập số lượng cần xuất: "))
        while quantity < 0:
            print(
                "Số lượng không hợp lệ, "
                "vui lòng nhập lại!"
            )
            quantity = int(input("Nhập lại số lượng: "))
        if product_choice == 1:
            if quantity > laptop_stock:
                print("Không đủ hàng")
            else:
                laptop_stock -= quantity
        elif product_choice == 2:
            if quantity > phone_stock:
                print("Không đủ hàng")
            else:
                phone_stock -= quantity
        elif product_choice == 3:
            if quantity > tablet_stock:
                print("Không đủ hàng")
            else:
                tablet_stock -= quantity
        else:
            print("Mặt hàng không hợp lệ")
    elif choice == 4:
        print("\n===== CẢNH BÁO =====")
        if laptop_stock < 10:
            print("[CẢNH BÁO] Laptop "
                f"sắp hết (Chỉ còn "
                f"{laptop_stock} sản phẩm)")

        if phone_stock < 10:
            print("[CẢNH BÁO] Phone "
                f"sắp hết (Chỉ còn "
                f"{phone_stock} sản phẩm)")

        if tablet_stock < 10:
            print("[CẢNH BÁO] Tablet "
                f"sắp hết (Chỉ còn "
                f"{tablet_stock} sản phẩm)")
    elif choice == 5:
        print("Thoát chương trình")
        break