# (1) Phân tích lỗi
# 1. Tại sao raw_diagnosis.strip() và raw_diagnosis.title() không làm thay đổi raw_diagnosis?

# Vì String trong Python là Immutable (bất biến). Các hàm strip() và title() trả về một chuỗi mới, không thay đổi chuỗi gốc.

# 2. Để lưu lại kết quả xử lý chuỗi cần sửa như thế nào?
# raw_diagnosis = raw_diagnosis.strip()
# raw_diagnosis = raw_diagnosis.title()

# Hoặc:

# raw_diagnosis = raw_diagnosis.strip().title()
# 3. extend() hoạt động như thế nào khi tham số là String?

# extend() sẽ duyệt từng phần tử của chuỗi và thêm từng ký tự vào list.

# Ví dụ:

# data = []
# data.extend("ABC")
# print(data)

# Kết quả:

# ['A', 'B', 'C']

# Do đó các ký tự 'v', 'i', 'E', 'm' xuất hiện rời rạc trong danh sách.

# 4. Cần thay extend() bằng phương thức nào?

# Dùng:

# append()

# để thêm nguyên vẹn chuỗi vào list.

# (2) Source code đúng
# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
patient_diagnoses = ["Sốt Xuất Huyết"]

# Hàm chuẩn hóa tên bệnh và thêm vào hồ sơ
def add_diagnosis(raw_diagnosis, current_list):
    raw_diagnosis = raw_diagnosis.strip().title()
    current_list.append(raw_diagnosis)
    return current_list

# Bác sĩ nhập thêm một chẩn đoán mới bị lỗi định dạng
new_diagnosis = "  viEm phE QUan  "

# Gọi hàm để xử lý và cập nhật hồ sơ
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)
# Hồ sơ bệnh án (Các chẩn đoán): ['Sốt Xuất Huyết', 'Viem Phe Quan']