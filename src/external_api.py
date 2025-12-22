import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction: Dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции
    """
    info = transaction.get("operationAmount")
    amount = info.get("amount")
    code = info.get("currency")
    currency = code.get("code")
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
