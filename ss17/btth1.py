# (1) Phân tích và thiết kế giải pháp
# Biến toàn cục
# raw_logs = []
# processed_logs = []
# Hàm 1: clean_log_data()

# Chức năng: Làm sạch dữ liệu log thô.

# Input:

# log_input (str)

# Output:

# list

# Xử lý:

# Tạo bảng ánh xạ bằng str.maketrans()
# Loại bỏ ký tự ! @ # $
# Dùng translate() làm sạch chuỗi
# Dùng split(";") tách thành danh sách log
# Hàm 2: filter_danger_logs()

# Chức năng: Lọc log nguy hiểm.

# Input:

# logs (list)

# Output:

# list

# Xử lý:

# Dùng List Comprehension
# Giữ lại log chứa:
# ERROR
# CRITICAL
# Không phân biệt hoa thường
# Hàm 3: mask_ip_address()

# Chức năng: Mã hóa IP trong một dòng log.

# Input:

# log_line (str)

# Output:

# str

# Ví dụ:

# 192.168.1.1
# ↓
# 192.168.*.*
# Hàm 4: generate_safe_report()

# Chức năng: Tạo báo cáo đã mã hóa IP.

# Input:

# logs (list)

# Output:

# list
# Phân tích maketrans() và translate()
# Cú pháp
# table = str.maketrans("", "", "!@#$")

# Ý nghĩa:

# {
#     "!": None,
#     "@": None,
#     "#": None,
#     "$": None
# }

# Python tạo sẵn một bảng ánh xạ (mapping table).

# Sau đó:

# clean_text = text.translate(table)

# Python chỉ cần tra cứu bảng này để xóa ký tự.

# Ưu điểm:

# Nhanh hơn vòng lặp for
# Tối ưu cho chuỗi lớn
# Thích hợp xử lý log hàng nghìn dòng
raw_logs = []
processed_logs = []


def clean_log_data(log_input):
    """
    Làm sạch dữ liệu log thô.

    Parameters:
        log_input (str): Chuỗi log người dùng nhập.

    Returns:
        list: Danh sách log đã được làm sạch.
    """

    translation_table = str.maketrans("", "", "!@#$")

    cleaned_text = log_input.translate(translation_table)

    logs = [log.strip() for log in cleaned_text.split(";") if log.strip()]

    return logs


def filter_danger_logs(logs):
    """
    Lọc các log chứa ERROR hoặc CRITICAL.

    Parameters:
        logs (list): Danh sách log.

    Returns:
        list: Danh sách log nguy hiểm.
    """

    return [
        log
        for log in logs
        if "ERROR" in log.upper() or "CRITICAL" in log.upper()
    ]


def mask_ip_address(log_line):
    """
    Mã hóa địa chỉ IP trong một dòng log.

    Parameters:
        log_line (str): Một dòng log.

    Returns:
        str: Dòng log sau khi mã hóa IP.
    """

    words = log_line.split()

    for i in range(len(words)):

        if "." in words[i]:

            parts = words[i].split(".")

            if len(parts) == 4:

                masked_ip = ".".join(parts[:2] + ["*", "*"])

                words[i] = masked_ip

    return " ".join(words)


def generate_safe_report(logs):
    """
    Tạo báo cáo log đã mã hóa IP.

    Parameters:
        logs (list): Danh sách log nguy hiểm.

    Returns:
        list: Danh sách log sau khi mã hóa.
    """

    return [mask_ip_address(log) for log in logs]


while True:

    print("\n============= SECURITY LOG ANALYZER =============")
    print("1. Nhập và làm sạch dữ liệu Log thô")
    print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
    print("3. Mã hóa địa chỉ IP (Masking)")
    print("4. Đóng hệ thống")
    print("=================================================")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":

        print("\n--- NẠP DỮ LIỆU LOG ---")

        log_input = input(
            "Nhập chuỗi log thô (cách nhau bởi dấu ;): "
        )

        raw_logs = clean_log_data(log_input)

        print(
            f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống."
        )

    elif choice == "2":

        print("\n--- LỌC CẢNH BÁO ---")

        if not raw_logs:
            print(
                "Chưa có dữ liệu log, vui lòng thực hiện chức năng 1"
            )
            continue

        processed_logs = filter_danger_logs(raw_logs)

        if processed_logs:

            print(
                f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:"
            )

            for log in processed_logs:
                print("-", log)

        else:
            print("Không tìm thấy cảnh báo nguy hiểm.")

    elif choice == "3":

        print("\n--- MÃ HÓA IP ---")

        if not raw_logs:
            print(
                "Chưa có dữ liệu log, vui lòng thực hiện chức năng 1"
            )
            continue

        if not processed_logs:
            processed_logs = filter_danger_logs(raw_logs)

        safe_logs = generate_safe_report(processed_logs)

        if safe_logs:

            print("Báo cáo log an toàn:")

            for index, log in enumerate(safe_logs, start=1):
                print(f"{index}. {log}")

        else:
            print("Không có log nguy hiểm để mã hóa.")

    elif choice == "4":

        print("\nĐóng hệ thống...")
        print("Cảm ơn đã sử dụng Security Log Analyzer.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")