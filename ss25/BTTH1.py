class BankAccount: 
    bank_name = "Vietcombank"
    transaction_fee = 2000
    def __init__(self, number, name):
        self.__account_number  = number
        self.__account_name = name
        self.__balance = 0
    @property
    def balance(self):
        return self.__balance
    @property 
    def account_name(self):
        return self.__account_name
    @account_name.setter
    def account_name(self, name : str):
        self.__account_name = name.strip().upper()

    @staticmethod
    def validate_account_number(account_number: str):
        if account_number.isdigit() and len(account_number) == 10:
            return True
        else:
            return False
        
    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee
    
    def deposit(self,amount):
        self.__balance += amount
    
    def withdraw(self, amount): 
        total = amount + self.transaction_fee
        if self.__balance < total:
            print("số dư tài khoản không đủ")
            return
        else: 
            self.__balance -= total
            print("rút tiền thành công")
    def display_info(self):
        print(f"Tên Ngân hàng: {self.bank_name}")
        print(f"Số TK: {self.__account_number}")
        print(f"Tên chủ TK: {self.account_name}")
        print(f"số dư hiện tại: {self.balance}")



def main(): 
    current_account = None
    while True :
        print("""===== VIETCOMBANK DIGIBANK SIMULATOR =====
                    1. Mở tài khoản mới
                    2. Xem thông tin tài khoản
                    3. Giao dịch Nạp / Rút tiền
                    4. Cập nhật Tên chủ tài khoản
                    5. Đổi phí giao dịch hệ thống
                    6. Thoát chương trình
                    ==========================================
                    """)
        choice = input("Chọn chức năng (1-6): ")
        match choice :
            case "1": 
                while True: 
                    acc_number_input = input("nhập số TK:")
                    acc_name_input = input("nhập tên TK:")
                    if BankAccount.validate_account_number(acc_number_input):
                        new_account = BankAccount(acc_number_input,acc_name_input)
                        new_account.account_name
                        current_account = new_account
                        print("Mở tài khoản thành công!")
                        break
                    else :
                        print("Số TK không hợp lệ!")
            case "2": 
                if current_account is None: 
                    print("hệ thống chưa có tài khoản")
                else:
                    current_account.display_info()
            case "3":
                choice = input("Nạp hoặc Rút").strip().lower()
                amount = float(input("nhập số tiền:"))
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản")
                    break
                match choice:
                    case "Nạp": 
                        current_account.deposit(amount)
                    case "Rút":
                        current_account.withdraw(amount)
                print(f"SỐ DƯ MỚI: {current_account.balance}")
            case "4":
                new_name = input("nhập tên cần cập nhật:")
                current_account.account_name = new_name 
                print("Cập nhật thành công")
            case "5":
                transaction_fee = input("nhập phí giao dịch mới: ")
                BankAccount.update_transaction_fee(transaction_fee)
            case "6":
                break
            case _: 
                print("lựa không phù hợp")

main()



        