while True:
    print("+============================================================+")
    print("|    HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPPEE              |")
    print("+============================================================+")
    print("|    1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê        |")
    print("|    2. Chuẩn hóa tên tên shop                               |")
    print("|    3. Kiểm tra mã giảm hợp lệ                              |")
    print("|    4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm    |")
    print("|    5. Thoát chương trình                                   |")
    print("+============================================================+")

    choise = input("> Mời bạn chọn chức năng (1-5): ")

    match choise:
        case "1":
            shop_name = input("Nhập tên shop: ")
            product_name = input("Nhập tên sản phẩm: ")
            description = input("Nhập mô tả sản phẩm: ")
            category = input("Nhập danh mục sản phẩm: ")
            list_search = input("Nhập danh sách từ khóa tìm kiếm: ")

            print(f"Tên shop: {shop_name.strip()}")
            print(f"Tên sản phẩm: {product_name.strip().title()}")
            print(f"Mô tả sản phẩm: {description.strip()}")
            print(f"Độ dài mô tả sản phẩm {len(description)}")
            print(f"Danh mục sản phẩm: {category.strip().lower()}")
            print(f"Danh sách từ khóa: {list_search.strip()}")
            count_keyword = list_search.count(",")
            print(f"Số lượng từ khóa tìm kiếm: {count_keyword + 1}")
            print(f"Mô tả được chuyển toàn bộ sang chữ thường: {description.lower()}")
            print(f"Mô tả được chuyển toàn bộ sang chữ hoa: {description.upper()}")

        case "2":
            print(f"Tên shop ban đầu: {shop_name}")
            new_shop = shop_name.strip().lower().replace(" ", "-")
            if(not "shop-" in new_shop):
                print(f"Tên shop sau chuẩn hóa: {"shop-" + new_shop}")
            else:
                print(f"Tên shop sau chuẩn hóa: {new_shop}")
        case "3":
            voucher = input("Nhập mã giảm giá: ")
            list_hashtag = "#SALE2026, #SALE305"
            if(voucher == ""):
                print("Mã giảm giá không được rỗng")
            elif(" " in voucher):
                print("Mã giảm giả không được chứa khoảng trắng")
            elif(len(voucher) > 12 or len(voucher) < 6):
                print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
            elif(not voucher.isupper()):
                print("Mã giảm giá phải viết hoa toàn bộ")
            elif(not voucher.isalnum()):
                print("Mã giảm giảm chỉ được chứa chữ cái và số")
            elif(not voucher.startswith("SALE")):
                print("Mã giảm giả phải bắt đầu bằng chuối SALE")
            else:
                print("Mã giảm giá hợp lệ")
                print(f"Danh sách hashtag hiện tại: {list_search + "#" + voucher}")
        case "4":
            find_word = input("Nhập vào từ khóa cần tìm: ")
            replace_word = input("Nhập vào từ khóa thay thế: ")
            count_word = description.count(find_word)
            if(find_word in description):
                description = description.replace(find_word, replace_word)
            print(f"Mô tả sau khi thay thế: {description}")
            print(f"Số lượng từ tìm được là: {count_word}")
        case "5":
            print("Đã thoát khỏi chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")