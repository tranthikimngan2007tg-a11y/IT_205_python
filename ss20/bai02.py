# Hàm xử lý cũ bị lỗi
# def process(ds):
#     print("--- BẢNG TÍNH THƯỞNG RP ---")
#     for p in ds:
#         t = p[0]
#         m = p[1]
#         r = p[2]

#         b = (m * 10) + (int(r) * 0.5)
#         print("Tuyển thủ", t, "nhận được", b, "RP")


# (1) Phân tích lỗi

# Với Levi:
# ("Levi", 120, 2500)

# Tuple có đủ 3 phần tử nên:
# p[0] -> tên
# p[1] -> số trận
# p[2] -> MMR

# Vì có đủ dữ liệu nên chương trình chạy bình thường

# Nhưng với SofM:
# ("SofM", 150)

# Tuple chỉ có 2 phần tử:
# p[0]
# p[1]

# Khi chương trình chạy:
# p[2]

# Python không tìm thấy phần tử thứ 3
# nên báo lỗi:
# IndexError: tuple index out of range

# Chương trình bị dừng nên tuyển thủ phía sau
# không được xử lý tiếp

# Nếu sửa SofM thành:
# ("SofM", 150, 2800)

# Thì đến Optimus:
# ("Optimus", 100, "N/A")

# Chương trình chạy:
# int("N/A")

# Nhưng "N/A" là chữ
# không thể đổi sang số nguyên

# Nên sẽ báo lỗi:
# ValueError

# Lỗi xảy ra ở dòng:
# int(r)


# Nếu thêm:
# print("Đang xử lý:", p)

# Nó giúp biết chương trình đang xử lý
# tuyển thủ nào trước khi bị lỗi

# Ví dụ:
# Đang xử lý: ('Levi', 120, 2500)
# Đang xử lý: ('SofM', 150)

# Nhìn vào đó sẽ biết lỗi xảy ra
# ở bản ghi của SofM

# Tên biến cũ:
# ds, p, t, m, r, b

# Nên đổi thành:
# ds -> player_records
# p -> record
# t -> name
# m -> matches
# r -> mmr
# b -> bonus

# Đổi tên giúp code dễ đọc hơn
# và đúng chuẩn Clean Code

# (2) Sửa lỗi

data = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]

def calculate_bonus(matches, mmr):
    bonus = (matches * 10) + (mmr * 0.5)
    return bonus

def process_player_bonus(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:
        name = record[0]

        try:
            matches = record[1]
            mmr = int(record[2])

            bonus = calculate_bonus(
                matches,
                mmr
            )

            print(
                "Tuyển thủ",
                name,
                "nhận được",
                bonus,
                "RP"
            )

        except IndexError:
            print(f"{name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue

        except ValueError:
            print(f"{name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue

process_player_bonus(data)

