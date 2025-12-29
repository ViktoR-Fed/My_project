import csv
import logging
import os
from typing import Any, Dict, List

import pandas as pd

os.chdir("C:/Users/20vik/myproject/My_project")

# Основная конфигурация logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="logs/data_processing.log",
    encoding="utf-8",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске

# Создаем логеры для различных компонентов программы
unpacking_csv_logger = logging.getLogger("unpacking_csv")
unpacking_xlsx_logger = logging.getLogger("unpacking_xlsx")


def unpacking_csv(filename: str = "data/transactions.csv") -> List[Dict[str, Any]]:
    """
    Функция, которая получает данные о финансовых транзакциях из csv-файла, по указанному пути до файла с транзакциями
    """
    # Записываем информацию о начале работы функции
    unpacking_csv_logger.info(f"Поиск файла по заданному пути: {filename}")

    if not os.path.exists(filename):
        unpacking_csv_logger.info(f"Неверный путь: {filename}")
        return []  # Возвращаем пустой список, если путь неверный
        # Проверка, что это файл, а не директория
    elif not os.path.isfile(filename):
        unpacking_csv_logger.info("Файл по заданному пути не найден")
        return []  # Возвращаем пустой список, если файл не найден
        # Проверка размера файла
    elif os.path.getsize(filename) == 0:
        unpacking_csv_logger.info("Найден пустой файл")
        return []  # Возвращаем пустой список, если файл пустой
    else:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                unpacking_csv_logger.info("Файл найден успешно")
                reader = csv.DictReader(file, delimiter=";")
                result = []
                for row in reader:
                    result.append(row)
            return result
        except Exception as e:
            unpacking_csv_logger.error(f"Произошла ошибка: {e}")
            return []


def unpacking_xlsx(filename: str = "data/transactions_excel.xlsx") -> List[Dict[str, Any]]:
    """
    Функция, которая получает данные о финансовых транзакциях из xlsx-файла, по указанному пути до файла с транзакциями
    """
    # Записываем информацию о начале работы функции
    unpacking_xlsx_logger.info(f"Поиск файла по заданному пути: {filename}")

    if not os.path.exists(filename):
        unpacking_xlsx_logger.info(f"Неверный путь: {filename}")
        return []  # Возвращаем пустой список, если путь неверный
        # Проверка, что это файл, а не директория
    elif not os.path.isfile(filename):
        unpacking_xlsx_logger.info("Файл по заданному пути не найден")
        return []  # Возвращаем пустой список, если файл не найден
        # Проверка размера файла
    elif os.path.getsize(filename) == 0:
        unpacking_xlsx_logger.info("Найден пустой файл")
        return []  # Возвращаем пустой список, если файл пустой
    else:
        try:
            df = pd.read_excel(filename)
            unpacking_xlsx_logger.info("Файл найден успешно")
            transaction_dict = df.to_dict(orient="records")
            return transaction_dict
        except Exception as e:
            unpacking_xlsx_logger.error(f"Произошла ошибка: {e}")
            return []
