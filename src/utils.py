import json
import logging
import os
from typing import Any, Dict, List

# Изменяем текущую директорию на корень проекта
os.chdir("C:/Users/20vik/myproject/My_project")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def receiving_financial_transactions(filepath: str = "data/operations.json") -> List[Dict[str, Any]]:
    """
    Функция, которая получает данные о финансовых транзакциях из JSON-файла, по указанному пути до файла с транзакциями
    """
    # Записываем информацию о начале работы функции
    logger.info(f"Поиск файла по заданному пути: {filepath}")

    if not os.path.exists(filepath):
        logger.info(f"Неверный путь: {filepath}")
        return []  # Возвращаем пустой список, если путь неверный
        # Проверка, что это файл, а не директория
    elif not os.path.isfile(filepath):
        logger.info("Файл по заданному пути не найден")
        return []  # Возвращаем пустой список, если файл не найден
        # Проверка размера файла
    elif os.path.getsize(filepath) == 0:
        logger.info("Найден пустой файл")
        return []  # Возвращаем пустой список, если файл пустой
    else:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                logger.info("Файл найден успешно")
                operations = json.load(file)
                if not isinstance(operations, list):
                    logger.info("Файл не содержит список")
                    return []  # Возвращаем пустой список, если в файле не список
                return operations
        except Exception as e:
            logger.error(f"Произошла ошибка: {e}")
            return []
