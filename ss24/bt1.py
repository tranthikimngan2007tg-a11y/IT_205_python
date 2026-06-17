# PHẦN 1: PHÂN TÍCH LỖI (CODE REVIEW)
# Câu 1
# Việc gán trực tiếp order_table1.total_amount = 0 từ bên ngoài đang vi phạm tính chất cốt lõi nào?

# Việc gán trực tiếp giá trị cho thuộc tính total_amount từ bên ngoài vi phạm tính Đóng gói (Encapsulation) trong lập trình hướng đối tượng.

# Do thuộc tính được khai báo dưới dạng public nên bất kỳ ai cũng có thể truy cập và thay đổi dữ liệu, làm mất tính an toàn của hệ thống.

# Câu 2
# Để ngăn chặn việc truy cập và gán giá trị tự do từ bên ngoài, ta cần đổi tên thuộc tính total_amount thành gì để kích hoạt cơ chế Name Mangling trong Python?

# Cần đổi:

# total_amount

# thành:

# __total_amount

# Khi thêm hai dấu gạch dưới ở đầu tên thuộc tính, Python sẽ áp dụng cơ chế Name Mangling để che giấu thuộc tính khỏi việc truy cập trực tiếp từ bên ngoài.

# Câu 3
# Sau khi đã che giấu thuộc tính total_amount, nếu muốn các phần khác của chương trình vẫn có thể xem được tổng tiền (chỉ đọc, không được sửa), ta cần dùng Decorator nào?

# Cần sử dụng decorator:

# @property

# Decorator này cho phép truy cập dữ liệu như một thuộc tính bình thường nhưng không cho phép thay đổi giá trị trực tiếp nếu không định nghĩa setter.

# Ví dụ:

# @property
# def total_amount(self):
#     return self.__total_amount
# Câu 4
# Tại dòng lệnh self.vat_rate = new_rate trong hàm update_vat_rate, Python thực chất đang làm hành động gì?

# Dòng lệnh:

# self.vat_rate = new_rate

# không thay đổi biến lớp vat_rate.

# Thay vào đó, Python tạo ra một instance attribute mới tên là vat_rate riêng cho đối tượng hiện tại.

# Do đó:

# order_table1.update_vat_rate(0.08)

# chỉ ảnh hưởng đến order_table1, còn các đối tượng khác vẫn sử dụng giá trị VAT của lớp là 0.10.

# Câu 5
# Để phương thức cập nhật thuế có thể thay đổi biến vat_rate cho toàn bộ các hóa đơn trong cửa hàng, ta phải cấu trúc lại hàm update_vat_rate bằng Decorator nào và thay tham số self bằng tham số gì?

# Cần sử dụng:

# @classmethod

# và thay tham số:

# self

# bằng:

# cls

# Ví dụ:

# @classmethod
# def update_vat_rate(cls, new_rate):
#     cls.vat_rate = new_rate

# Khi đó giá trị vat_rate của lớp sẽ được cập nhật và tất cả các đối tượng trong hệ thống đều sử dụng mức VAT mới.
class CoffeeOrder:
    vat_rate = 0.10
    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    @property
    def total_amount(self):
        return self.__total_amount

    def calculate_final_bill(self):
        return self.__total_amount + (self.__total_amount * CoffeeOrder.vat_rate)

    @classmethod
    def update_vat_rate(cls, new_rate):
        cls.vat_rate = new_rate

order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

order_table1.add_item(50000)
order_table2.add_item(30000)

try:
    order_table1.total_amount = 0
except AttributeError:
    print("Không thể gán đè tổng tiền hóa đơn!")

CoffeeOrder.update_vat_rate(0.08)

print(f"Tổng tiền Bàn 1 (sau VAT): {order_table1.calculate_final_bill()} VNĐ")
print(f"Tổng tiền Bàn 2 (sau VAT): {order_table2.calculate_final_bill()} VNĐ")

print(f"Thuế VAT đang áp dụng cho Bàn 1: {order_table1.vat_rate}")
print(f"Thuế VAT đang áp dụng cho Bàn 2: {order_table2.vat_rate}")