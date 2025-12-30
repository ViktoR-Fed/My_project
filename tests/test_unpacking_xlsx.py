from unittest.mock import MagicMock, patch

# Импортируем функцию для тестирования
from src.data_processing import unpacking_xlsx


def test_file_not_exists():
    """Тест: файл не существует"""
    with (
        patch("os.path.exists", return_value=False),
        patch("os.path.isfile", return_value=False),
        patch("os.path.getsize", return_value=0),
    ):
        result = unpacking_xlsx("nonexistent.xlsx")
        assert result == []


def test_path_is_directory():
    """Тест: путь ведет к директории"""
    with patch("os.path.exists", return_value=True), patch("os.path.isfile", return_value=False):
        result = unpacking_xlsx("some_directory/")
        assert result == []


def test_empty_file():
    """Тест: файл существует, но пустой"""
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=0),
    ):
        result = unpacking_xlsx("empty.xlsx")
        assert result == []


def test_successful_read():
    """Тест: успешное чтение файла"""
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=100),
        patch("pandas.read_excel") as mock_read_excel,
    ):
        # Создаем мок DataFrame
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [
            {"id": 1, "amount": 100, "date": "2023-01-01"},
            {"id": 2, "amount": 200, "date": "2023-01-02"},
        ]
        mock_read_excel.return_value = mock_df

        result = unpacking_xlsx("transactions.xlsx")

        assert len(result) == 2
        assert result[0]["id"] == 1
        assert result[0]["amount"] == 100
        assert result[0]["date"] == "2023-01-01"
        assert result[1]["id"] == 2
        assert result[1]["amount"] == 200

        mock_read_excel.assert_called_once_with("transactions.xlsx")
        mock_df.to_dict.assert_called_once_with(orient="records")


def test_read_excel_error():
    """Тест: ошибка при чтении Excel файла"""
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=100),
        patch("pandas.read_excel", side_effect=Exception("Invalid Excel file")),
    ):
        result = unpacking_xlsx("corrupted.xlsx")
        assert result == []


def test_empty_dataframe():
    """Тест: Excel файл с пустыми данными"""
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=50),
        patch("pandas.read_excel") as mock_read_excel,
    ):
        mock_df = MagicMock()
        mock_df.to_dict.return_value = []
        mock_read_excel.return_value = mock_df

        result = unpacking_xlsx("empty_data.xlsx")
        assert result == []


def test_default_filename():
    """Тест: вызов функции с именем файла по умолчанию"""
    with (
        patch("os.path.exists", return_value=True) as mock_exists,
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=100),
        patch("pandas.read_excel") as mock_read_excel,
    ):
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
        mock_read_excel.return_value = mock_df

        result = unpacking_xlsx()

        # Проверяем, что использовался путь по умолчанию
        mock_exists.assert_called_once_with("data/transactions_excel.xlsx")
        mock_read_excel.assert_called_once_with("data/transactions_excel.xlsx")
        assert len(result) == 1
