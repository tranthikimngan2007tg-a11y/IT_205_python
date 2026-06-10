def menu():
    print("=" * 50)
    print("1. Hiện thị danh sách cầu thủ\n" + 
          "2. Tiếp nhận cầu thủ mới\n" + 
          "3. Cập nhật thông tin và chỉ số\n" + 
          "4. Xóa cầu thủ\n" + 
          "5. Tìm kiếm cầu thủ\n" + 
          "6. Thống kê loại phong độ\n" + 
          "7. Đánh giá phong độ tự động\n" + 
          "8. Thoát chương trình\n")
    print("=" * 50)

def validate_input(promt: str, input_type :str = "string"):
    

def display_players(players):
    if not players:
        print("Danh sách cầu thủ rỗng")
        return
    print("====== DANH SÁCH CẦU THỦ ======")
    print(f"{'Mã CT':<8} | {'Họ tên':<20} | {'Số trận đấu':<15} | {'Số bàn thắng':<15} | {'Số kiến tạo':<15} | {'Hiệu suất':<15} | {'Phong độ':<20}")
    
    for player in players:
        print(f"{player.get('id'):<8} | {player.get('name'):<20} | {player.get('match'):<15} | {player.get('goal'):<15} | {player.get('assist'):<15} | {player.get('rank', 'Chưa tính toán'):<15} | {player.get('form', 'Chưa tính toán'):<20}")


def main():
    players = [
        {"id": "CT001", "name": "Kim Ngân", "match": 10, "goal": 10, "assist": 30},
        {"id": "CT002", "name": "Diễm Quỳnh", "match": 10, "goal": 20, "assist": 40}
    ]
    while True:
        menu()
        choice = input("Nhập vào lựa chọn của bạn (1-8): ")
        match choice:
            case "1":
                display_players(players)
            case "2":
                print("Chức năng thêm cầu thủ mới chưa viết")
            case "3":
                print("Chức năng cập nhật chưa viết")
            case "4":
                print("Chức năng xóa chưa viết")
            case "5":
                print("Chức năng tìm kiếm chưa viết")
            case "6":
                print("Chức năng thống kê chưa viết")
            case "7":
                print("Chức năng đánh giá chưa viết")
            case "8":
                break
            case _:
                print("Lựa chọn không hợp lệ!")

main()
