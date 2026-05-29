# transaction = " nguyEN vAn a | PYTHON-01 | 15000000 | paid "

# transaction.strip()

# parts = transaction.split("-")

# student_name = parts[0].title()
# course_code = parts[1]
# amount = parts[2]
# status = parts[3].upper()

# print("Học viên:", student_name)
# print("Khóa học:", course_code)
# print("Số tiền:", amount, "VND")
# print("Trạng thái:", status)

# Phân tích lỗi

# 1
# Vì sao transaction.strip() không làm thay đổi trực tiếp chuỗi ban đầu?
# Vì strip() không chỉnh sửa trực tiếp chuỗi gốc.
# Nó chỉ tạo ra một chuỗi mới đã xóa khoảng trắng đầu và cuối.
# Do không gán lại vào biến transaction nên giá trị ban đầu vẫn giữ nguyên.

# 2
# Chuỗi giao dịch thực tế được phân tách bằng ký tự nào?
# Chuỗi transaction được phân tách bằng ký tự "|"

# 3
# Vì sao transaction.split("-") là sai?
# Vì dữ liệu không được phân tách bằng dấu "-"
# mà phân tách bằng dấu "|".
# Nếu dùng split("-") thì Python sẽ tách sai dữ liệu,
# đặc biệt làm hỏng mã khóa học "PYTHON-01".

# 4
# Sau khi tách bằng sai delimiter, dữ liệu trong parts bị lệch như thế nào?
# Khi split("-"), kết quả parts sẽ thành:
# [' nguyEN vAn a | PYTHON', '01 | 15000000 | paid ']
# Lúc này:
# parts[0] = ' nguyEN vAn a | PYTHON'
# parts[1] = '01 | 15000000 | paid '
# Không tồn tại parts[2] và parts[3]
# nên chương trình sẽ báo lỗi IndexError.

# 5
# Vì sao cần .strip() lại từng phần sau khi split()?
# Vì sau khi split("|"), dữ liệu vẫn còn khoảng trắng dư.
# Ví dụ:
# " PYTHON-01 "
# " paid "
# Nếu không strip() thì dữ liệu hiển thị sẽ bị dư khoảng trắng
# gây sai định dạng báo cáo.

# 6
# Vì sao cần chuyển amount từ chuỗi sang số trước khi định dạng tiền?
# Vì dữ liệu sau split() đều là kiểu chuỗi (str).
# Muốn định dạng tiền hoặc tính toán doanh thu
# thì phải chuyển amount sang kiểu số (int hoặc float).
# Nếu không chuyển kiểu sẽ không thể format số tiền đúng chuẩn.

# Sửa

transaction = " nguyEN vAn a | PYTHON-01 | 15000000 | paid "
transaction = transaction.strip()
parts = transaction.split("|")
student_name = parts[0].strip().title()
course_code = parts[1].strip().upper()
amount = int(parts[2].strip())
status = parts[3].strip().upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", format(amount, ","), "VND")
print("Trạng thái:", status)