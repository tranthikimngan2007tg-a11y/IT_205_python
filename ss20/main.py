#  Tính toán giá sản phẩm sau khi giảm giá
def calculate_payment(amount : float, rate: float) -> float:
    if amount < 0:
        print("Số tiền không được phép âm!")
        raise TypeError("Số tiền âm!")
    # 100.0 - 10% -> 90.0
    # return amount * 1 - (amount * rate)
    return amount * (1 - rate)