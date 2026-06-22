class Product:
    def __init__(self, id, name, import_price, quantity, storage_fee):
        self.id = id
        self.name = name
        self.import_price = import_price
        self.quantity = quantity
        self.storage_fee = storage_fee
        self.total_value = 0
        self.stock_status = "Chưa cập nhật!"

    def calculate_total_value(self):
        self.total_value = (self.import_price * self.quantity) + self.storage_fee
    def classify_stock_status(self):
        if self.total_value >= 30000000:
            self.stock_status = "Rất cao (Rủi ro ứ đọng vốn)"
        elif self.total_value >= 15000000:
            self.stock_status = "Cao (Cần chú ý)"
        elif self.total_value >= 9000000:
            self.stock_status = "Trung bình"
        else:
            self.stock_status = "Thấp (An toàn)"

class ProductManager:
    def __init__(self):
        self.products = []
    


def main():
    pro_man = [
        Product("P001", "Áo sơ mi", 150000, 10, 80000),
        Product("P002", "Quần tây", 250000, 5, 100000)
    ]

    while True:
        print(

"""
=================== MENU ===================
1. Hiển thị dánh sách sản phẩm trong kho
2. Nhập sản phẩm mới vào kho
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm khỏi kho
5. Tìm kiếm sản phẩm theo tên
6. Thoát
===========================================
""")
        choice = input("Nhập lựa chọn của bạn: ")

        match choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                print("Thoát chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")
        
        

        
    
        