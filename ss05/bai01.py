branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

result = ""

for month in range(1, month_count + 1):
    for branch in range(1, branch_count + 1):
        revenue = int(
            input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: ")
        )

        result = result + f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng\n"

print(result)

# Phân tích lỗi

# 1
# Cách duyệt này khiến báo cáo không gom dữ liệu theo từng chi nhánh.
# Nguyên nhân là vì vòng lặp ngoài đang duyệt theo tháng trước,
# sau đó mới duyệt từng chi nhánh.
# Điều này làm dữ liệu của cùng một chi nhánh bị tách ra,
# không được gom theo từng chi nhánh như yêu cầu nghiệp vụ.

# 2 độ ưu tiên vòng lặp
# Theo yêu cầu nghiệp vụ:
# Vòng lặp ngoài nên duyệt theo chi nhánh.
# Vì hệ thống cần gom toàn bộ doanh thu của từng chi nhánh trước.

# Vòng lặp trong nên duyệt theo tháng.
# Vì mỗi chi nhánh sẽ cần nhập doanh thu của tháng 1, 2, 3 liên tiếp.

# 3 nguyên nhân báo cáo sai nghiệp vụ
# Vì vòng lặp month được đặt ở ngoài nên dữ liệu hiển thị
# bị nhóm theo tháng thay vì nhóm theo chi nhánh.
# Điều này làm báo cáo khó theo dõi và không đúng yêu cầu quản lý.

# Sửa

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

result = ""

for branch in range(1, branch_count + 1):
    result += f"\n--- Chi nhánh {branch} ---\n"
    for month in range(1, month_count + 1):
        revenue = int(
            input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: ")
        )
        result += (
            f"Tháng {month}: "
            f"{revenue} triệu đồng\n"
        )

print(result)