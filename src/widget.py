from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_details: str) -> str:
    """
    Функция принимает на вход реквизиты банка и возвращает их маску
    :param bank_details: (str) принимаемая строка с реквизитами
    :return: (str) строка с замаскированными номером счёта или номером карты
    """
    number_of_digits = sum([lit.isdigit() for lit in bank_details])
    number_for_transformations = int(bank_details[-number_of_digits:])

    if number_of_digits > 16:
        res_substring = get_mask_account(number_for_transformations)
    else:
        res_substring = get_mask_card_number(number_for_transformations)

    return f"{bank_details[: -number_of_digits]}{res_substring}"
