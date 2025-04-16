import re
from typing import Any


def selection_by_exp(operations: list[dict | Any], expression: str | None = "") -> list[dict | Any]:
    """
    Функция для фильтрации списка словарей операций по заданной строке,
    возвращает отфильтрованный список транзакций
    :param operations:(list[dict | Any]) список словарей транзакций
    :param expression:(str) строка в описании, по которой фильтруется список транзакций
    :return:(list[dict | Any]) отфильтрованный список транзакций
    """
    if expression is None:
        return []

    pattern = re.compile(f"{expression.lower()}")
    lst = [elem for elem in operations if re.search(pattern, elem.get("description", "").lower())]

    return lst
