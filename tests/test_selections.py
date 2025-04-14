from src.selections import selection_by_exp


def test_selection_by_exp(list_transactions, list_transactions_in_card):
    assert selection_by_exp(list_transactions, "с карты на карту") == list_transactions_in_card


def test_selection_by_exp_no_descriptions(list_transactions_no_descriptions):
    assert selection_by_exp(list_transactions_no_descriptions, "на карту") == []


def test_selection_by_exp_no_expression(list_transactions):
    assert selection_by_exp(list_transactions) == list_transactions


def test_selection_by_exp_empty():
    assert selection_by_exp([]) == []
