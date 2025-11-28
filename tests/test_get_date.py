from src.widget import get_date


def test_get_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'

def test_len_date():
    assert get_date('тут нет даты') == 'Ошибка ввода'

def test_len_zero_date():
    assert get_date('') == 'Ошибка ввода'

def test_max_len_date():
    assert get_date('2024-03-11T02:26:18.671407t') == 'Ошибка ввода'

def test_type_date():
    assert get_date(11032024) == "Введен неверный тип данных"