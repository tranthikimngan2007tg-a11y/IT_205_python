# (1) Phân tích và thiết kế giải pháp

# 1. Phân tích Input / Output
# Input (Dữ liệu đầu vào)
# - registration_count:
# Số lượng phiếu đăng ký cần xử lý (kiểu int)
# - registration_data:
# Chuỗi dữ liệu đăng ký (kiểu str)
# Định dạng:
# Họ tên | Tên khóa học | Mã học viên | Email
# Output (Dữ liệu đầu ra)
# Nếu số lượng phiếu <= 0:
# "Số lượng phiếu đăng ký không hợp lệ"
# Chương trình kết thúc.
# Nếu dữ liệu hợp lệ:
# Hiển thị phiếu đã chuẩn hóa:
# ===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====
# Học viên: Nguyen Van A
# Khóa học: Python Basic
# Mã học viên: RK-001
# Email: student01@gmail.com
# Mã xác nhận: RK-001_PYTHON-BASIC
# Nếu dữ liệu không hợp lệ:
# Hiển thị thông báo lỗi
# và bỏ qua phiếu hiện tại.

# 2. Đề xuất giải pháp

# Bước 1:
# Nhập số lượng phiếu đăng ký.

# Bước 2:
# Kiểm tra edge case:
# Nếu số lượng <= 0:
# Hiển thị:
# "Số lượng phiếu đăng ký không hợp lệ"
# Kết thúc chương trình.

# Bước 3:
# Dùng vòng lặp for để xử lý từng phiếu.

# Bước 4:
# Nhập chuỗi dữ liệu đăng ký.

# Bước 5:
# Tách dữ liệu bằng dấu "|"
# dùng split("|")

# Bẫy 1:
# Nếu số phần tử khác 4:
# "Dữ liệu đăng ký không hợp lệ.
# Bỏ qua phiếu này"
# continue

# Bước 6:
# Chuẩn hóa dữ liệu:
# - Họ tên:
# strip() + title()
# - Khóa học:
# strip() + title()
# - Mã học viên:
# strip() + upper()
# - Email:
# strip() + lower()

# Bẫy 2:
# Nếu email không chứa "@":
# "Email không hợp lệ.
# Bỏ qua phiếu này"
# continue

# Bẫy 3:
# Nếu mã học viên < 5 ký tự:
# "Mã học viên không hợp lệ.
# Bỏ qua phiếu này"
# continue

# Bước 7:
# Tạo mã xác nhận:
# Mã học viên + "_" + tên khóa học
# thay khoảng trắng bằng "-"
# viết hoa toàn bộ

# Bước 8:
# In phiếu chuẩn hóa

# 3. Thiết kế thuật toán (Pseudocode)

# Bắt đầu chương trình
# Nhập số lượng phiếu đăng ký
# Nếu số lượng <= 0
#     In thông báo lỗi
#     Kết thúc
# Lặp qua từng phiếu
#     Nhập dữ liệu đăng ký
#     Tách chuỗi bằng "|"
#     Nếu không đủ 4 phần
#         Báo lỗi
#         continue
#     Chuẩn hóa dữ liệu
#     Nếu email không chứa "@"
#         Báo lỗi
#         continue
#     Nếu mã học viên quá ngắn
#         Báo lỗi
#         continue
#     Tạo mã xác nhận
#     In phiếu chuẩn hóa



# (2) Triển khai code

registration_count = int(
    input(
        "Nhập số lượng phiếu đăng ký: "
    )
)

if registration_count <= 0:
    print(
        "Số lượng phiếu đăng ký "
        "không hợp lệ"
    )
else:
    for registration in range(
        1,
        registration_count + 1
    ):
        print(
            f"\nNhập thông tin "
            f"phiếu đăng ký "
            f"{registration}:"
        )
        registration_data = input(
            "Nhập dữ liệu: "
        )
        parts = (
            registration_data
            .split("|")
        )

        if len(parts) != 4:
            print(
                "Dữ liệu đăng ký "
                "không hợp lệ. "
                "Bỏ qua phiếu này"
            )
            continue

        student_name = (
            parts[0]
            .strip()
            .title())
        course_name = (
            parts[1]
            .strip()
            .title())
        student_code = (
            parts[2]
            .strip()
            .upper())
        email = (
            parts[3]
            .strip()
            .lower())

        if "@" not in email:
            print(
                "Email không hợp lệ. "
                "Bỏ qua phiếu này")
            continue

        if len(student_code) < 5:
            print(
                "Mã học viên "
                "không hợp lệ. "
                "Bỏ qua phiếu này")
            continue

        confirm_code = (
            student_code
            + "_"
            + course_name
            .replace(" ", "-")
            .upper()
        )
        print(
            "\n===== PHIẾU ĐĂNG KÝ "
            "ĐÃ CHUẨN HÓA =====" )
        print("Học viên:",student_name)
        print("Khóa học:",course_name)
        print("Mã học viên:",student_code)
        print("Email:", email)
        print("Mã xác nhận:",confirm_code)
print("\nChương trình kết thúc")