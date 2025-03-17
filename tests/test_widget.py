import pytest

from exceptions.my_error import MyError
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "bank_details, result",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card(bank_details, result):
    assert mask_account_card(bank_details) == result


def test_mask_account_card_empty():
    with pytest.raises(MyError) as err:
        mask_account_card()
    assert str(err.value) == "Ошибка: пустое значение на входе."


def test_mask_account_card_without_number():
    with pytest.raises(MyError) as err:
        mask_account_card("Visa Classic")
    assert str(err.value) == "Ошибка: нет номера реквизита на входе."


def test_mask_account_card_without_details():
    with pytest.raises(MyError) as err:
        mask_account_card("35383033474447895560")
    assert str(err.value) == "Ошибка: нет названия реквизита на входе."


@pytest.mark.parametrize(
    "date_string, result",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2003/06/30T02:08:58.425572", "30.06.2003"),
        ("2010-10-14T08:21:33", "14.10.2010"),
        ("2018.09.12T21:27:25", "12.09.2018"),
    ],
)
def test_get_date(date_string, result):
    assert get_date(date_string) == result


def test_get_date_empty():
    with pytest.raises(MyError) as err:
        get_date()
    assert str(err.value) == "Ошибка: пустое значение на входе."


def test_get_date_non_format():
    with pytest.raises(MyError) as err:
        get_date("www")
    assert str(err.value) == "Ошибка: неизвестный формат даты."
