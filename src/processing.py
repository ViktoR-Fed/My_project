from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]] | Any, state: str = "EXECUTED") -> List[Dict[str, Any]] | str:
    """Функция сортировки списка словарей по значению 'state'"""
    filter_type_list = type(data)
    new_list = []
    if len(data) < 1 or filter_type_list != list:
        return "Ошибка: неверный ввод данных"
    for item in data:
        try:
            item["state"] == state
        except KeyError:
            # Код, который выполняется в случае исключения
            return "Ошибка: ключ не найден"
        else:
            if item["state"] == state:
                new_list.append(item)
    return new_list


def sort_by_date(showing: List[Dict[str, Any]] | Any, is_ascending: bool = True) -> List[Dict[str, Any]] | str:
    """Функция для сортировки списка словарей,
    порядок сортировки 'is_ascending'(убывающий)"""
    date_showing_type = type(showing)
    if date_showing_type != list:
        return "Ошибка: неверный ввод данных"
    if len(showing) < 1:
        return "Ошибка: пустой список для сортировки"

    sorted_list = sorted(showing, key=lambda x: x["date"], reverse=is_ascending)

    return sorted_list
