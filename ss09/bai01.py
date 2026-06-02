# Danh sách đơn hàng ban đầu
# delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
# delivery_orders.append("GE004")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
# delivery_orders.insert(0, "GE000")

# # Sửa mã đon hàng GE002 thành GE002-UPDATED
# delivery_orders[1] = "GE002-UPDATED"

# # Xóa đơn hàng bị khach hủy
# delivery_orders.remove(3)

# # Lấy đơn hàng cuối cùng ra để bàn giao cho tài xế khác
# delivery_orders.pop()

# print("Danh sách đơn hàng còn lại:",delivery_orders)
# print("Đơn hàng được bàn giao:", transferred_orders)

# (1) Phân tích lỗi

# Sau khi chạy dòng lệnh delivery_orders.insert(0, "GE000")
# GE000 sẽ được thêm vào delivery_orders ở vị trí 0

# delivery_orders[1] = "GE002-UPDATED" dòng này sửa sai đơn hàng cần cập nhật vì
# Đã thêm GE000 vào vị trí 0 nên GE002 đã được cập nhật lại là vị trí 2 nên khi cập nhật vị trí 1 sẽ sai 

# Sau khi chèn GE000 vào vị trí 0 thì GE002 đang nằm ở index 2

# delivery_orders.remove(3) bị lỗi do remove là phương thức xóa theo giá trị
# Muốn xóa đơn hàng "GE003-CANCEL", cần viết lệnh delivery_orders.remove("GE003-CANCEL")
# Phương thức pop xóa phần từ theo vị trí
# chương trình báo lỗi khi in biến transferred_order vì transferred_order chưa được khai báo
# Muốn lưu lại đơn hàng vừa lấy ra bằng pop(), cần viết lệnh 
# transferred_orders = delivery_orders.pop(index)
# print(f"Giá trị đã xóa: {transferred_orders}")
# print(f"Giá trị còn lại: {delivery_orders})

# (2) Sửa

delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]
delivery_orders.append("GE004")
delivery_orders.insert(0, "GE000")
delivery_orders[2] = "GE002-UPDATED"
delivery_orders.remove("GE003-CANCEL")
transferred_orders = delivery_orders.pop(3)

print("Danh sách đơn hàng còn lại:",delivery_orders)
print("Đơn hàng được bàn giao:", transferred_orders)