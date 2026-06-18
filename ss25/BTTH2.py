# PHÂN TÍCH GIẢI PHÁP
# 1. Thiết kế Class NetflixAccount

# Hệ thống được xây dựng theo mô hình Lập trình Hướng đối tượng (OOP) với một lớp chính là NetflixAccount.

# Mỗi đối tượng của lớp đại diện cho một tài khoản Netflix và chứa các thông tin:

# Email
# Mật khẩu
# Gói cước
# Danh sách người xem (Profiles)

# Ngoài ra lớp còn chứa các thuộc tính dùng chung cho toàn hệ thống như tên nền tảng và số lượng Profile tối đa.

# 2. Áp dụng Name Mangling để bảo vệ dữ liệu

# Hai thuộc tính:

# self.__password
# self.__plan

# được khai báo với tiền tố __.

# Đây là kỹ thuật Name Mangling trong Python nhằm hạn chế việc truy cập trực tiếp từ bên ngoài lớp.

# Ví dụ:

# account.__password

# sẽ phát sinh lỗi truy cập.

# Nhờ đó:

# Mật khẩu người dùng không bị đọc trực tiếp.
# Gói cước không bị thay đổi trái phép.
# Tăng tính bảo mật và tính đóng gói của hệ thống.
# 3. Sử dụng Property và Setter
# Property password

# Thuộc tính password được xây dựng bằng @property.

# Khi hiển thị thông tin tài khoản:

# print(account.password)

# hệ thống không trả về mật khẩu thật mà chỉ hiển thị:

# ********

# Điều này giúp bảo vệ thông tin nhạy cảm của người dùng.

# Password Setter

# Khi cập nhật mật khẩu:

# account.password = "abcdef"

# Setter sẽ kiểm tra độ dài mật khẩu.

# Nếu mật khẩu ngắn hơn 6 ký tự:

# raise ValueError("Password is too short")

# Hệ thống sẽ từ chối cập nhật và yêu cầu nhập lại.

# Property plan

# Thuộc tính plan chỉ được cung cấp @property để đọc dữ liệu.

# Không xây dựng Setter cho plan.

# Nhờ đó người dùng không thể tự ý thực hiện:

# account.plan = "Premium"

# Muốn thay đổi gói cước bắt buộc phải thông qua phương thức:

# upgrade_plan()

# để đảm bảo đúng quy tắc nghiệp vụ.

# 4. Phân biệt Instance Method, Static Method và Class Method
# Instance Method

# Các phương thức:

# add_profile()
# upgrade_plan()
# display_info()

# làm việc trên dữ liệu của từng tài khoản cụ thể.

# Ví dụ:

# account.add_profile("Con Trai")

# chỉ ảnh hưởng đến tài khoản đang được gọi.

# Static Method

# Phương thức:

# validate_email()

# được khai báo bằng @staticmethod.

# Phương thức này chỉ thực hiện kiểm tra định dạng email và không cần truy cập:

# self

# hoặc

# cls

# nên phù hợp sử dụng Static Method.

# Class Method

# Phương thức:

# update_max_profiles()

# được khai báo bằng @classmethod.

# Phương thức này thao tác trực tiếp với thuộc tính lớp:

# max_profiles

# Khi Netflix thay đổi chính sách:

# NetflixAccount.update_max_profiles(10)

# thì tất cả các tài khoản hiện có và các tài khoản được tạo sau đó đều sử dụng giới hạn mới.

# Điều này giúp hệ thống quản lý tập trung và không cần cập nhật thủ công từng đối tượng.

# 5. Luồng hoạt động của chương trình
# Chức năng 1 – Đăng ký tài khoản
# Nhập Email.
# Kiểm tra Email bằng validate_email().
# Tạo đối tượng NetflixAccount.
# Gán mật khẩu thông qua Setter.
# Lưu đối tượng vào current_account.
# Chức năng 2 – Xem thông tin tài khoản
# Kiểm tra tài khoản đã tồn tại hay chưa.
# Gọi display_info().
# Mật khẩu hiển thị dưới dạng ********.
# Chức năng 3 – Thêm người xem
# Nhập tên Profile.
# Gọi add_profile().
# Kiểm tra giới hạn số lượng Profile trước khi thêm.
# Chức năng 4 – Nâng cấp gói cước
# Chọn gói Basic, Standard hoặc Premium.
# Gọi upgrade_plan().
# Cập nhật biến private __plan.
# Chức năng 5 – Cập nhật chính sách Netflix
# Nhập giới hạn Profile mới.
# Gọi update_max_profiles().
# Áp dụng ngay cho toàn bộ hệ thống.
# Chức năng 6 – Thoát chương trình
# Kết thúc vòng lặp menu.
# Dừng chương trình.

class NetflixAccount:
    """
    Netflix Account Management System
    """

    # Class Attributes
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        """
        Initialize account information
        """
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    @property
    def password(self):
        """
        Hide password when displaying
        """
        return "********"

    @password.setter
    def password(self, new_password):
        """
        Validate password before updating
        """
        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password

    @property
    def plan(self):
        """
        Read-only property
        """
        return self.__plan

    @staticmethod
    def validate_email(email):
        """
        Validate email format
        """
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        """
        Update profile limit globally
        """
        cls.max_profiles = int(new_limit)

    def add_profile(self, profile_name):
        """
        Add new profile
        """
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
            return

        self.profiles.append(profile_name)
        print("Thêm Profile thành công")

    def upgrade_plan(self, new_plan):
        """
        Upgrade account plan
        """
        valid_plans = ["Basic", "Standard", "Premium"]

        new_plan = new_plan.capitalize()

        if new_plan not in valid_plans:
            print("Gói cước không hợp lệ")
            return

        self.__plan = new_plan
        print("Nâng cấp gói cước thành công")

    def display_info(self):
        """
        Display account information
        """
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Current Plan: {self.plan}")
        print(f"Profiles: {self.profiles}")
def main():
    current_account = None
    while True:
        print("""
                ===== NETFLIX ACCOUNT MANAGER =====
                1. Đăng ký tài khoản mới
                2. Xem thông tin tài khoản
                3. Thêm người xem
                4. Nâng cấp gói cước
                5. Cập nhật chính sách Netflix
                6. Thoát chương trình
                ===================================
                """)
        choice = input("Chọn chức năng (1-6): ")
        match choice:
            case "1":
                while True:
                    email = input("Nhập Email: ")
                    if not NetflixAccount.validate_email(email):
                        print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")
                        continue
                    account = NetflixAccount(email)
                    while True:
                        password = input("Nhập mật khẩu: ")
                        try:
                            account.password = password
                            current_account = account
                            print("Đăng ký tài khoản thành công!")
                            break
                        except ValueError as e:
                            print(e)
                    break
            case "2":
                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                else:
                    current_account.display_info()
            case "3":
                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                else:
                    profile_name = input("Nhập tên Profile mới: ")
                    current_account.add_profile(profile_name)
            case "4":
                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                else:
                    print("""
                            Basic
                            Standard
                            Premium
                            """)
                    new_plan = input("Nhập gói cước mới: ")
                    current_account.upgrade_plan(new_plan)
            case "5":
                try:
                    new_limit = int(
                        input("Nhập số lượng Profile tối đa mới: ")
                    )
                    NetflixAccount.update_max_profiles(new_limit)
                    print(
                        f"Đã cập nhật giới hạn Profile toàn hệ thống thành {new_limit}"
                    )
                except ValueError:
                    print("Vui lòng nhập số hợp lệ")
            case "6":
                print("Thoát chương trình...")
                break
            case _:

                print("Lựa chọn không hợp lệ")


main()