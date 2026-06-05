# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

# 1. Phân tích thiết kế hàm

# Tên hàm: calculate_average(student)
# Input:
# - student (dictionary): thông tin một sinh viên
# Output:
# - Trả về điểm trung bình (float)
# Pseudocode:
# - Lấy điểm Toán, Lý, Hóa
# - Tính trung bình cộng
# - Return kết quả


# Tên hàm: get_rank(average_score)
# Input:
# - average_score (float)
# Output:
# - Trả về xếp loại học lực (str)
# Pseudocode:
# - Nếu ĐTB >= 8.0 -> Giỏi
# - Nếu ĐTB >= 6.5 -> Khá
# - Nếu ĐTB >= 5.0 -> Trung bình
# - Ngược lại -> Yếu


# Tên hàm: display_grades(records)
# Input:
# - records (list): danh sách sinh viên
# Output:
# - In bảng điểm và học lực
# Pseudocode:
# - Kiểm tra danh sách rỗng
# - Nếu rỗng -> thông báo
# - Duyệt danh sách sinh viên
# - Tính ĐTB
# - Xếp loại
# - In kết quả


# Tên hàm: find_student_by_id(records, student_id)
# Input:
# - records (list)
# - student_id (str)
# Output:
# - Trả về dictionary sinh viên
# - Hoặc None nếu không tìm thấy
# Pseudocode:
# - Duyệt danh sách
# - So sánh mã sinh viên
# - Nếu tìm thấy -> return sinh viên
# - Không thấy -> return None


# Tên hàm: validate_score(score_input)
# Input:
# - score_input (str)
# Output:
# - True nếu hợp lệ
# - False nếu không hợp lệ
# Pseudocode:
# - Kiểm tra có nhiều dấu "." không
# - Xóa dấu "." để kiểm tra digit
# - Ép float
# - Kiểm tra khoảng từ 0 đến 10


# Tên hàm: update_student_score(records)
# Input:
# - records (list)
# Output:
# - Cập nhật điểm hoặc báo lỗi
# Pseudocode:
# - Nhập mã sinh viên
# - Chuẩn hóa mã
# - Tìm sinh viên
# - Nếu không có -> báo lỗi
# - Chọn môn học
# - Nhập điểm mới
# - Kiểm tra điểm hợp lệ
# - Cập nhật điểm


# Tên hàm: generate_report(records)
# Input:
# - records (list)
# Output:
# - In thống kê Đỗ / Trượt
# Pseudocode:
# - Kiểm tra danh sách rỗng
# - Đếm số sinh viên đỗ
# - Đếm số sinh viên trượt
# - Tính tỷ lệ %
# - In báo cáo


# Tên hàm: find_valedictorian(records)
# Input:
# - records (list)
# Output:
# - In thông tin thủ khoa
# Pseudocode:
# - Kiểm tra danh sách rỗng
# - Tìm sinh viên có ĐTB cao nhất
# - In kết quả


# 2. Đề xuất giải pháp

# - Dùng list chứa dictionary để lưu dữ liệu sinh viên
# - Chia nghiệp vụ thành nhiều function riêng biệt
# - Sử dụng helper function để tránh lặp code
# - Dùng while True để hiển thị menu
# - Xử lý edge cases:
#   + Mã sinh viên không tồn tại
#   + Điểm không hợp lệ
#   + Danh sách rỗng
#   + Nhập sai menu


# (2) TRIỂN KHAI CODE

student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


# Tính điểm trung bình
def calculate_average(student):

    average_score = (
        student["math"]
        + student["physics"]
        + student["chemistry"]
    ) / 3

    return average_score


# Xếp loại học lực
def get_rank(average_score):

    if average_score >= 8:
        return "Giỏi"

    elif average_score >= 6.5:
        return "Khá"

    elif average_score >= 5:
        return "Trung bình"

    return "Yếu"


# Tìm sinh viên theo mã
def find_student_by_id(records, student_id):

    for student in records:
        if student["student_id"] == student_id:
            return student

    return None


# Kiểm tra điểm hợp lệ
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


# Hiển thị bảng điểm
def display_grades(records):

    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):

        average_score = calculate_average(student)

        rank = get_rank(average_score)

        print(
            f"{index}. "
            f"[{student['student_id']}] "
            f"{student['name']} | "
            f"Toán: {student['math']} | "
            f"Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | "
            f"ĐTB: {average_score:.2f} - "
            f"{rank}"
        )

    print("---------------------------")


# Cập nhật điểm sinh viên
def update_student_score(records):

    student_id = input(
        "Nhập mã sinh viên cần cập nhật: "
    ).strip().upper()

    found_student = find_student_by_id(
        records,
        student_id
    )

    if found_student is None:
        print(
            f"Không tìm thấy sinh viên "
            f"mang mã {student_id} "
            f"trong hệ thống!"
        )
        return

    print("1. Toán")
    print("2. Lý")
    print("3. Hóa")

    subject_choice = input(
        "Chọn môn học (1-3): "
    ).strip()

    subject = ""

    match subject_choice:
        case "1":
            subject = "math"
            subject_name = "Toán"

        case "2":
            subject = "physics"
            subject_name = "Lý"

        case "3":
            subject = "chemistry"
            subject_name = "Hóa"

        case _:
            print("Lựa chọn môn học không hợp lệ!")
            return

    while True:

        new_score = input(
            "Nhập điểm mới: "
        ).strip()

        if validate_score(new_score):
            new_score = float(new_score)
            break

        print(
            "Điểm số không hợp lệ. "
            "Vui lòng nhập từ 0 đến 10!"
        )

    found_student[subject] = new_score

    print(
        f">> Đã cập nhật điểm "
        f"{subject_name} của sinh viên "
        f"'{found_student['name']}' "
        f"thành {new_score}."
    )


# Báo cáo thống kê
def generate_report(records):

    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)

    passed_students = 0
    failed_students = 0

    for student in records:

        average_score = calculate_average(student)

        if average_score >= 5:
            passed_students += 1
        else:
            failed_students += 1

    pass_percent = (
        passed_students / total_students
    ) * 100

    fail_percent = (
        failed_students / total_students
    ) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(
        f"Tổng số sinh viên: "
        f"{total_students}"
    )

    print(
        f"Số lượng qua môn "
        f"(ĐTB >= 5.0): "
        f"{passed_students} sinh viên "
        f"(Chiếm {pass_percent:.2f}%)"
    )

    print(
        f"Số lượng trượt "
        f"(ĐTB < 5.0): "
        f"{failed_students} sinh viên "
        f"(Chiếm {fail_percent:.2f}%)"
    )

    print("----------------------")


# Tìm thủ khoa
def find_valedictorian(records):

    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = records[0]
    highest_average = calculate_average(
        top_student
    )

    for student in records:

        average_score = calculate_average(
            student
        )

        if average_score > highest_average:
            highest_average = average_score
            top_student = student

    print("\n--- VINH DANH THỦ KHOA ---")

    print(
        f" Sinh viên: "
        f"{top_student['name']} "
        f"(Mã: "
        f"{top_student['student_id']})"
    )

    print(
        f" Điểm Trung Bình: "
        f"{highest_average:.2f}"
    )

    print(
        "Chúc mừng sinh viên "
        "đã đạt thành tích "
        "xuất sắc nhất khóa!"
    )

    print("--------------------------")


# Hàm main
def main():

    while True:

        print(
            "\n===== HỆ THỐNG QUẢN LÝ "
            "ĐIỂM THI RIKKEI UNIVERSITY ====="
        )

        print("1. Xem bảng điểm và học lực")
        print("2. Cập nhật điểm thi sinh viên")
        print("3. Báo cáo thống kê (Đỗ/Trượt)")
        print("4. Tìm sinh viên Thủ khoa")
        print("5. Thoát chương trình")
        print("=" * 54)

        choice = input(
            "Chọn chức năng (1-5): "
        ).strip()

        match choice:

            case "1":
                display_grades(
                    student_records
                )

            case "2":
                update_student_score(
                    student_records
                )

            case "3":
                generate_report(
                    student_records
                )

            case "4":
                find_valedictorian(
                    student_records
                )

            case "5":
                print(
                    "Cảm ơn bạn đã sử dụng hệ thống!"
                )
                break

            case _:
                print(
                    "Lựa chọn không hợp lệ!"
                )

main()