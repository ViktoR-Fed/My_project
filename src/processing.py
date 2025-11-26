from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция сортировки списка словарей по значению 'state'"""
    new_list = []
    for item in data:
        if item["state"] == state:
            new_list.append(item)

    return new_list


def sort_by_date(showing: List[Dict[str, Any]], is_ascending: bool = True) -> List[Dict[str, Any]]:
    """Функция для сортировки списка словарей,
    порядок сортировки 'is_ascending'(убывающий)"""
    sorted_list = sorted(showing, key=lambda x: x["date"], reverse=is_ascending)

    return sorted_list
