# Skypro Homework — Module 2, Lesson 10.2

## 📘 Описание проекта
Домашняя работа по модулю 2 курса Skypro: тестирование функций проекта с помощью библиотеки **pytest**.

## 🗂 Структура проекта
src/
masks.py # функции маскировки номеров
widget.py # функции форматирования вывода
tests/
conftest.py # фикстуры
test_masks.py # тесты для masks.py
test_widget.py # тесты для widget.py
report/ # HTML-отчёт покрытия тестами

## 🧪 Тестирование
Для запуска тестов:

pytest

Проверка покрытия и создание HTML-отчёта:
pytest --cov=src --cov-report=html:tests/report

Открыть отчёт можно по пути:
tests/report/index.html

# Bank Widget Project

Проект для курса Python-разработки. Разрабатывается бэкенд для виджета в личном кабинете клиента, показывающего последние успешные банковские операции.


## Основные функции

- processing.py
  - filter_by_state(items, state="EXECUTED") — фильтрует операции по статусу.
  - sort_by_date(items, descending=True) — сортирует операции по дате.

- widget.py
  - mask_account_card(account) — маскирует номер карты или счета, оставляя последние 4 цифры.
  - get_date(date_str) — преобразует дату из формата ISO в "ДД.ММ.ГГГГ".

## Стиль и проверка кода

- PEP 8, flake8, isort, black, mypy.
- Git + GitFlow, атомарные коммиты.
