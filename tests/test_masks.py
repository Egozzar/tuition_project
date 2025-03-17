import pytest

from exceptions.my_error import MyError
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, result",
    [
        (1234567890123456, "1234 56** **** 3456"),
        (9_876_543_210_987_654, "9876 54** **** 7654"),
        ("1234567890123456", "1234 56** **** 3456"),
        (" 1234 5678  9012 3456 ", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number(card_number, result):
    assert get_mask_card_number(card_number) == result


def test_get_mask_card_number_empty():
    with pytest.raises(MyError) as err:
        get_mask_card_number()
    assert str(err.value) == "Ошибка: пустое значение на входе."


def test_get_mask_card_number_alpha():
    with pytest.raises(MyError) as err:
        get_mask_card_number("55iiiiiiiiiiii77")
    assert str(err.value) == "Ошибка: на входе могут быть только цифры."


def test_get_mask_card_number_outdated():
    with pytest.raises(MyError) as err:
        get_mask_card_number("123456789012345678")
    assert str(err.value) == "Ошибка: Ваша карта устарела."


def test_get_mask_card_number_wrong_len():
    with pytest.raises(MyError) as err:
        get_mask_card_number("123456789")
    assert str(err.value) == "Ошибка ввода."


@pytest.mark.parametrize(
    "account, result",
    [
        (12345678901234567899, "**7899"),
        (98_765_432_109_876_543_217, "**3217"),
        ("12345678901234567899", "**7899"),
        (" 1234 5678  9012 3456 7899 ", "**7899"),
    ],
)
def test_get_mask_account(account, result):
    assert get_mask_account(account) == result


def test_get_mask_account_empty():
    with pytest.raises(MyError) as err:
        get_mask_account()
    assert str(err.value) == "Ошибка: пустое значение на входе."


def test_get_mask_account_alpha():
    with pytest.raises(MyError) as err:
        get_mask_account("12iiiiiiiiiiiiiiii77")
    assert str(err.value) == "Ошибка: на входе могут быть только цифры."


def test_get_mask_account_wrong_len():
    with pytest.raises(MyError) as err:
        get_mask_account(123456789)
    assert str(err.value) == "Ошибка ввода."
