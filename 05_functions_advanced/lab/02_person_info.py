def get_info(name: str, town: str, age: int) -> str:
    """
    This function returns a string with the information about a person.

    Parameters:
        name (str): The name of the person.
        town (str): The town where the person is from.
        age (int): The age of the person.

    Returns:
        str: A string with the information about the person.

    """
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(name="George", town="Sofia", age=20))


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
