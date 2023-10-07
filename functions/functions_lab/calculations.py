def get_func(operation: str):
    operations = {
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: int(x / y),
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
    }
    return operations[operation]


input_operation = input()
first_num = int(input())
second_num = int(input())

operation = get_func(input_operation)
result = operation(first_num, second_num)
print(result)
