import logging

logging.basicConfig(
    filename = "information.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {
        "name": "Phin Sữa Đá",
        "price": 35000
    },
    "F1": {
        "name": "Freeze Trà Xanh",
        "price": 55000
    },
    "T1": {
        "name": "Trà Sen Vàng",
        "price": 45000
    }
}

current_order = []


def invalid_quantity_error():
    """Raise invalid quantity error."""
    raise Exception(
        "InvalidQuantityError"
    )


def item_not_found_error():
    """Raise item not found error."""
    raise Exception(
        "ItemNotFoundError"
    )


def display_menu():
    """Display main menu."""
    print(
        "\n========== "
        "HIGHLANDS MINI POS "
        "=========="
    )
    print("1. Xem thực đơn")
    print("2. Thêm món vào giỏ")
    print(
        "3. Xem giỏ hàng "
        "& Tính tổng tiền"
    )
    print(
        "4. Thanh toán "
        "& Xóa giỏ hàng"
    )
    print("5. Thoát ca làm việc")
    print(
        "===================="
        "===================="
    )


def view_menu():
    """Display drink menu."""
    print(
        "\n--- THỰC ĐƠN "
        "HIGHLANDS COFFEE ---"
    )

    for code, drink in (
        DRINK_MENU.items()
    ):
        print(
            f"[{code}] - "
            f"{drink['name']} - "
            f"{drink['price']:,} "
            f"VNĐ"
        )


def validate_drink_code(
    drink_code
):
    """Validate drink code."""
    drink_code = (
        drink_code
        .strip()
        .upper()
    )

    if drink_code not in (
        DRINK_MENU
    ):
        logging.warning(
            "ItemNotFoundError "
            "- Code: %s",
            drink_code
        )

        item_not_found_error()

    return drink_code


def validate_quantity(
    quantity
):
    """Validate quantity."""
    if quantity <= 0:
        logging.warning(
            "InvalidQuantityError "
            "- Quantity: %s",
            quantity
        )

        invalid_quantity_error()


def add_to_order(
    current_order
):
    """Add drink to order."""
    print(
        "\n--- THÊM MÓN "
        "VÀO GIỎ ---"
    )

    try:
        drink_code = input(
            "Nhập mã đồ uống: "
        )

        drink_code = (
            validate_drink_code(
                drink_code
            )
        )

        quantity = int(
            input(
                "Nhập số lượng: "
            )
        )

        validate_quantity(
            quantity
        )

        current_order.append(
            {
                "code":
                drink_code,
                "quantity":
                quantity
            }
        )

        logging.info(
            "Added %s of %s "
            "to order",
            quantity,
            drink_code
        )

        drink_name = (
            DRINK_MENU
            [drink_code]
            ["name"]
        )

        print(
            f"Đã thêm "
            f"{quantity} x "
            f"{drink_name} "
            f"vào giỏ hàng."
        )

    except ValueError:
        logging.error(
            "ValueError - "
            "Invalid quantity "
            "input"
        )

        print(
            "Vui lòng nhập "
            "số lượng là "
            "một số nguyên!"
        )

    except Exception as error:
        if str(error) == (
            "ItemNotFoundError"
        ):
            print(
                "Mã đồ uống "
                "không hợp lệ, "
                "vui lòng kiểm "
                "tra lại thực đơn!"
            )

        elif str(error) == (
            "InvalidQuantityError"
        ):
            print(
                "Số lượng phải "
                "lớn hơn 0!"
            )


def calculate_total(
    current_order
):
    """Calculate total."""
    total = 0

    for item in (
        current_order
    ):
        code = item["code"]

        quantity = item[
            "quantity"
        ]

        price = (
            DRINK_MENU
            [code]
            ["price"]
        )

        total += (
            price
            * quantity
        )

    return total


def view_order(
    current_order
):
    """Display cart."""
    if not current_order:
        print(
            "Giỏ hàng trống, "
            "vui lòng chọn món "
            "(Chức năng 2)."
        )
        return

    print(
        "\n--- GIỎ HÀNG "
        "HIỆN TẠI ---"
    )

    print(
        "Mã SP | "
        "Tên đồ uống "
        "| Đơn giá | "
        "Số lượng | "
        "Thành tiền"
    )

    print("-" * 65)

    for item in (
        current_order
    ):
        code = item["code"]

        quantity = item[
            "quantity"
        ]

        drink = (
            DRINK_MENU
            [code]
        )

        subtotal = (
            drink["price"]
            * quantity
        )

        print(
            f"{code:<5} | "
            f"{drink['name']:<20} "
            f"| "
            f"{drink['price']:,} "
            f"| {quantity:<8} "
            f"| "
            f"{subtotal:,} "
            f"VNĐ"
        )

    print("-" * 65)

    total = (
        calculate_total(
            current_order
        )
    )

    print(
        f"Tổng tiền "
        f"cần thanh toán: "
        f"{total:,} VNĐ"
    )


def checkout(
    current_order
):
    """Checkout order."""
    if not current_order:
        print(
            "Giỏ hàng trống, "
            "vui lòng chọn món "
            "(Chức năng 2)."
        )
        return

    print(
        "\n--- THANH TOÁN ---"
    )

    total = (
        calculate_total(
            current_order
        )
    )

    print(
        f"Tổng tiền cần "
        f"thanh toán: "
        f"{total:,} VNĐ"
    )

    confirm = input(
        f"Xác nhận "
        f"thanh toán "
        f"{total:,} VNĐ "
        f"(y/n): "
    ).lower()

    if confirm == "y":
        print(
            "Thanh toán "
            "thành công."
        )

        logging.info(
            "Checkout "
            "successful"
        )

        current_order.clear()

        print(
            "Giỏ hàng đã "
            "được làm trống."
        )

    elif confirm == "n":
        print(
            "Đã hủy thao tác "
            "thanh toán. "
            "Quay lại menu "
            "chính."
        )

    else:
        print(
            "Lựa chọn không "
            "hợp lệ. "
            "Thanh toán "
            "đã bị hủy."
        )


def main():
    """Run program."""
    while True:
        display_menu()

        choice = input(
            "Chọn chức năng "
            "(1-5): "
        )

        if choice == "1":
            view_menu()

        elif choice == "2":
            add_to_order(
                current_order
            )

        elif choice == "3":
            view_order(
                current_order
            )

        elif choice == "4":
            checkout(
                current_order
            )

        elif choice == "5":
            logging.info(
                "Cashier "
                "logged out. "
                "System shutdown."
            )

            print(
                "Đã thoát ca "
                "làm việc. "
                "Hẹn gặp lại!"
            )
            break

        else:
            print(
                "Lựa chọn "
                "không hợp lệ!"
            )


main()