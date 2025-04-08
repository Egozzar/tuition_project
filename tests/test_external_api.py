from unittest.mock import patch

import pytest

from exceptions.my_error import MyError
from src.external_api import conversion_of_amount


@patch("requests.get")
def test_conversion_of_amount_usd(mock_get, list_transaction_codes, result_for_transaction_usd):
    mock_get.return_value.json.return_value = result_for_transaction_usd
    assert conversion_of_amount(list_transaction_codes[0]) == 6699008.516758
    mock_get.assert_called()


def test_conversion_of_amount_rub(list_transaction_codes):
    assert conversion_of_amount(list_transaction_codes[1]) == 31957.58


def test_conversion_of_amount_empty():
    with pytest.raises(MyError) as err:
        conversion_of_amount()
    assert str(err.value) == "Ошибка: пустое значение на входе."


def test_conversion_of_amount_wrong_code(list_transaction_codes):
    assert conversion_of_amount(list_transaction_codes[2]) == 0.0
