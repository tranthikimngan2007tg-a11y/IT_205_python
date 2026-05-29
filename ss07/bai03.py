# (1) Phân tích và thiết kế giải pháp

# 1. Phân tích Input / Output
# Input (Dữ liệu đầu vào)
# - raw_data: chuỗi dữ liệu nhân sự (kiểu str)
# Chứa:
# ID | Họ tên | Phòng ban | Số điện thoại
# - choice: lựa chọn menu của người dùng
# - search_id: mã nhân viên cần tìm
# Output (Dữ liệu đầu ra)
# Chức năng 1:
# In toàn bộ dữ liệu gốc.
# Chức năng 2:
# Chuẩn hóa dữ liệu:
# - ID viết hoa
# - Họ tên viết hoa chữ cái đầu
# - Phòng ban viết hoa
# - Số điện thoại:
#     + Xóa dấu "-"
#     + Nếu hợp lệ -> che 6 số đầu
#     + Nếu sai -> Invalid Format
# In báo cáo dạng bảng.

# Chức năng 3:
# Tìm nhân viên theo ID.
# Nếu tìm thấy -> in thông tin.
# Không tìm thấy -> báo lỗi.

# Chức năng 4:
# Thoát chương trình.

# 2. Đề xuất giải pháp

# Bước 1:
# Tạo raw_data chứa dữ liệu nhân viên.

# Bước 2:
# Dùng while để hiển thị menu liên tục.

# Bước 3:
# Kiểm tra menu:
# Nếu nhập khác 1,2,3,4
# -> báo lỗi và nhập lại.

# Bước 4:
# Chức năng 1:
# In dữ liệu gốc.

# Bước 5:
# Chức năng 2:
# - split(";") để tách nhân viên
# - split("|") để tách thông tin
# - Chuẩn hóa dữ liệu
# - Kiểm tra số điện thoại

# Bước 6:
# Chức năng 3:
# - strip() khoảng trắng
# - upper() mã ID
# - tìm kiếm

# Bước 7:
# Chức năng 4:
# break để kết thúc chương trình.

# 3. Thiết kế thuật toán (Pseudocode)

# Bắt đầu chương trình
# Khởi tạo raw_data
# while True
#     Hiển thị menu
#     Nhập lựa chọn
#     Nếu lựa chọn không hợp lệ
#         Báo lỗi
#         continue
#     Nếu chọn 1
#         In dữ liệu gốc
#     Nếu chọn 2
#         Chuẩn hóa dữ liệu
#         In báo cáo
#     Nếu chọn 3
#         Nhập ID
#         Chuẩn hóa ID
#         Tìm nhân viên
#     Nếu chọn 4
#         Thoát chương trình


# (2) Triển khai code

raw_data = (
    "emp-001|nguyen van a|it|0912-345-678;"
    "emp-002|tran thi b|hr|0988-777-666;"
    "emp-003|le van c|finance|09ab-888-999"
)

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")
    choice = input("Nhập lựa chọn: ")

    if (
        choice != "1"
        and choice != "2"
        and choice != "3"
        and choice != "4"
    ):
        print(
            "Lựa chọn không hợp lệ, "
            "vui lòng nhập lại!")
        continue

    if choice == "1":
        print("\n=== DỮ LIỆU GỐC ===")
        print(raw_data)
    elif choice == "2":
        employee_list = raw_data.split(";")
        print("\n=== BÁO CÁO NHÂN SỰ ===")
        print(
            f"{'ID':<12}"
            f"{'HỌ TÊN':<25}"
            f"{'PHÒNG BAN':<15}"
            f"{'SỐ ĐIỆN THOẠI':<20}"
        )
        print("-" * 72)
        for employee in employee_list:
            parts = employee.split("|")
            employee_id = (
                parts[0]
                .strip()
                .upper()
            )

            full_name = (
                parts[1]
                .strip()
                .title()
            )

            department = (
                parts[2]
                .strip()
                .upper()
            )

            phone_number = (
                parts[3]
                .strip()
                .replace("-", "")
            )

            if phone_number.isdigit():
                masked_phone = ( "******"+ phone_number[-4:])
            else:
                masked_phone = ( "Invalid Format")

            print(
                f"{employee_id:<12}"
                f"{full_name:<25}"
                f"{department:<15}"
                f"{masked_phone:<20}")

    elif choice == "3":
        search_id = input(
            "Nhập mã nhân viên cần tìm: "
        )
        search_id = (
            search_id
            .strip()
            .upper()
        )
        employee_list = raw_data.split(";")

        found = False

        for employee in employee_list:
            parts = employee.split("|")
            employee_id = (
                parts[0]
                .strip()
                .upper()
            )

            if employee_id == search_id:
                full_name = (
                    parts[1]
                    .strip()
                    .title()
                )

                department = (
                    parts[2]
                    .strip()
                    .upper()
                )

                phone_number = (
                    parts[3]
                    .strip()
                    .replace("-", "")
                )

                if phone_number.isdigit():
                    masked_phone = ("******"+ phone_number[-4:])
                else:
                    masked_phone = ( "Invalid Format")
                print("\n=== THÔNG TIN NHÂN VIÊN ===")
                print("ID:", employee_id)
                print("Họ tên:",full_name)
                print("Phòng ban:",department)
                print("Số điện thoại:", masked_phone)
                found = True
                break
        if found == False:
            print("Không tìm thấy nhân viên")
    elif choice == "4":
        print("Thoát chương trình")
        break