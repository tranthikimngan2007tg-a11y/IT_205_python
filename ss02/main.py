# Yêu cầu nhập vào 2 số a, b , kểm tra số lớn nhất trong 2 
# f {} chuyền int và str

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# max = 0

# if (a > b):
#      max = a
# else:
#      max = b

# print("Số lớn nhất là: ", max)

# Yêu cầu 2: Cho người dùng nhập vào số nguyên dương 
# Dùng toán tử 3 ngổi kiểm tra. Nếu như lớn hơn 20 thì in ra là đúng

# c = int(input("Nhập số c: "))
# if c < 0:
#     print("Vui lòng nhập số nguyên dương!");
# else:
#     print("Đúng") if c > 20 else print("Sai")

# Yêu cầu 3: Cho người dùng nhập vào 1 số trong khoảng từ 2 -> 8
# Tương ứng sẽ in ra màn hình với thứ tương ứng

# n = int(input("Nhập 1 số từ 2 -> 8: "))
# if (n < 2) or (n > 8):
#     print("Vui lòng nhập trong khoảng 2 -> 8 !")
# else:
#     match n:
#         case 2:
#             print("Monday")
#         case 3:
#             print("Tuesday")
#         case 4:
#             print("Wednesday")
#         case 5:
#             print("Thursday")
#         case 6:
#             print("Friday")
#         case 7:
#             print("Saturday")
#         case 8 :
#             print("Sunday")

# Yêu cầu 4: In ra các số chẵn từ 1 -> 10 lưu ý bỏ qua số 4

# i = 2
# while (i <= 10):
#     if (i == 4):
#         i += 2
#         continue
#     print(i)
#     i +=2
               
# Yêu cầu 5: Cho người dùng nhập vào 1 số , nếu số đó không phải số nguyên dương , bắt nhập lại

# while(1):
#     a = int(input("Nhập vào số nguyên dương: "))
#     if(a <= 0):
#         print("Vui lòng nhập số nguyên dương !\n")
#     else:
#         print("Số nguyên dương là:",a)
#         break

# Yêu cầu 6: Cho 2 số a, b cho trước, tìm UCLN ủa 2 số.

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# min = 0

# if a > b:
#     min = b;
# else:
#     min = a;


# for i in range(min, 0, -1):
#     if ((a % i == 0) and (b % i == 0)):
#         print(f"UCLN của {a} và {b} là {i}")
#         break

# Yêu cầu 7: tìm bội chung nhỏ nhất của 2 số

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# max = 0

# if a < b:
#     max = b;
# else:
#     max = a;

# i = max
# while(i >= max):
#     if (i % a == 0) and (i % b == 0 ):
#         break
#     i += 1

# print(f"BCNN là {i}")

# Yêu cầu 8: Cho biểu thức 2a + b = 10 
# Tìm a và b thỏa mãn phương trình 

