from typing import Any, Dict, List

from src.processing import sort_by_date
from tests.conftest import unsorted_list_sort


def test_sort_by_date(unsorted_list_sort: List[Dict[str, Any]]) -> None:
    assert sort_by_date(unsorted_list_sort) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_reverse(unsorted_list_sort: List[Dict[str, Any]]) -> None:
    assert sort_by_date(unsorted_list_sort, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_zero_list_sort() -> None:
    assert sort_by_date([]) == "Ошибка: пустой список для сортировки"


def test_uncorrect_type() -> None:
    assert sort_by_date("") == "Ошибка: неверный ввод данных"
