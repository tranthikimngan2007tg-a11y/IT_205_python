print("--- EMERGENCY TRIAGE SYSTEM ---")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

# Hệ thống phân loại ưu tiên
if heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")

# Phân tích lỗi 
# 1
# Nếu heart_rate = 135 thì nó sẽ in ra khối lênh YELLOW vì if là khối lệnh thực hiện đầu tiên nếu if không thỏa mãn mới thực hiện tiêp elif 

# 2 độ ưu tiên 
# if: Điểm kiểm tra đầu tiên. Nếu điều kiện đúng, thực thi khối lệnh bên trong và thoát cấu trúc.
# elif (Else If): Điểm kiểm tra bổ sung. Chỉ được xét đến nếu tất cả các điều kiện if hoặc elif phía trên nó bị trả về giá trị False.
# else: Nhánh bao quát cuối cùng. Tự động thực thi nếu toàn bộ các điều kiện phía trên đều không thỏa mãn.

# 3 nguyên nhân  bỏ qua khối lệnh RED
# Vì haert_rate > 100 đã in ra khối lệnh YELLOW và kết thúc nên heart_rate > 120 khối lệnh elif nên nếu có lớn hơn 120 thì khi chạy lệnh if đầu đã in ra YELLOW nên không chạy tới lệnh RED

# Sửa

print("--- EMERGENCY TRIAGE SYSTEM ---")
heart_rate = int(input("Enter patient's heart rate (bpm): "))
# Chỉ cần chuyên điều kiện heart_rate > 120 lên lệnh if đầu là được
if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")  