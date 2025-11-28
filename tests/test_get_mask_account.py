from src.masks import get_mask_account


def test_correct_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'

def test_zero_input_mask_account():
    assert get_mask_account('') == 'Ошибка ввода номера счета'

def test_max_len_mask_account():
    assert get_mask_account('7365410843013587430511') == 'Ошибка ввода номера счета'

def test_correct_input_mask_account():
    assert get_mask_account('asdasdasdasdasdasdas') == 'Не введен номер счета'