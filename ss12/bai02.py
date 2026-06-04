# B1: Khởi tạo danh sách saving_accounts

# B2: Hiển thị menu

# B3: Người dùng chọn chức năng

# Nếu chọn 1:
#     Hiển thị toàn bộ sổ tiết kiệm

# Nếu chọn 2:
#     Nhập thông tin sổ mới
#     Validate dữ liệu
#     Kiểm tra mã trùng
#     Nếu hợp lệ → thêm mới

# Nếu chọn 3:
#     Nhập mã sổ
#     Tìm sổ
#     Nếu không tồn tại → báo lỗi
#     Nếu closed → báo lỗi
#     Nếu hợp lệ → cập nhật

# Nếu chọn 4:
#     Nhập mã sổ
#     Tìm sổ
#     Nếu tồn tại → đổi status = "closed"

# Nếu chọn 5:
#     Nhập mã sổ
#     Tính lãi:
#     lãi = balance * rate /100 * term /12

# Nếu chọn 6:
#     Nhập mã sổ
#     Nhập số tháng thực gửi
#     Nếu < kỳ hạn:
#         dùng lãi suất 0.5%
#     Nếu >= kỳ hạn:
#         dùng lãi suất gốc
#     Tính tổng tiền nhận

# Nếu chọn 7:
#     Thoát chương trình

# Nếu nhập sai menu:
#     Báo lỗi

saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    choice = input("Mời bạn chọn chức năng (1-7): ").strip()

    match choice:

        # ================= CHỨC NĂNG 1 =================
        case "1":
            if len(saving_accounts) == 0:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("\nDanh sách sổ tiết kiệm:")

                for index, account in enumerate(saving_accounts, start=1):
                    print(
                        f"{index}. "
                        f"Mã sổ: {account['account_id']} | "
                        f"Khách hàng: {account['customer_name']} | "
                        f"Số tiền gửi: {account['balance']} | "
                        f"Kỳ hạn: {account['term_months']} tháng | "
                        f"Lãi suất: {account['interest_rate']}%/năm | "
                        f"Trạng thái: {account['status']}"
                    )

        # ================= CHỨC NĂNG 2 =================
        case "2":

            account_id = input(
                "Nhập mã sổ tiết kiệm: "
            ).strip().upper()

            customer_name = input(
                "Nhập tên khách hàng: "
            ).strip()

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            # Kiểm tra mã trùng
            duplicate = False

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    duplicate = True
                    break

            if duplicate:
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue

            # Nhập số tiền gửi
            balance = input("Nhập số tiền gửi: ")

            if not balance.isdigit() or int(balance) <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            balance = int(balance)

            # Nhập kỳ hạn
            term_months = input(
                "Nhập kỳ hạn gửi theo tháng: "
            )

            if not term_months.isdigit() or int(term_months) <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            term_months = int(term_months)

            # Nhập lãi suất
            try:
                interest_rate = float(
                    input("Nhập lãi suất năm: ")
                )

                if interest_rate <= 0:
                    print("Lãi suất không hợp lệ!")
                    continue

            except:
                print("Lãi suất không hợp lệ!")
                continue

            new_account = {
                "account_id": account_id,
                "customer_name": customer_name,
                "balance": balance,
                "term_months": term_months,
                "interest_rate": interest_rate,
                "status": "active"
            }

            saving_accounts.append(new_account)

            print("Mở sổ tiết kiệm thành công!")

        # ================= CHỨC NĂNG 3 =================
        case "3":

            update_id = input(
                "Nhập mã sổ tiết kiệm cần cập nhật: "
            ).strip().upper()

            found = False

            for account in saving_accounts:

                if account["account_id"] == update_id:

                    found = True

                    if account["status"] == "closed":
                        print(
                            "Không thể cập nhật sổ tiết kiệm đã tất toán!"
                        )
                        break

                    customer_name = input(
                        "Nhập tên khách hàng mới: "
                    ).strip()

                    if customer_name == "":
                        print(
                            "Tên khách hàng không được để trống"
                        )
                        break

                    balance = input(
                        "Nhập số tiền gửi mới: "
                    )

                    term_months = input(
                        "Nhập kỳ hạn mới theo tháng: "
                    )

                    if (
                        not balance.isdigit()
                        or int(balance) <= 0
                        or not term_months.isdigit()
                        or int(term_months) <= 0
                    ):
                        print(
                            "Số tiền gửi hoặc kỳ hạn không hợp lệ"
                        )
                        break

                    try:
                        interest_rate = float(
                            input(
                                "Nhập lãi suất năm mới: "
                            )
                        )

                        if interest_rate <= 0:
                            print(
                                "Lãi suất không hợp lệ!"
                            )
                            break

                    except:
                        print("Lãi suất không hợp lệ!")
                        break

                    account["customer_name"] = customer_name
                    account["balance"] = int(balance)
                    account["term_months"] = int(term_months)
                    account["interest_rate"] = interest_rate

                    print("Cập nhật thành công!")
                    break

            if not found:
                print(
                    "Không tìm thấy mã sổ tiết kiệm!"
                )

        # ================= CHỨC NĂNG 4 =================
        case "4":

            close_id = input(
                "Nhập mã sổ tiết kiệm cần tất toán/xóa: "
            ).strip().upper()

            found = False

            for account in saving_accounts:

                if account["account_id"] == close_id:
                    account["status"] = "closed"
                    found = True

                    print("Tất toán thành công!")
                    break

            if not found:
                print(
                    "Không tìm thấy mã sổ tiết kiệm"
                )

        # ================= CHỨC NĂNG 5 =================
        case "5":

            account_id = input(
                "Nhập mã sổ tiết kiệm cần tính lãi: "
            ).strip().upper()

            found = False

            for account in saving_accounts:

                if account["account_id"] == account_id:

                    found = True

                    if account["status"] == "closed":
                        print(
                            "Không thể thao tác với sổ tiết kiệm đã tất toán"
                        )
                        break

                    interest = (
                        account["balance"]
                        * account["interest_rate"]
                        / 100
                        * account["term_months"]
                        / 12
                    )

                    total = (
                        account["balance"]
                        + interest
                    )

                    print(
                        f"Tiền lãi dự kiến: {interest:,.0f}đ"
                    )

                    print(
                        f"Tổng tiền nhận: {total:,.0f}đ"
                    )

                    break

            if not found:
                print(
                    "Không tìm thấy mã sổ tiết kiệm"
                )

        # ================= CHỨC NĂNG 6 =================
        case "6":

            account_id = input(
                "Nhập mã sổ tiết kiệm cần kiểm tra: "
            ).strip().upper()

            found = False

            for account in saving_accounts:

                if account["account_id"] == account_id:

                    found = True

                    if account["status"] == "closed":
                        print(
                            "Không thể thao tác với sổ tiết kiệm đã tất toán"
                        )
                        break

                    months = input(
                        "Nhập số tháng thực gửi: "
                    )

                    if (
                        not months.isdigit()
                        or int(months) <= 0
                    ):
                        print(
                            "Số tháng thực gửi không hợp lệ!"
                        )
                        break

                    months = int(months)

                    # Rút trước hạn
                    if months < account["term_months"]:

                        rate = 0.5

                        print(
                            "Khách hàng rút trước hạn!"
                        )

                    else:
                        rate = account[
                            "interest_rate"
                        ]

                        print(
                            "Khách hàng đủ điều kiện hưởng lãi đúng hạn!"
                        )

                    interest = (
                        account["balance"]
                        * rate
                        / 100
                        * months
                        / 12
                    )

                    total = (
                        account["balance"]
                        + interest
                    )

                    print(
                        f"Tiền lãi thực nhận: {interest:,.0f}đ"
                    )

                    print(
                        f"Tổng tiền thực nhận: {total:,.0f}đ"
                    )

                    break

            if not found:
                print(
                    "Không tìm thấy mã sổ tiết kiệm"
                )

        # ================= CHỨC NĂNG 7 =================
        case "7":
            print("Thoát chương trình...")
            break

        # ================= MENU INVALID =================
        case _:
            print(
                "Lựa chọn không hợp lệ, vui lòng nhập lại"
            )