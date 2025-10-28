import pytest
from processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_items():
    return [
        {"id": 1, "date": "2024-01-10", "state": "EXECUTED"},
        {"id": 2, "date": "2023-12-31", "state": "CANCELED"},
        {"id": 3, "date": "2024-05-05", "state": "EXECUTED"},
        {"id": 4, "date": "2022-07-20", "state": "PENDING"},
        {"id": 5, "date": "2024-01-10", "state": "EXECUTED"},
    ]


# ---------- filter_by_state tests ----------

def test_filter_by_state_default_filters_EXECUTED(sample_items):
    """без второго аргумента оставляет только state == 'EXECUTED'"""
    result = filter_by_state(sample_items)
    assert [item["id"] for item in result] == [1, 3, 5]


@pytest.mark.parametrize(
    "state_value, expected_ids",
    [
        ("EXECUTED", [1, 3, 5]),
        ("CANCELED", [2]),
        ("PENDING",  [4]),
        ("UNKNOWN",  []),
    ],
)
def test_filter_by_state_with_explicit_state(sample_items, state_value, expected_ids):
    """если передать другое состояние — фильтрует по нему"""
    result = filter_by_state(sample_items, state=state_value)
    assert [item["id"] for item in result] == expected_ids


def test_filter_by_state_is_case_sensitive(sample_items):
    """проверяем, что 'executed' не совпадает с 'EXECUTED'"""
    result = filter_by_state(sample_items, state="executed")
    assert result == []


def test_filter_by_state_does_not_modify_source(sample_items):
    """функция не должна менять входной список"""
    original_copy = list(sample_items)
    _ = filter_by_state(sample_items, state="EXECUTED")
    assert sample_items == original_copy


# ---------- sort_by_date tests ----------

def test_sort_by_date_descending_true(sample_items):
    """
    descending=True -> ожидание:
    более поздние даты (лексикографически больше) первыми.
    """
    result = sort_by_date(sample_items, descending=True)
    # Давай проверим порядок по id, чтобы было читаемо:
    assert [item["id"] for item in result] == [3, 1, 5, 2, 4]
    # Проверим, что он реально отсортирован по строке date убыванием
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_descending_false(sample_items):
    """
    descending=False -> возрастающий порядок дат.
    """
    result = sort_by_date(sample_items, descending=False)
    assert [item["id"] for item in result] == [4, 2, 1, 5, 3]
    dates = [item["date"] for item in result]
    assert dates == sorted(dates)


def test_sort_by_date_stable_for_equal_dates(sample_items):
    """
    При одинаковой дате ('2024-01-10') элементы с id=1 и id=5
    должны остаться в исходном относительном порядке.
    Python sorted гарантирует стабильность.
    """
    result = sort_by_date(sample_items, descending=False)
    # оба элемента c одинаковой датой '2024-01-10' должны остаться как [1, 5], не [5, 1]
    ordered_same_date = [item["id"] for item in result if item["date"] == "2024-01-10"]
    assert ordered_same_date == [1, 5]
