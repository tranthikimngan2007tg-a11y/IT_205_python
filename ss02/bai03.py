# BÀI TẬP: MODULE "KHỞI TẠO & PHÂN LUỒNG BỆNH ÁN SỐ"
# Phòng khám Đa khoa "Sức Khỏe Vàng"

# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

# 1. PHÂN TÍCH INPUT / OUTPUT

# Input (Dữ liệu đầu vào):
# - Họ và tên bệnh nhân (Kiểu chuỗi - string)
# - Tuổi bệnh nhân (Kiểu số nguyên - int)

# Output (Dữ liệu đầu ra):
# Nếu dữ liệu hợp lệ:
# - In phiếu khám bệnh điện tử gồm:
#   + Tên bệnh nhân
#   + Tuổi
#   + Kết quả phân luồng

# Nếu dữ liệu không hợp lệ:
# - In thông báo lỗi
# - Không in phiếu khám bệnh

# 2. ĐỀ XUẤT GIẢI PHÁP


# Sử dụng cấu trúc điều kiện if - elif - else để:
# 1. Kiểm tra dữ liệu lỗi (Validation)
#    - Tên bỏ trống hoặc chỉ chứa khoảng trắng
#    - Tuổi âm hoặc > 150
#
# 2. Phân luồng bệnh nhân
#    - Dưới 6 tuổi -> ưu tiên khám Nhi
#    - Từ 80 tuổi trở lên -> ưu tiên Lão khoa
#    - Các trường hợp còn lại -> khám thường
# 3. THIẾT KẾ THUẬT TOÁN (PSEUDOCODE)

# Bắt đầu chương trình
#
# Nhập họ tên bệnh nhân
# Nhập tuổi bệnh nhân
#
# Kiểm tra dữ liệu:
#     Nếu tên rỗng hoặc chỉ có khoảng trắng
#         In lỗi
#         Kết thúc
#
#     Nếu tuổi < 0 hoặc tuổi > 150
#         In lỗi
#         Kết thúc
#
# Phân luồng:
#     Nếu tuổi < 6
#         Xếp loại bệnh nhi ưu tiên
#
#     Ngược lại nếu tuổi >= 80
#         Xếp loại người cao tuổi ưu tiên
#
#     Ngược lại
#         Khám thường
#
# In phiếu khám bệnh
# Kết thúc chương trình

ten_benh_nhan = input("Nhập họ và tên bệnh nhân: ")
tuoi = int(input("Nhập tuổi bệnh nhân: "))

if ten_benh_nhan.strip() == "" or tuoi < 0 or tuoi > 150:
    print("\nLỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")

else:

    if tuoi < 6:
        ket_qua = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif tuoi >= 80:
        ket_qua = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        ket_qua = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

    print("\n===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====")
    print("Tên bệnh nhân:", ten_benh_nhan)
    print("Tuổi:", tuoi)
    print("Kết quả phân luồng:")
    print(ket_qua)

# Test 1:
# Tên: Bé Na
# Tuổi: 4
# kq: ƯU TIÊN: Bệnh nhi

# Test 2:
# Tên: Nguyễn Văn B
# Tuổi: 82
#kq: ƯU TIÊN: Người cao tuổi

# Test 3:
# Tên: Trần Minh C
# Tuổi: 30
# kq: KHÁM THƯỜNG

# Test 4:
# Tên: "     "
# Tuổi: 20
# kq: lỗi

# Test 5:
# Tên: Nguyễn Văn D
# Tuổi: -5
# kq: lỗi

# Test 6:
# Tên: Lê Thị E
# Tuổi: 200
# kq: lỗi 