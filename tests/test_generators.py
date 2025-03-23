from src.generators import filter_by_currency


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
