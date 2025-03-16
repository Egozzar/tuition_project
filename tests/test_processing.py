import pytest

from exceptions.my_error import MyError
from src.processing import filter_by_state, sort_by_date, sort_subfunc


def test_filter_by_state(list_of_dict):
    assert filter_by_state(list_of_dict) == [
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2003-06-30T02:08:58.425572"},
        {"id": 908767882, "state": "EXECUTED", "date": "2022-09-12T21:12:22.453288"},
    ]


def test_filter_by_state_canceled(list_of_dict):
    assert filter_by_state(list_of_dict, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 455432778, "state": "CANCELED", "date": "2024-09-12T21:14:10.778112"},
        {"id": 615064591, "state": "CANCELED", "date": "2010-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_no_executed(list_of_dict_no_executed):
    assert filter_by_state(list_of_dict_no_executed) == []


def test_filter_by_state_no_list():
    with pytest.raises(MyError) as err:
        filter_by_state()
    assert str(err.value) == "Ошибка: отсутствует список операций."


def test_filter_by_state_no_state(list_of_dict_no_state):
    with pytest.raises(MyError) as err:
        filter_by_state(list_of_dict_no_state)
    assert str(err.value) == 'Ошибка: в словаре отсутствует ключ "state".'


def test_sort_by_date(list_of_dict):
    assert sort_by_date(list_of_dict) == [
        {"id": 455432778, "state": "CANCELED", "date": "2024-09-12T21:14:10.778112"},
        {"id": 908767882, "state": "EXECUTED", "date": "2022-09-12T21:12:22.453288"},
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2010-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2003-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_no_vector(list_of_dict):
    assert sort_by_date(list_of_dict, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2003-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2010-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 908767882, "state": "EXECUTED", "date": "2022-09-12T21:12:22.453288"},
        {"id": 455432778, "state": "CANCELED", "date": "2024-09-12T21:14:10.778112"},
    ]


def test_sort_by_date_simult(list_of_dict_simult):
    assert sort_by_date(list_of_dict_simult) == list_of_dict_simult


def test_sort_by_date_diff_formats(list_of_dict_diff_formats):
    assert sort_by_date(list_of_dict_diff_formats) == [
        {"id": 455432778, "state": "CANCELED", "date": "2024/09/12T21:14:10"},
        {"id": 908767882, "state": "EXECUTED", "date": "2022-09-12T21:12:22.453288"},
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018.09.12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2010-10-14T08:21:33"},
        {"id": 939719570, "state": "EXECUTED", "date": "2003/06/30T02:08:58.425572"},
    ]


def test_sort_by_date_no_date(list_of_dict_no_date):
    with pytest.raises(MyError) as err:
        sort_by_date(list_of_dict_no_date)
    assert str(err.value) == 'Ошибка: в словаре отсутствует ключ "date".'


def test_sort_subfunc_wrong_date():
    with pytest.raises(MyError) as err:
        sort_subfunc({"id": 455432778, "state": "CANCELED", "date": "www"})
    assert str(err.value) == "Ошибка: неизвестный формат даты."


def test_sort_by_date_no_list():
    with pytest.raises(MyError) as err:
        sort_by_date()
    assert str(err.value) == "Ошибка: отсутствует список операций."
