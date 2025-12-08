from typing import Any, Dict, List

from src.generators import transaction_descriptions


def test_correct_type_descriptions_str() -> None:
    descriptions_work = transaction_descriptions("dsafds")
    assert next(descriptions_work) == "Ошибка: неверный тип входных данных"


def test_correct_type_descriptions_int() -> None:
    descriptions_work = transaction_descriptions(12144235)
    assert next(descriptions_work) == "Ошибка: неверный тип входных данных"


def test_correct_len() -> None:
    descriptions_work = transaction_descriptions([])
    assert next(descriptions_work) == "Ошибка: пустой список"


def test_correct_work_transactions_descriptions(transaction_list_for_filter: list[dict[str, Any]]) -> None:
    descriptions = transaction_descriptions(transaction_list_for_filter)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"
