# PHẦN 1. PHÂN TÍCH THIẾT KẾ OOP
# Câu 1. Tại sao thuộc tính __price phải được đóng gói (Encapsulation)?

# Giá bán là dữ liệu quan trọng của quán cà phê.

# Nếu khai báo giá bán dưới dạng thuộc tính public:

# self.price = 35000

# thì người dùng có thể tự ý sửa giá từ bên ngoài:

# drink.price = 1

# hoặc

# drink.price = -1000

# Điều này làm sai lệch dữ liệu thực đơn và ảnh hưởng đến hoạt động kinh doanh của cửa hàng.

# Vì vậy thuộc tính giá bán được khai báo dưới dạng:

# self.__price

# để áp dụng cơ chế Name Mangling của Python.

# Nhờ đó dữ liệu được bảo vệ tốt hơn và hạn chế việc thay đổi trực tiếp từ bên ngoài chương trình.

# Câu 2. Tại sao phải sử dụng @property cho thuộc tính giá bán?

# Sau khi sử dụng thuộc tính private:

# self.__price

# thì không thể truy cập trực tiếp:

# drink.__price

# Để các chức năng của chương trình vẫn có thể xem được giá bán, ta sử dụng:

# @property
# def price(self):
#     return self.__price

# Decorator @property cho phép đọc dữ liệu một cách an toàn nhưng không cho phép sửa trực tiếp.

# Ví dụ:

# print(drink.price)

# Nhờ đó chương trình có thể hiển thị giá bán mà vẫn đảm bảo tính đóng gói của dữ liệu.

# Câu 3. Tại sao phương thức toggle_available() phải là Instance Method?

# Mỗi đồ uống có trạng thái kinh doanh riêng.

# Ví dụ:

# CF01 -> Đang bán
# TS01 -> Ngừng bán
# TD01 -> Đang bán

# Khi cập nhật trạng thái, chương trình chỉ thay đổi trạng thái của đúng món được chọn.

# Do đó phương thức này cần thao tác trên dữ liệu của từng đối tượng cụ thể thông qua self.

# Ví dụ:

# def toggle_available(self):
#     self.is_available = not self.is_available

# Đây là Instance Method vì nó làm việc với dữ liệu của từng object riêng biệt.

# Nếu sử dụng Class Method hoặc Static Method thì sẽ không phù hợp vì trạng thái kinh doanh không phải dữ liệu dùng chung cho toàn bộ các món.


class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price

    def toggle_available(self):
        self.is_available = not self.is_available


menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]


def find_drink(code):
    for drink in menu:
        if drink.code == code:
            return drink
    return None


while True:
    print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
    print("1. Xem danh sách đồ uống")
    print("2. Thêm đồ uống mới")
    print("3. Cập nhật trạng thái kinh doanh")
    print("4. Thoát chương trình")
    print("==============================================")

    choice = input("Chọn chức năng (1-4): ")

    match choice:

        case "1":
            print("\n--- DANH SÁCH ĐỒ UỐNG ---\n")

            print(f"{'Mã món':<6} | {'Tên món':<18} | {'Giá bán':<7} | Trạng thái")
            print("-" * 55)

            for drink in menu:
                status = "Đang bán" if drink.is_available else "Ngừng bán"

                print(
                    f"{drink.code:<6} | "
                    f"{drink.name:<18} | "
                    f"{drink.price:<7} | "
                    f"{status}"
                )

        case "2":
            code = input("Nhập mã món: ").strip()

            if find_drink(code):
                print("Mã món đã tồn tại trong hệ thống!")
                continue

            name = input("Nhập tên món: ").strip()

            try:
                price = int(input("Nhập giá bán: "))

                if price <= 0:
                    print("Giá bán không hợp lệ!")
                    continue

            except ValueError:
                print("Giá bán không hợp lệ!")
                continue

            new_drink = Drink(code, name, price)

            menu.append(new_drink)

            print(f"Thành công: Đã thêm món {name} vào thực đơn!")

        case "3":
            code = input("Nhập mã món cần cập nhật: ").strip()

            drink = find_drink(code)

            if drink is None:
                print("Không tìm thấy món có mã này!")
                continue

            drink.toggle_available()

            status = (
                "Đang bán"
                if drink.is_available
                else "Ngừng bán"
            )

            print(f"Đã cập nhật trạng thái món {drink.code}.")
            print(f"Trạng thái hiện tại: {status}")

        case "4":
            print(
                "Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!"
            )
            break

        case _:
            print("Lựa chọn không hợp lệ!")