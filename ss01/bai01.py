print('--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---')

name_patient = input('Nhập tên bệnh nhân: ')
age = int(input('Mời bạn nhập tuổi: '))
symptom = input('Mời bạn nhập triệu chứng bệnh: ')

print('--- PHIẾU KHÁM BỆNH ---')

#tên bệnh nhân là name_patient nhưng lại truyền vào để in symptom dẫn tới sai thông tin
print('Tên bệnh nhân:', symptom)

#tên bệnh nhân là age nhưng lại truyền vào để in name_patient dẫn tới sai thông tin
print('Tuổi:', name_patient)

#tên bệnh nhân là name_patient nhưng lại truyền vào để in symptom dẫn tới sai thông tin
print('Triệu chứng:', age)