# (1) Phân tích và thiết kế giải pháp

# 1. Phân tích Input / Output

# Input (Dữ liệu đầu vào)
# - branch_count: số lượng chi nhánh (kiểu int)
# - student_count: số học viên đi học của từng lớp (kiểu int)
# Mỗi chi nhánh có cố định 2 lớp học.
# Output (Dữ liệu đầu ra)
# - Hiển thị trạng thái lớp học ngay sau khi nhập.
# Nếu số học viên >= 20:
# "Lớp học ổn định"
# Nếu số học viên từ 1 đến 19:
# "Lớp cần được nhắc nhở theo dõi"
# Nếu số học viên = 0:
# "Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
# Nếu số học viên < 0:
# "Số học viên không hợp lệ. Vui lòng nhập lại."

# 2. Đề xuất giải pháp

# Bước 1:
# Nhập số lượng chi nhánh.

# Bước 2:
# Dùng vòng lặp for để duyệt từng chi nhánh.

# Bước 3:
# Mỗi chi nhánh có 2 lớp học,
# dùng vòng lặp for để duyệt từ lớp 1 đến lớp 2.

# Bước 4:
# Nhập số học viên đi học.
# Kiểm tra dữ liệu hợp lệ:

# Bẫy 1:
# Nếu student_count < 0:
# Hiển thị:
# "Số học viên không hợp lệ. Vui lòng nhập lại."
# Sau đó nhập lại bằng while.

# Bẫy 2:
# Nếu student_count == 0:
# Hiển thị:
# "Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
# Dùng continue để bỏ qua đánh giá lớp đó.

# Bước 5:
# Đánh giá trạng thái lớp:
# Nếu student_count >= 20:
# "Lớp học ổn định"
# Ngược lại:
# "Lớp cần được nhắc nhở theo dõi"


# 3. Thiết kế thuật toán (Pseudocode)

# Bắt đầu chương trình
# Nhập số lượng chi nhánh
# Lặp qua từng chi nhánh
#     In tên chi nhánh
#     Lặp từ lớp 1 đến lớp 2
#         Nhập số học viên
#         Nếu số học viên < 0:
#             In thông báo lỗi
#             Nhập lại
#         Nếu số học viên = 0:
#             In thông báo lớp vắng
#             Bỏ qua kiểm tra trạng thái
#         Nếu số học viên >= 20:
#             In lớp học ổn định
#         Ngược lại:
#             In lớp cần nhắc nhở theo dõi


# (2) Triển khai code

branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}:")

    for classroom in range(1, 3):
        student_count = int(
            input(
                f"Nhập số học viên đi học của lớp "
                f"{classroom}: "
            )
        )

        while student_count < 0:
            print(
                "Số học viên không hợp lệ. "
                "Vui lòng nhập lại."
            )

            student_count = int(
                input(
                    f"Nhập lại số học viên lớp "
                    f"{classroom}: "
                )
            )

        if student_count == 0:
            print(
                "Lớp vắng toàn bộ. "
                "Bỏ qua kiểm tra trạng thái."
            )
            continue

        if student_count >= 20:
            print(
                f"Chi nhánh {branch} - "
                f"Lớp {classroom}: "
                f"Lớp học ổn định"
            )
        else:
            print(
                f"Chi nhánh {branch} - "
                f"Lớp {classroom}: "
                f"Lớp cần được nhắc nhở theo dõi"
            )

print("\nChương trình kết thúc")