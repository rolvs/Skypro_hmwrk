import json
from typing import Any
from external_api import convert_to_rub


def load_operations(path: str) -> list[dict]:
    """
    Reads financial operations from a JSON file.

    Returns an empty list if the file is not found,
    empty, or does not contain a list.
    """
    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []





def get_transaction_amount_rub(transaction: dict[str, Any]) -> float:
    """
    Takes a transaction dict and returns the transaction amount in RUB as float.
    If currency is USD or EUR, converts via external API.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount_raw = operation_amount.get("amount", 0)
    currency_info = operation_amount.get("currency", {})
    currency_code = currency_info.get("code") or currency_info.get("name")

    try:
        amount = float(amount_raw)
    except (TypeError, ValueError):
        amount = 0.0

    if currency_code in ("USD", "EUR"):
        return float(convert_to_rub(amount, currency_code))

    return float(amount)
