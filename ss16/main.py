# Hàm không có tham số -> không có giá trị trả về
# def sum():
#     a = 10
#     b = 20
#     print(a + b)
# Hàm có tham số
# def sum(a, b):
#     print(a + b)

# def sum(a, b):
#     return (a + b)

# result = sum(10, 20)
# print(result)

#  biến global toàn cục
# counter = 10

# def increment():
#     # Biến local
#     global counter
#     counter = counter + counter

# increment()

# print(counter)
# counter = 0
# for i in range(5):
#     counter += 1

# print(counter)

# Yêu cầu: Tạo 1 menu gôm 3 chức năng. Menu phải dùng hàm
# Chức năng 1: Nhập sinh viên vào danh sách (Nhập số lượng sv, rồi nhập từng sv vào)
# Chức năng 2: HIển thị danh sách sinh viên ra màn hình
# Chức năng 3: Tìm kiếm sinh viên theo tên (tìm tương đối)
# Lưu ý: tất cả đều dùng hàm để gọi vào trong mỗi case


def get_validate_input(prompt: str, input_type: str = "str"):
    while True:
    # "7.5"
        user_input = input(prompt)
        if not user_input:
            print("Dữ liệu không được để trống! Nhập lại")
            continue

        if input_type == "int":
            # if user_input.isdigit():
            #     value = int(user_input)
            #     return value
            # else:
            #     print("Dữ liệu không được chưa kí tự! Nhập lại")
            #     continue
            try:
                # -123 "7.5"
                value = int(user_input)
                if value <= 0:
                    print("Dữ liệu không được là số âm! Nhập lại")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ! Nhập lại")
                continue

        # if input_type == "float":
        #     try:
        #         # -123 "7.5"
        #         value = float(user_input)
        #         if value <= 0:
        #             print("Dữ liệu không được là số âm! Nhập lại")
        #             continue
        #         return value
        #     except ValueError:
        #         print("Dữ liệu không hợp lệ! Nhập lại")
        #         continue
        return user_input
    

# id = get_validate_input("Hãy nhập id: ", "int")



def menu():
    print("=" * 60)
    print("=====Menu=======")
    print("1. Nhập danh sách sinh viên\n" +
          "2. Hiển thị danh sách sinh viên\n" +
          "3. Tìm kiếm danh sách sinh viên theo tên\n" +
          "4. Thoát chương trình!\n"
    )
    print("=" * 60)

def input_std(students):
    num_std = get_validate_input("Hãy nhập số lượng sinh viên: ", "int")
    for i in range(num_std):
        print(f"Nhập sinh viên thứ {i + 1}")
        while True:
            id_std = get_validate_input("Nhập vào id sinh viên: ")
            # flag = False
            for item in students:
                if id_std.lower() == item.get("id").lower():
                    print("Id không được trùng! Nhập lại")
                    # flag = True
                    break
            else: 
            # if flag == False:
                break
        name_std = get_validate_input("Nhập vào tên sinh viên: ")
        new_std = { "id": id_std, "name": name_std }
        students.append(new_std)
        
        
def show_std(students):
    if not students:
        print("Danh sách rỗng")
        return
    print(f"{"STT":<3} | {"ID":<3} | {"Tên":<20}")
    for index, value in enumerate(students, start=1):
        print(f"{index:<3} | {value.get('id'):<3} | {value.get('name', 'Không có dữ liệu'):<20}")


def search_std(students):
    if not students:
        print("Danh sách rỗng")
        return
    found_name = get_validate_input("Nhập vào tên cần tìm: ")
    find_student = []
    for item in students:
        if found_name.lower() in item.get("name").lower():
            new_std = {"id": item.get("id"), "name": item.get("name")}
            find_student.append(new_std)

    show_std(find_student)

def main():
    students = [
        { "id": "S001", "name": "Khoa khấu khỉnh "},
        { "id": "S002", "name": "Khoa khờ khỉnh "}
    ]; 
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                input_std(students)
            case "2":
                show_std(students)
            case "3":
                search_std(students)
            case "4":
                print("Thoát chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

main()