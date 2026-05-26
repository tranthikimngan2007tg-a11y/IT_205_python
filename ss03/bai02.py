print("=== HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ===")

for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số",
          employee_number, "---")
    working_days = int(input("Nhập số ngày công trong tháng: "))

    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
    bonus_amount = working_days * 200000

    # Gửi email thưởng
    print("→ Đã gửi Email: Chúc mừng nhận được",
          bonus_amount, "VND tiền thưởng!")

    print("----------------------------------\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")

# Phân tích lỗi

# 1 Dò luồng thực thi của chương trình khi working_days = 0
# Khi nhập số ngày công = 0,
# chương trình in ra cảnh báo nhân viên nghỉ cả tháng.
# Nhưng sau đó chương trình vẫn chạy tiếp xuống dưới
# để tính tiền thưởng và gửi email.

# 2 Tại sao hệ thống vẫn tính thưởng và gửi email?
# Vì sau câu lệnh if không có else hoặc continue.
# Nên chương trình không dừng lại
# mà tiếp tục chạy các dòng code phía dưới.

# 3 Vấn đề liên quan đến cấu trúc điều kiện trong vòng lặp
# Điều kiện if chỉ dùng để in cảnh báo.
# Không có lệnh bỏ qua vòng lặp hiện tại.
# Vì vậy chương trình vẫn tính thưởng
# dù nhân viên không đủ điều kiện.

# Sửa

print("=== HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ===")

for employee_number in range(1, 4):
    print("\n--- Đang xử lý nhân viên số",
          employee_number, "---")
    working_days = int(input("Nhập số ngày công trong tháng: "))
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        continue
    bonus_amount = working_days * 200000
    print("→ Đã gửi Email: Chúc mừng nhận được",
          bonus_amount, "VND tiền thưởng!")

print("\nĐã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")