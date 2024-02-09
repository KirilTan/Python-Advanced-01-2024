def even_odd(*args):
    """
    This function takes in a variable number of arguments and returns a list of even or odd numbers based on the last argument passed.

    Parameters:
    args (list): A list of numbers

    Returns:
    list: A list of even or odd numbers based on the last argument passed

    """
    command = args[-1]

    if command == 'even':
        return [num for num in args[:-1] if num % 2 == 0]
    elif command == 'odd':
        return [num for num in args[:-1] if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
