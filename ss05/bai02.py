branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

total_students = 0

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}")

    for classroom in range(1, class_count + 1):
        student_count = int(
            input(f"Nhập số học viên lớp {classroom}: ")
        )

        total_students += student_count

    print(f"Chi nhánh {branch}: {total_students} học viên")


# Phân tích lỗi

# 1
# Vì sao Chi nhánh 1 hiển thị đúng là 83 học viên?
# Vì ban đầu biến total_students = 0.
# Khi nhập dữ liệu của Chi nhánh 1, hệ thống cộng dồn:
# 25 + 28 + 30 = 83
# nên kết quả hiển thị đúng là 83 học viên.

# 2
# Vì sao Chi nhánh 2 đúng là 60 nhưng hệ thống lại hiển thị 143 học viên?
# Nguyên nhân là biến total_students không được reset về 0.
# Sau Chi nhánh 1, total_students đang là 83.
# Khi sang Chi nhánh 2:
# 83 + 60 = 143
# nên hệ thống hiển thị sai thành 143 học viên.

# 3
# Vì sao Chi nhánh 3 đúng là 97 nhưng hệ thống lại hiển thị 240 học viên?
# Vì biến total_students vẫn tiếp tục cộng dồn.
# Sau Chi nhánh 2, total_students = 143.
# Khi nhập Chi nhánh 3:
# 143 + 97 = 240
# nên hệ thống hiển thị sai thành 240 học viên.

# Sửa

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
    total_students = 0
    
    print(f"\nChi nhánh {branch}")

    for classroom in range(1, class_count + 1):
        student_count = int(
            input(f"Nhập số học viên lớp {classroom}: ")
        )

        total_students += student_count

    print(
        f"Chi nhánh {branch}: "
        f"{total_students} học viên"
    )