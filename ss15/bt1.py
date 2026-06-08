inventory_stock = 100
total_revenue = 0.0

menu = """
========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
"""

def add_stock(amount):
    """
    Hàm nhập thêm hàng vào kho.
    Tham số:
        amount (int): số lượng sản phẩm muốn thêm.
    Trả về:
        None. Hàm cập nhật trực tiếp biến global inventory_stock.
    """
    global inventory_stock
    if amount <= 0:
        print("Lỗi: Dữ liệu nhập vào phải lớn hơn 0.")
        return
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")

def process_sale(quantity):
    """
    Hàm kiểm tra kho trước khi bán hàng.
    Tham số:
        quantity (int): số lượng sản phẩm khách muốn mua.
    Trả về:
        True nếu đủ hàng, False nếu không đủ hoặc dữ liệu không hợp lệ.
    """
    global inventory_stock
    if quantity <= 0:
        print("Lỗi: Dữ liệu nhập vào phải lớn hơn 0.")
        return False
    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}")
        return False
    return True

def calculate_final_price(quantity, price):
    """
    Hàm tính toán tổng tiền cuối cùng của đơn hàng.
    Tham số:
        quantity (int): số lượng sản phẩm mua.
        price (float): đơn giá mỗi sản phẩm.
    Trả về:
        final_total (float): tổng tiền sau giảm giá và thuế.
    """
    global inventory_stock, total_revenue
    if price <= 0:
        print("Lỗi: Đơn giá phải lớn hơn 0.")
        return None

    total_temp = quantity * price
    discount = 0
    if total_temp >= 1000:
        discount = total_temp * 0.1
    subtotal = total_temp - discount
    vat = subtotal * 0.08
    final_total = subtotal + vat

    inventory_stock -= quantity
    total_revenue += final_total

    bill = f"""
-> Hóa đơn chi tiết:
Số lượng: {quantity} | Đơn giá: ${price}
Tạm tính: ${total_temp}
Giảm giá (10%): ${discount}
Thuế VAT (8%): ${vat}
Tổng thanh toán: ${final_total}
Đã bán thành công!
"""
    print(bill)
    return final_total

def print_report():
    """In báo cáo tổng quan về tồn kho và doanh thu."""
    global inventory_stock, total_revenue
    report = f"""
--- BÁO CÁO KINH DOANH ---
Tồn kho hiện tại: {inventory_stock} sản phẩm
Tổng doanh thu: ${total_revenue}
"""
    print(report)

def main():
    """Hàm main() chạy vòng lặp menu CLI."""
    try:
        while True:
            print(menu)
            select = input("Chọn chức năng (1-4): ")

            if not select.isdigit():
                print("Bạn cần nhập số! Yêu cầu nhập lại!")
                continue

            select = int(select)

            if select == 1:
                print("--- NHẬP HÀNG ---")
                try:
                    amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))
                    add_stock(amount)
                except ValueError:
                    print("Bạn cần nhập số nguyên!")
            elif select == 2:
                print("--- BÁN HÀNG ---")
                try:
                    quantity = int(input("Nhập số lượng mua: "))
                    price = float(input("Nhập đơn giá ($): "))
                    if process_sale(quantity):
                        calculate_final_price(quantity, price)
                except ValueError:
                    print("Bạn cần nhập số!")
            elif select == 3:
                print_report()
            elif select == 4:
                print("Thoát chương trình thành công!")
                break
            else:
                print("Vui lòng chọn đúng chức năng! Chức năng từ 1 - 4 ")
    except KeyboardInterrupt:
        print("\nChương trình bị dừng bởi người dùng.")

if __name__ == "__main__":
    main()

# Phân tích & Thiết kế (Yêu cầu 1)
# Biến Global:

# inventory_stock: lưu số lượng sản phẩm trong kho.

# total_revenue: lưu tổng doanh thu.

# Biến Local:

# Các biến trong hàm như amount, quantity, price, discount, vat, final_total… chỉ tồn tại trong phạm vi hàm.

# Luồng chạy:

# Người dùng chọn chức năng từ menu.

# Hệ thống gọi hàm tương ứng (add_stock, process_sale, calculate_final_price, print_report).

# Các hàm cập nhật biến global hoặc in báo cáo.

# Vòng lặp main() duy trì CLI cho đến khi chọn thoát.