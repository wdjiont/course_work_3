from src.functions import get_executed_operations, sorted_operation, changed_date, operations_with_stars


def test_get_executed_operations():
    assert get_executed_operations([{'state': 'EXECUTED'}, {'state': 'CANCELED'}]) == [{'state': 'EXECUTED'}]


def test_sorted_operation():
    assert sorted_operation([
        {'date': 12},
        {'date': 48},
        {'date': 72},
        {'date': 3},
        {'date': 15},
        {'date': 1},
        {'date': 66},
    ]) == [{'date': 72}, {'date': 66}, {'date': 48}, {'date': 15}, {'date': 12}]


def test_changed_date():
    assert changed_date([{'date': '2019-08-26T10:50:58.294041'}]) == [{'date': '26.08.2019'}]


def test_operations_with_stars():
    assert operations_with_stars([
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880",
            "operationAmount": {
                "amount": "6381.58",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "МИР 5211277418228469",
            "to": "Счет 58518872592028002662"
        }
    ]) == ([
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880",
            "operationAmount": {
                "amount": "6381.58",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "МИР 5211 27** **** 8469",
            "to": "Счет **2662"
        }
    ])