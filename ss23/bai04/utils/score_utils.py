def calculate_average(
    scores
):
    """
    Tính điểm trung bình
    """

    if not scores:
        return 0

    valid_scores = []

    for score in scores:

        if isinstance(
            score,
            (int, float)
        ):
            valid_scores.append(
                score
            )

    if not valid_scores:
        return 0

    average = (
        sum(valid_scores)
        /
        len(valid_scores)
    )

    return average


def classify_student(
    average
):
    """
    Phân loại học lực
    """

    if average >= 8:
        return "Giỏi"

    if average >= 6.5:
        return "Khá"

    if average >= 5:
        return (
            "Trung bình"
        )

    return "Yếu"