from typing import Any, Dict, List

from src.processing import filter_by_state
from tests.conftest import unsorted_list


def test_filter_by_state(unsorted_list: List[Dict[str, Any]]) -> None:
    assert filter_by_state(unsorted_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2025-06-30T02:08:58.425572"},
    ]


def test_canceled_filter_by_state(unsorted_list: List[Dict[str, Any]]) -> None:
    assert filter_by_state(unsorted_list, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2025-10-14T08:21:33.419441"},
    ]


def test_uncorrect_key_filter(uncorrect_key_list: List[Dict[str, Any]]) -> None:
    assert filter_by_state((uncorrect_key_list)) == "Ошибка: ключ не найден"


def test_len_zero() -> None:
    assert filter_by_state([]) == "Ошибка: неверный ввод данных"


def test_uncorrect_type_filter() -> None:
    assert filter_by_state("") == "Ошибка: неверный ввод данных"
