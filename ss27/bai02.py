# PHÂN TÍCH THIẾT KẾ HỆ THỐNG

# BaseProduct là lớp trừu tượng (Abstract Base Class) đóng vai trò
# khuôn mẫu chung cho tất cả sản phẩm trong kho.
# Lớp này quản lý các thuộc tính dùng chung như:
# - warehouse_name
# - base_storage_fee
# - stock_quantity
# Đồng thời định nghĩa các phương thức bắt buộc:
# - import_stock()
# - export_stock()
# Mọi lớp con phải triển khai lại các phương thức này.

# ColdStorageProduct kế thừa BaseProduct để quản lý hàng đông lạnh.
# Lớp này bổ sung thuộc tính required_temperature và xử lý
# hao hụt 5% khi xuất kho.

# HazardousProduct kế thừa BaseProduct để quản lý hàng nguy hiểm.
# Lớp này bổ sung thuộc tính max_safety_limit nhằm kiểm soát
# số lượng tồn kho không vượt quá ngưỡng an toàn.

# HybridPremiumProduct sử dụng Multiple Inheritance:
# HybridPremiumProduct -> ColdStorageProduct -> HazardousProduct
# Sản phẩm Hybrid đồng thời sở hữu:
# - Tính năng bảo quản lạnh
# - Tính năng kiểm soát giới hạn an toàn
# giúp quản lý các mặt hàng đặc biệt yêu cầu nhiều điều kiện.

# MRO (METHOD RESOLUTION ORDER)

# Python sử dụng cơ chế MRO để xác định thứ tự tìm kiếm phương thức.
# Với HybridPremiumProduct, danh sách MRO là:
#
# HybridPremiumProduct
# -> ColdStorageProduct
# -> HazardousProduct
# -> BaseProduct
# -> ABC
# -> object
#
# Khi gọi một phương thức, Python sẽ tìm kiếm theo thứ tự trên.
# Nếu không tìm thấy ở lớp hiện tại, Python tiếp tục tìm xuống
# các lớp tiếp theo trong MRO.
#
# Cơ chế này giúp giải quyết xung đột khi nhiều lớp cha có cùng
# tên phương thức trong mô hình đa kế thừa.

# DUCK TYPING

# Hệ thống sử dụng Duck Typing trong chức năng vận chuyển.
# Hàm dispatch_to_carrier() không quan tâm đối tượng vận chuyển
# thuộc lớp FedExCarrier hay DHLCarrier.
#
# Điều kiện duy nhất là đối tượng đó phải có phương thức:
# ship_package(product, quantity)
#
# Nhờ vậy có thể mở rộng thêm các đơn vị vận chuyển mới như:
# UPSCarrier, GHTKCarrier, NinjaVanCarrier,...
# mà không cần sửa đổi mã nguồn của các lớp sản phẩm.
#
# Đây là ưu điểm lớn của Duck Typing:
# - Giảm sự phụ thuộc giữa các module
# - Dễ mở rộng hệ thống
# - Tuân thủ nguyên tắc Open/Closed Principle (OCP)

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    warehouse_name = "Amazon Logistics"
    base_storage_fee = 5000

    def __init__(self, product_code, product_name):
        self.product_code = product_code
        self.product_name = product_name
        self.__stock_quantity = 0

    @property
    def stock_quantity(self):
        return self.__stock_quantity

    def _set_stock_quantity(self, quantity):
        self.__stock_quantity = quantity

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = " ".join(value.strip().upper().split())

    @abstractmethod
    def import_stock(self, quantity):
        pass

    @abstractmethod
    def export_stock(self, quantity):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity + other.stock_quantity

    def __lt__(self, other):
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity < other.stock_quantity

    @staticmethod
    def validate_product_code(product_code):
        return (
            len(product_code) == 10
            and product_code[0].isalpha()
            and product_code[1:].isalnum()
        )

    @classmethod
    def update_warehouse_name(cls, new_name):
        cls.warehouse_name = new_name


class ColdStorageProduct(BaseProduct):
    def __init__(self, product_code, product_name, required_temperature):
        super().__init__(product_code, product_name)
        self.required_temperature = required_temperature

    def import_stock(self, quantity):
        self._set_stock_quantity(self.stock_quantity + quantity)

    def export_stock(self, quantity):
        loss = quantity * 0.05
        total = quantity + loss

        if total > self.stock_quantity:
            raise ValueError("Không đủ tồn kho")

        self._set_stock_quantity(self.stock_quantity - total)
        return loss

    def apply_cooling_cost(self):
        return self.stock_quantity * abs(self.required_temperature) * 50


class HazardousProduct(BaseProduct):
    def __init__(self, product_code, product_name, max_safety_limit):
        super().__init__(product_code, product_name)
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        if self.stock_quantity + quantity > self.max_safety_limit:
            raise ValueError(
                f"Tồn kho vượt giới hạn an toàn ({self.max_safety_limit})"
            )

        self._set_stock_quantity(self.stock_quantity + quantity)

    def export_stock(self, quantity):
        if quantity > self.stock_quantity:
            raise ValueError("Không đủ tồn kho")

        self._set_stock_quantity(self.stock_quantity - quantity)


class HybridPremiumProduct(ColdStorageProduct, HazardousProduct):
    def __init__(
        self,
        product_code,
        product_name,
        required_temperature,
        max_safety_limit,
    ):
        BaseProduct.__init__(self, product_code, product_name)
        self.required_temperature = required_temperature
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        if self.stock_quantity + quantity > self.max_safety_limit:
            raise ValueError(
                f"Tồn kho vượt giới hạn an toàn ({self.max_safety_limit})"
            )

        self._set_stock_quantity(self.stock_quantity + quantity)

    def export_stock(self, quantity):
        loss = quantity * 0.05
        total = quantity + loss

        if total > self.stock_quantity:
            raise ValueError("Không đủ tồn kho")

        self._set_stock_quantity(self.stock_quantity - total)
        return loss


class FedExCarrier:
    def ship_package(self, product, quantity):
        print(
            f"[Hệ thống FedEx]: Đang tiếp nhận mã sản phẩm {product.product_code}..."
        )
        product.export_stock(quantity)


class DHLCarrier:
    def ship_package(self, product, quantity):
        print(
            f"[Hệ thống DHL]: Đang tiếp nhận mã sản phẩm {product.product_code}..."
        )
        product.export_stock(quantity)


def dispatch_to_carrier(carrier_agent, product, quantity):
    try:
        carrier_agent.ship_package(product, quantity)
        print("Xác thực đối tác bằng Duck Typing thành công!")
        print(
            f"Đơn vị vận chuyển đã tiếp nhận đơn hàng số lượng: {quantity} đơn vị."
        )
        print(
            f"Số lượng tồn kho cập nhật: {product.stock_quantity:.2f} đơn vị."
        )
    except AttributeError:
        print(
            "Đơn vị vận chuyển không hợp lệ hoặc chưa ký kết hợp đồng kỹ thuật"
        )
    except Exception as e:
        print(e)


def create_product(products):
    print("\n--- CHỌN LOẠI SẢN PHẨM KHỞI TẠO ---")
    print("1. Cold Storage Product")
    print("2. Hazardous Product")
    print("3. Hybrid Premium Product")

    choice = input("Chọn loại sản phẩm (1-3): ")

    product_code = input("Nhập mã sản phẩm 10 ký tự: ")

    if not BaseProduct.validate_product_code(product_code):
        print("Mã sản phẩm không hợp lệ! Phải gồm đúng 10 ký tự.")
        return None

    product_name = input("Nhập tên sản phẩm: ")

    try:
        if choice == "1":
            temperature = float(
                input("Nhập nhiệt độ bảo quản yêu cầu: ")
            )

            product = ColdStorageProduct(
                product_code,
                product_name,
                temperature,
            )

        elif choice == "2":
            limit = int(
                input("Nhập hạn mức an toàn tối đa: ")
            )

            product = HazardousProduct(
                product_code,
                product_name,
                limit,
            )

        elif choice == "3":
            temperature = float(
                input("Nhập nhiệt độ bảo quản yêu cầu: ")
            )

            limit = int(
                input("Nhập hạn mức an toàn tối đa: ")
            )

            product = HybridPremiumProduct(
                product_code,
                product_name,
                temperature,
                limit,
            )

        else:
            print("Loại sản phẩm không hợp lệ")
            return None

        products.append(product)

        print("Đăng ký thành công!")
        print("Tên sản phẩm:", product.product_name)

        return product

    except Exception as e:
        print(e)
        return None


def show_product(product):
    if not product:
        print(
            "Hệ thống chưa có thông tin sản phẩm. Vui lòng đăng ký trước."
        )
        return

    print("\n--- THÔNG TIN SẢN PHẨM HIỆN TẠI ---")
    print("Loại sản phẩm:", type(product).__name__)
    print("Chuỗi kho:", product.warehouse_name)
    print("Mã sản phẩm:", product.product_code)
    print("Tên sản phẩm:", product.product_name)
    print(
        f"Số lượng tồn kho: {product.stock_quantity:.2f} đơn vị"
    )

    if hasattr(product, "required_temperature"):
        print(
            f"Nhiệt độ yêu cầu: {product.required_temperature} độ C"
        )

    if hasattr(product, "max_safety_limit"):
        print(
            f"Hạn mức an toàn tối đa: {product.max_safety_limit}"
        )

    print("\nMRO:")
    for cls in type(product).mro():
        print(cls.__name__)


def stock_transaction(product):
    if not product:
        print("Chưa có sản phẩm được chọn.")
        return

    print("\n1. Nhập kho")
    print("2. Xuất kho")

    choice = input("Chọn giao dịch (1-2): ")

    try:
        quantity = float(input("Nhập số lượng: "))

        if quantity <= 0:
            print("Số lượng phải lớn hơn 0")
            return

        if choice == "1":
            product.import_stock(quantity)
            print("Nhập kho thành công!")
            print(
                f"Tồn kho hiện tại: {product.stock_quantity:.2f}"
            )

        elif choice == "2":

            if isinstance(
                product,
                (ColdStorageProduct, HybridPremiumProduct),
            ):
                loss = product.export_stock(quantity)

                print("Xuất kho thành công!")
                print(
                    f"Số lượng yêu cầu: {quantity:.2f}"
                )
                print(
                    f"Số lượng hao hụt bảo quản (5%): {loss:.2f}"
                )
                print(
                    f"Tổng khấu trừ: {quantity + loss:.2f}"
                )

            else:
                product.export_stock(quantity)
                print("Xuất kho thành công!")

            print(
                f"Tồn kho còn lại: {product.stock_quantity:.2f}"
            )

    except Exception as e:
        print(e)


def cooling_cost(product):
    if isinstance(
        product,
        (ColdStorageProduct, HybridPremiumProduct),
    ):
        cost = product.apply_cooling_cost()

        print("\n--- TÍNH PHÍ BẢO QUẢN ĐÔNG LẠNH ---")
        print(
            f"Số lượng tồn kho: {product.stock_quantity:.2f}"
        )
        print(
            f"Nhiệt độ yêu cầu: {product.required_temperature}"
        )
        print(
            f"Chi phí làm lạnh phát sinh: +{cost:,.0f} VND"
        )
    else:
        print("Sản phẩm hiện tại không hỗ trợ tính năng này.")


def compare_products(products, current_product):
    if len(products) < 2:
        print("Cần ít nhất 2 sản phẩm.")
        return

    others = [
        product
        for product in products
        if product != current_product
    ]

    print("\n--- DANH SÁCH SẢN PHẨM ---")

    for index, product in enumerate(
        others,
        start=1,
    ):
        print(
            f"{index}. {product.product_code} - "
            f"{product.product_name} "
            f"({product.stock_quantity:.2f})"
        )

    try:
        choice = int(
            input("Chọn sản phẩm đối ứng: ")
        )

        other = others[choice - 1]

        if current_product < other:
            print(
                "[Kết quả So sánh (__lt__)]: "
                "Tồn kho sản phẩm A ÍT HƠN tồn kho sản phẩm B."
            )
        else:
            print(
                "[Kết quả So sánh (__lt__)]: "
                "Tồn kho sản phẩm A KHÔNG ÍT HƠN sản phẩm B."
            )

        print(
            f"[Kết quả Tổng hợp (__add__)]: "
            f"{current_product + other:.2f} đơn vị."
        )

    except Exception as e:
        print(e)


def carrier_dispatch(product):
    if not product:
        print("Chưa có sản phẩm được chọn.")
        return

    print("\n1. FedEx")
    print("2. DHL")

    choice = input("Chọn đối tác vận chuyển: ")

    try:
        quantity = float(
            input(
                "Nhập số lượng hàng hóa bàn giao: "
            )
        )

        if choice == "1":
            carrier = FedExCarrier()
        else:
            carrier = DHLCarrier()

        dispatch_to_carrier(
            carrier,
            product,
            quantity,
        )

    except Exception as e:
        print(e)


def choose_product(products):
    if not products:
        print("Danh sách sản phẩm trống.")
        return None

    for index, product in enumerate(
        products,
        start=1,
    ):
        print(
            f"{index}. {product.product_code} - "
            f"{product.product_name}"
        )

    try:
        choice = int(
            input("Chọn sản phẩm: ")
        )
        return products[choice - 1]
    except:
        return None


def main():
    products = []
    current_product = None

    while True:
        print(
            "\n===== AMAZON INVENTORY SIMULATOR PRO ====="
        )
        print("1. Đăng ký mã hàng hóa mới")
        print("2. Xem thông tin & Kiểm tra MRO")
        print("3. Giao dịch Nhập / Xuất kho")
        print("4. Tính chi phí bảo quản")
        print("5. So sánh & Gộp tồn kho")
        print("6. Điều phối vận chuyển")
        print("7. Chọn sản phẩm hiện tại")
        print("8. Thoát")
        print(
            "=========================================="
        )

        choice = input("Chọn chức năng: ")

        if choice == "1":
            product = create_product(products)

            if product:
                current_product = product

        elif choice == "2":
            show_product(current_product)

        elif choice == "3":
            stock_transaction(current_product)

        elif choice == "4":
            cooling_cost(current_product)

        elif choice == "5":
            compare_products(
                products,
                current_product,
            )

        elif choice == "6":
            carrier_dispatch(current_product)

        elif choice == "7":
            selected = choose_product(products)

            if selected:
                current_product = selected
                print(
                    "Đã chọn sản phẩm hiện tại."
                )

        elif choice == "8":
            print(
                "Cảm ơn đã sử dụng hệ thống Amazon Inventory Simulator Pro!"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ."
            )


if __name__ == "__main__":
    main()