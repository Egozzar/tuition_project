def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    :param card_number: (int) принимаемый номер карты
    :return: (str) строка с замаскированным номером карты
    """
    str_card_number = str(card_number)
    # Вариант решения с помощью форматирования строки

    mask_card_number = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"

    # Вариант решения с помощью списков

    # list_card_number = list(str_card_number)
    # list_card_number[6 : 12] = ['*'] * 6
    # i = len(list_card_number) - 1
    #
    # while i > 3:
    #     if i % 4 == 0:
    #         list_card_number.insert(i, ' ')
    #     i -= 1
    #
    # mask_card_number = ''.join(list_card_number)

    return mask_card_number


def get_mask_account(account: int) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску
    :param account:(int) принимаемый номер счёта
    :return:(str) строка с замаскированным номером счёта
    """
    str_account = str(account)
    mask_account = f"**{str_account[-4:]}"

    return mask_account
