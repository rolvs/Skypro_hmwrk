# tests/test_widget.py
import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_for_account(account_raw_and_mask):
    raw, expected = account_raw_and_mask
    assert mask_account_card(raw) == expected


def test_mask_account_card_for_card(card_raw_and_mask):
    raw, expected = card_raw_and_mask
    assert mask_account_card(raw) == expected


@pytest.mark.parametrize("iso_in, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2020-01-09T10:00:00", "09.01.2020"),
])
def test_get_date_formats_iso_to_dd_mm_yyyy(iso_in, expected):
    assert get_date(iso_in) == expected
