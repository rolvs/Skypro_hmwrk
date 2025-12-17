from typing import Any, Dict, List


def filter_by_state(
    items: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """Ф-ия возвращает список словарей, у которых ключ state соответствует указанному значению."""
    return [item for item in items if item.get("state") == state]


def sort_by_date(
    items: List[Dict[str, Any]], descending: bool = True
) -> List[Dict[str, Any]]:
    """Ф-ия возвращает новый список, отсортированный по дате"""
    return sorted(items, key=lambda x: x["date"], reverse=descending)
