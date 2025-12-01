from src.masks import get_mask_card_number


def test_get_correct_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_zero_unput_card_number() -> None:
    assert get_mask_card_number("") == "Ошибка ввода номера карты"


def test_max_len_card_number() -> None:
    assert get_mask_card_number(70007922896063612) == "Ошибка ввода номера карты"


def test_correct_number_card() -> None:
    assert get_mask_card_number("asdasdasdasdasda") == "Не введен номер карты"
