import logging

logging.basicConfig(
    filename = "log_energy.log",
    filemode = "a",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s -%(message)s"
)

def show_devices(devices):
    if not devices:
        print("Danh sách rỗng!")
        return
    print("==DANH SÁCH THIẾT BỊ GIÁM SÁT==")
    print(f"{"Mã TB":<5} | {"Vị trí phân xưởng":<25} | {"Chỉ số cũ":<15} | {"Chỉ số mới":<15} | {"Trạng thái":<20}")
    for item in devices:
        print(f"{item.get('id'):<5} | {item.get('location'):<25} | {item.get('old_index'):<15} | {item.get('new_index'):<15} | {item.get('status'):<20}")

def update_energy(devices):
    found_index = None
    device_id = input("Nhập vào mã thiết bị: ")
    for index, value in enumerate(devices):
        if device_id == value.get('id'):
            found_index = index
            break
    else:
        print("Không tìm thấy mã thiết bị!")
        return
    while True:
        try:
            old_index = int(input("Nhập vào chỉ số cũ: "))
            if old_index <= 0:
                print("Chỉ số cũ không được bé hơn 0")
                continue
            break
        except ValueError:
            print("Chỉ số cũ không phải số!")
            continue

    while True:
        try:
            new_index = int(input("Nhập vào chỉ số mới: "))
            if new_index <= 0 or new_index < old_index:
                print("Chỉ số cũ không hợp lệ")
                continue
            break
        except ValueError:
            print("Chỉ số mới không phải số!")
            continue

    devices[found_index]["old_index"] = old_index
    devices[found_index]["new_index"] = new_index
    print(f"Thiết bị {device_id} cập nhật thành công!")

def search_device(devices):
    device_id = input("Nhập vào mã thiết bị cần tìm: ")
    for index, value in enumerate(devices):
        if device_id == value.get('id'):
            found_index = index
            break
    else:
        print("Không tìm thấy mã thiết bị!")
        return
    energy_financials = devices[found_index].get("new_index") - devices[found_index].get("old_index")
    if energy_financials > 5000 and devices[found_index].get("status") != "Overload" :
        devices[found_index]["status"] = "Overload"
        logging.warning(f"Thiết bị {device_id} đã vượt ngưỡng tiêu thụ an toàn, chuyển sang OVERLOAD")
        print("Thiết bị đã được kích hoạt trạng thái Overload")
    elif energy_financials > 5000 and devices[found_index].get("status") == "Overload":
        print("Thao tác bị hủy! Thiết bị này đã được kích hoạt trạng thái OVERLOAD từ trước")

def cal_energy_financials(devices):
    total_money = 0
    energy_financials = 0
    for index, value in enumerate(devices):
        energy_financials += devices[index].get("new_index") - devices[index].get("old_index")

    if energy_financials >= 50000:
        rate = 0.03
        total_money = energy_financials * 3000 * (1 - rate)
    else:
        rate = 0
        total_money = energy_financials * 3000

    print("===BÁO CÁO THỐNG KÊ===")
    print(f"Tổng lượng điện tiêu thụ thực tế: {energy_financials}")
    print(f"Tỉ lệ chiết khấu áp dụng từ nhà nước: {rate}")
    print(f"Tổng chi phí năng lượng phải trả sau khi chiết khấu: {total_money}")


def main():
    devices = [
        {'id': 'M01', 'location': 'Mechanical Shop A', 'old_index': 1200, 'new_index': 55000, 'status': 'Normal'},
        {'id': 'M02', 'location': 'Assembly Line B', 'old_index': 2300, 'new_index': 10500, 'status': 'Normal'}
    ]
    while True:
        print("==========Smart Energy Monitor============\n")
        print("1. Xem danh sách thiết bị giám sát\n")
        print("2. Cập nhật chỉ số điện tiêu thụ\n")
        print("3. Kích hoạt trạng thái cảnh báo quá tải\n")
        print("4. Tính tổng lượng điện và chi phí năng lượng\n")
        print("5. Thoát chương trình\n")

        choice = input("Nhập lựa chọn của bạn (1-5): ")

        match choice:
            case "1":
                show_devices(devices)
            case "2":
                update_energy(devices)
            case "3":
                search_device(devices)
            case "4":
                cal_energy_financials(devices)
            case "5":
                print("Thoát chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()