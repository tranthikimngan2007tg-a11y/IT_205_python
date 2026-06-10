def menu():
    print("=" * 80)
    print("=========== HE THONG QUAN LY CHUYEN XE ===========")
    print(
        "1. Hien thi danh sach chuyen xe\n"
        + "2. Them chuyen xe moi\n"
        + "3. Dat ve chuyen xe\n"
        + "4. Xoa chuyen xe\n"
        + "5. Tim kiem chuyen xe\n"
        + "6. Thong ke trang thai chuyen xe\n"
        + "7. Thoat chuong trinh\n"
    )
    print("=" * 80)
def get_validate_input(message, data_type="string"):
    while True:
        value = input(message).strip()
        if value == "":
            print("Du lieu khong duoc de trong!")
            continue
        match data_type:
            case "int":
                try:
                    value = int(value)
                    if value <= 0:
                        print("Gia tri phai lon hon 0!")
                        continue
                    return value
                except:
                    print("Vui long nhap so nguyen hop le!")
            case _:
                return value
def classify_status(available_seats, total_seats):
    if available_seats == 0:
        return "Het ve"
    rate = available_seats / total_seats
    if rate < 0.15:
        return "Hut khach"
    elif rate <= 0.80:
        return "Binh thuong"
    else:
        return "E khach"
def update_trip_info(trip):
    sold_seats = (
        trip.get("total_seats")
        - trip.get("available_seats")
    )
    revenue = (
        trip.get("ticket_price")
        * sold_seats
    )
    trip["revenue"] = revenue
    trip["status"] = classify_status(
        trip.get("available_seats"),
        trip.get("total_seats")
    )
def show_trip(trips):
    if not trips:
        print("Danh sach chuyen xe rong!")
        return
    print("\n================ DANH SACH CHUYEN XE ================")
    print(
        f"{'STT':<5} | "
        f"{'Ma CX':<10} | "
        f"{'Tuyen duong':<25} | "
        f"{'Gia ve':<12} | "
        f"{'Ghe trong':<10} | "
        f"{'Tong ghe':<10} | "
        f"{'Doanh thu':<15} | "
        f"{'Trang thai':<15}"
    )
    for index, value in enumerate(trips, start=1):
        print(
            f"{index:<5} | "
            f"{value.get('trip_id'):<10} | "
            f"{value.get('route'):<25} | "
            f"{value.get('ticket_price'):<12} | "
            f"{value.get('available_seats'):<10} | "
            f"{value.get('total_seats'):<10} | "
            f"{value.get('revenue'):<15} | "
            f"{value.get('status'):<15}"
        )
def input_trip(trips):
    trip_id = get_validate_input(
        "Nhap ma chuyen xe: "
    )
    for item in trips:
        if trip_id.lower() == item.get("trip_id").lower():
            print("Ma chuyen xe khong duoc trung!")
            return
    route = get_validate_input(
        "Nhap tuyen duong: "
    )
    ticket_price = get_validate_input(
        "Nhap gia ve: ",
        "int"
    )
    total_seats = get_validate_input(
        "Nhap tong so ghe: ",
        "int"
    )
    new_trip = {
        "trip_id": trip_id,
        "route": route,
        "ticket_price": ticket_price,
        "available_seats": total_seats,
        "total_seats": total_seats,
        "revenue": 0,
        "status": classify_status(
            total_seats,
            total_seats
        )
    }
    trips.append(new_trip)
    print("Them chuyen xe thanh cong!")
def booking_ticket(trips):
    if not trips:
        print("Danh sach chuyen xe rong!")
        return
    trip_id = get_validate_input(
        "Nhap ma chuyen xe can dat: "
    )
    for item in trips:
        if trip_id.lower() == item.get("trip_id").lower():
            quantity = get_validate_input(
                "Nhap so luong ve dat: ",
                "int"
            )
            if quantity > item.get("available_seats"):
                print("So ve dat vuot qua ghe trong!")
                return
            item["available_seats"] -= quantity
            update_trip_info(item)
            print("Dat ve thanh cong!")
            return
    print("Khong tim thay ma chuyen xe!")
def delete_trip(trips):
    if not trips:
        print("Danh sach chuyen xe rong!")
        return
    trip_id = get_validate_input(
        "Nhap ma chuyen xe can xoa: "
    )
    for item in trips:
        if trip_id.lower() == item.get("trip_id").lower():
            confirm = input(
                "Ban co chac muon xoa? (Y/N): "
            ).upper()
            if confirm == "Y":
                trips.remove(item)
                print("Xoa chuyen xe thanh cong!")
            else:
                print("Da huy thao tac!")
            return
    print("Khong tim thay ma chuyen xe!")
def search_trip(trips):
    if not trips:
        print("Danh sach chuyen xe rong!")
        return
    keyword = get_validate_input(
        "Nhap ma CX hoac tuyen duong: "
    )
    find_trip = []
    for item in trips:
        if (
            keyword.lower()
            == item.get("trip_id").lower()
            or keyword.lower()
            in item.get("route").lower()
        ):
            new_trip = {
                "trip_id": item.get("trip_id"),
                "route": item.get("route"),
                "ticket_price": item.get("ticket_price"),
                "available_seats": item.get("available_seats"),
                "total_seats": item.get("total_seats"),
                "revenue": item.get("revenue"),
                "status": item.get("status")
            }
            find_trip.append(new_trip)
    show_trip(find_trip)
def statistics_trip(trips):
    if not trips:
        print("Danh sach chuyen xe rong!")
        return
    het_ve = 0
    hut_khach = 0
    binh_thuong = 0
    e_khach = 0
    for item in trips:
        update_trip_info(item)
        if item.get("status") == "Het ve":
            het_ve += 1
        elif item.get("status") == "Hut khach":
            hut_khach += 1
        elif item.get("status") == "Binh thuong":
            binh_thuong += 1
        elif item.get("status") == "E khach":
            e_khach += 1
    print("\n========== THONG KE ==========")
    print(f"Het ve: {het_ve}")
    print(f"Hut khach: {hut_khach}")
    print(f"Binh thuong: {binh_thuong}")
    print(f"E khach: {e_khach}")
def main():
    trips = [
        {
            "trip_id": "CX001",
            "route": "Sai Gon - Da Lat",
            "ticket_price": 300000,
            "available_seats": 5,
            "total_seats": 40,
            "revenue": 10500000,
            "status": "Hut khach"
        },
        {
            "trip_id": "CX002",
            "route": "Sai Gon - Nha Trang",
            "ticket_price": 250000,
            "available_seats": 35,
            "total_seats": 40,
            "revenue": 1250000,
            "status": "E khach"
        }
    ]
    while True:
        menu()
        choice = input(
            "Nhap lua chon cua ban: "
        )
        match choice:
            case "1":
                show_trip(trips)
            case "2":
                input_trip(trips)
            case "3":
                booking_ticket(trips)
            case "4":
                delete_trip(trips)
            case "5":
                search_trip(trips)
            case "6":
                statistics_trip(trips)
            case "7":
                print(
                    "Cam on ban da su dung chuong trinh!"
                )
                break
            case _:
                print(
                    "Lua chon khong hop le!"
                )
main()