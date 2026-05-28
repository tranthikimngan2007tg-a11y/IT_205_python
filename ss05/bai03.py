# (1) Phân tích và thiết kế giải pháp

# 1. Phân tích Input / Output

# Input (Dữ liệu đầu vào)
# - room_count: số lượng phòng học cần kiểm tra (kiểu int)
# - row_count: số hàng ghế của từng phòng (kiểu int)
# - seat_count: số ghế trên mỗi hàng (kiểu int)
# Output (Dữ liệu đầu ra)
# - In sơ đồ chỗ ngồi bằng dấu *
# - Hiển thị thông báo lỗi nếu dữ liệu không hợp lệ
# - Bỏ qua hoặc dừng chương trình theo yêu cầu Edge Cases

# 2. Đề xuất giải pháp

# Bước 1:
# Nhập số lượng phòng học.
# Nếu room_count <= 0:
# Hiển thị:
# "Số lượng phòng học không hợp lệ"
# Sau đó kết thúc chương trình.

# Bước 2:
# Dùng vòng lặp for để duyệt từng phòng học.

# Bước 3:
# Với mỗi phòng:
# - Nhập số hàng ghế
# - Nhập số ghế trên mỗi hàng

# Bước 4:
# Kiểm tra dữ liệu hợp lệ

# Bẫy 2:
# Nếu row_count <= 0 hoặc seat_count <= 0:
# Hiển thị:
# "Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này"
# Dùng continue để chuyển sang phòng tiếp theo.

# Bẫy 3:
# Nếu row_count > 10 hoặc seat_count > 10:
# Hiển thị:
# "Phòng quá lớn. Dừng nhập dữ liệu"
# Dùng break để dừng chương trình.

# Bước 5:
# Nếu dữ liệu hợp lệ:
# In sơ đồ ghế bằng dấu *
# Sử dụng vòng lặp lồng nhau:
# - Vòng ngoài duyệt theo hàng ghế
# - Vòng trong duyệt theo số ghế trên mỗi hàng

# 3. Thiết kế thuật toán (Pseudocode)

# Bắt đầu chương trình

# Nhập số lượng phòng học

# Nếu số lượng phòng <= 0:
#     In thông báo lỗi
#     Kết thúc chương trình

# Lặp qua từng phòng:

#     Nhập số hàng ghế
#     Nhập số ghế trên mỗi hàng
#     Nếu dữ liệu <= 0:
#         In thông báo lỗi
#         Bỏ qua phòng này
#     Nếu dữ liệu > 10:
#         In thông báo phòng quá lớn
#         Dừng chương trình
#     In sơ đồ ghế ngồi
#     Lặp theo số hàng:
#         Lặp theo số ghế:
#             In dấu *

# (2) Triển khai code

room_count = int(input("Nhập số lượng phòng học: "))

if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")

else:
    for room in range(1, room_count + 1):
        print(f"\n--- Phòng học {room} ---")
        row_count = int(input("Nhập số hàng ghế: "))
        seat_count = int(
            input("Nhập số ghế trên mỗi hàng: ")
        )

        if row_count <= 0 or seat_count <= 0:
            print(
                "Dữ liệu phòng học không hợp lệ. "
                "Bỏ qua phòng này"
            )
            continue

        if row_count > 10 or seat_count > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break
        print("Sơ đồ chỗ ngồi:")

        for row in range(row_count):
            for seat in range(seat_count):
                print("*", end=" ")
            print()

print("\nChương trình kết thúc")