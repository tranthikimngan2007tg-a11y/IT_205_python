
#Hiển thị tiêu đề hệ thống
#Nhập mã bệnh nhân
#Nhập nhiệt độ cơ thể
#Nhập nhịp tim
#Ép kiểu nhiệt độ sang float
#Ép kiểu nhịp tim sang int
#Hiển thị kết quả chuẩn hóa dữ liệu
#Hiển thị mã bệnh nhân
#Hiển thị nhiệt độ cơ thể
#Hiển thị kiểu dữ liệu của nhiệt độ
#Hiển thị nhịp tim
#Hiển thị kiểu dữ liệu của nhịp tim
#Hiển thị thông báo dữ liệu hợp lệ
#END

print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")

patient_id = input("Nhập mã bệnh nhân: ")
temperature_input = input("Nhập nhiệt độ cơ thể: ")
heart_rate_input = input("Nhập nhịp tim: ")
temperature = float(temperature_input)
heart_rate = int(heart_rate_input)

print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print("Mã bệnh nhân:", patient_id)
print("Nhiệt độ cơ thể:", temperature, "độ C")
print("→ Kiểu dữ liệu hệ thống ghi nhận:",
      type(temperature))
print("Nhịp tim:", heart_rate, "nhịp/phút")
print("→ Kiểu dữ liệu hệ thống ghi nhận:",
      type(heart_rate))
print("Thông báo: Dữ liệu hợp lệ.")
print("Màn hình Monitor đã sẵn sàng kết nối !")