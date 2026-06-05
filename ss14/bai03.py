# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

# 1. Phân tích Input / Output

# Input:
# - Người dùng nhập lựa chọn menu (1 - 5)
# - Người dùng nhập:
#   + Mã học viên (str)
#   + Tên học viên (str)
#   + Điểm Toán (float)
#   + Điểm Tiếng Anh (float)

# Output:
# - Hiển thị danh sách học viên
# - Thêm học viên mới thành công hoặc báo lỗi
# - Cập nhật điểm học viên thành công hoặc báo lỗi
# - Hiển thị đánh giá học lực học viên
# - Thông báo thoát chương trình

# Phân tích Input / Output cho từng hàm

# validate_score(score_input)
# Input:
# - score_input (str)
# Output:
# - True nếu điểm hợp lệ
# - False nếu điểm không hợp lệ

# find_student_by_id(student_list, student_id)
# Input:
# - student_list (list)
# - student_id (str)
# Output:
# - Trả về dictionary học viên nếu tìm thấy
# - Trả về None nếu không tìm thấy

# display_students(student_list)
# Input:
# - student_list (list)
# Output:
# - In danh sách học viên

# add_student(student_list)
# Input:
# - student_list (list)
# Output:
# - Thêm học viên hoặc báo lỗi

# update_score(student_list)
# Input:
# - student_list (list)
# Output:
# - Cập nhật điểm hoặc báo lỗi

# get_rank(average_score)
# Input:
# - average_score (float)
# Output:
# - Trả về chuỗi xếp loại

# evaluate_students(student_list)
# Input:
# - student_list (list)
# Output:
# - In danh sách học viên kèm xếp loại


# 2. Đề xuất giải pháp

# - Sử dụng list để lưu danh sách học viên
# - Mỗi học viên được lưu bằng dictionary:
#   + student_id
#   + name
#   + math_score
#   + english_score

# - Sử dụng while True để hiển thị menu liên tục

# - Chia chương trình thành nhiều hàm:
#   + display_students()
#   + add_student()
#   + update_score()
#   + evaluate_students()

# - Dùng helper function:
#   + validate_score() kiểm tra điểm hợp lệ
#   + find_student_by_id() tìm học viên theo mã
#   + get_rank() xếp loại học lực

# - Lợi ích:
#   + Code dễ đọc
#   + Dễ sửa lỗi
#   + Dễ nâng cấp
#   + Tránh spaghetti code

# - Xử lý edge cases:
#   + Trùng mã học viên
#   + Điểm không hợp lệ
#   + Nhập sai menu
#   + Tên học viên rỗng


# 3. Thiết kế thuật toán (Pseudocode)

# B1: Khởi tạo danh sách học viên

# B2: Hiển thị menu bằng while True

# B3: Người dùng nhập lựa chọn

# Nếu chọn 1:
#     Hiển thị danh sách học viên

# Nếu chọn 2:
#     Nhập mã học viên
#     Chuẩn hóa mã
#     Kiểm tra trùng mã
#     Nhập tên
#     Kiểm tra tên hợp lệ
#     Nhập điểm Toán
#     Kiểm tra điểm hợp lệ
#     Nhập điểm Anh
#     Kiểm tra điểm hợp lệ
#     Thêm học viên

# Nếu chọn 3:
#     Nhập mã học viên
#     Tìm học viên
#     Nếu tìm thấy:
#         Nhập điểm mới
#         Cập nhật điểm
#     Nếu không tìm thấy:
#         Báo lỗi

# Nếu chọn 4:
#     Duyệt danh sách học viên
#     Tính điểm trung bình
#     Xếp loại
#     Hiển thị kết quả

# Nếu chọn 5:
#     Thoát chương trình

# Ngược lại:
#     Báo lựa chọn không hợp lệ

# (2) TRIỂN KHAI CODE

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def validate_score(score_input):

    if score_input.count(".") > 1:
        return False

    temp_score = score_input.replace(".", "")

    if not temp_score.isdigit():
        return False

    score = float(score_input)

    if 0 <= score <= 10:
        return True

    return False

def find_student_by_id(student_list, student_id):

    for student in student_list:
        if student["student_id"] == student_id:
            return student

    return None

def display_students(student_list):

    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
    else:
        print("\nDanh sách học viên hiện tại:")

        for index, student in enumerate(student_list, start=1):
            print(
                f"{index}. "
                f"Mã: {student['student_id']} | "
                f"Tên: {student['name']} | "
                f"Toán: {student['math_score']} | "
                f"Anh: {student['english_score']}"
            )

def add_student(student_list):

    student_id = input(
        "Nhập mã học viên: "
    ).strip().upper()

    found_student = find_student_by_id(
        student_list,
        student_id
    )

    if found_student is not None:
        print(
            "Mã học viên đã tồn tại, "
            "vui lòng nhập mã khác!"
        )
        return

    while True:

        name = input(
            "Nhập tên học viên: "
        ).strip()

        if name == "":
            print(
                "Tên học viên "
                "không được để trống!"
            )
            continue

        name = name.title()
        break

    while True:

        math_score = input(
            "Nhập điểm Toán: "
        ).strip()

        if validate_score(math_score):
            math_score = float(math_score)
            break

        print(
            "Điểm không hợp lệ, "
            "phải là số từ 0 đến 10"
        )

    while True:

        english_score = input(
            "Nhập điểm Anh: "
        ).strip()

        if validate_score(english_score):
            english_score = float(
                english_score
            )
            break

        print(
            "Điểm không hợp lệ, "
            "phải là số từ 0 đến 10"
        )

    new_student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }

    student_list.append(new_student)

    print("Thêm học viên thành công!")

def update_score(student_list):

    student_id = input(
        "Nhập mã học viên cần cập nhật: "
    ).strip().upper()

    found_student = find_student_by_id(
        student_list,
        student_id
    )

    if found_student is None:
        print(
            f"Không tìm thấy học viên "
            f"mang mã {student_id}!"
        )
        return

    while True:

        math_score = input(
            "Nhập điểm Toán mới: "
        ).strip()

        if validate_score(math_score):
            math_score = float(math_score)
            break

        print(
            "Điểm không hợp lệ, "
            "phải là số từ 0 đến 10"
        )

    while True:
        english_score = input(
            "Nhập điểm Anh mới: "
        ).strip()

        if validate_score(english_score):
            english_score = float(
                english_score
            )
            break

        print(
            "Điểm không hợp lệ, "
            "phải là số từ 0 đến 10"
        )

    found_student["math_score"] = math_score
    found_student["english_score"] = english_score

    print("Cập nhật điểm thành công!")

def get_rank(average_score):

    if average_score >= 8:
        return "Giỏi"

    elif average_score >= 6.5:
        return "Khá"

    elif average_score >= 5:
        return "Trung bình"

    return "Yếu"

def evaluate_students(student_list):

    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
    else:
        print("\nĐánh giá học lực học viên:")

        for student in student_list:

            average_score = (
                student["math_score"]
                + student["english_score"]
            ) / 2

            rank = get_rank(
                average_score
            )

            print(
                f"Mã: {student['student_id']} | "
                f"Tên: {student['name']} | "
                f"ĐTB: {average_score:.2f} | "
                f"Xếp loại: {rank}"
            )


while True:

    print(
        "\n===== HỆ THỐNG QUẢN LÝ "
        "ĐIỂM THI RIKKEI ACADEMY ====="
    )

    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    match choice:

        case "1":
            display_students(students)
        case "2":
            add_student(students)
        case "3":
            update_score(students)
        case "4":
            evaluate_students(students)
        case "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break

        case _:
            print("Lựa chọn không hợp lệ, "
                "vui lòng nhập lại!")