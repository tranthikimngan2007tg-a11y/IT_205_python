# Hàm tính tổng tiền đơn hàng
# def calculate_final_price(price, discount, shipping_fee):
#     total = price - (price * discount) + shipping_fee
#     print("Đã tính xong tổng tiền:", total)

# Đơn hàng mua áo thun: Giá 100000, giảm giá 10% (0.1), phí ship 15000
# Gọi hàm để tính tiền
# order_total = calculate_final_price(100000, 15000, 0.1)

# Hệ thống cộng thêm 5000 phí đóng gói vào tổng tiền đơn hàng
# final_payment = order_total + 5000

# print("Khách hàng cần thanh toán:", final_payment)

# (1) Phân tích lỗi

# Theo định nghĩa hàm:
# calculate_final_price(price, discount, shipping_fee)

# Khi gọi:
# calculate_final_price(100000, 15000, 0.1)

# Python sẽ gán:
# 100000 -> price
# 15000 -> discount (sai)
# 0.1 -> shipping_fee (sai)

# Việc truyền sai tham số làm công thức tính bị sai:
# total = 100000 - (100000 * 15000) + 0.1
# = 100000 - 1500000000 + 0.1
# = -1499899999.9

# Chương trình tính ra số âm rất lớn vì discount bị hiểu là 15000
# thay vì tỉ lệ giảm giá 0.1 (10%)

# final_payment = order_total + 5000 bị lỗi TypeError vì
# hàm calculate_final_price() không có return

# print() chỉ hiển thị kết quả ra màn hình
# nhưng không trả dữ liệu về cho chương trình

# Vì không có return nên:
# order_total = None

# Python không thể cộng:
# None + 5000

# Muốn order_total nhận được kết quả tính toán
# cần dùng return total thay vì print(total)

# Đồng thời cần truyền đúng thứ tự tham số:
# calculate_final_price(100000, 0.1, 15000)

# (2) Sửa

def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total


order_total = calculate_final_price(100000, 0.1, 15000)

final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)