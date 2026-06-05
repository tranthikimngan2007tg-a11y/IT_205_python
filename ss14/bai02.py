# Biến toàn cục lưu tổng điểm hiện tại của khách hàng
# total_points = 100

# Hàm cộng điểm thưởng
# def add_reward_points(points_earned):
#     total_points = total_points + points_earned
#     print("Đã cộng thêm", points_earned, "điểm.")

# Khách mua hàng được thưởng 50 điểm
# add_reward_points(50)

# In ra kết quả
# print("Tổng điểm hiện tại của khách hàng:", total_points)

# (1) Phân tích lỗi

# total_points được khai báo ngoài hàm nên đây là biến toàn cục (Global Variable)
# Vì biến được tạo bên ngoài function và có thể được truy cập từ nhiều nơi trong chương trình

# Chương trình báo lỗi:
# UnboundLocalError: local variable 'total_points' referenced before assignment

# Vì trong hàm có dòng:
# total_points = total_points + points_earned

# Khi Python thấy phép gán (=)
# Python sẽ tự hiểu total_points trong hàm là biến cục bộ (local variable)

# Nhưng biến cục bộ này chưa được tạo giá trị ban đầu
# nên khi chạy:
# total_points + points_earned

# Python không biết total_points là gì
# dẫn đến lỗi referenced before assignment

# Mặc dù bên ngoài đã có total_points = 100
# nhưng Python vẫn ưu tiên coi biến trong hàm là local
# vì có phép gán giá trị

# Nếu chỉ đọc (print) biến total_points trong hàm
# mà không thay đổi giá trị thì chương trình không bị lỗi

# Ví dụ:
# def test():
#     print(total_points)

# Cách sửa 1:
# Dùng từ khóa global để báo với Python rằng
# hãy dùng biến toàn cục bên ngoài thay vì tạo local variable mới

# global total_points

# Cách sửa 2 (clean code hơn - ưu tiên):
# Không thao tác trực tiếp với biến global
# Hàm nên nhận tổng điểm cũ và điểm mới qua tham số
# Sau đó dùng return để trả về kết quả đã cộng

# (2) Sửa

def add_reward_points(current_points, points_earned):
    total_points = current_points + points_earned
    return total_points


total_points = 100

total_points = add_reward_points(total_points, 50)

print("Đã cộng thêm 50 điểm.")
print("Tổng điểm hiện tại của khách hàng:", total_points)