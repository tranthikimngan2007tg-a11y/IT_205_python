import random

print("Hãy nhập thông tin bệnh nhân")
name = input("Tên bệnh nhân: ")
gender = input("Giới tính: ")
year_of_birth = int(input("Năm sinh: "))
phone_number = int(input("Số điện thoại: "))
email = input("Email: ")
initial_symtoms = input("Triệu chứng ban đầu: ")
examination_costs = float(input("Chi phí khám: "))
random_number = random.randint(100, 999)

print("====== Thông tin bệnh nhân ======\n",
      "Mã bệnh nhân: ", "BN",str(year_of_birth) + str(random_number),"\n",
      "Tên bệnh nhân: ", name, type(name),"\n",
      "Giới tính: ", gender, type(gender),"\n",
      "Năm sinh: ", year_of_birth, type(year_of_birth ),"\n",
      "Số điện thoại: ", phone_number, type(phone_number),"\n",
      "Email: ", email, type(email),"\n",
      "Triệu chứng ban đầu: ",initial_symtoms, type(initial_symtoms),"\n",
       "Chi phí khám: ", examination_costs, type(examination_costs))

