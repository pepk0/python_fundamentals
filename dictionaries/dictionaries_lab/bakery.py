def make_dict(str_lit: list) -> dict:
    return {str_lit[i]: int(str_lit[i + 1]) for i in range(0, len(str_lit), 2)}


print(make_dict(input().split()))
