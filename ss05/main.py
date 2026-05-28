# col = 3, row = 5

# for i in range(5):
#     for j in range(3):
#         print("*", end=" ")
#     print()

# Tam giác vuông cân cạnh 5

# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# Tam giác ngược lại

# for i in range(1, 5 + 1):
#     for j in range(1,5-i +1):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()

# Tam giác góc vuông bên trái phía trên

# for i in range(1, 5 + 1):
#     for j in range(5 - i +1):
#         print("*",end=" ")
#     for k in range(i):
#         print(" ", end=" ")
#     print()

# Tam giác đỉnh trên

# canh = 5
# for i in range(canh):
#     for j in range(canh - i -1):
#         print(" ", end=" ")
#     for k in range(i*2+1):
#         print("*", end=" ")
#     print()

# Số nguyên tố
import math
a = int(input("Nhâp 1 số: "))
count = 0
if(a < 2):
    print(f"Số {a} không phải là số nguyên tố")
else:
    for i in range(2 ,int(math.sqrt(a)) , 1):
        if(a % i == 0 ):
            print("Không phải số nguyên tố")
            count = 1
            break
    if(count == 0):
        print(f"Số {a} là số nguyên tố")
    

