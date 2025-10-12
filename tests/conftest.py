# tests/conftest.py
import pytest

@pytest.fixture
def card_raw_and_mask():
    # входная строка с названием + 16 цифр
    raw = "Visa Platinum 7000792289606361"
    expected = "Visa Platinum 7000 79** **** 6361"
    return raw, expected

@pytest.fixture
def account_raw_and_mask():
    raw = "Счет 35383033474447895960"
    # widget.mask_account_card использует get_mask_account(),
    # который возвращает ТРИ звезды. Это отличается от masks.get_mask_card_number.
    expected = "Счет **5960"
    return raw, expected

@pytest.fixture
def iso_dates():
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2021-12-01T00:00:00", "01.12.2021"),
    ]
