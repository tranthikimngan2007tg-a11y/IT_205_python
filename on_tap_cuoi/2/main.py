class DeliveryOrder :
    def __init__(self, order_id, receiver_name, base_fee, distance, surcharge):
        self.order_id = order_id
        self.receiver_name = receiver_name
        self.base_fee = base_fee
        self.distance = distance
        self.surcharge = surcharge
        self.total_delivery = 0
        self.delivery_status = "Chưa cập nhật!"

    def calculate_total_cost(self):
        self.total_delivery = (self.base_fee * self.distance) + self.surcharge

    def classify_delivery_status(self):
        if self.total_delivery >= 600000:
            self.delivery_status = "Đơn hàng đặc biệt (Ưu tiên cao - Rủi ro cao)"
        elif self.total_delivery >= 300000:
            self.delivery_status = "Đơn hàng đường dai (Cần giám sát)"
        elif self.total_delivery >= 100000:
            self.delivery_status = "Đơn hàng Cận tỉnh"
        else:
            self.delivery_status = "Đơn hàng Tiêu chuẩn (Nội thành)"

class OrderManager:
    def __init__(self):
        self.orders: list[DeliveryOrder] = []

    def show_all_orders(self, orders=None):
        orders_to_show = orders if orders is not None else self.orders
        if not orders_to_show:
            print("Chưa có đơn hàng nào hết!")
            return
        print(f"{'Mã Đơn':<8} | {'Tên người nhận':<15} | {'Cước nền':<10} | {'Khoảng cách(km)':<16} | {'Phụ phí':<8} | {'Tổng chi phí':<12} | {'Tình trạng đơn':<30}")
        for order in orders_to_show:
            order.calculate_total_cost()
            order.classify_delivery_status()
            print(f"{order.order_id:<8} | {order.receiver_name:<15} | {order.base_fee:<10} | {order.distance:<16} | {order.surcharge:<8} | {order.total_delivery:<12} | {order.delivery_status:<30}")

    def add_order(self):
        while True:
            order_id = input("Nhập mã đơn hàng: ")
            if not order_id:
                print("Mã đơn hàng không được để trống!")
                continue
            if any(item.order_id == order_id for item in self.orders):
                print("Mã đơn hàng đã tồn tại!")
                continue
            break

        while True:
            name = input("Nhập tên người nhận: ")
            if not name:
                print("Tên người nhận không được để trống!")
                continue
            break

        while True:
            base_fee_raw = input("Nhập cước nền (số): ")
            try:
                base_fee = float(base_fee_raw)
                break
            except ValueError:
                print("Cước nền phải là số. Thử lại.")

        while True:
            distance_raw = input("Nhập khoảng cách (km): ")
            try:
                distance = float(distance_raw)
                break
            except ValueError:
                print("Khoảng cách phải là số. Thử lại.")

        while True:
            surcharge_raw = input("Nhập phụ phí (số): ")
            try:
                surcharge = float(surcharge_raw)
                break
            except ValueError:
                print("Phụ phí phải là số. Thử lại.")

        new_order = DeliveryOrder(order_id, name, base_fee, distance, surcharge)
        self.orders.append(new_order)
        print("Thêm đơn hàng thành công!")


def main():
    orders = [
        DeliveryOrder("OD001", "Kim Ngân", 150000, 20, 20),
        DeliveryOrder("OD002", "Ánh Hồng", 200000, 30, 50)
    ]

    order_manager = OrderManager()
    order_manager.orders.extend(orders)
    while True:
        print(
"""
===================== MENU =====================
1. Hiển thị danh sách vận đơn trong hệ thống
2. Nhập vận đơn mới
3. Cập nhật thông tin vận đơn
4. Xóa vận đơn khởi hệ thống 
5. Tìm kiếm vận đơn theo tên người nhận
6. Thoát
================================================
"""
        )
        choice = input("Nhập lựa chọn của bạn: ")

        match choice:
            case "1":
                order_manager.show_all_orders()
            case "2":
                order_manager.add_order()
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
        
    
if __name__ == "__main__":
    main()