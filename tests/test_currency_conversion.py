import os
from unittest.mock import Mock, patch

from dotenv import load_dotenv

from src.external_api import currency_conversion
from tests.conftest import for_currency_conversion

load_dotenv()

API_KEY = os.getenv("API_KEY")


def test_currency_conversion_rub(for_currency_conversion) -> None:
    assert currency_conversion(for_currency_conversion) == 31957.58


def test_currency_conversion_usd() -> None:
    """Тест для транзакции в USD"""
    with patch("src.external_api.requests.get") as mock_get:
        # Настройка мок-ответа
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 80.483327}
        mock_get.return_value = mock_response

        # Подготовка тестовых данных
        test_transaction = [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "1", "currency": {"name": "Доллар США", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447995560",
            }
        ]

        # Вызов функции
        result = currency_conversion(test_transaction)

        # Проверка результата
        assert result == 80.483327

        # Проверка, что API был вызван с правильными параметрами
        expected_url = "https://api.apilayer.com/fixer/convert?to=RUB&from=USD&amount=1"
        mock_get.assert_called_once_with(expected_url, headers={"apikey": API_KEY}, data={})


def test_currency_conversion_eur() -> None:
    """Тест для транзакции в EUR"""
    with patch("src.external_api.requests.get") as mock_get:
        # Настройка мок-ответа
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 95.25}
        mock_get.return_value = mock_response

        # Подготовка тестовых данных
        test_transaction = [
            {
                "id": 41428830,
                "state": "EXECUTED",
                "date": "2019-07-04T18:35:29.512364",
                "operationAmount": {"amount": "50", "currency": {"name": "Евро", "code": "EUR"}},
                "description": "Перевод организации",
                "from": "Visa 4150393755080000",
                "to": "Счет 35383033474447995560",
            }
        ]

        # Вызов функции
        result = currency_conversion(test_transaction)

        # Проверка результата
        assert result == 95.25

        # Проверка вызова API
        expected_url = "https://api.apilayer.com/fixer/convert?to=RUB&from=EUR&amount=50"
        mock_get.assert_called_once_with(expected_url, headers={"apikey": API_KEY}, data={})


def test_currency_conversion_api_error() -> None:
    """Тест для случая ошибки API"""
    with patch("src.external_api.requests.get") as mock_get:
        # Настройка мок-ответа с ошибкой
        mock_response = Mock()
        mock_response.status_code = 500  # Ошибка сервера
        mock_get.return_value = mock_response

        test_transaction = [
            {
                "id": 41428831,
                "state": "EXECUTED",
                "date": "2019-07-05T18:35:29.512364",
                "operationAmount": {"amount": "100", "currency": {"name": "Доллар США", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447995560",
            }
        ]

        # Вызов функции (вернёт 0.0 из-за ошибки)
        result = currency_conversion(test_transaction)

        # В текущей реализации при ошибке возвращается 0.0
        assert result == 0.0
