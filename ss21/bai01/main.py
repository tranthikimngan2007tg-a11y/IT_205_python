import logging
import re


logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InvalidAmountError(Exception):
    """Raised when transaction amount is invalid."""


class InsufficientBalanceError(Exception):
    """Raised when wallet balance is insufficient."""


def display_menu():
    """Display CLI menu."""
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("====================================")


def validate_amount(amount):
    """Validate transaction amount."""
    if amount <= 0:
        logging.error(
            "InvalidAmountError: Attempted to process "
            "%s VND.", amount
        )
        raise InvalidAmountError(
            "Số tiền giao dịch phải lớn hơn 0."
        )


def validate_phone(phone):
    """Validate phone number format."""
    pattern = r"^\d{10}$"

    if not re.match(pattern, phone):
        return False

    return True


def deposit(balance):
    """Handle deposit transaction."""
    print("\n--- NẠP TIỀN VÀO VÍ ---")

    while True:
        try:
            amount = int(
                input("Nhập số tiền cần nạp: ")
            )

            validate_amount(amount)

            balance += amount

            logging.info(
                "Deposit successful: +%s VND. "
                "Current Balance: %s",
                amount,
                balance
            )

            print(
                f"\nNạp tiền thành công: "
                f"+{amount:,} VND"
            )
            print(
                f"Số dư hiện tại: "
                f"{balance:,} VND"
            )

            return balance

        except ValueError:
            logging.error(
                "ValueError: Invalid numeric "
                "input for deposit."
            )
            print(
                "Lỗi: Vui lòng nhập "
                "số tiền hợp lệ."
            )

        except InvalidAmountError as error:
            print(f"Lỗi: {error}")


def transfer(balance):
    """Handle transfer transaction."""
    print("\n--- CHUYỂN TIỀN ---")

    phone = input(
        "Nhập số điện thoại người nhận: "
    )

    if not validate_phone(phone):
        print(
            "Lỗi: Số điện thoại "
            "không hợp lệ."
        )
        return balance

    try:
        amount = int(
            input("Nhập số tiền cần chuyển: ")
        )

        validate_amount(amount)

        if amount > balance:
            logging.error(
                "InsufficientBalanceError: "
                "Attempted to transfer "
                "%s VND with balance "
                "%s VND.",
                amount,
                balance
            )

            raise InsufficientBalanceError(
                "Số dư của bạn không đủ."
            )

        if amount >= 10000000:
            logging.warning(
                "High value transaction "
                "detected: %s VND "
                "to %s",
                amount,
                phone
            )

        balance -= amount

        logging.info(
            "Transfer successful: "
            "-%s VND to %s. "
            "Current Balance: %s",
            amount,
            phone,
            balance
        )

        print(
            f"\nChuyển tiền thành công "
            f"tới số điện thoại {phone}."
        )
        print(
            f"Số tiền đã chuyển: "
            f"{amount:,} VND"
        )
        print(
            f"Số dư còn lại: "
            f"{balance:,} VND"
        )

    except ValueError:
        logging.error(
            "ValueError: Invalid numeric "
            "input for transfer."
        )
        print(
            "Lỗi: Vui lòng nhập "
            "số tiền hợp lệ."
        )

    except InvalidAmountError as error:
        print(f"Lỗi: {error}")

    except InsufficientBalanceError as error:
        print(
            f"Giao dịch thất bại: "
            f"{error}"
        )
        print(
            f"Số dư hiện tại: "
            f"{balance:,} VND"
        )

    return balance

def check_balance(balance):
    """Display current balance."""
    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(
        f"Số dư hiện tại: "
        f"{balance:,} VND"
    )

    logging.info(
        "Balance checked. "
        "Current Balance: %s",
        balance
    )

def main():
    """Run wallet application."""
    balance = 0

    while True:
        display_menu()

        choice = input(
            "Chọn chức năng (1-4): "
        )

        if choice == "1":
            balance = deposit(balance)

        elif choice == "2":
            balance = transfer(balance)

        elif choice == "3":
            check_balance(balance)

        elif choice == "4":
            print(
                "Cảm ơn bạn đã "
                "sử dụng dịch vụ"
            )

            logging.info(
                "System shutdown"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ."
            )

main()