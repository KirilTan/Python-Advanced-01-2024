def even_odd_filter(**numbers_sets):
    """
    This function takes in a variable number of keyword arguments, where each keyword argument is a set of numbers.
    The function then filters out all the even numbers from the 'odd' set and all the odd numbers from the 'even' set,
    and returns a dictionary with the filtered sets as keys and the filtered numbers as values. The dictionary is sorted
    in descending order based on the length of the value list.

    Parameters:
        numbers_sets: a dictionary with keys 'odd' and 'even', each containing a list of numbers

    Returns:
        dict: a dictionary with filtered sets as keys and filtered numbers as values
    """
    if 'odd' in numbers_sets.keys():
        numbers_sets['odd'] = [x for x in numbers_sets['odd'] if x % 2 != 0]
    if 'even' in numbers_sets.keys():
        numbers_sets['even'] = [x for x in numbers_sets['even'] if x % 2 == 0]

    return dict(sorted(numbers_sets.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
