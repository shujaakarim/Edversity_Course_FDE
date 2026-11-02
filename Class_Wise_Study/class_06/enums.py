"""
2. Payment methods. Create a StrEnum called PaymentMethod with the options
CASH, CARD and BANK_TRANSFER, using auto(). Loop over it and print each option.
Then print whether PaymentMethod.CARD == "card".
"""

from enum import auto


class PaymentMethod:
    CASH = auto()
    CARD = auto()
    BANK_TRANSFER = auto()


for methods in PaymentMethod:
    if PaymentMethod.CARD == "card":
        print(methods)
