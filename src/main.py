from functions import get_data_operations, get_executed_operations, sorted_by_date, get_output_data

FILE_NAME = 'operations.json' #константа базы данных
CONTENT = get_data_operations(FILE_NAME) #константа отформатированной базы данных

filter_operations = get_executed_operations(CONTENT) #получение отфильтрованной базы по статусу "ВЫПОЛНЕНО"
sorted_operations = sorted_by_date(filter_operations, 5) #сортировка операций по дате, вывод требуемого кол-ва операций (по умолчанию, 5)

for operation in sorted_operations:
    print(get_output_data(operation)) #вывод последних выполненных операций в требуемом формате
