class PTITStudent:
    def __init__(self, para_name, para_gpa):
        self.name = para_name
        self.__gpa = para_gpa
    
    def phan_loai(self):        # Y/c tạo method để phân loại sinh viên trên 3.6 là in ra xuất sắc còn lại in ra khá
        if self.__gpa > 3.6:
            print(f"Xuất sắc")
        else:
            print("Khá")

    def say_goodbye():
        print("Good bye see you again!")

student_tuxa = PTITStudent("Ngân", 3.7)
print(f"Sinh viên {student_tuxa.name} có GPA là: {student_tuxa.__gpa}")
student_tuxa.phan_loai()


    