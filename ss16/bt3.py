# (1) Phân tích và thiết kế giải pháp
# Input/Output các hàm
# validate_gender(gender_input)

# Input:

# gender_input (str)

# Output:

# True  -> nếu là "nam" hoặc "nu"
# False -> ngược lại
# find_patient_index(patient_list, patient_id)

# Input:

# patient_list (list)
# patient_id (str)

# Output:

# int
# Trả về index nếu tìm thấy.
# Trả về -1 nếu không tìm thấy.
# display_patients(patient_list)

# Input:

# patient_list (list)

# Output:

# Không return

# Chỉ in danh sách bệnh nhân.

# add_patient(patient_list)

# Input:

# patient_list (list)

# Output:

# Không return

# Thêm bệnh nhân mới trực tiếp vào danh sách.

# update_diagnosis(patient_list)

# Input:

# patient_list (list)

# Output:

# Không return

# Cập nhật chẩn đoán trực tiếp trong danh sách.

# search_by_disease(patient_list)

# Input:

# patient_list (list)

# Output:

# Không return

# Hiển thị kết quả tìm kiếm và thống kê.

# String và List tương tác như thế nào?
# Dữ liệu nhập vào là String.
# Dùng:
# .strip()
# .upper()
# .title()
# .capitalize()
# .lower()

# để chuẩn hóa dữ liệu.

# Sau khi chuẩn hóa, các chuỗi được lưu vào List con:

# ["BN003", "Le Van Cuong", "Nam", "Dau da day"]

# Nhiều List con được lưu trong List lớn:

# patients = [
#     ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
#     ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
# ]
# Truyền tham chiếu hay truyền giá trị?

# Khi truyền:

# add_patient(patients)

# Python truyền tham chiếu tới List.

# Do đó:

# patient_list.append(...)

# sẽ làm thay đổi trực tiếp biến patients bên ngoài hàm.

# (2) Source Code Hoàn Chỉnh
# ================== DỮ LIỆU BAN ĐẦU ==================

# ================== DỮ LIỆU BAN ĐẦU ==================

patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]


# ================== HELPER FUNCTIONS ==================

def validate_gender(gender_input):
    """
    Kiểm tra giới tính hợp lệ.
    """
    gender = gender_input.strip().lower()
    return gender in ["nam", "nu"]


def find_patient_index(patient_list, patient_id):
    """
    Tìm index bệnh nhân theo mã.
    """
    patient_id = patient_id.strip().upper()

    for index in range(len(patient_list)):
        if patient_list[index][0] == patient_id:
            return index

    return -1


# ================== CHỨC NĂNG 1 ==================

def display_patients(patient_list):
    """
    Hiển thị danh sách bệnh nhân.
    """
    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return

    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")

    for i in range(len(patient_list)):
        patient = patient_list[i]

        print(
            f"{i + 1}. Mã: {patient[0]} | "
            f"Tên: {patient[1]} | "
            f"Giới tính: {patient[2]} | "
            f"Bệnh: {patient[3]}"
        )


# ================== CHỨC NĂNG 2 ==================

def add_patient(patient_list):
    """
    Tiếp nhận bệnh nhân mới.
    """
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    patient_name = input("Nhập tên bệnh nhân: ").strip()

    if len(patient_name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    patient_name = patient_name.title()

    while True:
        gender = input("Nhập giới tính Nam/Nu: ")

        if validate_gender(gender):
            gender = gender.strip().title()
            break

        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán bệnh: ").strip()

    if len(diagnosis) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    diagnosis = diagnosis.capitalize()

    patient = [
        patient_id,
        patient_name,
        gender,
        diagnosis
    ]

    patient_list.append(patient)

    print("Tiếp nhận bệnh nhân thành công!")


# ================== CHỨC NĂNG 3 ==================

def update_diagnosis(patient_list):
    """
    Cập nhật chẩn đoán bệnh.
    """
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(patient_list, patient_id)

    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id}!")
        return

    print(f"Tìm thấy bệnh nhân: {patient_list[index][1]}")
    print(f"Chẩn đoán hiện tại: {patient_list[index][3]}")

    new_diagnosis = input(
        "Nhập chẩn đoán mới: "
    ).strip()

    if len(new_diagnosis) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    new_diagnosis = new_diagnosis.capitalize()

    patient_list[index][3] = new_diagnosis

    print("Cập nhật chẩn đoán bệnh thành công!")


# ================== CHỨC NĂNG 4 ==================

def search_by_disease(patient_list):
    """
    Tìm kiếm theo tên bệnh.
    """
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")

    keyword = input(
        "Nhập từ khóa tên bệnh: "
    ).strip()

    if len(keyword) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return

    print("Kết quả tìm kiếm:")

    count = 0

    for patient in patient_list:

        if keyword.lower() in patient[3].lower():

            count += 1

            print(
                f"{count}. Mã: {patient[0]} | "
                f"Tên: {patient[1]} | "
                f"Giới tính: {patient[2]} | "
                f"Bệnh: {patient[3]}"
            )

    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(
        f"\nCó tổng cộng {count} bệnh nhân mắc bệnh "
        f"liên quan đến '{keyword}'."
    )


# ================== HÀM MAIN ==================

def main():

    while True:

        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        print("===========================================")

        choice = input("Nhập lựa chọn của bạn: ").strip()

        match choice:

            case "1":
                display_patients(patients)

            case "2":
                add_patient(patients)

            case "3":
                update_diagnosis(patients)

            case "4":
                search_by_disease(patients)

            case "5":
                print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
                break

            case _:
                print(
                    "Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!"
                )


# ================== CHẠY CHƯƠNG TRÌNH ==================

main()