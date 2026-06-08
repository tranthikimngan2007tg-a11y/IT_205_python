atm_vault_balance = 50000000   # Tiền mặt trong ATM
user_account_balance = 10000000  # Số dư tài khoản người dùng

menu = """
============= SMART ATM =============
1. Xem số dư
2. Nạp tiền
3. Rút tiền
4. Kết thúc giao dịch
=====================================
"""

def display_balances():
    """
    Hiển thị số dư tài khoản và (debug) số tiền mặt trong ATM.
    Trả về:
        None
    """
    global user_account_balance, atm_vault_balance
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")

def deposit_money(amount):
    """
    Nạp tiền vào tài khoản.
    Tham số:
        amount (int): số tiền muốn nạp.
    Trả về:
        True nếu nạp thành công, False nếu dữ liệu không hợp lệ.
    """
    global user_account_balance, atm_vault_balance
    if amount <= 0:
        print("Số tiền không hợp lệ.")
        return False
    user_account_balance += amount
    atm_vault_balance += amount
    print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND.")
    return True

def check_withdrawal_rules(amount):
    """
    Kiểm tra điều kiện rút tiền.
    Tham số:
        amount (int): số tiền khách muốn rút.
    Trả về:
        "INSUFFICIENT_FUNDS" nếu tài khoản không đủ.
        "ATM_OUT_OF_CASH" nếu ATM không đủ tiền mặt.
        "INVALID_AMOUNT" nếu số tiền không hợp lệ hoặc không phải bội số của 50,000.
        "OK" nếu hợp lệ.
    """
    global user_account_balance, atm_vault_balance
    fee = 1100
    total_deduction = amount + fee

    if amount <= 0:
        return "INVALID_AMOUNT"
    if amount % 50000 != 0:
        return "INVALID_AMOUNT"
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    return "OK"

def execute_withdrawal(amount):
    """
    Thực hiện rút tiền sau khi kiểm tra thành công.
    Tham số:
        amount (int): số tiền khách muốn rút.
    Trả về:
        None
    """
    global user_account_balance, atm_vault_balance
    fee = 1100
    total_deduction = amount + fee

    user_account_balance -= total_deduction
    atm_vault_balance -= amount

    print("Giao dịch đang xử lý...")
    print(f"Phí giao dịch: {fee:,} VND")
    print(f"Bạn đã rút thành công {amount:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")

def main():
    """Hàm main() chạy vòng lặp menu CLI."""
    try:
        while True:
            print(menu)
            choice = input("Vui lòng chọn giao dịch (1-4): ")

            if not choice.isdigit():
                print("Bạn cần nhập số! Yêu cầu nhập lại!")
                continue

            choice = int(choice)

            if choice == 1:
                display_balances()

            elif choice == 2:
                print("--- NẠP TIỀN ---")
                try:
                    amount = int(input("Nhập số tiền muốn nạp: "))
                    deposit_money(amount)
                except ValueError:
                    print("Bạn cần nhập số!")

            elif choice == 3:
                print("--- RÚT TIỀN ---")
                try:
                    amount = int(input("Nhập số tiền cần rút: "))
                    status = check_withdrawal_rules(amount)
                    if status == "INVALID_AMOUNT":
                        print("Số tiền rút phải là bội số của 50,000 và lớn hơn 0.")
                    elif status == "INSUFFICIENT_FUNDS":
                        print("Giao dịch thất bại: Tài khoản không đủ số dư.")
                    elif status == "ATM_OUT_OF_CASH":
                        print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                    elif status == "OK":
                        execute_withdrawal(amount)
                except ValueError:
                    print("Bạn cần nhập số!")

            elif choice == 4:
                print("Cảm ơn quý khách đã sử dụng dịch vụ!")
                break

            else:
                print("Vui lòng chọn đúng chức năng! (1-4)")
    except KeyboardInterrupt:
        print("\nChương trình bị dừng bởi người dùng.")

if __name__ == "__main__":
    main()

# Phân tích & Thiết kế
# Khi nào truyền dữ liệu qua Arguments?
# deposit_money(amount): cần truyền số tiền nạp vào để hàm xử lý.

# check_withdrawal_rules(amount): cần truyền số tiền rút để kiểm tra điều kiện.

# execute_withdrawal(amount): cần truyền số tiền rút để thực hiện trừ tiền và in biên lai.

# Các hàm này nhận dữ liệu từ người dùng, nên dùng arguments để truyền vào.

# Khi nào thao tác trực tiếp với Global Variables?
# display_balances(): chỉ đọc và in ra số dư, không cần tham số.

# deposit_money() và execute_withdrawal(): sau khi nhận tham số, sẽ cập nhật trực tiếp user_account_balance và atm_vault_balance.

# main(): gọi các hàm, duy trì vòng lặp CLI, không cần tham số.

# Các hàm này thao tác trực tiếp với global variables để cập nhật trạng thái hệ thống.