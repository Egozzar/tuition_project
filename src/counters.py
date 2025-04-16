from collections import Counter
from typing import Any

from src.selections import selection_by_exp


def counter_operations(operations: list[dict | Any] | None = None, categories: list[str | Any] | None = None) -> dict:
    """
    Функция для подсчета количества банковских операций определенной категории
    :param operations:(list[dict | Any]) список словарей с данными о транзакциях
    :param categories:(list[str | Any]) список категорий операций
    :return:(dict) словарь, в котором ключи — это названия категорий,
     а значения — это количество операций в каждой категории
    """
    if not operations or not categories:
        return {}

    filter_list = []

    for exp in categories:
        filter_list.extend(selection_by_exp(operations, exp))

    counted_categories = Counter([elem.get("description") for elem in filter_list])
    result = dict(counted_categories)

    return result
