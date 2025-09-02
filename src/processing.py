from typing import List, Dict

def filter_by_state(items: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Ф-ия возвращает список словарей, у которых ключ state соответствует указанному значению. """
    return [item for item in items if item.get('state') == state]


from typing import List, Dict

def sort_by_date(items: List[Dict], descending: bool = True) -> List[Dict]:
    """Ф-ия возвращает новый список, отсортированный по дате"""
    return sorted(items, key=lambda x: x['date'], reverse=descending)