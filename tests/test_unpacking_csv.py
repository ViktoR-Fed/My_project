from unittest.mock import mock_open, patch

# Импортируем функцию для тестирования
from src.data_processing import unpacking_csv


def test_file_not_exists():
    """Тест: файл не существует"""
    with (
        patch("os.path.exists", return_value=False),
        patch("os.path.isfile", return_value=False),
        patch("os.path.getsize", return_value=0),
    ):
        result = unpacking_csv("nonexistent.csv")
        assert result == []


def test_path_is_directory():
    """Тест: путь ведет к директории, а не файлу"""
    with patch("os.path.exists", return_value=True), patch("os.path.isfile", return_value=False):
        result = unpacking_csv("some_directory/")
        assert result == []


def test_empty_file():
    """Тест: файл существует, но пустой"""
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=0),
    ):
        result = unpacking_csv("empty.csv")
        assert result == []


def test_successful_read():
    """Тест: успешное чтение файла"""
    csv_content = "id;amount;date\n1;100;2023-01-01\n2;200;2023-01-02"

    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=100),
        patch("builtins.open", mock_open(read_data=csv_content)),
    ):
        result = unpacking_csv("transactions.csv")

        assert len(result) == 2
        assert result[0]["id"] == "1"
        assert result[0]["amount"] == "100"
        assert result[0]["date"] == "2023-01-01"
        assert result[1]["id"] == "2"
        assert result[1]["amount"] == "200"
        assert result[1]["date"] == "2023-01-02"


def test_default_filename():
    """Тест: вызов функции с именем файла по умолчанию"""
    csv_content = "id;amount;date\n1;100;2023-01-01"

    with (
        patch("os.path.exists", return_value=True) as mock_exists,
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=50),
        patch("builtins.open", mock_open(read_data=csv_content)),
    ):
        result = unpacking_csv()

        # Проверяем, что использовался путь по умолчанию
        mock_exists.assert_called_once_with("data/transactions.csv")
        assert len(result) == 1


def test_csv_with_different_delimiter():
    """Тест: проверка работы с разделителем ';'"""
    csv_content = "id;amount;date\n1;150.50;2023-01-01\n2;299.99;2023-01-02"
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=100),
        patch("builtins.open", mock_open(read_data=csv_content)),
    ):
        result = unpacking_csv("transactions.csv")

        assert len(result) == 2
        # Проверяем, что разделитель работает корректно
        assert "id" in result[0]
        assert "amount" in result[0]
        assert "date" in result[0]
