# PHẦN 1. PHÂN TÍCH THIẾT KẾ (CODE REVIEW & ARCHITECTURE)
# Câu 1. Tại sao point_value_vnd lại được đặt làm Class Attribute thay vì Instance Attribute? Nếu khai báo nó trong hàm __init__ (với self) thì hệ thống sẽ gặp rắc rối gì ở Chức năng số 5?

# point_value_vnd là quy định chung áp dụng cho toàn bộ hệ thống thẻ thành viên.

# Ví dụ:

# 1 điểm = 1000 VNĐ

# Mọi khách hàng đều sử dụng cùng một tỷ giá quy đổi nên thuộc tính này cần được khai báo dưới dạng Class Attribute.

# Ví dụ:

# class MemberCard:
#     point_value_vnd = 1000

# Khi ban giám đốc thay đổi chương trình khuyến mãi:

# 1 điểm = 2000 VNĐ

# chỉ cần gọi:

# MemberCard.update_point_value(2000)

# thì toàn bộ các thẻ trong hệ thống đều tự động áp dụng tỷ giá mới.

# Nếu khai báo trong __init__:

# self.point_value_vnd = 1000

# thì mỗi đối tượng sẽ có một bản sao riêng của tỷ giá.

# Khi cập nhật ở Chức năng 5, lập trình viên sẽ phải cập nhật từng thẻ một, gây mất đồng bộ dữ liệu và làm hệ thống khó quản lý.

# Câu 2. Tại sao is_valid_card_id() lại nên dùng @staticmethod? Có bắt buộc phải khởi tạo (tạo object) một thẻ rồi mới kiểm tra định dạng mã thẻ được không?

# Hàm:

# is_valid_card_id(card_id)

# chỉ có nhiệm vụ kiểm tra chuỗi mã thẻ có đúng định dạng hay không.

# Ví dụ:

# RC01
# RC99

# Hàm này không sử dụng dữ liệu của đối tượng (self) và cũng không sử dụng dữ liệu của lớp (cls).

# Do đó nó phù hợp với:

# @staticmethod

# Ví dụ:

# MemberCard.is_valid_card_id("RC01")

# Có thể gọi trực tiếp từ tên lớp mà không cần tạo object.

# Không cần phải khởi tạo thẻ thành viên trước rồi mới kiểm tra mã thẻ.

# Điều này giúp ngăn chặn việc tạo ra các đối tượng có dữ liệu không hợp lệ ngay từ đầu.

# Câu 3. Tính Đóng gói (Encapsulation) thông qua Name Mangling (__points) đã giải quyết bài toán bảo mật nào của cửa hàng?

# Điểm thưởng là dữ liệu quan trọng của khách hàng.

# Nếu khai báo:

# self.points = 100

# thì nhân viên có thể tự ý sửa:

# card.points = 9999

# hoặc:

# card.points = -100

# làm sai lệch dữ liệu và ảnh hưởng đến chương trình khách hàng thân thiết.

# Để bảo vệ dữ liệu, thuộc tính điểm được khai báo:

# self.__points

# Python sẽ áp dụng cơ chế Name Mangling, giúp che giấu thuộc tính khỏi việc truy cập trực tiếp từ bên ngoài.

# Người dùng không thể tùy ý sửa điểm tích lũy.

# Điểm chỉ được thay đổi thông qua các phương thức nghiệp vụ:

# earn_points()
# redeem_points()

# Nhờ đó:

# Đảm bảo tính toàn vẹn dữ liệu.
# Ngăn chặn gian lận điểm thưởng.
# Hạn chế các thao tác sửa dữ liệu trái phép.
# Đảm bảo mọi thay đổi điểm đều tuân theo quy tắc của hệ thống.

import re
class MemberCard:
    # Class Attribute
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()
        self.__points = 0
        self.__tier = "Standard"

    # Getter điểm
    @property
    def points(self):
        return self.__points

    # Getter hạng thẻ
    @property
    def tier(self):
        return self.__tier

    # Static Method
    @staticmethod
    def is_valid_card_id(card_id):
        pattern = r"^RC\d{2}$"
        return bool(re.match(pattern, card_id))

    # Instance Method - Tích điểm
    def earn_points(self, bill_amount):
        earned_points = bill_amount // 10000

        self.__points += earned_points

        upgraded = False

        if self.__points >= 100 and self.__tier == "Standard":
            self.__tier = "VIP"
            upgraded = True

        return earned_points, upgraded

    # Instance Method - Đổi điểm
    def redeem_points(self, points_to_use):
        if points_to_use <= 0:
            return False, "invalid"

        if points_to_use > self.__points:
            return False, "not_enough"

        self.__points -= points_to_use

        discount = points_to_use * MemberCard.point_value_vnd

        return True, discount

    # Class Method
    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value


# ==========================
# DATABASE
# ==========================

cards_database = []


# ==========================
# DỮ LIỆU MẪU
# ==========================

card1 = MemberCard("RC01", "Nguyen Van A")
card2 = MemberCard("RC02", "Tran Thi B")

# RC01 có 150 điểm -> VIP
card1.earn_points(1500000)

# RC02 có 20 điểm -> Standard
card2.earn_points(200000)

cards_database.append(card1)
cards_database.append(card2)


# ==========================
# HÀM TÌM THẺ
# ==========================

def find_card(card_id):
    for card in cards_database:
        if card.card_id == card_id:
            return card
    return None

while True:
    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)")
    print("6. Thoát chương trình")
    print("================================================")

    choice = input("Chọn chức năng (1-6): ")

    match choice:

        # ==========================
        # CHỨC NĂNG 1
        # ==========================
        case "1":

            print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")

            if len(cards_database) == 0:
                print("Chưa có dữ liệu.")
            else:
                for i, card in enumerate(cards_database, start=1):
                    print(
                        f"{i}. Mã: {card.card_id} | "
                        f"Tên: {card.name} | "
                        f"Điểm: {card.points} | "
                        f"Hạng: {card.tier}"
                    )

        # ==========================
        # CHỨC NĂNG 2
        # ==========================
        case "2":

            print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")

            card_id = input("Nhập mã thẻ: ").strip()

            if find_card(card_id):
                print("\nMã thẻ đã tồn tại trong hệ thống!")
                print("Vui lòng kiểm tra lại.")
                continue

            if not MemberCard.is_valid_card_id(card_id):
                print("\nMã thẻ không hợp lệ!")
                continue

            name = input("Nhập tên khách hàng: ").strip()

            new_card = MemberCard(card_id, name)
            cards_database.append(new_card)

            print("\nĐăng ký thẻ thành viên thành công!")
            print(f"Mã thẻ: {new_card.card_id}")
            print(f"Tên khách hàng: {new_card.name}")
            print(f"Điểm ban đầu: {new_card.points}")
            print(f"Hạng thẻ: {new_card.tier}")

        # ==========================
        # CHỨC NĂNG 3
        # ==========================
        case "3":

            print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")

            card_id = input("Nhập mã thẻ: ").strip()

            card = find_card(card_id)

            if card is None:
                print("Không tìm thấy thẻ!")
                continue

            try:
                bill_amount = int(input("Nhập tổng tiền hóa đơn: "))

                if bill_amount <= 0:
                    print("Hóa đơn phải lớn hơn 0!")
                    continue

            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue

            earned_points, upgraded = card.earn_points(bill_amount)

            print(f"\nKhách hàng: {card.name}")
            print(f"Hóa đơn: {bill_amount:,} VNĐ")
            print(f"Số điểm được tích: {earned_points}")
            print(f"Tổng điểm hiện tại: {card.points}")

            if upgraded:
                print("\nChúc mừng! Khách hàng đã được nâng hạng lên VIP.")

            print(f"Hạng thẻ hiện tại: {card.tier}")

        # ==========================
        # CHỨC NĂNG 4
        # ==========================
        case "4":

            print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")

            card_id = input("Nhập mã thẻ: ").strip()

            card = find_card(card_id)

            if card is None:
                print("Không tìm thấy thẻ!")
                continue

            try:
                points_to_use = int(
                    input("Nhập số điểm muốn sử dụng: ")
                )

            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue

            result, value = card.redeem_points(points_to_use)

            if result:

                print(f"\nĐã trừ {points_to_use} điểm.")
                print(
                    f"Khách hàng được giảm giá "
                    f"{value:,} VNĐ vào hóa đơn!"
                )
                print(f"Số điểm còn lại: {card.points}")
                print(f"Hạng thẻ hiện tại: {card.tier}")

            else:

                if value == "invalid":
                    print("\nKhông thể đổi điểm!")
                    print("Số điểm sử dụng phải lớn hơn 0.")

                elif value == "not_enough":
                    print("\nKhông thể đổi điểm!")
                    print(
                        "Số điểm muốn sử dụng vượt quá "
                        "số điểm hiện có."
                    )
                    print(f"Điểm hiện tại của khách: {card.points}")
                    print("Điểm cũ được giữ nguyên:")
                    print(f"Số điểm sau giao dịch: {card.points}")

        # ==========================
        # CHỨC NĂNG 5
        # ==========================
        case "5":

            print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")

            print(
                f"Tỷ giá hiện tại: "
                f"1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
            )

            try:
                new_value = int(
                    input("Nhập tỷ giá mới cho 1 điểm: ")
                )

                if new_value <= 0:
                    print("Tỷ giá phải lớn hơn 0!")
                    continue

            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue

            MemberCard.update_point_value(new_value)

            print("\nCập nhật tỷ giá thành công!")
            print(
                f"Tỷ giá mới: "
                f"1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
            )

        # ==========================
        # CHỨC NĂNG 6
        # ==========================
        case "6":

            print(
                "\nCảm ơn bạn đã sử dụng hệ thống "
                "thẻ thành viên Rikkei Coffee!"
            )
            break
        case _:
            print("Lựa chọn không hợp lệ!")
