def show_orders(orders_list):
    if len(orders_list) == 0:
        print("[Thông báo]: Chưa có đơn hàng nào trong hệ thống!")
        return

    print("\n{:<10} {:<20} {:<20} {:<15}".format(
        "MÃ ĐƠN", "TÊN ĐẠI LÝ", "GIÁ TRỊ", "TRẠNG THÁI"
    ))

    for order in orders_list:
        print("{:<10} {:<20} {:<20,.0f} {:<15}".format(
            order["id"],
            order["agent_name"],
            order["total_amount"],
            order["status"]
        ))


def create_order(orders_list):
    order_id = input("Nhập mã đơn hàng: ").strip()

    for order in orders_list:
        if order["id"] == order_id:
            print("[Lỗi] ERR-01: Mã đơn hàng này đã tồn tại trong hệ thống!")
            return

    agent_name = input("Nhập tên đại lý: ").strip()

    while agent_name == "":
        print("[Lỗi]: Tên đại lý không được để trống!")
        agent_name = input("Nhập tên đại lý: ").strip()

    while True:
        try:
            total_amount = float(input("Nhập giá trị đơn hàng: "))

            if total_amount <= 0:
                print("[Lỗi] ERR-02: Giá trị đơn hàng phải là số tiền lớn hơn 0!")
            else:
                break

        except:
            print("[Lỗi] ERR-02: Giá trị đơn hàng phải là số tiền lớn hơn 0!")

    new_order = {
        "id": order_id,
        "agent_name": agent_name,
        "total_amount": total_amount,
        "status": "Unpaid"
    }

    orders_list.append(new_order)
    print(f"[Thành công]: Đã thêm đơn hàng {order_id}")


def update_payment_status(orders_list):
    if len(orders_list) == 0:
        print("[Thông báo]: Chưa có đơn hàng nào trong hệ thống!")
        return

    order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip()

    for order in orders_list:
        if order["id"] == order_id:

            if order["status"] == "Paid":
                print("[Lỗi] ERR-04: Đơn hàng này đã được thanh toán trước đó!")
                return

            order["status"] = "Paid"
            print(f"[Thành công]: Đơn hàng {order_id} đã được cập nhật trạng thái ĐÃ THANH TOÁN")
            return

    print(f"[Lỗi] ERR-03: Không tìm thấy đơn hàng nào có mã {order_id}!")


def calculate_financials(orders_list):
    total_revenue = 0

    for order in orders_list:
        if order["status"] == "Paid":
            total_revenue += order["total_amount"]

    discount = 0

    if total_revenue >= 100000000:
        discount = total_revenue * 0.05

    return total_revenue, discount


def main():
    orders_list = []

    while True:
        print("\n===== QUẢN LÝ ĐƠN HÀNG ĐẠI LÝ =====")
        print("1. Xem danh sách đơn hàng")
        print("2. Tạo mới đơn hàng")
        print("3. Cập nhật trạng thái thanh toán")
        print("4. Tính doanh thu và chiết khấu")
        print("5. Thoát")

        try:
            choice = int(input("Nhập lựa chọn của bạn: "))

            if choice == 1:
                show_orders(orders_list)

            elif choice == 2:
                create_order(orders_list)

            elif choice == 3:
                update_payment_status(orders_list)

            elif choice == 4:
                total_revenue, discount = calculate_financials(orders_list)

                print("\n===== BÁO CÁO TÀI CHÍNH =====")
                print(f"Tổng doanh thu thực tế: {total_revenue:,.0f} VND")
                print(f"Chiết khấu doanh nghiệp: {discount:,.0f} VND")

            elif choice == 5:
                print("Thoát chương trình!")
                break

            else:
                print("[Lỗi] ERR-05: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5!")

        except:
            print("[Lỗi] ERR-05: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5!")


main()