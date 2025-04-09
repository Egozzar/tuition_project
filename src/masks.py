import logging
import os
from typing import Any

from constants import ROOT_PATH
from exceptions.my_error import MyError

address = os.path.join(ROOT_PATH, "logs", "masks.log")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(address, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str = "") -> Any:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    :param card_number: (int, str) принимаемый номер карты
    :return: (str) строка с замаскированным номером карты
    """
    try:
        str_card_number = str(card_number).replace(" ", "")
        str_length = len(str_card_number)

        if not str_card_number:
            raise MyError("пустое значение на входе")
        if not str_card_number.isdigit():
            raise MyError("на входе могут быть только цифры")

        match str_length:
            case 18 | 19:
                raise MyError("ваша карта устарела")
            case 16:
                logger.info(f"Успешное создание маски для карты {card_number}")
                return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
            case _:
                raise MyError
    except MyError as err:
        logger.error(f"{err}")


def get_mask_account(account: int | str = "") -> Any:
    """
    Функция принимает на вход номер счета и возвращает его маску
    :param account:(int, str) принимаемый номер счёта
    :return:(str) строка с замаскированным номером счёта
    """
    try:
        str_account = str(account).replace(" ", "")
        account_length = len(str_account)

        if not str_account:
            raise MyError("пустое значение на входе")
        if not str_account.isdigit():
            raise MyError("на входе могут быть только цифры")
        if account_length != 20:
            raise MyError

        logger.info(f"Успешное создание маски для номера счёта {account}")
        return f"**{str_account[-4:]}"
    except MyError as err:
        logger.error(f"{err}")
