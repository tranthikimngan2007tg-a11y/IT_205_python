while True:
    print("+============================================================+")
    print("|    HỆ THỐNG QUẢN LÝ NỘI DUNG ĐƠN HÀNG GRAB EXPRESS         |")
    print("+============================================================+")
    print("|    1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê        |")
    print("|    2. Chuẩn hóa mã đơn hàng                                |")
    print("|    3. Ẩn số điện thoại khách hàng                          |")
    print("|    4. Tìm kiếm và thay thế từ khóa trong ghi chú đơn hàng  |")
    print("|    5. Thoát chương trình                                   |")
    print("+============================================================+")

    choise = input("> Mời bạn chọn chức năng (1-5): ")
    
    match choise:
        case "1":
            name_gui = input("Nhập tên người gửi: ")
            phone_gui = input("Nhập số điện thoại người gửi: ")
            address_lay = input("Nhập địa chỉ lấy hàng: ")
            name_nhan = input("Nhập tên người nhận: ")
            phone_nhan = input("Nhập số điện thoại người nhận: ")
            address_giao = input("Nhập địa chỉ gia hàng: ")
            note = input("Nhập ghi chú giao hàng: ")

            print(f"Tên người gửi: {name_gui.strip().title()}")
            print(f"Tên người nhận: {name_nhan.strip().title()}")
            print(f"Địa chỉ lấy hàng: {address_lay.strip()}")
            print(f"Địa chỉ giao hàng: {address_giao.strip()}")
            print(f"Ghi chú giao hàng: {note.strip()}")
            print(f"Độ dài ghi chú giao hàng: {len(note)}")
            count_keyword = note.count(" ")
            print(f"Số từ trong ghi chú giao hàng: {count_keyword + 1}")
            print(f"Ghi chú giao hàng dạng chữ thường: {note.lower()}")
            print(f"Ghi chú giao hàng dạng chữ hoa: {note.upper()}")
        case "2":
            order_code = input("Nhập mã đơn hàng: ")
            print(f"Mã đơn hàng ban đầu: {order_code}")
            new_order_code = order_code.strip().upper().replace(" ","-")
            if(not "GRAB-" in new_order_code):
                print(f"Mã đơn hàng sau chuẩn hóa: {"GRAB-" + new_order_code}")
            else:
                print(f"Mã đơn hàng sau chuẩn hóa: {new_order_code}")
        case "3":
            if(phone_gui == ""):
                print("Số điện thoại người gửi không được rỗng")
            elif(phone_gui.isdigit()):
                print("Số điện thoại chỉ chứa chữ số")
            elif(len(phone_gui) != 10):
                print("Số điện thoại phải có đúng 10 ký tự")
            else:
                print(f"SĐT người gửi: {phone_gui[0:3] + "*" * 5 + phone_gui[-2:]}")

            if(phone_nhan == ""):
                print("Số điện thoại người nhận không được rỗng")
            elif(phone_nhan.isdigit()):
                print("Số điện thoại chỉ chứa chữ số")
            elif(len(phone_nhan) != 10):
                print("Số điện thoại phải có đúng 10 ký tự")
            else:
                print(f"SĐT người nhận: {phone_nhan[0:3] + "*" * 5 + phone_nhan[-2:]}")
        case "4":
            find_word = input("Nhập vào từ khóa cần tìm: ")
            replace_word = input("Nhập vào từ khóa thay thế: ")
            count_word = note.count(find_word)
            if(find_word in note):
                note = note.replace(find_word, replace_word)
            print(f"Ghi chú sau khi thay thế: {note}")
            print(f"Số lượng từ tìm được là: {count_word}")
        case "5":
            print("Đã thoát khỏi chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")