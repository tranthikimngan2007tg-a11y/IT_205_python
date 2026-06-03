# # Thông tin nhân viên ban đầu
# employee = {
#     "employee_id": "NV001",
#     "full_name": "Nguyễn Văn An",
#     "department": "Python Backend",
#     "status": "probation"
# }

# # Lấy mã nhân viên
# employee_id = employee[0]

# # Lấy họ tên nhân viên
# full_name = employee["name"]

# # Cập nhật trạng thái nhân viên
# employee["employee_status"] = "official"

# # Thêm lương cơ bản
# employee.append("base_salary", 15000000)

# # Xóa phòng ban
# del employee["team"]

# print("Mã nhân viên:", employee_id)
# print("Họ tên nhân viên:", full_name)
# print("Thông tin nhân viên sau xử lý:", employee)

# (1) Phân tích lỗi

# Dictionary employee gồm các key:
# "employee_id", "full_name", "department", "status"

# employee_id = employee[0] lỗi vì
# Dictionary không truy cập dữ liệu bằng index giống list hoặc tuple
# Dictionary truy cập bằng key
# Muốn lấy mã nhân viên "NV001"
# code -> employee_id = employee["employee_id"]

# full_name = employee["name"] lỗi vì
# Dictionary không có key "name"
# Key đúng để lấy họ tên nhân viên là "full_name"
# code -> full_name = employee["full_name"]

# employee["employee_status"] = "official" chưa cập nhật đúng vì
# Key đúng của trạng thái nhân viên là "status"
# truyền sai key "employee_status" nên chỉ tạo key mới
# không cập nhật dữ liệu cũ
# code -> employee["status"] = "official"

# employee.append("base_salary", 15000000) lỗi vì
# Dictionary không có phương thức append()
# append() chỉ dùng cho list
# Muốn thêm lương cơ bản base_salary
# code -> employee["base_salary"] = 15000000

# del employee["team"] lỗi vì
# Dictionary không có key "team"
# Key đúng của phòng ban là "department"
# code -> del employee["department"]


# (2) Sửa

employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

employee_id = employee["employee_id"]
full_name = employee["full_name"]
employee["status"] = "official"
employee["base_salary"] = 15000000
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)