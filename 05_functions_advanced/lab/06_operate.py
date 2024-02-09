from functools import reduce


def operate(operator: str, *args) -> float:
    """
    This function takes in a string operator and a variable number of arguments, and returns the result of the operation.

    Parameters:
        operator (str): The operation to be performed, can be one of the following: "+", "-", "*", "/".
        args (float): The arguments to be operated on.

    Returns:
        float: The result of the operation.

    Raises:
        ValueError: If the operator is not one of the supported operations.

    """
    if operator == "+":
        return reduce(lambda x, y: x + y, args)
    elif operator == "-":
        return reduce(lambda x, y: x - y, args)
    elif operator == "*":
        return reduce(lambda x, y: x * y, args)
    elif operator == "/":
        return reduce(lambda x, y: x / y, args)


print(operate("+", 1, 2, 3))
