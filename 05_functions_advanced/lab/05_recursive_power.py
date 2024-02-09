def recursive_power(number: float, power: int) -> float:
    """
    This function calculates the recursive power of a number.

    Parameters:
    number (float): The base number.
    power (int): The exponent.

    Returns:
    float: The result of the recursive power calculation.

    Raises:
    ValueError: If the power is less than 0.

    Examples:
    >>> recursive_power(2, 3)
    8.0
    >>> recursive_power(2, 0)
    1.0
    >>> recursive_power(2, -1)
    Traceback (most recent call last):
        ...
    ValueError: The power must be greater than or equal to 0.
    """
    if power < 0:
        raise ValueError("The power must be greater than or equal to 0.")
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)


print(recursive_power(2, 3))
