import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Фильтрует список операций по наличию строки поиска в описании.
    """
    if not data or not search:
        return []

    result = []
    pattern = re.compile(re.escape(search), re.IGNORECASE)  # регистронезависимый поиск

    for operation in data:
        description = operation.get("description", "")
        if pattern.search(description):
            result.append(operation)

    return result


def process_bank_operations(data: list[dict], categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям.
    """
    if not data or not categories:
        return {}

    # Создаем словарь счётчика для категорий
    category_counter = Counter()

    # Приводим категории к нижнему регистру для регистронезависимого поиска
    categories_lower = [cat.lower() for cat in categories]

    for operation in data:
        description = operation.get("description", "").lower()
        for category in categories_lower:
            if category in description:
                category_counter[category] += 1

    # Преобразуем Counter в обычный dict, возвращая оригинальные названия категорий
    result = {}
    for category in categories:
        result[category] = category_counter.get(category.lower(), 0)

    return result
