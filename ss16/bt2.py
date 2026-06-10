# (1) Phân tích lỗi
# 1. Tại sao new_prescription.append("Oresol") làm thay đổi cả yesterday_prescription?

# Vì:

# new_prescription = old_prescription

# không tạo List mới mà chỉ tạo thêm một biến tham chiếu đến cùng vùng nhớ với old_prescription.

# Do đó:

# new_prescription.append("Oresol")

# thực chất đang sửa trực tiếp List gốc yesterday_prescription.

# 2. Các cách tạo bản sao độc lập của List

# Cách 1:

# new_prescription = old_prescription.copy()

# Cách 2:

# new_prescription = old_prescription[:]

# Cách 3:

# new_prescription = list(old_prescription)
# 3. Tại sao new_prescription[0].replace("Panadol", "Paracetamol") không có tác dụng?

# Vì String là Immutable.

# Hàm replace() trả về một chuỗi mới nhưng không thay đổi chuỗi cũ.

# Kết quả trả về không được gán lại nên bị bỏ đi.

# 4. Cần sửa như thế nào?
# new_prescription[0] = new_prescription[0].replace(
#     "Panadol",
#     "Paracetamol"
# )

# Hoặc:

# new_prescription[0] = "Paracetamol"
# (2) Source code đúng
# Danh sách thuốc ngày hôm qua
yesterday_prescription = [
    "Panadol",
    "Vitamin C",
    "Amoxicillin"
]

# Hàm tạo và cập nhật đơn thuốc cho ngày mới
def update_prescription(old_prescription):

    # Tạo bản sao độc lập
    new_prescription = old_prescription.copy()

    # Đổi tên thuốc
    new_prescription[0] = new_prescription[0].replace(
        "Panadol",
        "Paracetamol"
    )

    # Thêm thuốc mới
    new_prescription.append("Oresol")

    return new_prescription

# Cấp thuốc ngày hôm nay
today_prescription = update_prescription(
    yesterday_prescription
)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)
# Kết quả
# Đơn thuốc hôm qua: ['Panadol', 'Vitamin C', 'Amoxicillin']
# Đơn thuốc hôm nay: ['Paracetamol', 'Vitamin C', 'Amoxicillin', 'Oresol']