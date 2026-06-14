# (1) Phân tích Thiết kế
# Refactoring Plan (áp dụng Clean Code – PEP 8)
# Đặt tên biến/hàm theo snake_case: ví dụ display_roster, sign_player, update_player_status.

# Docstrings cho mỗi hàm: mô tả chức năng, tham số, và giá trị trả về.

# Single Responsibility Principle: mỗi hàm chỉ làm một việc duy nhất (hiển thị, thêm, cập nhật, báo cáo).

# Logging Strategy
# File log: roster_app.log.

# Format: [Thời gian] - [Level] - [Message].

# Level sử dụng:

# INFO: hành động thành công (xem roster, thêm, cập nhật, báo cáo).

# WARNING: nhập sai, dữ liệu trùng, thiếu thông tin.

# ERROR: lỗi nghiêm trọng (thiếu key, nhập lương không hợp lệ).

# Input/Output & Luồng xử lý cho update_player_status(roster_list)
# Input: danh sách roster (list of dict), mã tuyển thủ nhập từ HLV.

# Output: cập nhật lương hoặc trạng thái của tuyển thủ trong danh sách.

# Exceptions:

# ValueError: nhập lương không phải số hoặc âm → yêu cầu nhập lại.

# KeyError: thiếu key trong dữ liệu → log ERROR, hiển thị thông báo.

# Pseudocode:

# Code
# function update_player_status(roster_list):
#     ask player_id
#     find player in roster_list
#     if not found:
#         print error, log WARNING
#         return
#     show current info
#     ask choice (1: update salary, 2: update status)
#     if choice == 1:
#         loop until valid salary:
#             try convert to float
#             if <=0: print error
#             else update salary, log INFO
#     if choice == 2:
#         ask new status (Active/Benched)
#         update status, log INFO
# (2) Triển khai Code & Testing

import logging
import unittest

# ================== CẤU HÌNH LOGGING ==================
logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)

# ================== DỮ LIỆU BAN ĐẦU ==================
roster = [
    {"player_id": "P01", "name": "Faker", "role": "Mid Lane", "salary": 5000.0, "status": "Active"},
    {"player_id": "P02", "name": "Oner", "role": "Jungle", "salary": 3500.0, "status": "Active"},
    {"player_id": "P03", "name": "Ruler", "role": "ADC", "salary": 6000.0, "status": "Benched"}
]

# ================== HÀM PHỤ TRỢ ==================
def calculate_actual_pay(player_dict):
    """Tính lương thực nhận dựa trên trạng thái."""
    try:
        if player_dict["status"] == "Active":
            return player_dict["salary"]
        elif player_dict["status"] == "Benched":
            return player_dict["salary"] * 0.5
        else:
            return 0.0
    except KeyError as e:
        logging.error(f"Missing key in player data: {e}")
        return 0.0

# ================== CHỨC NĂNG 1 ==================
def display_roster(roster_list):
    """Hiển thị đội hình thi đấu."""
    if not roster_list:
        print("Đội hình hiện đang trống.")
        return
    print("--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print("ID   | Tên tuyển thủ        | Vị trí       | Lương   | Trạng thái")
    print("---------------------------------------------------------------")
    for player in roster_list:
        try:
            name_display = player["name"]
            if player.get("status") == "Benched":
                name_display += " [DỰ BỊ]"
            print(f"{player['player_id']:<5}| {name_display:<20}| {player['role']:<12}| "
                  f"{player['salary']:<10}| {player.get('status','Unknown')}")
        except KeyError as e:
            logging.error(f"Missing key in roster: {e}")
    logging.info("Coach viewed the team roster.")

# ================== CHỨC NĂNG 2 ==================
def sign_player(roster_list):
    """Chiêu mộ tuyển thủ mới."""
    print("--- CHIÊU MỘ TUYỂN THỦ MỚI ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()
    if not player_id:
        print("Mã tuyển thủ không được để trống.")
        logging.warning("Failed to sign player - Empty player ID")
        return
    if any(p["player_id"] == player_id for p in roster_list):
        print(f"Lỗi: Mã tuyển thủ {player_id} đã tồn tại.")
        logging.warning(f"Failed to sign player - Duplicate player ID {player_id}")
        return
    name = input("Nhập tên tuyển thủ: ").strip().title()
    role = input("Nhập vị trí thi đấu: ").strip().title()
    while True:
        try:
            salary = float(input("Nhập mức lương hàng tháng: "))
            if salary <= 0:
                print("Lương phải là số dương. Vui lòng nhập lại.")
                logging.warning("Failed to sign player - Invalid salary input")
                continue
            break
        except ValueError:
            print("Lương phải là số. Vui lòng nhập lại.")
            logging.warning("Failed to sign player - Invalid salary input")
    new_player = {"player_id": player_id, "name": name, "role": role, "salary": salary, "status": "Active"}
    roster_list.append(new_player)
    print(f"Thành công: Đã chiêu mộ tuyển thủ {name}.")
    logging.info(f"Signed new player {name} with salary {salary}")

# ================== CHỨC NĂNG 3 ==================
def update_player_status(roster_list):
    """Cập nhật lương hoặc trạng thái thi đấu."""
    print("--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ cần cập nhật: ").strip().upper()
    player = next((p for p in roster_list if p["player_id"] == player_id), None)
    if not player:
        print(f"Không tìm thấy tuyển thủ mang mã {player_id}.")
        logging.warning(f"Failed to update player - Player ID {player_id} not found")
        return
    print(f"Tuyển thủ: {player['name']}\nVị trí: {player['role']}\nLương hiện tại: {player['salary']}\nTrạng thái hiện tại: {player['status']}")
    choice = input("Bạn muốn cập nhật:\n1. Cập nhật lương\n2. Cập nhật trạng thái thi đấu\nChọn (1-2): ")
    if choice == "1":
        while True:
            try:
                new_salary = float(input("Nhập mức lương mới: "))
                if new_salary <= 0:
                    print("Lương phải là số dương. Vui lòng nhập lại.")
                    continue
                old_salary = player["salary"]
                player["salary"] = new_salary
                print(f"Thành công: Đã cập nhật lương cho tuyển thủ {player_id}.")
                logging.info(f"Updated player {player_id} salary from {old_salary} to {new_salary}")
                break
            except ValueError:
                print("Lương phải là số. Vui lòng nhập lại.")
    elif choice == "2":
        status_choice = input("Chọn trạng thái mới:\n1. Active\n2. Benched\nNhập (1-2): ")
        if status_choice == "1":
            player["status"] = "Active"
        elif status_choice == "2":
            player["status"] = "Benched"
        print(f"Thành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}.")
        logging.info(f"Updated player {player_id} status to {player['status']}")

# ================== CHỨC NĂNG 4 ==================
def generate_payroll_report(roster_list):
    """Báo cáo quỹ lương hàng tháng."""
    print("--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")
    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        return
    total = 0.0
    print("ID   | Tên tuyển thủ   | Trạng thái | Lương gốc | Lương thực nhận")
    print("---------------------------------------------------------------")
    for player in roster_list:
        try:
            actual_pay = calculate_actual_pay(player)
            print(f"{player['player_id']:<5}| {player['name']:<15}| {player['status']:<10}| {player['salary']:<10}| {actual_pay:<10}")
            total += actual_pay
        except KeyError as e:
            print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
            logging.error(f"Missing key while generating payroll report: {e}")
            total = 0.0
            break
    print("---------------------------------------------------------------")
    print(f"Tổng quỹ lương hàng tháng: {total}")
    logging.info(f"Generated monthly payroll report. Total: {total}")

# ================== MENU CHÍNH ==================
def main():
    while True:
        print("===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====")
        print("1. Xem đội hình thi đấu hiện tại")
        print("2. Chiêu mộ tuyển thủ mới")
        print("3. Cập nhật lương & Trạng thái thi đấu")
        print("4. Báo cáo quỹ lương hàng tháng")
        print("5. Thoát hệ thống")
        print("==================================================")
        choice = input("Chọn chức năng (1-5): ")
        match choice:
            case "1": display_roster(roster)
            case "2": sign_player(roster)
            case "3": update_player_status(roster)
            case "4": generate_payroll_report(roster)
            case "5":
                print("Thoát hệ thống.")
                logging.info("System closed by user.")
                break
            case _: 
                print("Lựa chọn không hợp lệ.")
                logging.warning("Invalid menu choice selected.")


class TestCalculateActualPay(unittest.TestCase):
    def test_active_player(self):
        player = {"name": "Faker", "salary": 5000.0, "status": "Active"}
        self.assertEqual(calculate_actual_pay(player), 5000.0)

    def test_benched_player(self):
        player = {"name": "Ruler", "salary": 6000.0, "status": "Benched"}
        self.assertEqual(calculate_actual_pay(player), 3000.0)

    def test_unknown_status(self):
        player = {"name": "Zeus", "salary": 4000.0, "status": "Unknown"}
        self.assertEqual(calculate_actual_pay(player), 0.0)

    def test_missing_salary_key(self):
        player = {"name": "Zeus", "status": "Active"}
        self.assertEqual(calculate_actual_pay(player), 0.0)

main()


