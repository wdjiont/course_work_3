from functions import load_operation, get_executed_operations, sorted_operation, operations_with_stars

file = "operations.json"
open_file = load_operation(file)
executed_opr = get_executed_operations(open_file)
sorted_five_opr = sorted_operation(executed_opr)
finished_opr = operations_with_stars(sorted_five_opr)


def main():
    for operation in finished_opr:
        if operation.get('from') is not None:
            print(f"""{operation['date']} {operation['description']}
{operation['from']} -> {operation['to']}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']} \n""")
        else:
            print(f"""{operation['date']} {operation['description']}
{operation['to']}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']} \n""")


if __name__ == '__main__':
    main()
