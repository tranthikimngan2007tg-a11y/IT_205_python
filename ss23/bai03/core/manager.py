from datetime import datetime


def check_duplicate_id(
    flight_id,
    flight_list
):
    """
    Kiểm tra mã
    chuyến bay trùng
    """

    normalized_id = (
        flight_id
        .strip()
        .upper()
    )

    for flight in flight_list:

        if (
            flight[
                "flight_id"
            ]
            ==
            normalized_id
        ):
            return True

    return False


def add_new_flight(
    flight_list
):
    """
    Thêm chuyến bay mới
    """

    print(
        "----- TIẾP NHẬN "
        "CHUYẾN BAY MỚI -----"
    )

    flight_id = input(
        "Nhập mã chuyến bay: "
    )

    normalized_id = (
        flight_id
        .strip()
        .upper()
    )

    if check_duplicate_id(
        normalized_id,
        flight_list
    ):
        print(
            "Mã chuyến bay "
            "đã tồn tại!"
        )
        return

    try:

        passengers = int(
            input(
                "Nhập số lượng "
                "hành khách: "
            )
        )

        depart_time = input(
            "Nhập thời gian "
            "cất cánh "
            "(YYYY-MM-DD "
            "HH:MM:SS): "
        )

        datetime.strptime(
            depart_time,
            "%Y-%m-%d %H:%M:%S"
        )

        duration_min = int(
            input(
                "Nhập số "
                "phút bay: "
            )
        )

        new_flight = {
            "flight_id":
            normalized_id,
            "passengers":
            passengers,
            "depart_time":
            depart_time,
            "duration_min":
            duration_min
        }

        flight_list.append(
            new_flight
        )

        print(
            f">> Thêm "
            f"chuyến bay "
            f"{normalized_id} "
            "thành công!"
        )

    except ValueError:
        print(
            "Sai định dạng "
            "thời gian! "
            "Vui lòng nhập "
            "đúng chuẩn "
            "YYYY-MM-DD "
            "HH:MM:SS"
        )