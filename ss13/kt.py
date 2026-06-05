employee = [
    {"id": 101, "name": "Nguyen Van A", "salary": 10.0},
    {"id": 102, "name": "Le Thi B", "salary": 15.5}
]

while True:
    print("\nQUẢN LÝ NHÂN SỰ - STAFF MANAGER")
    print("1. Thêm nhân viên mới")
    print("2. Danh sách nhân viên")
    print("3. Xóa nhân viên khỏi hệ thống")
    print("4. Thoát chương trình")

    choise = input("> Mời bạn lựa chọn: ")

    match choise:
        case "1":
            # id tự tăng
            if(employee == ""):
                id = 101
            else:
                id = employee[-1].get("id") + 1
                id = int(id)
            while True:
                name = input("Nhập tên nhân viên: ")
                if( name == ""):
                    print("Tên nhân viên không được để trống")
                else: 
                    break
            
            while True:
                salary = input("Nhập mức lương: ")
                if(float(salary) <= 0 or salary == ""):
                    print("Lỗi: Vui lòng nhập mức lương lớn hơn 0!")
                else:
                    salary = float(salary)
                    break
            
            new_employee = {"id": id, "name": name, "salary": salary}
            employee.append(new_employee)
            print(f"Thêm nhân viên thành công! ID: {id}")

        case "2":
            if(employee == ""):
                print("Chưa có dữ liệu nhân sự!")
            else:
                print(f"{'ID':<5} | {'TÊN NHÂN VIÊN':<19}| MỨC LƯƠNG")
                print("-------------------------------------")
                for i in employee:
                    print(f"{i.get("id"):<5}| {i.get("name"):<19}| {i.get("salary"):.2f}")
        case "3":
            del_id = input("Nhập id muốn xóa: ")
            flag = False
            for index, value in enumerate(employee,start=0):
                if(int(del_id) == value.get("id")):
                    employee.pop(index)

                    flag = True
            
            if(flag == False):
                print("Không tìm thấy nhân viên để xóa!")
            else:
                print(f"Đã xóa nhân viên ID {del_id} thành công!")

        case "4":
            break

        case _:
            print("Lựa chọn không hợp lệ!")