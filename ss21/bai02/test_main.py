from main import (
    calculate_total,
    validate_quantity
)


def test_calculate_total():
    """Test calculate total."""

    mock_order = [
        {
            "code": "P1",
            "quantity": 2
        },
        {
            "code": "F1",
            "quantity": 1
        }
    ]

    result = calculate_total(
        mock_order
    )

    assert result == 125000


def test_invalid_quantity():
    """Test invalid quantity."""

    try:
        validate_quantity(-1)

    except Exception as error:
        assert (
            str(error)
            == "InvalidQuantityError"
        )


def run_tests():
    """Run all tests."""

    test_calculate_total()
    test_invalid_quantity()

    print("2 tests passed.")

run_tests()