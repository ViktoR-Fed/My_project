
from typing import Any, Dict, List, Iterator


def filter_by_currency(transaction_list : List[Dict[str, Any]], currency_type: str) -> Iterator:
    result = (x for x in transaction_list if x["operationAmount"]["currency"]["code"] == currency_type)
    return result


def transaction_descriptions(transactions : List[Dict[str, Any]]) -> str:
    for item in transactions:
        yield item["description"]


def card_number_generator(start:int = 1 , stop:int = 9999999999999999) -> int:
    for x in range(start,stop + 1):
        x = str(x).zfill(16)
        result = x[0:4] +' '+ x[4:8] + ' ' + x[8:12] + ' ' + x[12:]
        yield result
