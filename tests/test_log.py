from src.decorators import log


@log()
def add_numbers(a, b):
    return a + b


def test_log_correct(capsys) -> None:
    add_numbers(1, 2)
    captured = capsys.readouterr()
    assert (
        captured.out == "Функция add_numbers начинает выполняться.\n\nadd_numbers успешно выполнена. Результат: 3\n\n"
    )


def test_log_error(capsys) -> None:
    add_numbers(1, [])
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Функция add_numbers начинает выполняться.\n\nadd_numbers выдает ошибку: TypeError. Параметры: (1, []), {}.\n\n"
    )
