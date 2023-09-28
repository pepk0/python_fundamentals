# Function to perform linear search
def linear_search(input_list: list, target: int) -> int:
    """preforms a linear search, returns index if found, -1 else"""
    index = -1
    for i in range(len(input_list)):
        if input_list[i] == target:
            return i
    return index


my_list = [1, 3, 5, 7, 9, 11]
target = 7
result = linear_search(my_list, target)
if result != -1:
    print(f"The target element {target} is at index {result}.")
else:
    print(f"The target element {target} was not found in the list.")
