import os
from datetime import datetime
from functools import wraps
from typing import Any, Callable

from constants import ROOT_PATH


def log(filename: str = "") -> Callable[[Callable], Callable]:
    """
    Функция-декоратор, принимает название файла и устанавливает его в качестве
    параметра декоратору, который возвращает.
    :param filename:(str) название файла для логирования
    :return:(Callable) функция-декоратор с переданным параметром
    """

    def sub_decor(func: Callable) -> Callable:
        """
        Функция-декоратор, принимает функцию, оборачивает её
        и возвращает отдекорированную функцию с добавленным функционалом
        :param func:(Callable) целевая функция
        :return:(Callable) функция-обёртка с возможностью логирования
        """

        @wraps(func)
        def wrapper(*args: tuple[Any], **kwargs: dict) -> Any:
            """
            Функция-обёртка целевой функции, принимает и передаёт возможные параметры и
            добавляет возможность логирования работы целевой функции
            :param args:(tuple) возможные позиционные аргументы
            :param kwargs:(dict) возможные именованные аргументы
            :return: результат работы целевой функции
            """
            start_text = f"Function {func.__name__} started ({datetime.now().strftime('%d.%m.%y %H:%M:%S.%f')})\n"
            good_text = f"Function {func.__name__} ok\n"
            finish_text = f"Function {func.__name__} finished ({datetime.now().strftime('%d.%m.%y %H:%M:%S.%f')})\n"

            if not filename:
                print(start_text)
            else:
                with open(os.path.join(ROOT_PATH, filename), "a", encoding="UTF-8") as file:
                    file.write(start_text)

            try:
                result = func(*args, **kwargs)

                if not filename:
                    print(good_text)
                    print(finish_text)
                else:
                    with open(os.path.join(ROOT_PATH, filename), "a", encoding="UTF-8") as file:
                        file.write(good_text)
                        file.write(finish_text)

                return result

            except Exception as err:
                wrong_text = f"Function {func.__name__} error: {err}. Inputs: {args}, {kwargs}\n"

                if not filename:
                    print(wrong_text)
                else:
                    with open(os.path.join(ROOT_PATH, filename), "a", encoding="UTF-8") as file:
                        file.write(wrong_text)

        return wrapper

    return sub_decor
