from src.search import process_bank_operations

test_data = [
    {"description": "Покупка в магазине Ашан", "amount": 1000, "date": "2024-01-01"},
    {"description": "Оплата услуг Билайн", "amount": 500, "date": "2024-01-02"},
    {"description": "Перевод в банк Тинькофф", "amount": 2000, "date": "2024-01-03"},
    {"description": "Покупка в АШАН онлайн", "amount": 1500, "date": "2024-01-04"},
    {"description": "Снятие наличных в банке", "amount": 3000, "date": "2024-01-05"},
    {"description": "Оплата мобильного билайн", "amount": 450, "date": "2024-01-06"},
]


def test_categories_basic():
    """Тест базового подсчета по категориям"""
    categories = ["ашан", "билайн", "банк"]
    result = process_bank_operations(test_data, categories)

    assert result == {"ашан": 2, "билайн": 2, "банк": 2}


def test_categories_case_insensitive():
    """Тест регистронезависимых категорий"""
    categories = ["АШАН", "БиЛайн", "БАНК"]
    result = process_bank_operations(test_data, categories)

    assert result == {"АШАН": 2, "БиЛайн": 2, "БАНК": 2}


def test_categories_no_matches():
    """Тест категорий без совпадений"""
    categories = ["яндекс", "пятерочка"]
    result = process_bank_operations(test_data, categories)

    assert result == {"яндекс": 0, "пятерочка": 0}


def test_categories_empty_data():
    """Тест с пустыми данными"""
    result = process_bank_operations([], ["ашан", "билайн"])
    assert result == {}


def test_categories_empty_categories():
    """Тест с пустым списком категорий"""
    result = process_bank_operations(test_data, [])
    assert result == {}


def test_categories_partial_match():
    """Тест частичного совпадения в категориях"""
    test_data_partial = [
        {"description": "Ашан супермаркет"},
        {"description": "магазин аш"},
        {"description": "АШАНчик маленький"},
    ]

    categories = ["аш", "ашан", "маркет"]
    result = process_bank_operations(test_data_partial, categories)

    # Проверяем, что 'аш' находит все три, 'ашан' - два, 'маркет' - один
    assert result.get("аш", 0) == 3
    assert result.get("ашан", 0) == 2
    assert result.get("маркет", 0) == 1


def test_categories_overlapping_matches():
    """Тест пересекающихся категорий в одной операции"""
    test_data_overlap = [
        {"description": "Перевод в банк Тинькофф"},
        {"description": "Билайн банк оплата"},
    ]

    categories = ["банк", "тинькофф", "билайн"]
    result = process_bank_operations(test_data_overlap, categories)

    # Каждая операция должна учитываться для каждой подходящей категории
    assert result == {
        "банк": 2,  # Обе операции содержат "банк"
        "тинькофф": 1,  # Только первая операция
        "билайн": 1,  # Только вторая операция
    }


def test_categories_special_characters_in_categories():
    """Тест со специальными символами в категориях"""
    test_data_special = [
        {"description": "Покупка в магазине (Ашан)"},
        {"description": "Оплата [Netflix]"},
    ]

    categories = ["(ашан)", "[netflix]"]
    result = process_bank_operations(test_data_special, categories)

    assert result == {"(ашан)": 1, "[netflix]": 1}
