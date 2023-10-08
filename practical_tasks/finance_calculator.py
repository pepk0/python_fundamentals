def get_num(prompt: str, scope=None) -> float | int:
    """"loops until a valid int or float are given, 
    space controls the range of the number"""
    while True:
        try:
            number = float(input(prompt))
            if number.is_integer():  # type: ignore
                number = int(number)
            if scope:
                if number not in scope:
                    raise ValueError
            return number
        except ValueError:
            print("Invalid number")


def calc_simple_interest() -> str:
    principal_amount = get_num("Enter principal amount: ")
    interest_rate = get_num("Enter annual interest rate %: ", range(1, 101))
    time = get_num("Enter time (in years): ")
    interest_rate /= 100
    result = principal_amount * (1 + interest_rate * time)
    result -= principal_amount
    return f"Simple interest ${result:.1f}"


def calc_compound_interest() -> str:
    principal_amount = get_num("Enter principal amount: ")
    interest_rate = get_num("Enter annual interest rate %: ", range(1, 101))
    time = get_num("Enter time (in years): ")
    compound_per_year = get_num(
        "Enter the number of times interest is compounded per year: ",
        range(1, 13))
    interest_rate /= 100
    result = (principal_amount * (1 + (interest_rate / compound_per_year))
              ** (compound_per_year * time))
    result -= principal_amount
    return f"Compound Interest: ${result:.1f}"


def calc_loan_payment() -> str:
    loan_amount = get_num("Enter loan amount: ")
    interest_rate = get_num("Enter interest rate %: ")
    number_mounts = get_num("Enter number mounts: ")
    interest_rate /= 100