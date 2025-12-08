from typing import Any, Dict, Generator, List


def filter_by_currency(transaction_list: List[Dict[str, Any]], currency_type: str) -> Any:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""
    try:
        result = (x for x in transaction_list if x["operationAmount"]["currency"]["code"] == currency_type)
    except KeyError:
        return "Ошибка: ключ не найден"
    else:
        try:
            next_element = next(result)
        except StopIteration:
            return "Генератор исчерпан"
        else:
            result = (x for x in transaction_list if x["operationAmount"]["currency"]["code"] == currency_type)
    return result


def transaction_descriptions(transactions: List[Dict[str, Any]] | Any) -> Generator:
    """Функция - генератор,который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    transactions_type = type(transactions)
    if transactions_type == list:
        if len(transactions) < 1:
            yield "Ошибка: пустой список"
        else:
            for item in transactions:
                yield item["description"]
    else:
        yield "Ошибка: неверный тип входных данных"


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция - генератор, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты"""
    start = int(start)
    stop = int(stop)
    for x in range(start, stop + 1):
        x = str(x).zfill(16)
        result = x[0:4] + " " + x[4:8] + " " + x[8:12] + " " + x[12:]
        yield result
