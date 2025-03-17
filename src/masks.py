from exceptions.my_error import MyError


def get_mask_card_number(card_number: int | str = "") -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    :param card_number: (int, str) принимаемый номер карты
    :return: (str) строка с замаскированным номером карты
    """
    str_card_number = str(card_number).replace(" ", "")
    str_length = len(str_card_number)

    if not str_card_number:
        raise MyError("пустое значение на входе")
    if not str_card_number.isdigit():
        raise MyError("на входе могут быть только цифры")

    match str_length:
        case 18 | 19:
            raise MyError("Ваша карта устарела")
        case 16:
            return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
        case _:
            raise MyError


def get_mask_account(account: int | str = "") -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску
    :param account:(int, str) принимаемый номер счёта
    :return:(str) строка с замаскированным номером счёта
    """
    str_account = str(account).replace(" ", "")
    account_length = len(str_account)

    if not str_account:
        raise MyError("пустое значение на входе")
    if not str_account.isdigit():
        raise MyError("на входе могут быть только цифры")
    if account_length != 20:
        raise MyError

    return f"**{str_account[-4:]}"
