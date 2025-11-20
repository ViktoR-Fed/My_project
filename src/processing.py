from typing import Iterable

def filter_by_state(data:[Iterable[list]], state: str = "EXECUTED") -> Iterable[list]:
    ''' Функция сортировки списка словарей по значению 'state' '''
    new_list = []
    for item in data:
        if item['state'] == state:
            new_list.append(item)

    return new_list




