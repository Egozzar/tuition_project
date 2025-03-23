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


def card_number_generator(start: int = 1, stop: int = 0) -> Iterator[str]:
    """
    Функция принимает начальное и конечное число диапазона и формирует генератор,
    который выдает номера банковских карт в заданном диапазоне в необходимом формате.
    :param start:(int) начальное число диапазона.
    :param stop:(int) конечное число диапазона.
    """
    if stop > 9999999999999999:
        raise MyError("задан чрезмерный диапазон")

    if start >= stop:
        raise MyError

    for num in range(start, stop + 1):
        str_card = str(num).rjust(16, "0")

        yield f"{str_card[:4]} {str_card[4:8]} {str_card[8:12]} {str_card[-4:]}"
