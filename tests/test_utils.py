from unittest.mock import patch

from utils import get_transaction_amount_rub


def test_get_transaction_amount_rub_rub_no_conversion():
    tx = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"},
        }
    }

    assert get_transaction_amount_rub(tx) == 100.50


@patch("utils.convert_to_rub", return_value=9000.0)
def test_get_transaction_amount_rub_usd_conversion(mock_convert):
    tx = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"},
        }
    }

    assert get_transaction_amount_rub(tx) == 9000.0
    mock_convert.assert_called_once_with(100.0, "USD")


@patch("utils.convert_to_rub", return_value=11000.0)
def test_get_transaction_amount_rub_eur_conversion(mock_convert):
    tx = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "EUR"},
        }
    }

    assert get_transaction_amount_rub(tx) == 11000.0
    mock_convert.assert_called_once_with(100.0, "EUR")


def test_get_transaction_amount_rub_missing_fields_returns_float():
    # если структура транзакции кривая — функция должна вернуть float
    tx = {}
    result = get_transaction_amount_rub(tx)
    assert isinstance(result, float)
