# HỆ THỐNG NHẬP SỐ LƯỢNG NHÂN SỰ MỚI
# TechCorp - Bộ phận HR
# (1) PHÂN TÍCH & ĐỀ XUẤT GIẢI PHÁP

# 1. PHÂN TÍCH INPUT / OUTPUT

# Input:
# - Số lượng nhân sự mới
# - Kiểu dữ liệu: số nguyên (int)

# Điều kiện hợp lệ:
# - Phải là số nguyên > 0

# Output:
# - Nếu nhập sai (<=0):
#   Báo lỗi và yêu cầu nhập lại
#
# - Nếu nhập đúng (>0):
#   In thông báo ghi nhận thành công


# 2. ĐỀ XUẤT 2 GIẢI PHÁP

# Giải pháp 1: Dùng while True
#
# - Chạy vòng lặp vô hạn
# - Nếu nhập đúng thì dùng break để thoát

# Giải pháp 2: Dùng biến điều kiện
#
# Ví dụ:
# is_valid = False
#
# while is_valid == False:
#     nhập dữ liệu
#     nếu đúng:
#         is_valid = True

# 3. SO SÁNH HAI GIẢI PHÁP

# Độ ngắn gọn:
# while True -> ngắn hơn
# biến điều kiện -> dài hơn

# Dễ hiểu:
# biến điều kiện -> dễ hiểu hơn
# while True -> cần hiểu break

# 4. CHỐT GIẢI PHÁP

# Chọn giải pháp 1: while True
#
# Lý do:
# - Code ngắn gọn
# - Dễ xử lý validation loop
# - Thường dùng trong nhập liệu

print("=== HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ===")

while True:
    employee_quantity = int(
        input("Vui lòng nhập số lượng nhân sự mới trong tháng này: ")
    )
    if employee_quantity <= 0:
        print("LỖI: Số lượng phải lớn hơn 0. Vui lòng nhập lại!")
    else:
        print("Ghi nhận thành công!")
        print("Số lượng nhân sự mới:", employee_quantity)
        break