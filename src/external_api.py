import os
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction: List[Dict[str, Any]]) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции
    """
    for item in transaction:
        currency = item["operationAmount"]["currency"]["code"]
        amount = item["operationAmount"]["amount"]
        if currency == "RUB":
            result = float(amount)
            return result
        else:
            url = f"https://api.apilayer.com/fixer/convert?to={"RUB"}&from={currency}&amount={amount}"
            payload = {}
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers, data=payload)
            status_code = response.status_code
            if status_code == 200:
                result = response.json()["result"]
                return float(result)
    # Возвращаем 0.0, если нет транзакций
    return 0.0
