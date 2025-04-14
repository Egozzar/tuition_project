from src.counters import counter_operations


def test_counter_operations(list_transactions, dict_result_counter):
    list_categories = [elem["description"] for elem in list_transactions]
    assert counter_operations(list_transactions, list_categories) == dict_result_counter


def test_counter_operations_empty():
    assert counter_operations([], []) == {}


def test_counter_operations_no_args():
    assert counter_operations() == {}
