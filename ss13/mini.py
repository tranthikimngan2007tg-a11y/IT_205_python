parking_list = []
next_id = 1

while True:

    print("\n========== SMART PARKING SYSTEM ==========")
    print("1. Check-in xe")
    print("2. Báo cáo tồn kho")
    print("3. Tìm kiếm xe")
    print("4. Check-out xe")
    print("5. Thoát")
    print("==========================================")

    choice = input("Nhập lựa chọn (1-5): ").strip()

    if not choice.isdigit():
        print("ERR-01: Menu không hợp lệ!")
        continue
    choice = int(choice)

    if choice == 1:
        plate = input("Nhập biển số xe: ").strip().upper()

        if plate == "":
            print("ERR-02: Biển số không được để trống!")
            continue
        duplicate = False
        for vehicle in parking_list:
            if vehicle["plate"] == plate:
                duplicate = True
                break
        if duplicate:
            print("ERR-03: Biển số đã tồn tại!")
            continue
        while True:
            vehicle_type = input(
                "Chọn loại xe (1-Xe máy | 2-Ô tô): ").strip()

            if vehicle_type == "1":
                vehicle_type = "Xe máy"
                break
            elif vehicle_type == "2":
                vehicle_type = "Ô tô"
                break
            else:
                print("ERR-05: Loại xe không hợp lệ!")
        while True:
            entry_time = input(
                "Nhập giờ vào: "
            ).strip()

            if (
                entry_time.isdigit()
                and int(entry_time) >= 0
            ):
                entry_time = int(entry_time)
                break

            else:
                print("ERR-06: Giờ vào không hợp lệ!")
        new_vehicle = {
            "id": next_id,
            "plate": plate,
            "type": vehicle_type,
            "entry_time": entry_time
        }
        parking_list.append(new_vehicle)
        print("Check-in thành công!")
        next_id += 1
    elif choice == 2:

        if len(parking_list) == 0:
            print("ERR-07: Bãi xe hiện đang trống!")
        else:
            print("\n===== DANH SÁCH XE TRONG BÃI =====")
            print(
                f"{'ID':<5}"
                f"{'BIỂN SỐ':<15}"
                f"{'LOẠI XE':<15}"
                f"{'GIỜ VÀO':<10}"
            )

            print("-" * 45)
            for vehicle in parking_list:
                print(
                    f"{vehicle['id']:<5}"
                    f"{vehicle['plate']:<15}"
                    f"{vehicle['type']:<15}"
                    f"{vehicle['entry_time']:<10}"
                )

    elif choice == 3:

        search_plate = input(
            "Nhập biển số cần tìm: "
        ).strip().upper()

        found = False
        for vehicle in parking_list:

            if vehicle["plate"] == search_plate:
                print("Tìm thấy xe:")
                print(vehicle)

                found = True
                break

        if not found:
            print("ERR-04: Không tìm thấy xe!")
    elif choice == 4:

        plate = input("Nhập biển số cần check-out: ").strip().upper()
        found = False
        for vehicle in parking_list:
            if vehicle["plate"] == plate:
                found = True
                while True:
                    exit_time = input("Nhập giờ ra: ").strip()

                    if (
                        exit_time.isdigit()
                        and int(exit_time)
                        >= vehicle["entry_time"]
                    ):
                        exit_time = int(exit_time)
                        break

                    else:
                        print("ERR-08: Giờ ra không hợp lệ!")

                duration = (
                    exit_time
                    - vehicle["entry_time"]
                )

                if vehicle["type"] == "Xe máy":
                    fee = duration * 5000
                else:
                    fee = duration * 20000
                print("Check-out thành công!")
                print(f"Phí gửi xe: {fee:,} VNĐ")
                parking_list.remove(vehicle)
                break
        if not found:
            print("ERR-04: Không tìm thấy xe!")
    elif choice == 5:
        print("Thoát chương trình...")
        break
    else:
        print("ERR-01: Menu không hợp lệ!")