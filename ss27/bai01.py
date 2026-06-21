# PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# 1. SƠ ĐỒ KIẾN TRÚC HỆ THỐNG
#
#                   BaseAccount (Abstract Class)
#                           |
#         -----------------------------------------
#         |                                       |
#         v                                       v
#   SavingsAccount                        CreditAccount
#         |
#         v
#   HybridAccount
#         ^
#         |
# DigitalPremiumMixin
#
# VNPayGateway
# ViettelMoneyGateway
#
# process_payment()
#
# BaseAccount là lớp trừu tượng đóng vai trò lớp cha của toàn bộ
# hệ thống tài khoản. Lớp này quản lý các thuộc tính chung như
# số tài khoản, tên chủ tài khoản, số dư và định nghĩa các hành vi
# bắt buộc gồm deposit() và withdraw().
#
# SavingsAccount kế thừa BaseAccount để quản lý tài khoản tiết kiệm,
# hỗ trợ tính lãi suất và xử lý phí rút tiền trước hạn.
#
# CreditAccount kế thừa BaseAccount để quản lý tài khoản tín dụng,
# cho phép số dư âm trong phạm vi hạn mức tín dụng được cấp.
#
# DigitalPremiumMixin là lớp bổ trợ cung cấp tính năng hoàn tiền
# cho các giao dịch giá trị lớn.
#
# HybridAccount sử dụng cơ chế đa kế thừa từ SavingsAccount và
# DigitalPremiumMixin. Nhờ đó tài khoản Hybrid vừa có khả năng
# sinh lãi như tài khoản tiết kiệm vừa có khả năng hoàn tiền
# như dịch vụ số cao cấp.

# 2. MRO (METHOD RESOLUTION ORDER)
#
# Python sử dụng MRO (Method Resolution Order) để xác định thứ tự
# tìm kiếm thuộc tính và phương thức khi sử dụng đa kế thừa.
#
# Đối với lớp HybridAccount:
#
# HybridAccount
# -> SavingsAccount
# -> DigitalPremiumMixin
# -> BaseAccount
# -> ABC
# -> object
#
# Khi gọi một phương thức trên đối tượng HybridAccount,
# Python sẽ tìm kiếm lần lượt theo thứ tự trên.
#
# Ví dụ:
#
# hybrid.deposit(1000000)
#
# Python sẽ kiểm tra:
# 1. HybridAccount
# 2. SavingsAccount
# 3. DigitalPremiumMixin
# 4. BaseAccount
# 5. ABC
# 6. object
#
# Nếu phương thức được tìm thấy ở lớp nào thì việc tìm kiếm sẽ
# dừng lại tại lớp đó.
#
# Cơ chế MRO giúp Python giải quyết xung đột khi nhiều lớp cha
# cùng chứa phương thức có tên giống nhau trong mô hình đa kế thừa.

# 3. DUCK TYPING
#
# Hệ thống sử dụng Duck Typing trong chức năng thanh toán hóa đơn.
#
# Hàm:
#
# process_payment(payment_gateway, account, amount)
# không quan tâm payment_gateway thuộc lớp VNPayGateway,
# ViettelMoneyGateway hay bất kỳ lớp nào khác.
# Điều kiện duy nhất là đối tượng được truyền vào phải có
# phương thức:
# execute_pay(account, amount)
# Ví dụ:
# class VNPayGateway:
#     def execute_pay(self, account, amount):
#         ...
# class ViettelMoneyGateway:
#     def execute_pay(self, account, amount):
#         ...
# Trong tương lai có thể bổ sung:

# class MoMoGateway:
#     def execute_pay(self, account, amount):
#         ...
# class ZaloPayGateway:
#     def execute_pay(self, account, amount):
#         ...
# mà không cần sửa đổi mã nguồn của BaseAccount,
# SavingsAccount, CreditAccount hoặc HybridAccount.
#
# Nhờ cơ chế Duck Typing, hệ thống có khả năng mở rộng rất cao,
# giảm sự phụ thuộc giữa các thành phần và tuân thủ nguyên tắc
# Open/Closed Principle (OCP) trong thiết kế phần mềm.

from abc import ABC, abstractmethod


class BaseAccount(ABC):
    bank_name = "Vietcombank"

    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def _set_balance(self, amount):
        self.__balance = amount

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = " ".join(value.strip().upper().split())

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance + other.balance

    def __lt__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance < other.balance

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name


class SavingsAccount(BaseAccount):
    def __init__(self, account_number, owner_name, interest_rate, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self._set_balance(self.balance + amount)

    def withdraw(self, amount):
        fee = amount * 0.02
        total = amount + fee

        if total > self.balance:
            raise ValueError("Insufficient balance")

        self._set_balance(self.balance - total)
        return fee

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self._set_balance(self.balance + interest)
        return interest


class CreditAccount(BaseAccount):
    def __init__(self, account_number, owner_name, credit_limit, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.credit_limit = credit_limit

    def deposit(self, amount):
        self._set_balance(self.balance + amount)

    def withdraw(self, amount):
        if self.balance - amount < -self.credit_limit:
            raise ValueError("Vượt quá hạn mức thấu chi cho phép")

        self._set_balance(self.balance - amount)


class DigitalPremiumMixin:
    def cashback_reward(self, amount):
        if amount > 5_000_000:
            cashback = amount * 0.01
            self.deposit(cashback)
            return cashback
        return 0


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    pass


class VNPayGateway:
    def execute_pay(self, account, amount):
        print(
            f"[Hệ thống VNPay]: Đang kết nối tới tài khoản {account.account_number}..."
        )
        account.withdraw(amount)


class ViettelMoneyGateway:
    def execute_pay(self, account, amount):
        print(
            f"[Hệ thống Viettel Money]: Đang kết nối tới tài khoản {account.account_number}..."
        )
        account.withdraw(amount)


def process_payment(payment_gateway, account, amount):
    try:
        payment_gateway.execute_pay(account, amount)
        print("Xác thực thanh toán bằng Duck Typing thành công!")
        print(f"Tài khoản đã thanh toán hóa đơn giá trị: {amount:,.0f} VND.")
        print(f"Số dư mới: {account.balance:,.0f} VND")
    except AttributeError:
        print("Cổng thanh toán không hợp lệ hoặc chưa được tích hợp")
    except Exception as e:
        print(e)


def select_account(accounts):
    if not accounts:
        return None

    print("\n--- DANH SÁCH TÀI KHOẢN ---")
    for i, acc in enumerate(accounts, start=1):
        print(
            f"{i}. {acc.account_number} - {acc.owner_name} ({acc.balance:,.0f} VND)"
        )

    try:
        choice = int(input("Chọn tài khoản: "))
        return accounts[choice - 1]
    except:
        return None


def open_account(accounts):
    print("\n--- CHỌN LOẠI TÀI KHOẢN ---")
    print("1. Savings Account")
    print("2. Credit Account")
    print("3. Hybrid Account")

    account_type = input("Chọn loại tài khoản (1-3): ")

    account_number = input("Nhập số tài khoản 10 chữ số: ")

    if not BaseAccount.validate_account_number(account_number):
        print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
        return None

    owner_name = input("Nhập tên chủ tài khoản: ")

    if account_type == "1":
        interest_rate = float(input("Nhập lãi suất năm: "))
        acc = SavingsAccount(
            account_number,
            owner_name,
            interest_rate,
            10_000_000
        )

    elif account_type == "2":
        credit_limit = float(input("Nhập hạn mức tín dụng: "))
        acc = CreditAccount(
            account_number,
            owner_name,
            credit_limit
        )

    elif account_type == "3":
        interest_rate = float(input("Nhập lãi suất năm: "))
        acc = HybridAccount(
            account_number,
            owner_name,
            interest_rate,
            10_000_000
        )
    else:
        print("Loại tài khoản không hợp lệ")
        return None

    accounts.append(acc)

    print("\nMở tài khoản thành công!")
    print("Chủ tài khoản:", acc.owner_name)

    return acc


def show_info(account):
    if not account:
        print("Hệ thống chưa có thông tin tài khoản.")
        return

    print("\n--- THÔNG TIN TÀI KHOẢN ---")
    print("Loại tài khoản:", type(account).__name__)
    print("Ngân hàng:", account.bank_name)
    print("Số tài khoản:", account.account_number)
    print("Chủ tài khoản:", account.owner_name)
    print(f"Số dư: {account.balance:,.0f} VND")

    if hasattr(account, "interest_rate"):
        print(f"Lãi suất: {account.interest_rate * 100:.1f}%")

    if hasattr(account, "credit_limit"):
        print(f"Hạn mức tín dụng: {account.credit_limit:,.0f} VND")

    print("\nMRO:")
    for cls in type(account).mro():
        print(cls.__name__)


def transaction(account):
    if not account:
        print("Chưa có tài khoản.")
        return

    print("\n1. Nạp tiền")
    print("2. Rút tiền")

    choice = input("Chọn giao dịch: ")
    amount = float(input("Nhập số tiền: "))

    try:
        if choice == "1":
            account.deposit(amount)
            print("Nạp tiền thành công!")

            if isinstance(account, HybridAccount):
                cashback = account.cashback_reward(amount)

                if cashback:
                    print(
                        f"[Ưu đãi Premium]: Hoàn tiền {cashback:,.0f} VND"
                    )

            print(f"Số dư mới: {account.balance:,.0f} VND")

        elif choice == "2":
            if isinstance(account, SavingsAccount) and not isinstance(
                account,
                CreditAccount
            ):
                fee = account.withdraw(amount)
                print("Rút tiền thành công!")
                print(f"Phí phạt: {fee:,.0f} VND")
            else:
                account.withdraw(amount)
                print("Rút tiền thành công!")

            print(f"Số dư hiện tại: {account.balance:,.0f} VND")

    except Exception as e:
        print(e)


def apply_interest(account):
    if isinstance(account, (SavingsAccount, HybridAccount)):
        before = account.balance
        interest = account.apply_interest()

        print("\n--- TÍNH LÃI ---")
        print(f"Số dư trước: {before:,.0f} VND")
        print(f"Tiền lãi: +{interest:,.0f} VND")
        print(f"Số dư mới: {account.balance:,.0f} VND")
    else:
        print("Tài khoản hiện tại không hỗ trợ tính lãi.")


def compare_accounts(accounts, current_account):
    if len(accounts) < 2:
        print("Cần ít nhất 2 tài khoản.")
        return

    print("\n--- DANH SÁCH TÀI KHOẢN ---")

    others = [acc for acc in accounts if acc != current_account]

    for i, acc in enumerate(others, start=1):
        print(
            f"{i}. {acc.account_number} - {acc.owner_name} ({acc.balance:,.0f} VND)"
        )

    try:
        choice = int(input("Chọn tài khoản đối ứng: "))
        other = others[choice - 1]

        if current_account < other:
            print("Tài khoản hiện tại NHỎ HƠN tài khoản đối ứng.")
        else:
            print("Tài khoản hiện tại KHÔNG NHỎ HƠN tài khoản đối ứng.")

        print(
            f"Tổng số dư: {(current_account + other):,.0f} VND"
        )

    except Exception as e:
        print(e)


def payment(account):
    if not account:
        print("Chưa có tài khoản.")
        return

    print("\n1. VNPay")
    print("2. Viettel Money")

    choice = input("Chọn cổng thanh toán: ")
    amount = float(input("Nhập số tiền hóa đơn: "))

    gateway = VNPayGateway() if choice == "1" else ViettelMoneyGateway()

    process_payment(gateway, account, amount)


def main():
    accounts = []
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin & MRO")
        print("3. Giao dịch Nạp / Rút")
        print("4. Áp dụng lãi suất")
        print("5. So sánh & Gộp tài khoản")
        print("6. Thanh toán hóa đơn")
        print("7. Chọn tài khoản hiện tại")
        print("8. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            acc = open_account(accounts)
            if acc:
                current_account = acc

        elif choice == "2":
            show_info(current_account)

        elif choice == "3":
            transaction(current_account)

        elif choice == "4":
            apply_interest(current_account)

        elif choice == "5":
            compare_accounts(accounts, current_account)

        elif choice == "6":
            payment(current_account)

        elif choice == "7":
            selected = select_account(accounts)
            if selected:
                current_account = selected
                print("Đã chuyển tài khoản hiện tại.")

        elif choice == "8":
            print(
                "Cảm ơn đã trải nghiệm hệ thống Vietcombank Digibank Pro Simulator!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()