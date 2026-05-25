print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")

name_patient = input("Nhập tên bệnh nhân : ")

# input trả về kiểu chuỗi str
weight = input("Nhập cân nặng bệnh nhân : ")

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : ", name_patient)
print("Cân nặng đã nhập : ", weight)

# Kiểm tra kiểu dữ liệu
# Kết quả hiện tại sẽ là <class 'str'>
# Sai kiểu dữ liệu vì cân nặng phải là số thực
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type(weight))

print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân : ")

# sửa lại đúng
# ép  sang kiểu float để cân nặng được lưu là số thực
weight = float(input("Nhập cân nặng bệnh nhân : "))

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : ", name_patient)
print("Cân nặng đã nhập : ", weight)

# sau khi sửa sẽ trả về <class 'float'>
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type(weight))