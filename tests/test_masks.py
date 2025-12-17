# tests/test_masks.py
import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "inp, expected",
    [
        # карта с названием → группировка 4-4-4-4 с маской "79** ****"
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
        # строка, начинающаяся со "Счет" → маска от этой функции ДВЕ звезды
        ("Счет 73546108430315874305", "Счет **4305"),
    ],
)
def test_get_mask_card_number_various(inp, expected):
    assert get_mask_card_number(inp) == expected


@pytest.mark.parametrize(
    "number, expected_tail",
    [
        (7000792289606361, "6361"),
        (4305, "4305"),
        (12, "12"),  # короткий номер — берём как есть
    ],
)
def test_get_mask_account_returns_three_stars_plus_last4(number, expected_tail):
    res = get_mask_account(number)
    assert res.endswith(expected_tail)
    assert res.startswith("**")
