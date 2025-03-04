from datetime import datetime
from typing import Any

type Oper = list[dict[str, int | str]]


def filter_by_state(operations: Oper, state: str = "EXECUTED") -> Oper:
    """
     Функция принимает список банковских операций, фильтрует их по параметру состояния (выполнен, отменён и пр.)
     и возвращает отфильтрованный список.
    :param operations: (Oper) список операций, представленных в виде словарей
    :param state: (str) состояние операции, по которому фильтруется передаваемый список
    :return: (Oper) список отфильтрованных операций
    """
    selected_operations = filter(lambda x: x["state"] == state, operations)

    return list(selected_operations)


def sort_subfunc(operation: dict[str, Any]) -> datetime:
    """
     Вспомогательная функция получения ключа (key) для сортировки.
     Принимает словарь с данными по банковской операции и возвращает объект даты проведения этой операции.
    :param operation: (dict[str, int | str]) словарь с данными по банковской операции
    :return: (datetime) объект даты операции
    """
    moment = datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")

    return moment
