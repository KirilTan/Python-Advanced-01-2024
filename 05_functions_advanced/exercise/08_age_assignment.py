def age_assignment(*names, **age_data) -> str:
    """
    This function takes a variable number of names and a dictionary of age data, where the keys of the dictionary are the letters of the alphabet and the values are the ages of the people with those initials. It then loops through the names and the age data, checking if each name starts with a given letter. If it does, it adds a message to the result list indicating the name and age. The result list is then sorted and returned as a string with newlines between the messages.

    Parameters:
        names: A list of names to check.
        age_data: A dictionary where the keys are letters of the alphabet and the values are ages.

    Returns:
        str: A string containing the names and ages of the people who have initials that match the given letters.

    """
    result = []

    for letter, age in age_data.items():
        for name in names:
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")
                break

    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
