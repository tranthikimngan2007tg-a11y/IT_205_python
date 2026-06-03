n = (1, 2, 3, 4, 5)
# print(n[-1])
# for i in range(len(n)):
#     print(n[i])
# for i in n:
#     print(i)
# for i, v in enumerate(n,start=0):
#     print(i, v)
# user = {
#     "name": "Ngân",
#     "age": 19
# }
# print(user["name"])
# print(user.get("name"))

# list_user = ("user01", "user02", "user03")

# user = {
#     list_user[0]: {"name": "Ngân"} ,
#     "user02": {"name": "Nga"} ,
#     "user03": {"name": "Nguyệt"} 
# }
# print(user["user02"]["name"])
# print(user.get(list_user[0]).get("name"))

# Yêu cầu: Tạo 1 danh sách users
# Thêm 5 phần tử vào danh sánh
# Mỗi phần tử là 1 dict
# Hiển thị toàn bộ thông tin users ra màn hình



users = [
    { "name": "Tuấn", "age": 25 },
    { "name": "Trường", "age": 25 },
    { "name": "Bảo", "age": 25 },
]

for i in range(len(users)):
    print(f"Sinh viên: {users[i]["name"]} - tuổi: {users[i]["age"]}")
