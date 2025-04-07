import json


def loader_json(address: str = "") -> list:
    """
    функция принимает на вход путь к JSON-файлу и возвращает список словарей
    с данными о финансовых транзакциях
    :param address:(str) путь к JSON-файлу
    :return:(list) список словарей с данными о финансовых транзакциях
    """
    try:
        with open(address, encoding="UTF-8") as file:
            if not file:
                return []

            result = json.load(file)
            if isinstance(result, list):
                return result

            return []

    except FileNotFoundError:
        return []
