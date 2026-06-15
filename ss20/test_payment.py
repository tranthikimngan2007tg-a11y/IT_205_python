from main import calculate_payment
import pytest 

# Trường hợp tốt nhất
def test_happy():
    assert calculate_payment(100.0, 0.1) == 90.0

def test_full_rate():
    assert calculate_payment(100.0, 1) == 0.0

def test_zero_rate():
    assert calculate_payment(100.0, 0.0 ) == 100.0

def test_negative():
    with pytest.raises(TypeError):
        calculate_payment(-100.0, 0.0)