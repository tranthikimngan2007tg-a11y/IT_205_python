i = 1
sum = 0 
count = 0
while True:
    value = int(input(f"Khách hàng {i} - Nhập giá trị hóa đơn: "))
    if(value >= 1000000):
        count += 1
    choise = input("Co muón nhập tiếp không? (C/K): ")
    if(choise == "k" or choise == "K"):
        break
    
    sum += value
    i += 1;

print("--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---")
print(f"Tổng số hóa đơn đã xử lý: {i} hóa đơn")
print(f"Tổng doanh thu ngày hôm nay: {int(sum)} VND.")
print(f"Số hóa đon lớn (>= 1000000 VND): {count} hóa đơn.")
print(f"Tỷ lệ hóa đơn lớn đạt: {(count / i) * 100}% trên tổng đơn hàng.")