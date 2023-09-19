import json
import datetime

def get_data_operations(file_name):
    """
    Конвертирует список операций из файла json в словарь Python.
    :param file_name: Файл.json со всеми операциями.
    :return: Cловарь Python со всеми операциями.
    """
    with open(file_name, encoding='utf-8') as file:
        operations_list = json.load(file)
    return operations_list

def get_executed_operations(list_of_dicts):
    """
    Фильтрует операции по статусу выполнения.
    :param list_of_dicts: Список словарей операций.
    :return: Список выполненных операций.
    """
    filtered_list = []
    for operation in list_of_dicts:
        if operation.get("state") == "EXECUTED":
            filtered_list.append(operation)
    return filtered_list

def sorted_by_date(prepared_list, count=5):
    """
    Сортирует операции по дате: от новых к старым.
    :param prepared_list: Подготовленный список выполненных операций.
    :param count: Количество последних операций.
    :return: Отсортированный список заданного количества операций от новых к старым.
    """
    sorted_list_operations = sorted(prepared_list, key=lambda x: x['date'], reverse=True)
    last_count_operations = sorted_list_operations[:count]
    return last_count_operations

def get_formated_date(date): #TEST
    """
    Обрабатывает дату в требуемый формат.
    :param date: Ожидаемый ключ поиска в словаре.
    :return: Нужный формат даты операции.
    """
    current_date = datetime.datetime.fromisoformat(date)
    formated_date = current_date.strftime("%d.%m.%Y")
    return formated_date

def get_masking_number(number): #TEST
    """
    Маскирует номер карты/счёта.
    :param number: Номер на входе.
    :return: Номер на выходе с маской.
    """
    if len(number) == 16:
        return f'{number[:4]} {number[4:6]}** **** {number[-4:]}' #для карты
    else:
        return f'**{number[-4:]}' #для счёта

def transfer_transaction(operation):
    """
    Предоставляет информацию о пути транзакции.
    Использует функцию маскировки счёта (get_masking_number(number)).
    :param operation: Строка (имя номер).
    :return: Данные о транзакции в требуемом формате.
    """
    if operation:
        operation_in_list = operation.split(' ')
        except_the_last_one = " ".join(operation_in_list[:-1])
        number = operation_in_list[-1]
        maska = get_masking_number(number)
        return f'{except_the_last_one} {maska}'
    else:
        return 'Нет данных'

def get_output_data(operation):
    """
    Обрабатывает исходный список данных.
    Формирует вывод информации в запрошенном виде.
    :param operation: Список словарей операций.
    :return: Трёхстрочный резюмирующий вывод.
    """
    operation_date = get_formated_date(operation['date'])
    operation_description = operation['description']
    transfer_from = transfer_transaction(operation.get('from'))
    transfer_to = transfer_transaction(operation.get('to'))
    operation_amount = operation['operationAmount']['amount']
    operation_currency_name = operation['operationAmount']['currency']['name']

    return (f'{operation_date} {operation_description}\n'
            f'{transfer_from} -> {transfer_to}\n'
            f'{operation_amount} {operation_currency_name}\n')
