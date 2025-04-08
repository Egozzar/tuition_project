import os
from typing import Any, Optional

import requests
from dotenv import load_dotenv

from exceptions.my_error import MyError


def conversion_of_amount(operation: Optional[dict] = None) -> Any:
    """
    функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, то сумма конвертируется в рубли на удалённом ресурсе
    :param operation:(dict) словарь с деталями транзакции
    :return:(float) сумма транзакции в рублях
    """
    if not operation:
        raise MyError("пустое значение на входе")

    currency_code = operation.get("operationAmount", {}).get("currency", {}).get("code", "")
    total = operation.get("operationAmount", {}).get("amount", 0)

    if currency_code == "RUB":
        return float(total)

    elif currency_code in ("USD", "EUR"):
        # Загрузка переменных из .env-файла
        load_dotenv()
        # Получение значения переменной APILAYER_KEY из .env-файла
        apilayer_key = os.getenv("APILAYER_KEY")
        url = "https://api.apilayer.com/exchangerates_data/convert"

        headers = {"apikey": apilayer_key}
        payload = {"amount": total, "from": currency_code, "to": "RUB"}

        response = requests.get(url, headers=headers, params=payload)
        result = response.json()

        return result["result"]
    else:
        return 0.0
