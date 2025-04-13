from unittest.mock import patch

from src.table_converters import reader_csv, reader_excel


def test_reader_csv_wrong():
    wrong_path = "wrong.csv"
    assert reader_csv(wrong_path) == []


@patch("builtins.open")
@patch("csv.DictReader")
def test_reader_csv(mock_dict, mock_open, convert_csv_table_normal):
    mock_dict.return_value = convert_csv_table_normal

    assert reader_csv("www.csv") == convert_csv_table_normal
    mock_open.assert_called_once_with("www.csv", encoding="UTF=8")


def test_reader_excel_wrong():
    wrong_path = "wrong.xlsx"
    assert reader_excel(wrong_path) == []


def test_reader_excel():
    assert len(reader_excel()) == 1000
