playlist = []

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ DANH SÁCH PHÁT =====")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và trích xuất danh sách")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    match choice:
        case "1":
            while True:
                print("\n===== THÊM BÀI HÁT =====")
                print("1. Thêm vào cuối danh sách")
                print("2. Chèn vào vị trí bất kỳ")
                sub_choice = input("Nhập lựa chọn: ").strip()
                if sub_choice.isdigit() == False:
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
                    continue
                match sub_choice:
                    case "1":
                        song_name = input("Nhập tên bài hát: ").strip()
                        playlist.append(song_name)
                        print("Thêm bài hát thành công!")
                        print("Số lượng bài hát hiện tại:", len(playlist))
                        break
                    case "2":
                        song_name = input("Nhập tên bài hát: ").strip()
                        index = input("Nhập vị trí muốn chèn: ").strip()
                        if index.isdigit():
                            index = int(index)
                            if 0 <= index <= len(playlist):
                                playlist.insert(index, song_name)
                                print("Thêm bài hát thành công!")
                                print("Số lượng bài hát hiện tại:", len(playlist))
                                break
                            else:
                                print("Vị trí không hợp lệ.")
                        else:
                            print("Vị trí không hợp lệ.")
                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
        case "2":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\n===== DANH SÁCH PHÁT =====")
                count = 1
                for song in playlist:
                    print(f"{count}. {song}")
                    count += 1
        case "3":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
            else:
                while True:
                    print("\n===== XÓA BÀI HÁT =====")
                    print("1. Xóa theo tên bài hát")
                    print("2. Xóa theo số thứ tự")
                    delete_choice = input("Nhập lựa chọn: ").strip()
                    if delete_choice.isdigit() == False:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
                        continue
                    match delete_choice:
                        case "1":
                            song_name = input("Nhập tên bài hát cần xóa: ").strip()
                            if song_name in playlist:
                                playlist.remove(song_name)
                                print(f"Đã xóa bài hát [{song_name}] khỏi danh sách.")
                            else:
                                print("Không tìm thấy bài hát trong danh sách phát.")
                            break
                        case "2":
                            index = input("Nhập số thứ tự bài hát cần xóa: ").strip()
                            if index.isdigit():
                                index = int(index)
                                if 1 <= index <= len(playlist):
                                    deleted_song = playlist.pop(index - 1)
                                    print(f"Đã xóa bài hát [{deleted_song}] khỏi danh sách.")
                                else:
                                    print("Vị trí không hợp lệ.")
                            else:
                                print("Vị trí không hợp lệ.")
                            break
                        case _:
                            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
        case "4":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
            else:
                while True:
                    print("\n===== SẮP XẾP VÀ TRÍCH XUẤT =====")
                    print("1. Sắp xếp theo bảng chữ cái")
                    print("2. Nghe thử 3 bài hát đầu tiên")
                    sort_choice = input("Nhập lựa chọn: ").strip()
                    if sort_choice.isdigit() == False:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
                        continue
                    match sort_choice:
                        case "1":
                            playlist.sort()
                            print("Danh sách sau khi sắp xếp:")
                            count = 1
                            for song in playlist:
                                print(f"{count}. {song}")
                                count += 1
                            break
                        case "2":
                            print("3 bài hát đầu tiên:")
                            first_songs = playlist[:3]
                            count = 1
                            for song in first_songs:
                                print(f"{count}. {song}")
                                count += 1
                            break
                        case _:
                            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
        case "5":
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")