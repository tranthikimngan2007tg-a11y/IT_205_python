# (1) Phân tích và thiết kế giải pháp

# 1. Phân tích Input / Output

# Input (Dữ liệu đầu vào)
# - choice: lựa chọn menu của người dùng (kiểu int)
# - branch_count: số lượng chi nhánh (kiểu int)
# - class_count: số lớp học của từng chi nhánh (kiểu int)
# - student_count: số học viên của từng lớp (kiểu int)
# Output (Dữ liệu đầu ra)

# Chức năng 1:
# - Hiển thị tổng số học viên từng chi nhánh
# - Hiển thị chi nhánh có tổng số học viên cao nhất
# - Hiển thị danh sách lớp có sĩ số dưới 10 học viên
# - Nếu không có lớp nào dưới 10 học viên:
#   "Không có lớp nào dưới 10 học viên"

# Chức năng 2:
# - Hiển thị hướng dẫn sử dụng hệ thống
# Chức năng 3:
# - Hiển thị:
#   "Thoát chương trình"
# - Kết thúc chương trình

# 2. Đề xuất giải pháp

# Bước 1:
# Tạo menu gồm:
# 1. Nhập dữ liệu và xem báo cáo
# 2. Hướng dẫn sử dụng
# 3. Thoát chương trình

# Bước 2:
# Dùng vòng lặp while True để menu chạy liên tục
# cho đến khi người dùng chọn thoát.

# Bước 3:
# Kiểm tra lựa chọn menu.

# Bẫy 2:
# Nếu nhập menu không hợp lệ
# (không nằm trong khoảng từ 1 đến 5):
# Hiển thị thông báo lỗi
# và yêu cầu nhập lại.

# Bước 4:
# Nếu chọn chức năng 1:
# - Nhập số lượng chi nhánh
# - Duyệt từng chi nhánh bằng for
# - Nhập số lớp học
# - Duyệt từng lớp

# Bẫy 1:
# Nếu student_count < 0:
# Hiển thị:
# "Số học viên không hợp lệ. Vui lòng nhập lại"
# Sau đó nhập lại bằng while.

# Bước 5:
# Trong lúc nhập:
# - Tính tổng số học viên từng chi nhánh
# - Tìm chi nhánh có tổng cao nhất
# - Kiểm tra lớp dưới 10 học viên

# Bẫy 3:
# Nếu không có lớp nào dưới 10:
# Hiển thị:
# "Không có lớp nào dưới 10 học viên"

# Bước 6:
# Nếu chọn chức năng 2:
# Hiển thị hướng dẫn sử dụng.

# Bước 7:
# Nếu chọn chức năng 3:
# Hiển thị:
# "Thoát chương trình"
# rồi dùng break kết thúc.

# 3. Thiết kế thuật toán (Pseudocode)

# Bắt đầu chương trình
# Lặp menu
#     Hiển thị menu
#     Nhập lựa chọn
#     Nếu menu không hợp lệ
#         Báo lỗi
#         Quay lại menu
#     Nếu chọn 1:
#         Nhập số lượng chi nhánh
#         Tạo biến lưu:
#         - chi nhánh cao nhất
#         - tổng học viên lớn nhất
#         - danh sách lớp dưới 10
#         Lặp từng chi nhánh
#             Nhập số lớp học
#             total_students = 0
#             Lặp từng lớp
#                 Nhập số học viên
#                 Nếu số học viên âm:
#                     nhập lại
#                 Cộng tổng
#                 Nếu lớp < 10:
#                     lưu danh sách
#             In tổng chi nhánh
#             Kiểm tra chi nhánh cao nhất
#         Nếu không có lớp dưới 10:
#             In thông báo
#         Ngược lại:
#             In danh sách lớp dưới 10
#     Nếu chọn 2:
#         In hướng dẫn
#     Nếu chọn 3:
#         Thoát chương trình



# (2) Triển khai code

while True:

    print("\n===== MENU =====")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Hiển thị hướng dẫn sử dụng")
    print("3. Thoát chương trình")

    choice = int(input("Nhập lựa chọn: "))
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
        continue
    if choice == 1:
        branch_count = int(
            input("Nhập số lượng chi nhánh: ")
        )
        highest_branch = 0
        highest_total = 0
        low_class_list = []
        for branch in range(1, branch_count + 1):

            class_count = int(
                input(
                    f"\nNhập số lớp của "
                    f"chi nhánh {branch}: "
                )
            )
            total_students = 0
            for classroom in range(
                1, class_count + 1
            ):
                student_count = int(
                    input(
                        f"Nhập số học viên "
                        f"lớp {classroom}: "
                    )
                )

                while student_count < 0:
                    print(
                        "Số học viên không "
                        "hợp lệ. Vui lòng nhập lại"
                    )
                    student_count = int(
                        input(
                            f"Nhập lại số học viên "
                            f"lớp {classroom}: "
                        )
                    )
                total_students += student_count
                if student_count < 10:
                    low_class_list.append(
                        (
                            branch,
                            classroom,
                            student_count
                        )
                    )

            print(
                f"Chi nhánh {branch} có "
                f"{total_students} học viên"
            )

            # Tìm chi nhánh lớn nhất
            if total_students > highest_total:
                highest_total = total_students
                highest_branch = branch

        print(
            f"\nChi nhánh có tổng học viên "
            f"cao nhất là "
            f"Chi nhánh {highest_branch} "
            f"({highest_total} học viên)"
        )

        if len(low_class_list) == 0:
            print(
                "Không có lớp nào "
                "dưới 10 học viên"
            )
        else:
            print(
                "\nDanh sách lớp dưới "
                "10 học viên:"
            )
            for item in low_class_list:
                branch = item[0]
                classroom = item[1]
                student_count = item[2]

                print(
                    f"Chi nhánh {branch} - "
                    f"Lớp {classroom}: "
                    f"{student_count} học viên"
                )

    elif choice == 2:
        print("\n===== HƯỚNG DẪN =====")
        print("- Chọn chức năng 1 để nhập dữ liệu.")
        print(
            "- Nhập số lượng chi nhánh, "
            "số lớp và số học viên."
        )
        print(
            "- Hệ thống sẽ thống kê "
            "tự động."
        )
        print(
            "- Các lớp dưới 10 học viên "
            "sẽ được hiển thị."
        )

    elif choice == 3:
        print("Thoát chương trình")
        break