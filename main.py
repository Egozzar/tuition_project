from typing import Any, Iterator, Hashable

from src.table_converters import reader_csv, reader_excel
from src.utils import loader_json
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.selections import selection_by_exp
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Функция формирует основную логику проекта и связывает функциональности между собой.
    :return: None
    """
    # Объявление локальных переменных
    gotted_list_json: list[dict[Hashable, Any] | None]  # список транзакций из выбранного JSON-файла
    gotted_list_csv: list[dict[str, Any] | None]  # список транзакций из выбранного CSV-файла
    gotted_list_excel: list[dict[Hashable, Any] | None]  # список транзакций из выбранного EXCEL-файла
    sorted_by_state: list[dict[str, int | str]] | None  # список транзакций, отсортированный по статусу
    sorted_ascending: list[dict[str, int | str]] | None  # список транзакций, отсортированный по возростанию

    sorted_by_exp: list[dict | Any]  # список транзакций, отсортированный по выражению в описании
    sorted_descending: list[dict[str, int | str]] | None  # список транзакций, отсортированный по убыванию
    arguments: list[dict | Any]  # список аргументов, определяющих положение интерпретатора

    gen_transactions: Iterator[dict]  # генератор выбранных транзакций
    selected_type: str  # выбранный тип файла
    selected_state: str  # выбранный статус операций для сортировки

    menu_item: str  # пункт меню

    # негативные сообщения
    negative_loop_message: str = "Такого номера в меню нет. Попробуйте ещё раз."
    negative_script_message: str = "Не найдено ни одной транзакции, подходящей под Ваши условия фильтрации."

    arguments = list()

    # Приветствие
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Работа программы. Получение списка транзакций из выбранного источника
    while True:
        print(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла"
        )
        menu_item = input().strip()

        match menu_item:
            case "1":
                selected_type = "JSON"
                gotted_list_json = loader_json()
                arguments.append(gotted_list_json)
                break
            case "2":
                selected_type = "CSV"
                gotted_list_csv = reader_csv()
                arguments.append(gotted_list_csv)
                break
            case "3":
                selected_type = "XLSX"
                gotted_list_excel = reader_excel()
                arguments.append(gotted_list_excel)
                break
            case _:
                print(negative_loop_message)

    print(f"Для обработки выбран {selected_type}-файл.")
    print("_" * 20)
    print()

    # Фильтрация транзакций по состоянию: выполненные, отменённые, ожидающие
    while True:
        print(
            "Выберите статус, по которому необходимо выполнить фильтрацию.\n"
            "Введите необходимый пункт меню:\n"
            "1. EXECUTED (ВЫПОЛНЕНО)\n"
            "2. CANCELED (ОТМЕНЕНО)\n"
            "3. PENDING (В ОЖИДАНИИ)"
        )
        menu2_item = input().strip()

        match menu2_item:
            case "1":
                selected_state = "EXECUTED"
                break
            case "2":
                selected_state = "CANCELED"
                break
            case "3":
                selected_state = "PENDING"
                break
            case _:
                print(negative_loop_message)

    sorted_by_state = filter_by_state(arguments.pop(), selected_state)
    arguments.append(sorted_by_state)

    if not sorted_by_state:
        print(negative_script_message)
        return

    print(f"Операции отфильтрованы по статусу {selected_state}")
    print("_" * 20)
    print()

    # Предложение отсортировать транзакции по дате
    while True:
        print("Отсортировать операции по дате?\n" "1. Да\n" "2. Нет")
        menu3_item = input().strip()

        match menu3_item:
            # Блок с сортировкой по дате
            case "1":
                while True:
                    print("_" * 20)
                    print()

                    print("1. Сортировать по возростанию\n" "2. Сортировать по убыванию")

                    menu3_1_item = input().strip()

                    match menu3_1_item:
                        case "1":
                            sorted_ascending = sort_by_date(sorted_by_state, vector=False)
                            arguments.append(sorted_ascending)
                            break
                        case "2":
                            sorted_descending = sort_by_date(sorted_by_state)
                            arguments.append(sorted_descending)
                            break
                        case _:
                            print(negative_loop_message)
                break
            # Блок без сортировки по дате
            case "2":
                break
            case _:
                print(negative_loop_message)

    print("_" * 20)
    print()

    # Предложение работать только с рублёвыми транзакциями
    print("Выводить только рублёвые операции?\n" "1. Да\n" "2. Нет")
    menu4_item = input().strip()

    match menu4_item:
        case "1":
            gen_transactions = filter_by_currency(arguments.pop(), "RUB")
            arguments.append(list(gen_transactions))
        case "2":
            gen_transactions = filter_by_currency(arguments.pop())
            arguments.append(list(gen_transactions))

    print("_" * 20)
    print()

    # Предложение работать с транзакциями с конкретными описаниями
    print("Отфильтровать список транзакций по определенному слову в описании?\n" "1. Да\n" "2. Нет")
    menu5_item = input().strip()
    descriptions = {
        "1": "Открытие вклада",
        "2": "Перевод организации",
        "3": "Перевод с карты на счет",
        "4": "Перевод с карты на карту",
        "5": "Перевод со счета на счет",
    }
    match menu5_item:
        case "1":
            print("_" * 20)
            print()
            print(
                "Выберите номер описания:\n"
                "1. Открытие вклада\n"
                "2. Перевод организации\n"
                "3. Перевод с карты на счет\n"
                "4. Перевод с карты на карту\n"
                "5. Перевод со счета на счет"
            )

            menu5_1_item = input().strip()
            sorted_by_exp = selection_by_exp(arguments.pop(), descriptions[menu5_1_item])
            arguments.append(sorted_by_exp)

    # Подсчёт и вывод результатов
    result_list = arguments.pop()
    if not result_list:
        print(negative_script_message)
        return

    print("_" * 20)
    print()
    print(f"Всего банковских операций в выборке: {len(result_list)}")

    for elem in result_list:
        # переменные для форматирования вывода
        exp = elem.get("description")
        d = get_date(elem.get("date"))
        from_whom = mask_account_card(elem.get("from")) if elem.get("from") else None
        for_whom = mask_account_card(elem.get("to"))

        match selected_type:
            case "JSON":
                total = round(float(elem.get("operationAmount", {}).get("amount", 0.0)))
                name = elem.get("operationAmount", {}).get("currency", {}).get("name", "no name")
            case "XLSX":
                total = round(elem.get("amount"))
                name = elem.get("currency_name")
            case "CSV":
                total = elem.get("amount")
                name = elem.get("currency_name")

        match exp:
            case "Открытие вклада":
                text = f"{d} {exp}\n" f"{for_whom}\n" f"Сумма: {str(total)} {name}"
            case _:
                text = f"{d} {exp}\n" f"{from_whom} -> {for_whom}\n" f"Сумма: {str(total)} {name}"

        print()
        print(text)


if __name__ == "__main__":
    main()
