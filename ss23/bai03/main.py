"""
=========================================================
PHẦN 1: PHÂN TÍCH GIẢI PHÁP & KIẾN TRÚC HỆ THỐNG
=========================================================

1. Vì sao không nên dùng 'from math import *'?

Đây là một Anti-pattern (thực hành xấu)
trong Python vì:

- Gây ô nhiễm namespace:
  Toàn bộ hàm trong thư viện math sẽ
  được import vào chương trình.

Ví dụ:
    ceil()
    floor()
    sqrt()

=> Khó kiểm soát nguồn gốc hàm.

- Dễ gây xung đột tên:
  Nếu lập trình viên tự viết hàm trùng tên,
  chương trình có thể bị ghi đè hoặc lỗi logic.

Ví dụ:

    from math import *

    def ceil(number):
        return "Lỗi"

=> Hàm ceil() của math có thể bị ảnh hưởng.

- Khó đọc và bảo trì:
  Người đọc không biết hàm đến từ đâu.

Ví dụ:
    result = ceil(12.5)

Không rõ đây là hàm tự viết
hay thuộc thư viện math.

=> Cách import tốt hơn:

Cách 1:
    import math

    result = math.ceil(12.5)

Cách 2:
    from math import ceil

    result = ceil(12.5)


2. Cấu trúc thư mục sau khi tái cấu trúc

rikkei_aviation/
│── main.py
│── README.md
│
├── core/
│   ├── __init__.py
│   ├── logistics.py
│   └── manager.py
│
├── utils/
│   ├── __init__.py
│   ├── time_helper.py
│   └── file_helper.py
│
└── aviation_logs/

Giải thích:

- main.py:
    File điều hướng menu chính.
    Chỉ chứa vòng lặp while và gọi hàm.

- core/:
    Chứa các module xử lý
    nghiệp vụ chính.

    + logistics.py:
        Hiển thị lịch trình
        và tính số thùng nước.

    + manager.py:
        Thêm chuyến bay mới
        và kiểm tra mã trùng.

- utils/:
    Chứa các hàm tiện ích hỗ trợ.

    + time_helper.py:
        Tính ETA bằng datetime.

    + file_helper.py:
        Tạo thư mục log
        bằng os.

- aviation_logs/:
    Thư mục lưu trữ log hệ thống.


3. Vai trò của việc chia Package/Module

- Giúp code dễ đọc
- Dễ bảo trì và nâng cấp
- Tránh viết toàn bộ logic
  trong một file lớn
- Dễ sửa lỗi khi hệ thống mở rộng

Ví dụ:
- Sửa tính ETA -> vào time_helper.py
- Sửa hậu cần -> vào logistics.py
- Sửa quản lý chuyến bay -> manager.py

=========================================================
"""

from core.logistics import (
    show_flight_schedule
)

from core.manager import (
    add_new_flight
)

from utils.time_helper import (
    calculate_eta
)

from utils.file_helper import (
    create_folder
)


flights = [
    {
        "flight_id":
        "RA001",
        "passengers":
        154,
        "depart_time":
        "2026-06-15 "
        "08:00:00",
        "duration_min":
        120
    },
    {
        "flight_id":
        "RA002",
        "passengers":
        85,
        "depart_time":
        "2026-06-15 "
        "13:30:00",
        "duration_min":
        45
    }
]


def show_menu():

    print(
        "\n===== HỆ THỐNG "
        "ĐIỀU HÀNH BAY "
        "RIKKEI AVIATION ====="
    )

    print(
        "1. Hiển thị "
        "lịch trình "
        "và Thống kê "
        "hậu cần"
    )

    print(
        "2. Tiếp nhận "
        "chuyến bay mới"
    )

    print(
        "3. Tính thời "
        "gian hạ cánh "
        "dự kiến (ETA)"
    )

    print(
        "4. Khởi tạo "
        "thư mục lưu "
        "trữ log hệ thống"
    )

    print(
        "5. Thoát "
        "chương trình"
    )

    print("=" * 50)


while True:

    show_menu()

    try:
        choice = int(
            input(
                "Nhập lựa chọn "
                "của bạn: "
            )
        )

        if choice == 1:
            show_flight_schedule(
                flights
            )

        elif choice == 2:
            add_new_flight(
                flights
            )

        elif choice == 3:
            calculate_eta(
                flights
            )

        elif choice == 4:
            create_folder()

        elif choice == 5:
            print(
                "Cảm ơn kỹ sư "
                "đã sử dụng "
                "hệ thống!"
            )
            break

        else:
            print(
                "Vui lòng nhập "
                "từ 1-5!"
            )

    except ValueError:
        print(
            "Lỗi! "
            "Vui lòng nhập "
            "số từ 1-5."
        )