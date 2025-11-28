from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция для обработки информации о картах и и счетах"""
    # Записывем информацию о карте в новый список
    mask_card_input_type = type(account_card)
    if mask_card_input_type != str:
        return "Введен неверный тип данных"
    elif len(account_card) < 1 or 1 < len(account_card) < 16:
        return "Данные введены не корректно"
    info_list = account_card.split()
    # Делим название карты/счета и номер
    name_card = []
    num_card = []
    for card_name in info_list:
        if card_name.isalpha():
            name_card.append(card_name)
        else:
            num_card.append(card_name)

    # Преобразуем название карты в строку
    last_name = ""
    for i in range(len(name_card)):
        last_name += "".join(name_card[i])
        last_name += " "
    # Преобразуем номер карты в строку
    last_card = ""
    for i in range(len(num_card)):
        last_card += "".join(num_card[i])

    # Проверяем номер счета это или номер карты и маскируем его
    if len(last_card) == 20:
        masked_number = get_mask_account((last_card))
    else:
        masked_number = get_mask_card_number((last_card))

    return f"{last_name}{masked_number}"


def get_date(date: str) -> str:
    """Функция для обработки полученной даты в нужном формате"""
    get_date_input_type = type(date)
    if get_date_input_type != str:
        return "Введен неверный тип данных"
    elif len(date) < 26 or len(date) > 26:
        return "Ошибка ввода"
    split_date = date.split("T")
    new_date = split_date[0]
    new_date_str = "".join(new_date)
    format_date = new_date_str.replace("-", ".")
    day = format_date[-2:]
    month = format_date[5:7]
    year = format_date[0:4]

    return f"{day}.{month}.{year}"
