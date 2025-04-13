import pytest


@pytest.fixture
def list_of_dict():
    return [
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2003-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 908767882, "state": "EXECUTED", "date": "2022-09-12T21:12:22.453288"},
        {"id": 455432778, "state": "CANCELED", "date": "2024-09-12T21:14:10.778112"},
        {"id": 615064591, "state": "CANCELED", "date": "2010-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_no_state():
    return [
        {"id": 414288291, "status": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "status": "EXECUTED", "date": "2003-06-30T02:08:58.425572"},
        {"id": 594226727, "status": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 908767882, "status": "EXECUTED", "date": "2022-09-12T21:12:22.453288"},
        {"id": 455432778, "status": "CANCELED", "date": "2024-09-12T21:14:10.778112"},
        {"id": 615064591, "status": "CANCELED", "date": "2010-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_no_executed():
    return [
        {"id": 414288291, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2003-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 908767882, "state": "CANCELED", "date": "2022-09-12T21:12:22.453288"},
        {"id": 455432778, "state": "CANCELED", "date": "2024-09-12T21:14:10.778112"},
        {"id": 615064591, "state": "CANCELED", "date": "2010-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_simult():
    return [
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 908767882, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 455432778, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def list_of_dict_diff_formats():
    return [
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2003/06/30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018.09.12T21:27:25.241689"},
        {"id": 908767882, "state": "EXECUTED", "date": "2022-09-12T21:12:22.453288"},
        {"id": 455432778, "state": "CANCELED", "date": "2024/09/12T21:14:10"},
        {"id": 615064591, "state": "CANCELED", "date": "2010-10-14T08:21:33"},
    ]


@pytest.fixture
def list_of_dict_no_date():
    return [
        {"id": 414288291, "state": "EXECUTED", "datetime": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "datetime": "2003-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "datetime": "2018-09-12T21:27:25.241689"},
        {"id": 908767882, "state": "EXECUTED", "datetime": "2022-09-12T21:12:22.453288"},
        {"id": 455432778, "state": "CANCELED", "datetime": "2024-09-12T21:14:10.778112"},
        {"id": 615064591, "state": "CANCELED", "datetime": "2010-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_transactions_shortcut():
    return [
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
            "id": 873106923,
            "state": "EXECUTED",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        },
    ]


@pytest.fixture
def list_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def list_transactions_no_descriptions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def list_transaction_codes():
    return [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {"amount": "51463.70", "currency": {"name": "gbr", "code": "GBR"}},
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358",
        },
    ]


@pytest.fixture
def result_for_transaction_usd():
    return {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 79114.93},
        "info": {"timestamp": 1743979383, "rate": 84.674391},
        "date": "2025-04-06",
        "result": 6699008.516758,
    }


@pytest.fixture
def str_transaction_codes():
    return '[{"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", \
           "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}}, \
           "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542", "to": \
           "Счет 75651667383060284188"}, {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",\
           "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},\
           "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": \
           "Счет 64686473678894779589"}, {"id": 522357576, "state": "EXECUTED", "date": "2019-07-12T20:41:47.882230", \
           "operationAmount": {"amount": "51463.70", "currency": {"name": "gbr", "code": "GBR"}}, "description": \
           "Перевод организации", "from": "Счет 48894435694657014368", "to": "Счет 38976430693692818358"}]'


@pytest.fixture
def result_for_transaction_first():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def convert_csv_table_normal():
    return [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
