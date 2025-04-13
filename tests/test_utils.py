from unittest.mock import patch

from src.utils import loader_json


def test_loader_json_wrong_address():
    wrong_way = "ex.json"
    assert loader_json(wrong_way) == []


@patch("builtins.open")
@patch("json.load")
def test_loader_json_no_list(mock_json, mock_open):
    mock_json.return_value = "qwert"

    assert loader_json("test.json") == []
    mock_open.assert_called_once_with("test.json", encoding="UTF=8")


@patch("builtins.open")
@patch("json.load")
def test_loader_json(mock_json, mock_open, str_transaction_codes, list_transaction_codes):
    mock_json.return_value = list_transaction_codes

    assert loader_json(str_transaction_codes) == list_transaction_codes
    mock_open.assert_called_once_with(str_transaction_codes, encoding="UTF=8")
