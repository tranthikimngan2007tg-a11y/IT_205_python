# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# 1. PHÂN TÍCH INPUT / OUTPUT

# Input:
# - Mã nhân viên (string)
# - Họ và tên nhân viên (string)
# - Phòng ban công tác (string)

# Output:
# - Phiếu hồ sơ điện tử của nhân viên
# hoặc
# - Thông báo lỗi nếu dữ liệu không hợp lệ

# 2. ĐỀ XUẤT GIẢI PHÁP

# - Dùng vòng lặp for chạy đúng 3 lần
#   để nhập thông tin cho 3 nhân viên.

# - Dùng if để kiểm tra dữ liệu:
#   + Nếu mã nhân viên hoặc họ tên bị rỗng
#   + Hoặc chỉ chứa khoảng trắng
#   => Báo lỗi và không in phiếu.

# - Nếu hợp lệ:
#   => In phiếu hồ sơ điện tử.

# - Sau mỗi lượt:
#   => Tự động chuyển sang nhân viên tiếp theo.

# 3. THIẾT KẾ THUẬT TOÁN (PSEUDOCODE)

# Bắt đầu chương trình

# Lặp 3 lần:
#     Nhập mã nhân viên
#     Nhập họ tên
#     Nhập phòng ban

#     Nếu mã nhân viên rỗng
#     hoặc họ tên rỗng:
#         In lỗi
#         Chuyển sang nhân viên tiếp theo

#     Ngược lại:
#         In phiếu hồ sơ điện tử
#
# Báo hoàn thành
# Kết thúc


print("=== HỆ THỐNG KHỞI TẠO HỒ SƠ NHÂN VIÊN ===")

# Vòng lặp nhập thông tin cho 3 nhân viên
for employee_number in range(1, 4):

    print("\n--- Nhập thông tin nhân viên",
      employee_number, "---")
    employee_id = input("Nhập mã nhân viên: ")
    full_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban: ")

    if employee_id.strip() == "" or full_name.strip() == "":
        print("LỖI: Mã nhân viên hoặc Họ tên không hợp lệ!")
        continue

    print("\n===== PHIẾU HỒ SƠ ĐIỆN TỬ =====")
    print("Mã nhân viên:", employee_id)
    print("Họ và tên:", full_name)
    print("Phòng ban:", department)
    print("================================")

print("\nĐã hoàn tất nhập hồ sơ cho 3 nhân viên!")