import random
import string


def generate_assignment_code():
    """
    Sinh mã bài tập
    """

    characters = (
        string.ascii_uppercase
        +
        string.digits
    )

    random_code = (
        "".join(
            random.choices(
                characters,
                k=4
            )
        )
    )

    assignment_code = (
        f"PY-"
        f"{random_code}"
    )

    print(
        "\n--- SINH "
        "MÃ BÀI TẬP ---"
    )

    print(
        "Mã bài tập "
        "của bạn là: "
        f"{assignment_code}"
    )