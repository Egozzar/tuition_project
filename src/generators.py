from typing import Iterator, Optional, Union

from exceptions.my_error import MyError


def filter_by_currency(operations: list[dict], curr_code: str) -> Iterator[dict[str, Union[int, str, dict]]]:
    """
    Функция принимает список транзакций и название валюты,
    по которому транзакции отбираются в возвращаемый генератор.
    :param operations: (list[dict]) список транзакций в виде словарей.
    :param curr_code: (str) название валюты, по которому транзакции будут помещены в возвращаемый генератор
    :return: генератор отобранных транзакций
    """
    return (
        elem for elem in operations if elem.get("operationAmount", {}).get("currency", {}).get("code", "") == curr_code
    )


def transaction_descriptions(operations: Optional[list[dict]] = None) -> Iterator[str]:
    """
    Функция принимает список транзакций и формирует итератор, перебирающий описание входных транзакций.
    :param operations: (list[dict]) список транзакций в виде словарей.
    :return: (None)
    """
    try:
        if not operations:
            raise MyError
    except MyError:
        operations = [{"description": "Список транзакций пуст или отсутствует"}]

    for operation in operations:
        yield operation.get("description", "Описание транзакции отсутствует")
