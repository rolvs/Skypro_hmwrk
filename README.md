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

