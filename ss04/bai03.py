quantity = int(input("Nhập số lượng hóa đơn trong ca: "))

i = 1
max = None;
min = None;
while(i <= quantity):
    value = float(input(f"Nhập giá trị hóa đơn thứ {i}: "))
    if (max is None or max < value):
        max = value;
    if(min is None or value < min):
        min = value;
    i += 1;

print(f"--- KẾT QUẢ KIỂM TRA TOÁN CA RIKKEI STORE ---")
print(f"Hóa đơn giá trị cao nhất: {int(max)} VND")
print(f"Hoaas đơn có giá trị thấp nhất: {int(min)} VND")

