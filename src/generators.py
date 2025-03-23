from typing import Iterator, Union


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
