def sorting_cheeses(**kwargs: dict) -> str:
    """
    This function sorts a list of cheeses by their name and quantity in descending order.

    Parameters:
    -----------
    **kwargs: dict
        A dictionary containing the cheese names as keys and their quantities as values.

    Returns:
    --------
    str:
        A string containing the sorted cheese names and their quantities.

    """
    result = ""
    sorted_result = sorted(
        kwargs.items(),
        key=lambda kvp: (-len(kvp[1]), kvp[0])
    )
    for cheese_name, quantities in sorted_result:
        result += cheese_name + "\n"
        for quantity in sorted(quantities, reverse=True):
            result += f"{quantity}\n"
    return result
