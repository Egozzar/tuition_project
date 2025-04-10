import os

from constants import ROOT_PATH
from src.decorators import log


def test_log_console_good(capsys):
    @log()
    def division(a, b):
        return a / b

    division(10, 2)
    captured = capsys.readouterr()
    assert captured.out[-55:-29] == "Function division finished"


def test_log_console_wrong(capsys):
    @log()
    def division(a, b):
        return a / b

    division(10, 0)
    captured = capsys.readouterr()
    assert captured.out[-64:-41] == "Function division error"


def test_log_file_good():
    @log("test_log.log")
    def division(a, b):
        return a / b

    division(10, 2)
    test_path = os.path.join(ROOT_PATH, "test_log.log")
    assert os.path.exists(test_path)

    with open(test_path, encoding="UTF-8") as file:
        assert file.read()[-54:-28] == "Function division finished"


def test_log_file_wrong():
    @log("test_log2.log")
    def division(a, b):
        return a / b

    division(10, 0)
    test_path = os.path.join(ROOT_PATH, "test_log2.log")
    assert os.path.exists(test_path)

    with open(test_path, encoding="UTF-8") as file:
        assert file.read()[-63:-40] == "Function division error"
