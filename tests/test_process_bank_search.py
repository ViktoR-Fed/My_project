from collections import Counter

import pytest

from src.search import process_bank_search

# Тестовые данные
test_data = [
    {"description": "Покупка в магазине Ашан", "amount": 1000, "date": "2024-01-01"},
    {"description": "Оплата услуг Билайн", "amount": 500, "date": "2024-01-02"},
    {"description": "Перевод в банк Тинькофф", "amount": 2000, "date": "2024-01-03"},
    {"description": "Покупка в АШАН онлайн", "amount": 1500, "date": "2024-01-04"},
    {"description": "Снятие наличных в банке", "amount": 3000, "date": "2024-01-05"},
    {"description": "Оплата мобильного билайн", "amount": 450, "date": "2024-01-06"},
    {"description": "", "amount": 100, "date": "2024-01-07"},  # Пустое описание
]


def test_search_basic():
    """Тест базового поиска"""
    result = process_bank_search(test_data, "ашан")
    assert len(result) == 2
    assert all("ашан" in op["description"].lower() for op in result)


def test_search_case_insensitive():
    """Тест регистронезависимого поиска"""
    result1 = process_bank_search(test_data, "АШАН")
    result2 = process_bank_search(test_data, "ашан")
    result3 = process_bank_search(test_data, "Ашан")

    assert len(result1) == len(result2) == len(result3) == 2


def test_search_no_match():
    """Тест поиска без совпадений"""
    result = process_bank_search(test_data, "яндекс")
    assert result == []


def test_search_empty_string():
    """Тест поиска с пустой строкой"""
    result = process_bank_search(test_data, "")
    assert result == []


def test_search_empty_data():
    """Тест с пустыми данными"""
    result = process_bank_search([], "ашан")
    assert result == []


def test_search_special_characters():
    """Тест поиска со специальными символами"""
    test_data_special = [
        {"description": "Покупка в IKEA (Москва)", "amount": 5000},
        {"description": "Оплата [Netflix]", "amount": 699},
    ]

    result = process_bank_search(test_data_special, "(Москва)")
    assert len(result) == 1
    assert result[0]["description"] == "Покупка в IKEA (Москва)"


def test_search_multiple_words():
    """Тест поиска нескольких слов"""
    result = process_bank_search(test_data, "оплата услуг")
    assert len(result) == 1
    assert result[0]["description"] == "Оплата услуг Билайн"
