# # Danh sách đơn hàng ban đầu
# express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# # Thêm đơn hàng mới vào cuối danh sách
# express_orders.append("GE104")

# # Chèn đơn hàng hỏa tốc vào đầu danh sách
# express_orders.insert(0, "GE100-FAST")

# # Sửa mã đơn hàng bị nhập sai
# express_orders[1] = "GE102-UPDATED"

# # Xóa đơn hàng bị khách hủy 
# express_orders.pop(3)

# # Lấy đơn hàng đầu tiền ra để bắt đầu giao
# current_order = express_orders.pop()

# print("Danh sách đơn hàng còn lại:", express_orders)
# print("Đơn hàng đang giao:", current_order)

# (1) Phân tích lỗi

# Sau khi chạy dòng lệnh express_orders.insert(0, "GE100-FAST") 
# GE100-FAST sẽ được thêm vào express_orders tại vị trí 0

# dòng express_orders[1] = "GE102-UPDATED" sửa nhầm đơn hàng "GE101" thay vì sửa "GE102-WRONG"
# Vì trước đó đã thêm GE100-FAST vào express_orders tại vị trí 0
# Nên GE102-WRONG đang nằm ở index 2 nên khi sửa index 1 sẽ bị sai

# Sau khi chèn "GE100-FAST" vào đầu danh sách, "GE102-WRONG" đang nằm ở index 2

# dòng express_orders.pop(3) không xóa đúng đơn hàng bị hủy 
# pop(3) nghĩa là xóa phần tử ở vị trí số 3 trong danh sách (tính từ 0).
# Nếu danh sách thay đổi (ví dụ bạn thêm phần tử mới vào đầu), thì vị trí của các phần tử cũng thay đổi theo.
# Vì vậy, có lúc pop(3) sẽ xóa đúng "GE103-CANCEL", nhưng nếu trước đó bạn chưa chèn "GE100-FAST" vào đầu thì index 3 lại là "GE104"

# Nếu muốn xóa đúng đơn hàng "GE103-CANCEL" dùng remove() ta viết lệnh như sau
# express_orders.remove("GE103-CANCEL")

# Phương thức pop() không truyền index vào mặc nó sẽ xóa phần từ cuối 

# dòng current_order = express_orders.pop() lấy sai đơn hàng đang giao
# Vì pop() lấy phần tử cuối là "GE104" trong khi đơn hàng đang giao là "GE100-FAST" ở vị trí đầu

# Muốn lấy đơn hàng đầu tiên trong danh sách ra để giao, cần viết lệnh
# current_order = express_orders.pop(0)

# Muốn chương trình cho ra kết quả đúng , cần sửa các dòng
# express_orders[1] = "GE102-UPDATED"
# express_orders.pop(3)
# current_order = express_orders.pop()


express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]
express_orders.append("GE104")
express_orders.insert(0, "GE100-FAST")
express_orders[2] = "GE102-UPDATED"
express_orders.remove("GE103-CANCEL")
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)