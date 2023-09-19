from src import functions
import os


def test_get_data_operations():
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_FOR_TEST_PATH = os.path.join(CURRENT_DIR, 'data_for_test.json')
    assert functions.get_data_operations(DATA_FOR_TEST_PATH) == [1, 2, 3]


def test_get_executed_operations():
    CURRENT_DIR = os.path.dirname(__file__)
    OPERATION_FOR_TEST_PATH = os.path.join(CURRENT_DIR, 'operation_for_test.json')
    list_of_dict = functions.get_data_operations(OPERATION_FOR_TEST_PATH)
    assert len(functions.get_executed_operations(list_of_dict)) == 1
    # assert functions.get_executed_operations(list_of_dict['state']) == "EXECUTED"


def test_sorted_by_date():
    date_list = [{'date': '2018-07-11T02:26:18.671407'},
                 {'date': '2019-08-26T10:50:58.294041'},
                 {'date': '2019-07-03T18:35:29.512364'},
                 {'date': '2018-04-04T17:33:34.701093'},
                 {'date': '2018-12-28T23:10:35.459698'},
                 {'date': '2019-01-15T17:58:27.064377'},
                 ]
    assert functions.sorted_by_date(date_list) == [
        {'date': '2019-08-26T10:50:58.294041'},
        {'date': '2019-07-03T18:35:29.512364'},
        {'date': '2019-01-15T17:58:27.064377'},
        {'date': '2018-12-28T23:10:35.459698'},
        {'date': '2018-07-11T02:26:18.671407'},
    ]


def test_get_formated_date():
    assert functions.get_formated_date("2019-08-26T10:50:58.294041") == '26.08.2019'
    assert functions.get_formated_date("2019-04-04T23:20:05.206878") == '04.04.2019'


def test_get_masking_number():
    assert functions.get_masking_number("41421565395219882431") == '**2431'
    assert functions.get_masking_number("7158300734726758") == '7158 30** **** 6758'

def test_get_output_data():
    CURRENT_DIR = os.path.dirname(__file__)
    OPERATION_FOR_TEST_PATH = os.path.join(CURRENT_DIR, 'operation_for_test.json')
    list_of_dict = functions.get_data_operations(OPERATION_FOR_TEST_PATH)
    sorted_operations = functions.sorted_by_date(functions.get_executed_operations(list_of_dict))
    for operation in sorted_operations:
        pass
    assert functions.get_output_data(operation) == '03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD\n'

