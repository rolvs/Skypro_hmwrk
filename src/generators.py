from typing import Iterable, Iterator, Dict, Any

Transaction = Dict[str, Any]


def filter_by_currency(
    transactions: Iterable[Transaction],
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
            # если структура кривая или нет поля currency — просто пропускаем
            continue

        if code == currency_code:
            yield tx


def transaction_descriptions(transactions):
    """
    Генератор, который по очереди возвращает description каждой транзакции.
    """
    for tx in transactions:
        desc = tx.get("description")
        if desc:
            yield desc


def card_number_generator(start: int, end: int):
    """
    Генератор номеров "карт" в формате XXXX XXXX XXXX XXXX.
    start и end — целые числа в диапазоне от 1 до 9999_9999_9999_9999.
    """
    # Ограничение диапазона
    if start < 1:
        start = 1
    if end > 9999_9999_9999_9999:
        end = 9999_9999_9999_9999

    for num in range(start, end + 1):
        s = f"{num:016d}"  # Превращаем в строку из 16 цифр с лидирующими нулями
        formatted = f"{s[0:4]} {s[4:8]} {s[8:12]} {s[12:16]}"
        yield formatted
