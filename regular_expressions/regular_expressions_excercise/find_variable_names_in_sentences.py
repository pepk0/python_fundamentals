import re


def extract_variable_names(text: str) -> list:
    pattern = r"\b(_){1}([A-Za-z0-9]+)\b"
    matches = re.findall(pattern, text)
    return [var_name[1] for var_name in matches]


input_text = input()
print(*extract_variable_names(input_text), sep=",")
