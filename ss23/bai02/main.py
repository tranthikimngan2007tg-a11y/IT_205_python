"""
=========================================================
PHẦN 1: PHÂN TÍCH & THIẾT KẾ KIẾN TRÚC HỆ THỐNG
=========================================================

1. Tác hại của 'from datetime import *'

Đây là Anti-pattern trong Python vì:

- Gây ô nhiễm namespace:
  Toàn bộ hàm, class của thư viện datetime
  được import vào chương trình.

- Dễ gây xung đột tên biến (Name Collision):
  Nếu chương trình có biến trùng tên với
  hàm/class của datetime thì dễ bị ghi đè.

Ví dụ:

    time = 120
    from datetime import *

Lúc này có thể gây xung đột với các thành phần
liên quan đến time trong thư viện datetime,
làm chương trình khó đọc và khó debug.

=> Cách import tốt hơn:

    import datetime

Hoặc:

    from datetime import datetime


2. Hàm tối ưu hơn os.mkdir()

Thư viện os hỗ trợ:

    os.makedirs(path, exist_ok=True)

Ưu điểm:
- Tạo được thư mục lồng nhau.

Ví dụ:
    media_vault/2026/video

- Không bị lỗi nếu thư mục cha đã tồn tại.
- Tránh lỗi FileExistsError làm sập chương trình.


3. Cấu trúc thư mục sau khi tái cấu trúc

rikkei_media/
│── main.py
│
├── analytics/
│   ├── __init__.py
│   └── time_validator.py
│
├── storage/
│   ├── __init__.py
│   ├── disk_manager.py
│   └── io_helper.py
│
└── media_vault/

Giải thích:
- storage/:
    Xử lý lưu trữ và thao tác thư mục.

- analytics/:
    Xử lý logic phân tích thời gian.

- media_vault/:
    Nơi lưu dữ liệu media.

- main.py:
    File điều phối trung tâm.

"""

from storage.disk_manager import (
    calculate_disk_blocks
)

from storage.io_helper import (
    safe_create_dir
)

from analytics.time_validator import (
    parse_and_inspect_date
)


raw_files = [
    {
        "filename": "pod_ep1.mp3",
        "size_bytes": 4500,
        "duration_sec": 180,
        "upload_at": "2026-06-10"
    },
    {
        "filename":
        "movie_trailer.mp4",
        "size_bytes": 105000,
        "duration_sec": 145,
        "upload_at": "2026-06-31"
    },
    {
        "filename":
        "clip_short.mp4",
        "size_bytes": 8200,
        "duration_sec": 15,
        "upload_at": "2026-05-15"
    }
]


def get_media_type(
    file_name
):
    """
    Phân loại media
    """
    if file_name.endswith(
        ".mp3"
    ):
        return "audio"

    if file_name.endswith(
        ".mp4"
    ):
        return "video"

    return "unknown"


def main():

    success_count = 0

    print(
        "======== HỆ THỐNG "
        "QUẢN LÝ LƯU TRỮ "
        "RIKKEI MEDIA ======"
    )

    safe_create_dir(
        "media_vault"
    )

    print(
        "[SYSTEM] Kiểm tra "
        "hạ tầng lưu trữ..."
        " Hoàn tất."
    )

    print("-" * 75)

    for media_file in raw_files:

        print(
            f"[TỆP TIN: "
            f"{media_file['filename']}]"
        )

        upload_date = (
            parse_and_inspect_date(
                media_file[
                    "upload_at"
                ]
            )
        )

        if upload_date is None:

            print(
                " + Trạng thái "
                "phân loại: "
                "🔴 THẤT BẠI "
                "(Lỗi: Định dạng "
                "ngày upload "
                f"'{media_file['upload_at']}' "
                "không tồn tại)"
            )

            print()

            continue

        disk_blocks = (
            calculate_disk_blocks(
                media_file[
                    "size_bytes"
                ]
            )
        )

        media_type = (
            get_media_type(
                media_file[
                    "filename"
                ]
            )
        )

        safe_create_dir(
            f"media_vault/"
            f"{upload_date.year}/"
            f"{media_type}"
        )

        print(
            " + Dung lượng "
            f"thực tế: "
            f"{media_file['size_bytes']:,} "
            "Bytes"
        )

        print(
            " + Số khối "
            "phân vùng "
            "(4KB Block): "
            f"{disk_blocks} "
            "Blocks"
        )

        print(
            " + Trạng thái "
            "phân loại: "
            "🟢 HỢP LỆ "
            f"(Lưu trữ vào "
            f"thư mục "
            f"'{media_type}')"
        )

        print()

        success_count += 1

    print("=" * 56)

    print(
        "TIẾN ĐỘ QUÉT: "
        f"Hoàn thành xử lý "
        f"{success_count}/"
        f"{len(raw_files)} "
        "tệp tin thành công. "
        "Hệ thống ổn định."
    )


if __name__ == "__main__":
    main()