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
