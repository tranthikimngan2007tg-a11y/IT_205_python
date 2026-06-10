# 1) Phân tích thiết kế hàm
# Hàm find_patient_index(records, patient_id)
# Input
# records: list[str]
# patient_id: str
# Output
# int
# Trả về vị trí bệnh nhân trong danh sách.
# Không tìm thấy trả về -1.
# Pseudocode
# Chuẩn hóa patient_id
# Duyệt từng record trong records
# Nếu record bắt đầu bằng patient_id + "-"
#     return index
# Kết thúc vòng lặp
# return -1
# Hàm display_records(records)
# Input
# records: list[str]
# Output
# None
# Pseudocode
# Nếu danh sách rỗng
#     In thông báo
#     Kết thúc

# Duyệt từng hồ sơ
# split("-")
# Lấy mã, tên, năm sinh, chẩn đoán
# In ra màn hình
# Hàm add_patient(records)
# Input
# records: list[str]
# Output
# None
# Pseudocode
# Nhập mã BN
# Chuẩn hóa mã

# Kiểm tra trùng mã
# Nếu trùng
#     Báo lỗi
#     return

# Nhập tên
# Thay "-" thành khoảng trắng
# Title()

# Nhập năm sinh
# Kiểm tra:
#     là số
#     từ 1900 đến năm hiện tại

# Nếu sai
#     nhập lại

# Nhập chẩn đoán
# Thay "-" thành khoảng trắng
# Capitalize()

# Ghép dữ liệu bằng join()

# Append vào records

# Thông báo thành công
# Hàm update_diagnosis(records)
# Input
# records: list[str]
# Output
# None
# Pseudocode
# Nhập mã BN

# Tìm index

# Nếu không thấy
#     báo lỗi
#     return

# split record

# In thông tin hiện tại

# Nhập chẩn đoán mới

# Thay "-" thành khoảng trắng
# Capitalize()

# Cập nhật phần tử cuối

# join lại thành chuỗi mới

# Gán lại vào records[index]

# Thông báo thành công
# Hàm generate_age_report(records)
# Input
# records: list[str]
# Output
# None
# Pseudocode
# Khởi tạo 3 biến đếm

# Duyệt records

# split()

# Lấy năm sinh

# Tính tuổi

# Nếu tuổi < 16
#     tăng trẻ em

# Nếu 16 <= tuổi <= 60
#     tăng trưởng thành

# Nếu tuổi > 60
#     tăng cao tuổi

# In báo cáo

from datetime import datetime

# ================= DỮ LIỆU BAN ĐẦU =================

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


# ================= HÀM PHỤ TRỢ =================

def find_patient_index(records, patient_id):
    """
    Tìm vị trí bệnh nhân theo mã.
    Trả về index nếu tìm thấy, ngược lại trả về -1.
    """
    patient_id = patient_id.strip().upper()

    for index in range(len(records)):
        if records[index].startswith(patient_id + "-"):
            return index

    return -1


# ================= CHỨC NĂNG 1 =================

def display_records(records):
    """
    Hiển thị danh sách hồ sơ bệnh án.
    """
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("\n--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")

    for index, record in enumerate(records, start=1):
        patient_id, name, birth_year, diagnosis = record.split("-")

        print(
            f"{index}. [{patient_id}] {name:<18} | "
            f"Năm sinh: {birth_year} | "
            f"Chẩn đoán: {diagnosis}"
        )

    print("--------------------------------------------------------------------------")


# ================= CHỨC NĂNG 2 =================

def add_patient(records):
    """
    Thêm hồ sơ bệnh nhân mới.
    """
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip()

    if len(name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    name = name.replace("-", " ").title()

    current_year = datetime.now().year

    while True:
        birth_year = input("Nhập năm sinh: ").strip()

        if birth_year.isdigit():
            birth_year = int(birth_year)

            if 1900 <= birth_year <= current_year:
                break

        print("Năm sinh không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán: ").strip()

    if len(diagnosis) == 0:
        print("Chẩn đoán không được để trống!")
        return

    diagnosis = diagnosis.replace("-", " ").capitalize()

    new_record = "-".join([
        patient_id,
        name,
        str(birth_year),
        diagnosis
    ])

    records.append(new_record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print("Dữ liệu được lưu là:")
    print(new_record)


# ================= CHỨC NĂNG 3 =================

def update_diagnosis(records):
    """
    Cập nhật chẩn đoán theo mã BN.
    """
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    patient_info = records[index].split("-")

    print(f"\nTìm thấy bệnh nhân: {patient_info[1]}")
    print(f"Chẩn đoán hiện tại: {patient_info[3]}")

    new_diagnosis = input(
        "Nhập chẩn đoán mới: "
    ).strip()

    if len(new_diagnosis) == 0:
        print("Chẩn đoán không được để trống!")
        return

    new_diagnosis = (
        new_diagnosis
        .replace("-", " ")
        .capitalize()
    )

    patient_info[3] = new_diagnosis

    records[index] = "-".join(patient_info)

    print("\nCập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(records[index])


# ================= CHỨC NĂNG 4 =================

def generate_age_report(records):
    """
    Báo cáo phân loại theo độ tuổi.
    """
    current_year = datetime.now().year

    children = 0
    adults = 0
    elderly = 0

    for record in records:
        birth_year = int(record.split("-")[2])

        age = current_year - birth_year

        if age < 16:
            children += 1

        elif age <= 60:
            adults += 1

        else:
            elderly += 1

    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adults} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


# ================= HÀM MAIN =================

def main():

    while True:

        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
        print("1. Xem danh sách hồ sơ bệnh án")
        print("2. Thêm hồ sơ bệnh nhân mới")
        print("3. Cập nhật chẩn đoán theo Mã BN")
        print("4. Báo cáo phân loại theo độ tuổi")
        print("5. Thoát chương trình")
        print("==================================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:

            case "1":
                display_records(patient_records)

            case "2":
                add_patient(patient_records)

            case "3":
                update_diagnosis(patient_records)

            case "4":
                generate_age_report(patient_records)

            case "5":
                print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
                break

            case _:
                print(
                    "Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5!"
                )


# ================= CHẠY CHƯƠNG TRÌNH =================

main()