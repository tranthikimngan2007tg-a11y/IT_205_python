MAX_CHANCE = 5
number_lucky = 30
count = 0
for i in range(1, MAX_CHANCE + 1, 1):
    number = int(input(f"\nLượt đoán {i} - Nhập số của bạn: "))
    if(number == number_lucky):
        print("=> Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        print("--- TRÒ CHƠI KẾT THÚC ---")
        count = 1
        break
    else:
        if(number > number_lucky):
            print("=> Gợi ý: Số của bạn lớn hơn mã số may mắn!")
        else:
            print(f"=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!");

if(count != 1):
    print("\nBạn đã sử dụng hết lượt đón rồi! hehe")
    print("\n--- TRÒ CHƠI KẾT THÚC ---")