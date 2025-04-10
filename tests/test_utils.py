import os

from constants import ROOT_PATH
from src.utils import loader_json

way = os.path.join(ROOT_PATH, "data", "operations.json")
way2 = os.path.join(ROOT_PATH, "tests", "ex2.json")
way3 = os.path.join(ROOT_PATH, "tests", "ex3.json")
way4 = os.path.join(ROOT_PATH, "tests", "ex.json")


def test_loader_json(result_for_transaction_first):
    assert loader_json()[0] == result_for_transaction_first


def test_loader_json_no_content():
    assert loader_json(way2) == []


def test_loader_json_no_list():
    assert loader_json(way3) == []


def test_loader_json_wrong_address():
    assert loader_json(way4) == []


# @patch("open")
# def test_loader_json(mock_open, str_transaction_codes, list_transaction_codes):
#     mock_open.return_value = str_transaction_codes
#     assert loader_json("../data/operations") == list_transaction_codes
