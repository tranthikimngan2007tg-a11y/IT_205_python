# Hàm xử lý cũ bị lỗi
# def tinh_toan(ds):
#     print("--- BẢNG XẾP HẠNG KDA ---")
#     for x in ds:
#         n = x[0]
#         k = x[1]
#         d = x[2]
#         a = x[3]

#         kda = (int(k) + int(a)) / int(d)
#         print("Tuyển thủ", n, "có chỉ số KDA là:", kda)

# (1) Phân tích lỗi

# Khi xử lý đến ShowMaker:
# ("ShowMaker", "15", "0", "10")

# Chương trình tính:
# (15 + 10) / 0

# Vì không thể chia cho 0 nên Python báo lỗi:
# ZeroDivisionError: division by zero

# Chương trình bị dừng ngay nên tuyển thủ phía sau
# sẽ không được xử lý tiếp

# Nếu xóa ShowMaker thì đến Chovy:
# ("Chovy", "12", "ba", "5")

# Python sẽ chạy:
# int("ba")

# Nhưng "ba" là chữ, không phải số
# nên sẽ báo lỗi:
# ValueError

# Vì Python không thể đổi chữ sang số nguyên

# Tên biến cũ:
# ds, x, n, k, d, a

# Các tên này khó hiểu và không đúng Clean Code

# Nên đổi thành:
# ds -> player_stats_list
# x -> player_stats
# n -> name
# k -> kills
# d -> deaths
# a -> assists

# Đổi tên biến giúp code dễ đọc
# và tự giải thích ý nghĩa hơn

# Tách công thức KDA thành hàm riêng:
# calculate_kda(kills, deaths, assists)

# Lợi ích:
# - Không lặp lại công thức nhiều lần
# - Dễ sửa nếu công thức thay đổi
# - Code dễ đọc hơn
# - Dễ kiểm tra lỗi

# (2) Sửa lỗi

data = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]

def calculate_kda(kills, deaths, assists):
    return (kills + assists) / deaths

def process_player_kda(player_stats_list):
    print("--- BẢNG XẾP HẠNG KDA ---")

    for player_stats in player_stats_list:
        name = player_stats[0]
        kills = player_stats[1]
        deaths = player_stats[2]
        assists = player_stats[3]

        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(
                kills,
                deaths,
                assists
            )

            print(
                "Tuyển thủ",
                name,
                "có chỉ số KDA là:",
                kda
            )

        except ZeroDivisionError:
            print(f"{name}: KDA Hoàn hảo (Perfect Game)!")
            continue

        except ValueError:
            print(f"{name}: Lỗi dữ liệu không hợp lệ!")
            continue

process_player_kda(data)
