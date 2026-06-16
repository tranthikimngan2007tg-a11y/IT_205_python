"""
=========================================================
PHẦN 1: PHÂN TÍCH THIẾT KẾ MODULE & HÀM
=========================================================

1. CẤU TRÚC THƯ MỤC DỰ ÁN

rikkei_learning_tools/
│── main.py
│
├── data/
│   └── students.py
│
├── utils/
│   ├── __init__.py
│   ├── score_utils.py
│   ├── string_utils.py
│   └── random_utils.py
│
└── reports/
    ├── __init__.py
    └── report_generator.py


2. PHÂN TÍCH MODULE

-----------------------------------------
Module: data/students.py
-----------------------------------------
Vai trò:
- Chứa dữ liệu sinh viên ban đầu.

Hàm chính:
- Không có hàm.

Kiểu import:
    from data.students import student_records


-----------------------------------------
Module: utils/score_utils.py
-----------------------------------------
Vai trò:
- Xử lý tính điểm trung bình
- Phân loại học lực

Hàm chính:
- calculate_average(scores)
- classify_student(average)

Kiểu import:
    from utils.score_utils
    import calculate_average


-----------------------------------------
Module: utils/string_utils.py
-----------------------------------------
Vai trò:
- Chuẩn hóa tên sinh viên

Hàm chính:
- normalize_student_names(records)

Kiểu import:
    import utils.string_utils
    as string_utils


-----------------------------------------
Module: utils/random_utils.py
-----------------------------------------
Vai trò:
- Sinh mã bài tập ngẫu nhiên

Hàm chính:
- generate_assignment_code()

Module chuẩn dùng:
- random
- string

Kiểu import:
    import random
    import string


-----------------------------------------
Module: reports/report_generator.py
-----------------------------------------
Vai trò:
- Hiển thị điểm sinh viên
- Xuất báo cáo học tập

Hàm chính:
- display_student_scores(records)
- export_learning_report(records)

Module chuẩn dùng:
- datetime

Third-party:
- colorama


-----------------------------------------
Module: main.py
-----------------------------------------
Vai trò:
- Điều hướng menu
- Gọi các module

Bắt buộc:
- while True
- try-except xử lý lỗi menu


3. PHÂN TÍCH HÀM

-----------------------------------------
Tên hàm:
calculate_average(scores)

Input:
scores (list)

Output:
float

Module:
utils/score_utils.py

Luồng xử lý:
- Nếu danh sách rỗng -> return 0
- Duyệt từng điểm
- Chỉ lấy dữ liệu kiểu số
- Tính trung bình
- Nếu không có điểm hợp lệ -> return 0


-----------------------------------------
Tên hàm:
classify_student(average)

Input:
average (float)

Output:
str

Module:
utils/score_utils.py

Luồng xử lý:
- average >= 8 -> Giỏi
- average >= 6.5 -> Khá
- average >= 5 -> Trung bình
- còn lại -> Yếu


-----------------------------------------
Tên hàm:
display_student_scores(records)

Input:
records (list)

Output:
None

Module:
reports/report_generator.py

Luồng xử lý:
- Kiểm tra dữ liệu rỗng
- Gọi calculate_average()
- Gọi classify_student()
- In danh sách sinh viên


-----------------------------------------
Tên hàm:
normalize_student_names(records)

Input:
records (list)

Output:
None

Module:
utils/string_utils.py

Luồng xử lý:
- Xóa khoảng trắng dư
- Gộp khoảng trắng
- Viết hoa chữ cái đầu


-----------------------------------------
Tên hàm:
generate_assignment_code()

Input:
Không có

Output:
str

Module:
utils/random_utils.py

Luồng xử lý:
- Random 4 ký tự
- Dùng chữ hoa + số
- Ghép theo format:
    PY-XXXX


-----------------------------------------
Tên hàm:
export_learning_report(records)

Input:
records (list)

Output:
txt file

Module:
reports/report_generator.py

Luồng xử lý:
- Đếm tổng sinh viên
- Đếm đạt yêu cầu
- Đếm cần cải thiện
- Ghi file txt
- Dùng datetime ghi thời gian
- Dùng colorama in màu


-----------------------------------------
Tên hàm:
main()

Input:
Không có

Output:
None

Module:
main.py

Luồng xử lý:
- while True
- Hiển thị menu
- try-except lỗi nhập
- Điều hướng chức năng
- Thoát khi chọn 5

=========================================================
"""

import utils.string_utils as string_utils

from data.students import (
    student_records
)

from reports.report_generator import (
    display_student_scores,
    export_learning_report
)

from utils.random_utils import (
    generate_assignment_code
)


def show_menu():

    print(
        "\n===== HỆ THỐNG "
        "TIỆN ÍCH HỌC TẬP "
        "RIKKEI ACADEMY ====="
    )

    print(
        "1. Xem danh sách "
        "sinh viên và "
        "điểm trung bình"
    )

    print(
        "2. Chuẩn hóa "
        "tên sinh viên"
    )

    print(
        "3. Sinh mã "
        "bài tập "
        "ngẫu nhiên"
    )

    print(
        "4. Xuất báo "
        "cáo học tập"
    )

    print(
        "5. Thoát "
        "chương trình"
    )

    print("=" * 50)


def main():

    while True:

        show_menu()

        try:

            choice = int(
                input(
                    "Chọn chức năng "
                    "(1-5): "
                )
            )

            if choice == 1:

                display_student_scores(
                    student_records
                )

            elif choice == 2:

                string_utils.normalize_student_names(
                    student_records
                )

            elif choice == 3:

                generate_assignment_code()

            elif choice == 4:

                export_learning_report(
                    student_records
                )

            elif choice == 5:

                print(
                    "Cảm ơn bạn "
                    "đã sử dụng "
                    "hệ thống!"
                )

                break

            else:
                print(
                    "Chức năng "
                    "không hợp lệ. "
                    "Vui lòng "
                    "chọn từ "
                    "1 đến 5."
                )

        except ValueError:

            print(
                "Chức năng "
                "không hợp lệ. "
                "Vui lòng "
                "chọn từ "
                "1 đến 5."
            )


if __name__ == "__main__":
    main()