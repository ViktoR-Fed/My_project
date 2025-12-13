from functools import wraps


def log(filename=None):
    """Декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def write_log(message):
        if filename:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(message)
        else:
            print(message)

    def my_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            log_start_function = f"Функция {function.__name__} начинает выполняться.\n"
            write_log(log_start_function)
            try:
                result = function(*args, **kwargs)
                log_end_function = f"{function.__name__} успешно выполнена. Результат: {result}\n"
                write_log(log_end_function)
                return result
            except Exception as error:
                log_end_function = (
                    f"{function.__name__} выдает ошибку: {type(error).__name__}. Параметры: {args}, {kwargs}.\n"
                )
                write_log(log_end_function)

        return wrapper

    return my_decorator

