from src.masks import get_mask_account, get_mask_card_number, Union


def mask_account_card(account_card: Union[str, str]) -> str:
    """Функция для обработки информации о картах и и счетах"""
    # Записывем информацию о карте в новый список
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
