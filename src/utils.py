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
        with open(address, encoding="UTF=8") as file:
            result = json.load(file)
            if isinstance(result, list):
                logger.info("Содержимое полученного файла успешно преобразовано в список словарей")
                return result

            logger.info("Содержимое полученного файла не преобразовывается в список. Возвращён пустой список.")
            return []

    except FileNotFoundError as err:
        logger.error(f"{err}")
        return []
