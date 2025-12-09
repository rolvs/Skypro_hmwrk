# test_generators.py
import pytest

from generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


# ==============================
# ФИКСТУРЫ
# ==============================

@pytest.fixture
def sample_transactions():
    """
    Набор транзакций с разными валютами и кривыми структурами
    для тестирования filter_by_currency и transaction_descriptions.
    """
    return [
        {
            "operationAmount": {
                "currency": {"code": "RUB"},
            },
            "description": "Перевод в рублях",
        },
        {
            "operationAmount": {
                "currency": {"code": "USD"},
            },
            "description": "Покупка в долларах",
        },
        {
            "operationAmount": {
                "currency": {"code": "RUB"},
            },
            "description": "Оплата услуг в рублях",
        },
        # Кривые/неполные структуры:
        {
            # нет operationAmount
            "description": "Без operationAmount",
        },
        {
            "operationAmount": {
                # нет currency
            },
            "description": "Без currency",
        },
        {
            "operationAmount": {
                "currency": {
                    # нет code
                }
            },
            "description": "Без code",
        },
        {
            "operationAmount": None,  # вызовет TypeError при обращении ["currency"]
            "description": "operationAmount=None",
        },
        {
            "operationAmount": {
                "currency": {"code": "EUR"},
            },
            # нет description
        },
        {
            "operationAmount": {
                "currency": {"code": "RUB"},
            },
            "description": "",  # пустое описание
        },
        {
            "operationAmount": {
                "currency": {"code": "RUB"},
            },
            "description": None,  # None-описание
        },
    ]


# ==============================
# ТЕСТЫ ДЛЯ filter_by_currency
# ==============================

@pytest.mark.parametrize(
    "currency_code, expected_count",
    [
        ("RUB", 4),  # 4 рублёвые транзакции с корректной структурой
        ("USD", 1),
        ("EUR", 1),
        ("CHF", 0),  # нет таких
    ],
)
def test_filter_by_currency_basic(sample_transactions, currency_code, expected_count):
    result = list(filter_by_currency(sample_transactions, currency_code))

    # Количество должно совпасть
    assert len(result) == expected_count

    # Все найденные транзакции должны иметь нужный код валюты
    for tx in result:
        assert tx["operationAmount"]["currency"]["code"] == currency_code


def test_filter_by_currency_empty_list():
    # Пустой список не должен ломать генератор
    result = list(filter_by_currency([], "RUB"))
    assert result == []


def test_filter_by_currency_only_broken_transactions():
    # Все транзакции кривые — должен просто вернуть пустой список, без ошибок
    broken = [
        {},
        {"operationAmount": {}},
        {"operationAmount": {"currency": {}}},
        {"operationAmount": None},
    ]
    result = list(filter_by_currency(broken, "RUB"))
    assert result == []


# ==============================
# ТЕСТЫ ДЛЯ transaction_descriptions
# ==============================

def test_transaction_descriptions_basic(sample_transactions):
    """
    Берём те же sample_transactions:
    - часть имеет description (непустой)
    - часть имеет пустой / None / отсутствует
    Функция должна вернуть только "truthy"-описания.
    """
    result = list(transaction_descriptions(sample_transactions))

    # Ожидаемые описания (только непустые и не-None)
    expected = [
        "Перевод в рублях",
        "Покупка в долларах",
        "Оплата услуг в рублях",
        "Без operationAmount",
        "Без currency",
        "Без code",
        "operationAmount=None",
    ]

    assert result == expected


@pytest.mark.parametrize(
    "transactions, expected",
    [
        ([], []),  # пустой список
        (
            [{"description": "Одна транзакция"}],
            ["Одна транзакция"],
        ),
        (
            [
                {"description": "Есть"},
                {"description": ""},       # пустая — не попадёт
                {"description": None},     # None — не попадёт
                {},                        # нет description
            ],
            ["Есть"],
        ),
    ],
)
def test_transaction_descriptions_various_inputs(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected


# ==============================
# ТЕСТЫ ДЛЯ card_number_generator
# ==============================

def test_card_number_generator_small_range():
    """
    Проверяем пример из задания:
    1..5 → 0000 0000 0000 0001 ... 0000 0000 0000 0005
    """
    result = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == expected


@pytest.mark.parametrize("start, end", [(1, 1), (123, 123), (9999_9999_9999_9999, 9999_9999_9999_9999)])
def test_card_number_generator_single_value(start, end):
    """
    Когда start == end, генератор должен вернуть ровно один номер.
    """
    result = list(card_number_generator(start, end))
    assert len(result) == 1

    card = result[0]
    # Формат: длина 19, пробелы в нужных местах
    assert len(card) == 19
    assert card[4] == " "
    assert card[9] == " "
    assert card[14] == " "

    # Все остальные символы — цифры
    digits_only = card.replace(" ", "")
    assert len(digits_only) == 16
    assert digits_only.isdigit()


def test_card_number_generator_formatting():
    """
    Проверяем форматирование для нескольких значений.
    """
    numbers = list(card_number_generator(12_345, 12_347))
    # Для наглядности просто проверим, что формат правильный
    for card in numbers:
        assert len(card) == 19
        assert card[4] == " "
        assert card[9] == " "
        assert card[14] == " "
        digits_only = card.replace(" ", "")
        assert len(digits_only) == 16
        assert digits_only.isdigit()


def test_card_number_generator_clamps_low_start():
    """
    start < 1 → должен быть приведён к 1.
    """
    result = list(card_number_generator(0, 3))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]
    assert result == expected


def test_card_number_generator_clamps_high_end():
    """
    end > максимума → должен быть приведён к 9999_9999_9999_9999.
    """
    max_val = 9999_9999_9999_9999
    result = list(card_number_generator(max_val - 2, max_val + 100))
    # Должно быть только 3 значения
    assert len(result) == 3
    assert result[-1] == "9999 9999 9999 9999"


def test_card_number_generator_start_greater_than_end():
    """
    Если start > end — range() вернёт пустой диапазон,
    генератор должен вернуть пустой список (без ошибок).
    """
    result = list(card_number_generator(10, 5))
    assert result == []
