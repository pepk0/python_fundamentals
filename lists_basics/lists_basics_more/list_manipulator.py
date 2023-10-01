def exchange(index: int, list_arg: list):
    if 0 <= index < len(list_arg):
        fist_half = list_arg[:index + 1]
        second_haf = list_arg[index + 1:]
        return second_haf + fist_half
    return False


def max_number(condition, list_arg: list):
    last_index = None
    compare = -float("inf")
    for index in range(len(list_arg)):
        if condition(list_arg[index]) and list_arg[index] >= compare:
            compare = list_arg[index]
            last_index = index
    if last_index != None:
        return last_index
    return -1


def min_number(condition, list_arg: list):
    last_index = None
    compare = float("inf")
    for index in range(len(list_arg)):
        if condition(list_arg[index]) and list_arg[index] <= compare:
            compare = list_arg[index]
            last_index = index
    if last_index != None:
        return last_index
    return -1


def number_elements(condition, key: str, count: int, list_arg: list):
    result = []
    if count > len(list_arg):
        return -1
    elif key == "first":
        for index in range(len(list_arg)):
            if len(result) == count:
                return result
            elif condition(list_arg[index]):
                result.append(list_arg[index])
        return result
    elif key == "last":
        for index in range(len(list_arg) - 1, -1, -1):
            if len(result) == count:
                return result
            elif condition(list_arg[index]):
                result.insert(0, list_arg[index])
        return result


original_list = [int(i) for i in input().split()]
option = {"even": lambda x: x % 2 == 0, "odd": lambda x: x % 2 != 0}

while True:

    user_command = input()
    if user_command == "end":
        break

    to_print = None
    command, *conditions = user_command.split()

    if command == "exchange":
        index = int(conditions[0])
        result = exchange(index, original_list)
        if result:
            original_list = result
        else:
            to_print = "Invalid index"

    elif command == "max":
        condition = option[conditions[0]]
        result = max_number(condition, original_list)
        if result == -1:
            to_print = "No matches"
        else:
            to_print = result

    elif command == "min":
        condition = option[conditions[0]]
        result = min_number(condition, original_list)
        if result == -1:
            to_print = "No matches"
        else:
            to_print = result

    elif command == "first" or command == "last":
        count = int(conditions[0])
        condition = option[conditions[1]]
        result = number_elements(condition, command, count, original_list)
        if result == -1:
            to_print = "Invalid count"
        else:
            to_print = result

    if to_print != None:
        print(to_print)

print(original_list)
