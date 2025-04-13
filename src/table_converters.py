import csv
import os
from typing import Any, Hashable

import pandas as pd

from constants import ROOT_PATH

path_csv = os.path.join(ROOT_PATH, "data", "transactions.csv")
path_xlsx = os.path.join(ROOT_PATH, "data", "transactions_excel.xlsx")


def reader_csv(address: str = path_csv) -> list[dict[str, Any] | None]:
    """
    Функция для считывания финансовых операций из CSV принимает путь
    к файлу CSV, выдает список словарей с транзакциями в виде словарей
    :param address:(str) путь к файлу проекта с таблицей CSV
    :return:(list[dict]) преобразованный список транзакций
    """
    try:
        with open(address, encoding="UTF=8") as file:
            dct_csv = csv.DictReader(file, delimiter=";")

            return list(dct_csv)
    except FileNotFoundError:
        return []


def reader_excel(address: str = path_xlsx) -> list[dict[Hashable, Any] | None]:
    """
    Функция для считывания финансовых операций из Excel принимает путь
    к файлу Excel, выдает список словарей с транзакциями в виде словарей
    :param address:(str) путь к файлу проекта с таблицей Excel
    :return:(list[dict]) преобразованный список транзакций
    """
    try:
        df = pd.read_excel(address)
        result = df.to_dict(orient="records")

        return list(result)
    except FileNotFoundError:
        return []
