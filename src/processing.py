from datetime import datetime
from typing import Any, Optional

from dateutil import parser

from exceptions.my_error import MyError

type Oper = Optional[list[dict[str, int | str]]]


def filter_by_state(operations: Oper = None, state: str = "EXECUTED") -> Oper:
    """
     Функция принимает список банковских операций, фильтрует их по параметру состояния (выполнен, отменён и пр.)
     и возвращает отфильтрованный список.
    :param operations: (Oper) список операций, представленных в виде словарей
    :param state: (str) состояние операции, по которому фильтруется передаваемый список
    :return: (Oper) список отфильтрованных операций
    """
    if not operations:
        raise MyError("отсутствует список операций")

    selected_operations = list()
    for elem in operations:
        if not elem.get("state", False):
            raise MyError('в словаре отсутствует ключ "state"')
        if elem.get("state", False) == state:
            selected_operations.append(elem)

    return selected_operations


def sort_subfunc(operation: dict[str, Any]) -> datetime:
    """
     Вспомогательная функция получения ключа (key) для сортировки.
     Принимает словарь с данными по банковской операции и возвращает объект даты проведения этой операции.
    :param operation: (dict[str, int | str]) словарь с данными по банковской операции
    :return: (datetime) объект даты операции
    """
    date_string = operation.get("date", "")
    if not date_string:
        raise MyError('в словаре отсутствует ключ "date"')

    try:
        moment = parser.parse(date_string)
    except ValueError:
        raise MyError("неизвестный формат даты")

    return moment


def sort_by_date(operations: Oper = None, vector: bool = True) -> Oper:
    """
     Функция принимает список банковских операций и возвращает новый список, отсортированный
     по дате проведения операции.
    :param operations: (Oper) список операций, представленных в виде словарей
    :param vector: (bool) порядок сортировки (True - убывание)
    :return: (Oper) отсортированный список словарей
    """
    if not operations:
        raise MyError("отсутствует список операций")

    sorted_list = sorted(operations, key=sort_subfunc, reverse=vector)

    return sorted_list
