sum = 0;
count = 0;
number = 0;
for i in range (1, 8, 1):
    revenue = int(input(f"Nhập doanh thu Ngày {i}: "))
    sum += revenue;
    count += 1
    if(revenue >= 5000000):
        number += 1

avg = sum / count;
print("--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print(f"Tổng doanh thu cả tuần: {sum} VND")
print(f"Doanh thu trung bình mỗi ngày: {avg} VND")
print(f"Số ngày đạt doanh thu mục tiêu (>= 5000000 VND): {number:2f} ngày")
