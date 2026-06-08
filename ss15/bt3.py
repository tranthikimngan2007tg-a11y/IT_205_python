# Phân tích & Thiết kế
# Biến Global
# available_seats = 50: số ghế trống ban đầu.

# flight_revenue = 0.0: tổng doanh thu ban đầu.

# BASE_PRICE = 2000.0: giá vé cơ bản (hằng số).

# Đây là các biến toàn cục, cần cập nhật trực tiếp khi đặt vé hoặc hủy vé.

# Biến Local
# quantity: số lượng vé nhập vào.

# seat_class: hạng vé (1 Economy, 2 Business).

# service_fee: phí dịch vụ sân bay (5%).

# refund_amount: số tiền hoàn lại khi hủy vé.
# Luồng dữ liệu (Pseudo-code)
# Code
# main():
#     hiển thị menu
#     nếu chọn 1:
#         nhập quantity, seat_class
#         total_price = calculate_ticket_price(quantity, seat_class)
#         nếu đủ ghế:
#             confirm_booking(quantity, total_price)
#         else:
#             báo lỗi overbooking
#     nếu chọn 2:
#         nhập quantity
#         refund = process_refund(quantity)
#         nếu hợp lệ:
#             in số tiền hoàn
#         else:
#             báo lỗi ghost refund
#     nếu chọn 3:
#         print_flight_status()
#     nếu chọn 4:
#         thoát
# Tính toàn vẹn dữ liệu
# Doanh thu (flight_revenue) phải là biến global
# vì nó lưu trạng thái tổng cộng của toàn hệ thống chuyến bay.
# Nếu chỉ dùng biến local, doanh thu sẽ mất khi thoát hàm,
# không phản ánh đúng tình trạng thực tế.
available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0

menu = """
============= SKYBOOKING SYSTEM =============
Chuyến bay: VN2026 | Khởi hành: Hà Nội
1. Đặt vé máy bay
2. Hủy vé & Hoàn tiền
3. Xem tình trạng chuyến bay
4. Đóng hệ thống
=============================================
"""

def calculate_ticket_price(quantity: int, seat_class: int) -> float:
    """
    Tính toán chi phí vé.
    Tham số:
        quantity (int): số lượng vé.
        seat_class (int): hạng vé (1 Economy, 2 Business).
    Trả về:
        float: tổng tiền cuối cùng sau phí dịch vụ.
    """
    if quantity <= 0:
        print("Số lượng vé phải lớn hơn 0.")
        return None
    if seat_class not in [1, 2]:
        print("Hạng vé không hợp lệ. Chỉ chọn 1 (Economy) hoặc 2 (Business).")
        return None

    if seat_class == 1:
        price_per_ticket = BASE_PRICE
        seat_type = "Economy"
    else:
        price_per_ticket = BASE_PRICE * 1.5
        seat_type = "Business"

    subtotal = quantity * price_per_ticket
    service_fee = subtotal * 0.05
    total_price = subtotal + service_fee

    print("-> Xác nhận đặt chỗ:")
    print(f"Số lượng: {quantity} | Hạng: {seat_type}")
    print(f"Tạm tính: ${subtotal}")
    print(f"Phí dịch vụ (5%): ${service_fee}")
    print(f"Tổng thanh toán: ${total_price}")

    return total_price

def confirm_booking(quantity: int, total_price: float):
    """Xử lý đặt vé, cập nhật ghế trống và doanh thu."""
    global available_seats, flight_revenue
    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return
    available_seats -= quantity
    flight_revenue += total_price
    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")

def process_refund(quantity: int) -> float:
    """
    Xử lý hoàn vé.
    Tham số:
        quantity (int): số vé muốn hủy.
    Trả về:
        float: số tiền hoàn lại, hoặc None nếu không hợp lệ.
    """
    global available_seats, flight_revenue
    if quantity <= 0:
        print("Số lượng vé hủy phải lớn hơn 0.")
        return None
    if available_seats + quantity > 50:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return None

    refund_amount = quantity * BASE_PRICE * 0.8
    available_seats += quantity
    flight_revenue -= refund_amount
    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refund_amount} (80% giá cơ bản).")
    print(f"Ghế trống hiện tại: {available_seats}")
    return refund_amount

def print_flight_status():
    """
    In tình trạng chuyến bay VN2026.
    Báo cáo gồm: sức chứa tối đa, số ghế đã đặt, số ghế trống, tổng doanh thu.
    """
    global available_seats, flight_revenue
    booked_seats = 50 - available_seats
    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print("Sức chứa tối đa: 50")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")

def main():
    """Hàm main() chạy vòng lặp CLI."""
    try:
        while True:
            print(menu)
            choice = input("Chọn chức năng (1-4): ")

            if not choice.isdigit():
                print("Bạn cần nhập số! Yêu cầu nhập lại!")
                continue

            choice = int(choice)

            if choice == 1:
                print("--- ĐẶT VÉ MÁY BAY ---")
                try:
                    quantity = int(input("Nhập số lượng vé: "))
                    seat_class = int(input("Chọn hạng vé (1: Economy, 2: Business): "))
                    total_price = calculate_ticket_price(quantity, seat_class)
                    if total_price is not None:
                        confirm_booking(quantity, total_price)
                except ValueError:
                    print("Bạn cần nhập số!")

            elif choice == 2:
                print("--- HỦY VÉ & HOÀN TIỀN ---")
                try:
                    quantity = int(input("Nhập số lượng vé muốn hủy: "))
                    process_refund(quantity)
                except ValueError:
                    print("Bạn cần nhập số!")

            elif choice == 3:
                print_flight_status()

            elif choice == 4:
                print("Đóng hệ thống. Cảm ơn quý khách!")
                break

            else:
                print("Vui lòng chọn đúng chức năng (1-4).")
    except KeyboardInterrupt:
        print("\nChương trình bị dừng bởi người dùng.")

if __name__ == "__main__":
    main()
