from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция сортировки списка словарей по значению 'state'"""
    new_list = []
    for item in data:
        if item["state"] == state:
            new_list.append(item)

    return new_list


def sort_by_date(list_dict: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """Функция для сортировки списка словарей по параметру 'key_sort',
    порядок сортировки 'decreasing'(убывающий)"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=ascending)
    return sorted_list
