from datetime import datetime

from dateutil import parser

from exceptions.my_error import MyError
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_details: str = "") -> str:
    """
    Функция принимает на вход реквизиты банка и возвращает их маску
    :param bank_details: (str) принимаемая строка с реквизитами
    :return: (str) строка с замаскированными номером счёта или номером карты
    """
    if not bank_details:
        raise MyError("пустое значение на входе")

    number_of_digits = sum([lit.isdigit() for lit in bank_details])
    if not number_of_digits:
        raise MyError("нет номера реквизита на входе")

    if number_of_digits == len(bank_details):
        raise MyError("нет названия реквизита на входе")

    string_for_transformations = bank_details[-number_of_digits:]

    if 18 < number_of_digits < 21:
        res_substring = get_mask_account(string_for_transformations)
    else:
        res_substring = get_mask_card_number(string_for_transformations)

    return f"{bank_details[: -number_of_digits]}{res_substring}"


def get_date(date_string: str = "") -> str:
    """
    Функция принимает на вход строку с датой одного формата и возвращает строку этой же даты,
    но уже другого формата
    :param date_string: (str) принимаемая строка с датой
    :return: format_string (str) строка полученной даты необходимого формата
    """
    if not date_string:
        raise MyError("пустое значение на входе")

    try:
        date_object = parser.parse(date_string)
    except ValueError:
        raise MyError("неизвестный формат даты")

    format_string = datetime.strftime(date_object, "%d.%m.%Y")

    return format_string
