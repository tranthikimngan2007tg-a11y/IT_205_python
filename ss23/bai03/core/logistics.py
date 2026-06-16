import math


def show_flight_schedule(
    flight_list
):
    """
    Hiển thị lịch trình
    và hậu cần
    """

    print(
        "----- DANH SÁCH "
        "CHUYẾN BAY "
        "& HẬU CẦN -----"
    )

    for index, flight in enumerate(
        flight_list,
        start=1
    ):

        water_boxes = (
            math.ceil(
                flight[
                    "passengers"
                ] / 10
            )
        )

        print(
            f"{index}. "
            f"Mã: "
            f"{flight['flight_id']} "
            f"| Khởi hành: "
            f"{flight['depart_time']} "
            f"| Số khách: "
            f"{flight['passengers']} "
            f"| Dự phòng: "
            f"{water_boxes} "
            "thùng nước."
        )