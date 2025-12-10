from typing import Any, Dict, Iterator, List

Transaction = Dict[str, Any]


def filter_by_currency(
    transactions: List[Transaction],
    currency_code: str,
) -> Iterator[Transaction]:
    """
    Генератор, который по очереди возвращает только те транзакции,
    у которых код валюты совпадает с переданным currency_code.
    """
    for tx in transactions:
        try:
            code = tx["operationAmount"]["currency"]["code"]
        except (KeyError, TypeError):
            # если структура некорректная — пропускаем транзакцию
            continue

        if code == currency_code:
            yield tx


def transaction_descriptions(
    transactions: List[Transaction],
) -> Iterator[str]:
    """
    Генератор, который по очереди возвращает description каждой транзакции.
    """
    for tx in transactions:
        desc = tx.get("description")
        if desc:
            yield desc


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров "карт" в формате XXXX XXXX XXXX XXXX.

    start и end — целые числа в диапазоне от 1 до 9_999_999_999_999_999.
    """
    if start < 1:
        start = 1
    if end > 9_999_999_999_999_999:
        end = 9_999_999_999_999_999

    for num in range(start, end + 1):
        s = f"{num:016d}"
        yield f"{s[0:4]} {s[4:8]} {s[8:12]} {s[12:16]}"
