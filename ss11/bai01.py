# # Thông tin sản phẩm ban đầu
# product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# # Lấy mã sản phẩm
# product_code = product_info[1]

# # Lấy tên sản phẩm
# product_name = product_info[2]

# # Đếm số lượng thông tin sản phẩm
# product_length = product_info.length()

# # Cập nhật giá bán
# product_info[3] = 279000

# print("Mã sản phẩm:", product_code)
# print("Tên sản phẩm:", product_name)
# print("Số lượng thông tin sản phẩm:", product_length)
# print("Thông tin sản phẩm sau cập nhật:", product_info)

# (1) Phân tích lỗi

# Tuple product_info ban đầu có 4 phần tử
# Phần tử "SP001" đang nằm ở index 0
# product_code = product_info[1] sai vì
# Mã sản phẩm nằm ở index 0 mà truyền vào index 1 dẫn đến sai kết quả
# Phần tử "Áo polo nam" đang nằm ở index 1
# Tên sản phẩm nằm ở index 1 mà truyền vào index 2 dẫn đến sai kết quả

# product_length = product_info.length() lỗi vì
# Tuple trong python không có hàm .length()
# Muốn đếm số phần tử trong tuple ta sử dụng hàm len()
# code -> product_length = len(product_info)


# product_info[3] = 279000 không hợp lệ vì
# không hợp lệ vì tuple là immutable (không thể sửa trực tiếp phần tử sau khi tạo)
# Tuple không cho phép cập nhật, thêm, xóa trực tiếp dữ liệu bên trong 
# Muốn cập nhật giá bán từ 299000 thành 279000 
# Ta có thể chuyển tuple sang list sau khi sửa thì chuyển lại tuple

# (2) Sửa

product_info = ("SP001", "Áo polo nam", "Size L", 299000)
product_code = product_info[0]
product_name = product_info[1]
product_length = len(product_info)
temp = list(product_info)
temp[3] = 279000
product_info = tuple(temp)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)