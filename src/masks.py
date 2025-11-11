from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""
    # Преобразуем номер карты в строку, если он не строка
    card_str = str(card_number)
    # Вырезаем первые 6 и последние 4 цифры
    first_six = card_str[:6]
    last_four = card_str[-4:]
    # Остальные цифры заменяем на звездочки
    middle_mask = "**** ****"
    # Формируем маску в нужном формате
    masked_card = f"{first_six[:4]} {first_six[4:]} {middle_mask} {last_four}"
    return masked_card


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""

    account_str = str(account_number)
    last_four = account_str[-4:]
    return f"**{last_four}"
