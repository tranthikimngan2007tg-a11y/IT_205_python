while True:
    print("+================================================+")
    print("|    HỆ THỐNG QUẢN LÝ NỘI DUNG TIK TOK           |")
    print("+================================================+")
    print("|    1. Nhập và phân tích thông tin video        |")
    print("|    2. Chuẩn hóa tên tài khoản                  |")
    print("|    3. Kiểm tra tính hợp lệ hashtag             |")
    print("|    4. Tìm kiếm và thay thế từ khóa trong mô tả |")
    print("|    5. Thoát chương trình                       |")
    print("+================================================+")

    choise = input("> Mời bạn chọn chức năng (1-5): ")

    match choise:
        case "1":
            account_name = input("Nhập vào tên tài khoản: ")
            title = input("Nhập vào tiêu đề: ")
            description = input("Nhập vào mô tả: ")
            list_hashtag = input("Nhập vào danh sách hashtag: ")
            print(f"Tên tài khoản: {account_name.strip()}")
            print(f"Tiêu đề: {title.strip().title()}")
            print(f"Mô tả: {description.strip()}")
            print(f"Độ dài mô tả trong video: {len(description)}")
            count_space = description.count(" ")
            print(f"Số lượng từ trong mô tả: {count_space + 1}")
            temp = list_hashtag.split(",")
            new_list_hashtag = "".jpin(temp)
            print(f"Danh sách hashtag sau khi chuẩn hóa khoảng trắng: {new_list_hashtag.strip()}")
            count_hashtag = list_hashtag.split(",")
            print(f"Số lượng hashtag: {len(count_hashtag)}")
            print(f"Mô tả video được chuyển hóa toàn bộ sang chứ thường: {description.lower()}")
            print(f"Mô tả video được chuyển sang toàn bộ chứ hoa: {description.upper()}")
        case "2":
            print(f"Tên tài khoản ban đầu: {account_name}")
            print(f"Tên tài khoản được chuẩn hóa: {"@" + account_name.lower()}")
        case "3":
            new_hashtag = input("Nhập vào hashtag mới: ")
            if(len(new_hashtag) == 0):
                print("Không được rỗng!")
            elif( not new_hashtag.startswith("#")):
                print("Phải bắt đầu bằng dấu #")
            elif(" " in new_hashtag):
                print("Không được chứa khoảng trắng!")
            elif(len(new_hashtag) < 2):
                print("Hashtag không được ít hơn 2 kí tự")
            else:
                print("Hashtag hợp lệ!")
                list_hashtag = list_hashtag + new_hashtag
                print(f"Danh sách hashtag mới: {list_hashtag}")
        case "4":
            find_word = input("Nhập vào từ khóa cần tìm: ")
            replace_word = input("Nhập vào từ khóa mới: ")
            count_word = description.count(find_word)
            if(find_word in description):
                description = description.replace(find_word, replace_word)
            print(f"Mô tả sau khi thay thế: {description}")
            print(f"Số lượng từ tìm được là: {count_word}")
        case "5":
            print("Đã thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
