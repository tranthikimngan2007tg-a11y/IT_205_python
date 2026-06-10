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
    # global students; 
    num_std = int(input("Nhập số lượng sinh viên: "))
    for i in range(num_std):
        print(f"Nhập sinh viên thứ {i + 1}")
        id_std = input("Nhập vào id sinh viên: ")
        name_std = input("Nhập vào tên sinh viên: ")
        new_std = { "id": id_std, "name": name_std }
        students.append(new_std)

def show_std(students):
    # global students
    print("Danh sách sinh viên!")
    for index, value in enumerate(students):
        print(f"Sinh viên thứ {index + 1}: Id: {value.get("id")} - Tên: {value.get("name")}")

def search_std(students):
    search_name = input("Nhập vào tên muốn tìm: ")
    flag = False
    for item in students:
        if (search_name in  item.get("name")):
            print(f"Sinh viên id: {item.get('id')} Tên: {item.get('name')}")
            flag = True
    if (not flag):
        print("Không tìm thấy sinh viên có tên là", search_name)

def main():
    
    students = []; 
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