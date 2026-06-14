# (1) Phân tích & Clean Code
# Tên biến/hàm: dùng snake_case theo PEP 8 (display_matches, update_score, generate_report).

# Docstrings: mỗi hàm đều có mô tả chức năng, tham số, và giá trị trả về.

# Logging: cấu hình ghi log ra file tournament_app.log với định dạng [Thời gian] - [Cấp độ Log] - [Tin nhắn].

# Exception Handling: mọi input từ người dùng đều được bọc trong try...except.

# Module hóa: mỗi chức năng menu là một hàm riêng biệt.

# (2) Triển khai Code (main.py)

import logging
import unittest

logging.basicConfig(
    filename="tournament_app.log",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)

matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]

def display_matches(match_list):
    """Hiển thị lịch thi đấu và kết quả."""
    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return
    print("--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print("Mã trận   | Đội A           | Đội B           | Tỷ số   | Trạng thái")
    print("----------------------------------------------------------------------")
    for match in match_list:
        try:
            print(f"{match['match_id']:<9}| {match['team_a']:<15}| {match['team_b']:<15}| "
                  f"{match['score_a']}-{match['score_b']:<5}| {match['status']}")
        except KeyError as e:
            logging.error(f"Missing key in match data: {e}")
    logging.info("User viewed the match list.")

def add_match(match_list):
    """Thêm trận đấu mới vào danh sách."""
    print("--- THÊM TRẬN ĐẤU MỚI ---")
    match_id = input("Nhập mã trận đấu: ").strip()
    if not match_id:
        print("Mã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return
    if any(m["match_id"] == match_id for m in match_list):
        print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
        logging.warning(f"Match ID {match_id} already exists.")
        return
    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()
    if not team_a or not team_b:
        print("Tên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return
    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
    match_list.append(new_match)
    print(f"Thành công: Đã thêm trận đấu {match_id}.")
    logging.info(f"Match {match_id} added successfully")

def update_score(match_list):
    """Cập nhật tỷ số trận đấu."""
    print("--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")
    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip()
    match = next((m for m in match_list if m["match_id"] == match_id), None)
    if not match:
        print(f"Không tìm thấy trận đấu mang mã {match_id}.")
        logging.warning(f"User tried to update non-existing match {match_id}")
        return
    print(f"Trận đấu: {match['team_a']} vs {match['team_b']} ({match['status']})")

    while True:
        try:
            score_a = int(input("Nhập điểm Đội A: "))
            if score_a < 0:
                logging.error(f"Negative score input detected: {score_a}")
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                continue
            break
        except ValueError as e:
            logging.error(f"Invalid score input. Error: {e}")
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")

    while True:
        try:
            score_b = int(input("Nhập điểm Đội B: "))
            if score_b < 0:
                logging.error(f"Negative score input detected: {score_b}")
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                continue
            break
        except ValueError as e:
            logging.error(f"Invalid score input. Error: {e}")
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")

    match["score_a"] = score_a
    match["score_b"] = score_b

    if score_a == 0 and score_b == 0:
        confirm = input("Tỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): ").lower()
        if confirm == "y":
            match["status"] = "Completed"
    else:
        match["status"] = "Completed"

    print(f"Thành công: Đã cập nhật tỷ số trận đấu {match_id}.")
    logging.info(f"Match {match_id} score updated successfully")

def determine_winner(match):
    """Xác định đội thắng của một trận đấu."""
    if match["status"] != "Completed":
        return "Not Started"
    if match["score_a"] > match["score_b"]:
        return match["team_a"]
    elif match["score_b"] > match["score_a"]:
        return match["team_b"]
    else:
        return "Draw"

def generate_report(match_list):
    """Tạo báo cáo thống kê giải đấu."""
    print("--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")
    completed_matches = [m for m in match_list if m["status"] == "Completed"]
    if not completed_matches:
        print("Chưa có trận đấu nào hoàn thành.")
        print("Tổng số trận đã hoàn thành: 0")
        return
    for match in completed_matches:
        winner = determine_winner(match)
        print(f"{match['match_id']}: {match['team_a']} {match['score_a']}-{match['score_b']} {match['team_b']} | Kết quả: {winner}")
    print(f"Tổng số trận đã hoàn thành: {len(completed_matches)}")
    logging.info("User generated tournament report.")

def main():
    while True:
        print("===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====")
        print("1. Hiển thị lịch thi đấu & Kết quả")
        print("2. Thêm trận đấu mới")
        print("3. Cập nhật tỷ số trận đấu")
        print("4. Báo cáo thống kê")
        print("5. Thoát chương trình")
        print("==================================================")
        choice = input("Chọn chức năng (1-5): ")

        match choice:
            case "1":
                display_matches(matches)
            case "2":
                add_match(matches)
            case "3":
                update_score(matches)
            case "4":
                generate_report(matches)
            case "5":
                print("Thoát chương trình.")
                logging.info("System closed by user.")
                break
            case _:
                print("Lựa chọn không hợp lệ.")
                logging.warning("Invalid menu choice selected.")


class TestDetermineWinner(unittest.TestCase):
    def test_team_a_wins(self):
        match = {"team_a": "T1", "team_b": "GenG", "score_a": 2, "score_b": 0, "status": "Completed"}
        self.assertEqual(determine_winner(match), "T1")

    def test_team_b_wins(self):
        match = {"team_a": "T1", "team_b": "GenG", "score_a": 0, "score_b": 3, "status": "Completed"}
        self.assertEqual(determine_winner(match), "GenG")

    def test_draw(self):
        match = {"team_a": "T1", "team_b": "GenG", "score_a": 1, "score_b": 1, "status": "Completed"}
        self.assertEqual(determine_winner(match), "Draw")

    def test_not_started(self):
        match = {"team_a": "T1", "team_b": "GenG", "score_a": 0, "score_b": 0, "status": "Pending"}
        self.assertEqual(determine_winner(match), "Not Started")

main()

