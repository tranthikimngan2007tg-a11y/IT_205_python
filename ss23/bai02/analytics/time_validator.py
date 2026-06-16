from datetime import datetime


def parse_and_inspect_date(
    date_str
):
    """
    Kiểm tra định dạng ngày
    """
    try:
        upload_date = (
            datetime.strptime(
                date_str,
                "%Y-%m-%d"
            )
        )

        return upload_date

    except ValueError:
        print(
            f"[ERROR] "
            f"Định dạng ngày upload "
            f"'{date_str}' "
            f"không tồn tại"
        )

        return None