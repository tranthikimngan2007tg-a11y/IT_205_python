print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra điều kiện hiến máu
if donor_age >= 18 or donor_weight >=50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")

# Phân tích lỗi 
# 1
# Sử dụng toán tử logic or là sai phải sử dụng and

# 2 Dò luồng thực thi (trace code) với test case: donor_age = 16, donor_weight = 55.
# Bởi vì đây đã sử dụng toan tử or nên khi thỏa 1 trong 2 điều kiện thì nó vẫn đúng và in ra khối lệnh if

# 3
# Toán tử and là khi cả 2 đều thỏa điều kiện thì mới trả về true còn or thì chỉ cần ít nhất 1 điều kiện đúng đã trả thì true rồi


print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Thay or thành and
if donor_age >= 18 and donor_weight >=50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")
