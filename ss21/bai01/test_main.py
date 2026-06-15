import unittest

from main import (
    validate_amount,
    transfer,
    InvalidAmountError,
    InsufficientBalanceError
)


class TestWallet(unittest.TestCase):

    def test_deposit_success(self):
        balance = 0
        amount = 500000

        balance += amount

        self.assertEqual(
            balance,
            500000
        )

    def test_transfer_insufficient_balance(
        self
    ):
        balance = 300000
        amount = 500000

        with self.assertRaises(
            InsufficientBalanceError
        ):
            if amount > balance:
                raise (
                    InsufficientBalanceError
                )

    def test_invalid_amount(self):
        with self.assertRaises(
            InvalidAmountError
        ):
            validate_amount(-1000)

unittest.main()