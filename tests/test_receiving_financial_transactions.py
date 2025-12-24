import json
from unittest.mock import mock_open, patch

from src.utils import receiving_financial_transactions


def test_file_not_exists() -> None:
    """Тест на несуществующий файл"""
    with patch("os.path.exists", return_value=False):
        result = receiving_financial_transactions("nonexistent.json")
        assert result == []


def test_path_is_directory_not_file() -> None:
    """Тест, когда путь ведет к директории, а не файлу"""
    with patch("os.path.exists", return_value=True):
        with patch("os.path.isfile", return_value=False):
            result = receiving_financial_transactions("some_directory/")
            assert result == []


def test_empty_file() -> None:
    """Тест на пустой файл"""
    with patch("os.path.exists", return_value=True):
        with patch("os.path.isfile", return_value=True):
            with patch("os.path.getsize", return_value=0):
                result = receiving_financial_transactions("empty.json")
                assert result == []


def test_successful_load_json_list() -> None:
    """Тест успешной загрузки JSON-списка"""
    test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    with patch("os.path.exists", return_value=True):
        with patch("os.path.isfile", return_value=True):
            with patch("os.path.getsize", return_value=100):
                mock_file = mock_open(read_data=json.dumps(test_data))

                with patch("builtins.open", mock_file):
                    result = receiving_financial_transactions("data.json")

                    assert result == test_data
                    mock_file.assert_called_once_with("data.json", "r", encoding="utf-8")


def test_json_not_list_returns_empty() -> None:
    """Тест, когда JSON не является списком"""
    test_data = {"id": 1, "amount": 100}

    with patch("os.path.exists", return_value=True):
        with patch("os.path.isfile", return_value=True):
            with patch("os.path.getsize", return_value=100):
                mock_file = mock_open(read_data=json.dumps(test_data))

                with patch("builtins.open", mock_file):
                    result = receiving_financial_transactions("data.json")
                    assert result == []


def test_default_filepath() -> None:
    """Тест использования пути по умолчанию"""
    test_data = [{"id": 1}]

    with patch("os.path.exists", return_value=True):
        with patch("os.path.isfile", return_value=True):
            with patch("os.path.getsize", return_value=100):
                mock_file = mock_open(read_data=json.dumps(test_data))

                with patch("builtins.open", mock_file):
                    result = receiving_financial_transactions()

                    assert result == test_data
                    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


def test_invalid_json_returns_empty() -> None:
    """Тест на невалидный JSON"""
    with patch("os.path.exists", return_value=True):
        with patch("os.path.isfile", return_value=True):
            with patch("os.path.getsize", return_value=100):
                mock_file = mock_open(read_data="{invalid json")

                with patch("builtins.open", mock_file):
                    result = receiving_financial_transactions("data.json")
                    assert result == []
