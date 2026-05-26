# (1) PHÂN TÍCH & ĐỀ XUẤT GIẢI PHÁP
# 1. PHÂN TÍCH INPUT / OUTPUT
# Input (Dữ liệu đầu vào):
# 1. Tuổi (Age) -> kiểu số nguyên (int)
#    Điều kiện: phải dưới 75 tuổi

# 2. Huyết áp tâm thu (Systolic Blood Pressure)
#    -> kiểu số nguyên (int)
#    Điều kiện: từ 90 đến 140 mmHg
#
# 3. Đường huyết (Blood Sugar)
#    -> kiểu số nguyên (int)
#    Điều kiện: dưới 150 mg/dL

# Output (Dữ liệu đầu ra):
# Nếu bệnh nhân đạt TẤT CẢ điều kiện:
# -> "ĐỦ ĐIỀU KIỆN PHẪU THUẬT"

# Nếu trượt bất kỳ điều kiện nào:
# -> "TỪ CHỐI PHẪU THUẬT"

# Nếu dữ liệu âm hoặc vô lý:
# -> "Dữ liệu nhập vào không hợp lệ"

# 2. ĐỀ XUẤT 2 GIẢI PHÁP
# GIẢI PHÁP 1: GỘP ĐIỀU KIỆN (FLAT LOGIC)
# Dùng toán tử logic AND để gộp toàn bộ điều kiện vào 1 câu if.

# Ưu điểm:
# - Code ngắn gọn
# - Dễ viết

# Nhược điểm:
# - Khó biết bệnh nhân trượt tiêu chí nào
# - Không chi tiết về mặt y khoa
# Kiểm tra từng điều kiện theo thứ tự.

# Ví dụ:
# if tuoi < 75:
#     if 90 <= huyet_ap <= 140:
#         if duong_huyet < 150:
#             print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")

# Ưu điểm:
# - Biết chính xác bệnh nhân trượt ở đâu
# - Thông báo chi tiết hơn
# - Giá trị y khoa cao hơn

# Nhược điểm:
# - Code dài hơn
# - Nhiều cấp thụt lề

# Tiêu chí                | Flat Logic | Nested If
# Độ ngắn gọn             | Cao        | Thấp
# Độ dễ đọc code          | Dễ         | Khó hơn
# Độ phức tạp thụt lề     | Thấp       | Cao
# Thông báo lỗi chi tiết  | Không      | Có
# Giá trị y khoa          | Trung bình | Cao

# 4. CHỐT GIẢI PHÁP

# Chọn GIẢI PHÁP 2: NESTED IF (Điều kiện lồng nhau)
# Lý do:
# Trong môi trường bệnh viện, việc biết bệnh nhân bị từ chối
# do tiêu chí nào rất quan trọng để điều dưỡng xử lý tiếp.

# Trade-off:
# - Code dài hơn
# - Nhưng rõ ràng hơn và hữu ích hơn về mặt y khoa

tuoi = int(input("Nhập tuổi bệnh nhân: "))
huyet_ap = int(input("Nhập huyết áp tâm thu (mmHg): "))
duong_huyet = int(input("Nhập đường huyết (mg/dL): "))

if tuoi < 0 or huyet_ap < 0 or duong_huyet < 0:
    print("\nDữ liệu nhập vào không hợp lệ")
else:
    if tuoi >= 75:
        print("\nTỪ CHỐI PHẪU THUẬT")
        print("Lý do: Tuổi bệnh nhân phải dưới 75")
    else:
        if huyet_ap < 90 or huyet_ap > 140:
            print("\nTỪ CHỐI PHẪU THUẬT")
            print("Lý do: Huyết áp tâm thu phải từ 90 đến 140 mmHg")
        else:
            if duong_huyet >= 150:
                print("\nTỪ CHỐI PHẪU THUẬT")
                print("Lý do: Đường huyết phải dưới 150 mg/dL")
            else:
                print("\nĐỦ ĐIỀU KIỆN PHẪU THUẬT")
# Kiểm tra
# Test 1:
# Tuổi: 50
# Huyết áp: 120
# Đường huyết: 110
# -> ĐỦ ĐIỀU KIỆN PHẪU THUẬT

# Test 2:
# Tuổi: 80
# Huyết áp: 120
# Đường huyết: 110
# -> TỪ CHỐI
# Lý do: Tuổi bệnh nhân phải dưới 75

# Test 3:
# Tuổi: 40
# Huyết áp: 150
# Đường huyết: 110
# -> TỪ CHỐI
# Lý do: Huyết áp không đạt

# Test 4:
# Tuổi: 40
# Huyết áp: 120
# Đường huyết: 180
# -> TỪ CHỐI
# Lý do: Đường huyết không đạt

# Test 5:
# Tuổi: -10
# Huyết áp: 120
# Đường huyết: 110
# -> Dữ liệu nhập vào không hợp lệ