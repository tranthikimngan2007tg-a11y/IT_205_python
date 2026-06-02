# student = list()
# students = [1, 2, 3, 4, 5]
# students = ["Kim Ngân", 18, 1.56, True]

# print(students[1])

# students = ["Ngân", "A"]
# # result = students.append("B") # Phương thức này không trả về gì hết
# # print(result)  # None

# # studens.extend(["C", "D"])
# # stt = 1
# # for i in students:
# #     print(f"Số thứ {stt}: {i}")
# #     stt += 1

# for index, value in enumerate(students, start=1):
#     print(f"{index} {value}")

# Yêu cầu: Tạo 1 danh sách sinh viên cho người dùng nhập vào sl sv
# Chức năng 1: Nhập vào từng sinh viên (nhập sinh viên thứ 1 ....)
# Chức năng 2: Hiển thị ra từng sv

students = []
sl_sv = input("Nhập vào số lượng sinh viên muốn thêm: ")

for i in range(int(sl_sv)):
    sv = input(f"Nhập sinh viên thứ {i+1}: ")
    students.append(sv)
for i in range(len(students)):
    print(f"Sinh viên thứ {i+1}: {students[i]}")
