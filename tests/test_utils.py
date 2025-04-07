from src.utils import loader_json


def test_loader_json_no_args():
    assert loader_json() == []


def test_loader_json_wrong_address():
    assert loader_json("www") == []


# @patch("open")
# def test_loader_json(mock_open, str_transaction_codes, list_transaction_codes):
#     mock_open.return_value = str_transaction_codes
#     assert loader_json("../data/operations") == list_transaction_codes
