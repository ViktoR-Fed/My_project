import json
import os
from typing import Any, Dict, List


def receiving_financial_transactions(filepath: str = "data/operations.json") -> List[Dict[str, Any]]:
    """
    Функция, которая получает данные о финансовых транзакциях из JSON-файла, по указанному пути до файла с транзакциями.
    """
    if not os.path.exists(filepath):
        return []  # Возвращаем пустой список, если путь неверный
        # Проверка, что это файл, а не директория
    elif not os.path.isfile(filepath):
        return []  # Возвращаем пустой список, если файл не найден
        # Проверка размера файла
    elif os.path.getsize(filepath) == 0:
        return []  # Возвращаем пустой список, если файл пустой
    else:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                operations = json.load(file)
                if not isinstance(operations, list):
                    return []  # Возвращаем пустой список, если в файле не список
                return operations
        except Exception:
            return []
