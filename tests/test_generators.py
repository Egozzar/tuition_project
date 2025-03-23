import pytest

from exceptions.my_error import MyError
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(list_transactions_shortcut):
    res_for_comparison = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        },
    ]
    result = list(filter_by_currency(list_transactions_shortcut, "USD"))
    assert res_for_comparison == result


def test_filter_by_currency_rub(list_transactions_shortcut):
    res_for_comparison = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        },
    ]
    result = list(filter_by_currency(list_transactions_shortcut, "RUB"))
    assert res_for_comparison == result


def test_filter_by_currency_no_code(list_transactions_shortcut):
    res_for_comparison = []
    result = list(filter_by_currency(list_transactions_shortcut, "EUR"))
    assert res_for_comparison == result


def test_filter_by_currency_empty():
    assert filter_by_currency([], "RUB")


def test_transaction_descriptions_empty():
    gen = transaction_descriptions()
    result = next(gen)
    res_for_comparison = "Список транзакций пуст или отсутствует"
    assert res_for_comparison == result


def test_transaction_descriptions_empty_list():
    gen = transaction_descriptions([])
    result = next(gen)
    res_for_comparison = "Список транзакций пуст или отсутствует"
    assert res_for_comparison == result


def test_transaction_descriptions(list_transactions):
    gen = transaction_descriptions(list_transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"
    assert next(gen) == "Перевод организации"


def test_transaction_descriptions_no_descriptions(list_transactions_no_descriptions):
    gen = transaction_descriptions(list_transactions_no_descriptions)
    assert next(gen) == "Описание транзакции отсутствует"
    assert next(gen) == "Описание транзакции отсутствует"


def test_card_number_generator():
    gen_1 = card_number_generator(12, 14)
    assert next(gen_1) == "0000 0000 0000 0012"
    assert next(gen_1) == "0000 0000 0000 0013"
    assert next(gen_1) == "0000 0000 0000 0014"

    gen_2 = card_number_generator(9999999999999997, 9999999999999999)
    assert next(gen_2) == "9999 9999 9999 9997"
    assert next(gen_2) == "9999 9999 9999 9998"
    assert next(gen_2) == "9999 9999 9999 9999"


def test_card_number_generator_empty():
    with pytest.raises(MyError) as err:
        gen = card_number_generator()
        next(gen)
        assert str(err.value) == "Ошибка ввода."


def test_card_number_generator_over():
    with pytest.raises(MyError) as err:
        gen = card_number_generator(1, 99999999999999999)
        next(gen)
        assert str(err.value) == "Ошибка: задан чрезмерный диапазон."
