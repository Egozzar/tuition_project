import json
import logging
import os

from constants import ROOT_PATH

uni_path = os.path.join(ROOT_PATH, "logs", "utils.log")
way = os.path.join(ROOT_PATH, "data", "operations.json")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(uni_path, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def loader_json(address: str = way) -> list:
    """
    функция принимает на вход путь к JSON-файлу, возвращает список словарей
    с данными о финансовых транзакциях
    :param address:(str) путь к JSON-файлу
    :return:(list) список словарей с данными о финансовых транзакциях
    """
    try:
        with open(address, encoding="UTF-8") as file:
            content = file.read()
            if not content:
                logger.info("В полученном файле нет содержимого. Возвращён пустой список.")
                return []

            result = json.loads(content)
            if isinstance(result, list):
                logger.info("Содержимое полученного файла успешно преобразовано в список словарей")
                return result

            logger.info("Содержимое полученного файла не преобразовывается в список. Возвращён пустой список.")
            return []

    except FileNotFoundError as err:
        logger.error(f"{err}")
        return []


#
#
# if __name__ == "__main__":
#     way2 = os.path.join(ROOT_PATH, "tests", "ex2.json")
#     way3 = os.path.join(ROOT_PATH, "tests", "ex3.json")
#     way4 = os.path.join(ROOT_PATH, "tests", "ex.json")
#
#     loader_json()
#     loader_json(way2)
#     loader_json(way3)
#     loader_json(way4)
