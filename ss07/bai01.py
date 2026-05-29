# student_name = " nguYEn vAn a "
# student_code = " rk-001-python "
# email = " Student01@GMAIL.COM "

# student_name.strip()
# student_name.title()

# student_code.strip()
# student_code.upper()

# email.strip()
# email.lower()

# print("Họ tên:", student_name)
# print("Mã học viên:", student_code)
# print("Email:", email)

# Phân tích lỗi

# 1
# Vì sao student_name.strip() không làm thay đổi trực tiếp biến student_name?
# Vì trong Python, phương thức strip() không thay đổi trực tiếp chuỗi gốc.
# Nó chỉ tạo ra một chuỗi mới đã được xử lý.
# Do không gán lại vào biến student_name nên giá trị cũ vẫn được giữ nguyên.

# 2
# Vì sao student_name.title() không tạo ra kết quả "Nguyen Van A"?
# Vì title() cũng trả về một chuỗi mới chứ không chỉnh sửa trực tiếp.
# Chương trình chỉ gọi student_name.title() nhưng không lưu lại kết quả.
# Ngoài ra chuỗi ban đầu còn có khoảng trắng dư nên cần strip() trước.

# 3
# Vì sao student_code.upper() không làm mã học viên chuyển thành chữ hoa?
# Vì upper() chỉ trả về chuỗi mới viết hoa.
# Chương trình không gán kết quả lại vào student_code
# nên giá trị gốc không bị thay đổi.

# 4
# Vì sao email.lower() không làm email chuyển thành chữ thường?
# Vì lower() cũng chỉ tạo ra chuỗi mới.
# Do không gán lại vào biến email nên email vẫn giữ nguyên giá trị cũ.

# 5
# Muốn các phương thức xử lý chuỗi có hiệu lực cần làm gì?
# Cần gán kết quả trả về lại cho biến.
# Ví dụ:
# student_name = student_name.strip().title()

# Sửa

student_name = " nguYEn vAn a "
student_code = " rk-001-python "
email = " Student01@GMAIL.COM "
student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)