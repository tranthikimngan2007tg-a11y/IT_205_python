"""
PHẦN 1: PHÂN TÍCH & TÁI CẤU TRÚC KIẾN TRÚC DỰ ÁN

1. Vì sao 'from math import *' là Anti-pattern?

- Gây ô nhiễm namespace:
  Tất cả hàm trong thư viện math được import vào bộ nhớ,
  làm chương trình khó kiểm soát.

- Dễ xung đột tên hàm:
  Nếu lập trình viên tự viết hàm trùng tên như sqrt(),
  sẽ bị ghi đè hoặc gây lỗi logic.

- Khó đọc và khó bảo trì:
  Người đọc không biết hàm đang dùng đến từ thư viện nào.

Ví dụ không tốt:
    from math import *

Ví dụ tốt hơn:
    import math
   distance = math.sqrt(16)

Hoặc chỉ import đúng hàm cần dùng:
    from math import radians, sin, cos, sqrt, atan2


2. Làm sao để biến thư mục thành Package?

Python cần file đặc biệt:

    __init__.py

Vai trò:
- Giúp Python nhận diện thư mục là package
- Cho phép import module giữa các thư mục
- Hỗ trợ tổ chức code theo kiến trúc modular


3. Cấu trúc thư mục sau khi tối ưu

rikkei_logistics/
│── main.py
│
├── core/
│   ├── __init__.py
│   ├── geo_calculator.py
│   └── time_estimator.py
│
├── utils/
│   ├── __init__.py
│   └── file_helper.py
│
└── logs/

Giải thích:
- core/:
    Chứa các module xử lý logic nghiệp vụ chính.

- utils/:
    Chứa các hàm hỗ trợ hệ thống.

- logs/:
    Lưu log hành trình xe.

- main.py:
    File gốc để chạy hệ thống.
"""

from datetime import datetime

from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta
from utils.file_helper import create_log_dir


shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 10.8231,
        "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 16.0544,
        "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00"
    }
]


def main():
    print(
        "====== HỆ THỐNG ĐIỀU PHỐI "
        "RIKKEI LOGISTICS ======="
    )

    print(
        "[INFO] Khởi tạo hệ thống "
        "lưu trữ log hành trình..."
    )

    create_log_dir("logs")

    print("Thành công.")
    print("-" * 75)

    for shipment in shipments:

        distance = calculate_distance(
            shipment["from_lat"],
            shipment["from_lon"],
            shipment["to_lat"],
            shipment["to_lon"]
        )

        eta = predict_eta(
            shipment["depart"],
            distance
        )

        deadline = datetime.strptime(
            shipment["deadline"],
            "%Y-%m-%d %H:%M:%S"
        )

        print(f"[CHUYẾN XE {shipment['id']}]")

        print(
            f" + Khoảng cách vận chuyển: "
            f"{distance:.2f} km"
        )

        print(
            f" + Thời gian khởi hành: "
            f"{shipment['depart']}"
        )

        print(
            f" + Dự kiến cập bến (ETA): "
            f"{eta.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        if eta <= deadline:
            print(
                " + Trạng thái: "
                "🟢 AN TOÀN "
                "(Kịp tiến độ trước deadline)"
            )
        else:
            print(
                " + Trạng thái: "
                "🔴 CẢNH BÁO "
                "(Trễ hạn! Deadline yêu cầu lúc "
                f"{deadline.strftime('%H:%M:%S')})"
            )

        print()


    print("=" * 56)


if __name__ == "__main__":
    main()