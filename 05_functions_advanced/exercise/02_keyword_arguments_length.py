def kwargs_length(**kwargs) -> int:
    """
    Returns the length of a dictionary-like object containing keyword arguments.

    Parameters:
    -----------
    **kwargs: dict-like
        The dictionary-like object to be measured.

    Returns:
    --------
    int:
        The length of the dictionary-like object.

    """
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
