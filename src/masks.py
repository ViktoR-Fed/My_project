import logging
import os
from typing import Union

# Изменяем текущую директорию на корень проекта
os.chdir("C:/Users/20vik/myproject/My_project")

# Основная конфигурация logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="logs/masks.log",
    encoding="utf-8",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске

# Создаем логеры для различных компонентов программы
card_logger = logging.getLogger("masks.card")
mask_logger = logging.getLogger("masks.mask_account")


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""
    # Преобразуем номер карты в строку, если он не строка
    card_logger.info(f"Функция начала работу с номером карты: {card_number}")
    card_str = str(card_number)
    if len(card_str) < 16 or len(card_str) > 16:
        result = "Ошибка ввода номера карты"
        card_logger.error(result)
        return result
    elif card_str.isalpha():
        result = "Не введен номер карты"
        card_logger.error(result)
        return result
    card_logger.info("Функция обрабатывает номер карты")
    # Вырезаем первые 6 и последние 4 цифры
    first_six = card_str[:6]
    last_four = card_str[-4:]
    # Остальные цифры заменяем на звездочки
    middle_mask = "** ****"
    # Формируем маску в нужном формате
    masked_card = f"{first_six[:4]} {first_six[4:]}{middle_mask} {last_four}"
    card_logger.info("Функция завершила работу")
    return masked_card


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""
    mask_logger.info(f"Функция начала работу с номером счета: {account_number}")
    account_str = str(account_number)
    if len(account_str) < 20 or len(account_str) > 20:
        result = "Ошибка ввода номера счета"
        mask_logger.error(f"{result}")
        return result
    elif account_str.isalpha():
        result = "Не введен номер счета"
        mask_logger.error(f"{result}")
        return result
    mask_logger.info("Функция обрабатывает номер счета")
    last_four = account_str[-4:]
    mask_logger.info("Функция завершила работу")
    return f"**{last_four}"
