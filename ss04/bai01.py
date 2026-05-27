total_invoice = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---");

if(total_invoice >= 500000):
    discount_money = total_invoice * 0.1;
else:
    discount_money = 0;

print("Số tiền được giảm giá: ", int(discount_money),"VND");
print("Tổng tiền khách phải ", int(total_invoice) - int(discount_money),"VND");