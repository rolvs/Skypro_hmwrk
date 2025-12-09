# Skypro Homework — Module 2, Lesson 11.1  
## Генераторы и обработка транзакций

В проект добавлен модуль **`generators.py`**, содержащий три функции:

---

### 1. `filter_by_currency(transactions, currency_code)`
Возвращает только те транзакции, у которых код валюты совпадает с `currency_code`.

**Пример использования:**

```python
from src.generators import filter_by_currency

usd_transactions = list(filter_by_currency(transactions, "USD")) 
```

### 2. transaction_descriptions(transactions)

Генератор, возвращающий описания (description) транзакций, если они не пустые.

Пример использования:
```python
from src.generators import transaction_descriptions

for desc in transaction_descriptions(transactions):
    print(desc)
```
### 3. card_number_generator(start, end)

Генерирует последовательность номеров карт в формате:

```
XXXX XXXX XXXX XXXX
```

Пример использования:

```python
from src.generators import card_number_generator

for num in card_number_generator(1, 5):
    print(num)
```

###📌 Пример входных данных для тестирования
```python
transactions = [
    {
        "id": 939719570,
        "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}},
        "description": "Перевод организации"
    },
    {
        "id": 873106923,
        "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB"}},
        "description": "Перевод со счета на счет"
    },
    ...
]

```

### 🧪 Тестирование

Тесты находятся в папке tests/ и покрывают функции более чем на 80%
(фактическое покрытие: 100%).

Запуск тестов
```python
pytest -q
```

HTML-отчёт:

file:///C:/Users/bekmu/PycharmProjects/Homework/htmlcov/index.html
