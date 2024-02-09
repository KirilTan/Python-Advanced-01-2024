def concatenate(*words, **kwargs) -> str:
    """
    This function concatenates a variable number of words together
    and replaces any keyword arguments in the text with their corresponding values.

    Parameters:
        words: a variable number of strings to be concatenated
        kwargs: a dictionary of keyword arguments to be replaced in the text

    Returns:
        The concatenated and processed text

    """
    text = ''.join(words)

    for key, value in kwargs.items():
        text = text.replace(key, value)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
