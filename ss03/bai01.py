print("=== PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ===")

for employee_number in range(1, 4):
    total_budget = 0
    print("Đang xử lý nhân viên số", employee_number)
    salary = int(input("Nhập mức lương (VND): "))
    total_budget = total_budget + salary
print("KẾT QUẢ:", total_budget, "VND")

# Phân tích lỗi

# 1 Dò luồng thực thi của chương trình
# Chương trình chạy vòng lặp 3 lần để nhập lương.
# Nhưng mỗi lần lặp biến total_budget lại được gán = 0
# rồi mới cộng lương vừa nhập.

# 2 Tại sao total_budget không cộng dồn được?
# Vì total_budget = 0 được đặt trong vòng lặp for.
# Nên sau mỗi lần lặp biến sẽ bị reset về 0.
# Kết quả là chỉ giữ lại giá trị của lần nhập cuối cùng.

# 3 Lỗi logic kinh điển
# Lỗi đặt biến cộng dồn sai vị trí.
# Biến total_budget phải đặt ngoài vòng lặp
# để giữ tổng cũ và cộng dồn tiếp.

# Sửa

print("=== PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ===")

# Đúng: đặt ngoài vòng lặp để cộng dồn
total_budget = 0

for employee_number in range(1, 4):

    print("Đang xử lý nhân viên số", employee_number)

    salary = int(input("Nhập mức lương (VND): "))

    # Cộng dồn lương
    total_budget = total_budget + salary

print("KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:",
      total_budget, "VND")