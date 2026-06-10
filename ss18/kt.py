def menu():
    print("=" * 60)
    print("    QUẢN LÝ KHO HÀNG - GROCERY STORE    ")
    print("1. Xem danh sách hàng tồn kho\n" + 
          "2. Nhập thêm hàng hóa mới\n" + 
          "3. Cập nhật số lượng tồn kho theo ID\n" +
          "4. Thoát chương trình\n")
    print("=" * 60)
    
def show_inventory(inventory_list):
    if not inventory_list:
        print("Kho hàng hiện đang trống!")
        return

    print("--- DANH SÁCH HÀNG TỒN KHO ---")
    print(f"{'ID':<5} | {'Tên hàng hóa':<15} | {'Số lượng tồn':<10}")

    for index in inventory_list:
        print(f"{index.get('id'):<5} | {index.get('name'):<15} | {index.get('quantity'):<10}")

def validate_input(prompt: str, type_input: str = "str"):
    while True:
        user_input = input(prompt).strip()
        
        if not user_input:
            if type_input == "id":
                print("Mã hàng hóa không được để trống!")
            elif type_input == "name":
                print("Tên hàng hóa không được để trống!")
            elif type_input == "quantity":
                print("Số lượng kho không được để trống!")
            continue 

        if type_input == "quantity":
            if not user_input.isdigit() or int(user_input) <= 0:
                print("Số lượng nhập kho phải là số nguyên lớn hơn 0!")
                continue  

        return user_input 


def add_item(inventory_list):
    print("--- NHẬP HÀNG HÓA MỚI ---")
    new_id = validate_input("Nhập mã hàng hóa (ID): ","id")
    new_name = validate_input("Nhập tên hàng hóa: ", "name")
    new_quantity = validate_input("Nhập số lượng tồn kho: ", "quantity")

    new_inventory = {"id": new_id, "name": new_name, "quantity": new_quantity}
    inventory_list.append(new_inventory)
    print("Thêm hàng hóa vào kho thành công!")

def update_quantity(inventory_list):
    print("--- CẬP NHẬT SỐ LƯỢNG TỒN KHO ---")
    id_update = validate_input("Nhập mã hàng hóa cần sửa: ", "id")
    for index in inventory_list:
        if id_update == index.get("id"):
            print(f"Tìm thấy hàng hóa: {index.get("name")} (Số lượng hiện tại: {index.get("quantity")})")
            quantity_update = validate_input("Nhập số lượng mới: ", "quantity")
            index["quantity"] = quantity_update
            print("Cập nhật số lượng thành công!")
    else:
        print(f"Không tìm thấy hàng hóa có mã [{id_update}]")
        

def main():
    inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
    ]

    while True:
        menu()
        
        choise = input("Mời bạn chọn chức năng (1-4): ")

        match choise:
            case "1":
                show_inventory(inventory)
            case "2":
                add_item(inventory)
            case "3":
                update_quantity(inventory)
            case "4":
                break
            case _:
                print("Lựa chọn không hợp lệ!")

main()