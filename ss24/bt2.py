# PHẦN 1: PHÂN TÍCH LỖI (CODE REVIEW)
# Câu 1. Nếu để thuộc tính points tự do (public), hậu quả đối với cơ sở dữ liệu và các phép toán cộng trừ điểm sau này là gì?
# Nếu thuộc tính points được khai báo dưới dạng public thì người dùng có thể thay đổi giá trị trực tiếp từ bên ngoài đối tượng.
# Ví dụ:
# card1.points = -50
# card1.points = "một trăm"
# Điều này làm dữ liệu mất tính toàn vẹn (Data Integrity),
#  gây sai lệch điểm thưởng của khách hàng. Ngoài ra,
#  nếu gán dữ liệu không đúng kiểu (ví dụ chuỗi ký tự), 
# các phép toán cộng trừ điểm sau này có thể bị lỗi và
#  làm chương trình bị crash.
# Câu 2. Khi ta che giấu points thành __points, người 
# dùng không thể gán giá trị được nữa. Để tạo ra một "bộ lọc" 
# kiểm tra dữ liệu trước khi cho phép gán giá trị mới vào __points 
# (ví dụ: bắt buộc phải là số int và >= 0), ta cần sử dụng Decorator nào của Python?
# Ta cần sử dụng:
# @points.setter

# Decorator này cho phép kiểm tra dữ liệu trước khi gán giá trị vào thuộc tính.

# Ví dụ:

# @points.setter
# def points(self, value):
#     if isinstance(value, int) and value >= 0:
#         self.__points = value
#     else:
#         print("Dữ liệu điểm không hợp lệ!")

# Nhờ đó hệ thống chỉ chấp nhận dữ liệu hợp lệ và từ chối dữ liệu sai.

# Câu 3. Quan sát hàm is_eligible_for_voucher. Tại sao việc truyền tham số self vào hàm này lại bị coi là dư thừa và thiết kế tồi?

# Hàm:

# def is_eligible_for_voucher(self, bill_amount):
#     return bill_amount >= 200000

# không sử dụng bất kỳ thuộc tính nào của đối tượng như:

# self.customer_name
# self.points

# Hàm chỉ kiểm tra giá trị của bill_amount, vì vậy nó không phụ thuộc vào trạng thái của một đối tượng MemberCard cụ thể.

# Do đó việc truyền tham số self là dư thừa, làm cho chương trình phải tạo object mới có thể sử dụng hàm, gây bất tiện và thiết kế chưa hợp lý.

# Câu 4. Để hàm is_eligible_for_voucher hoạt động như một hàm tiện ích độc lập (utility function) bên trong Class — tức là có thể gọi trực tiếp bằng MemberCard.is_eligible_for_voucher(250000) mà không cần tạo object — ta cần dùng Decorator nào? Sự khác biệt giữa Decorator này và @classmethod là gì?

# Ta cần sử dụng:

# @staticmethod

# Ví dụ:

# @staticmethod
# def is_eligible_for_voucher(bill_amount):
#     return bill_amount >= 200000

# Khi đó có thể gọi trực tiếp:

# MemberCard.is_eligible_for_voucher(250000)

# mà không cần tạo object.

# Sự khác biệt giữa @staticmethod và @classmethod
# @staticmethod	@classmethod
# Không nhận self	Không nhận self
# Không nhận cls	Nhận cls
# Không truy cập dữ liệu object	Có thể truy cập dữ liệu class
# Dùng cho hàm tiện ích độc lập	Dùng để thao tác với thuộc tính của lớp

class MemberCard:

    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = 0
        self.points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu điểm không hợp lệ!")

    def add_points(self, amount):
        self.__points += amount

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000

card1 = MemberCard("Le Van C", 100)

card1.points = -50

print(f"Khách hàng: {card1.customer_name} | Điểm hiện tại: {card1.points}")

result = MemberCard.is_eligible_for_voucher(250000)

print(f"Hóa đơn 250k có được tặng Voucher không? {result}")