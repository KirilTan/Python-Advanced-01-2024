from typing import List


def positive_vs_negative(numbers: List[int]) -> list:
    """
    This function takes a list of integers as input and returns a list of two elements.

    The first element is the sum of all positive integers in the input list
    and the second element is the sum of all negative integers in the input list.

    The function also adds a string to the output list indicating whether the sum of positive integers
    is greater than or less than the sum of negative integers.

    Parameters:
    numbers (List[int]): A list of integers.

    Returns:
    list: A list containing two elements.
    The first element is the sum of all positive integers in the input list.
    The second element is the sum of all negative integers in the input list.
    The function also adds a string to the output list indicating whether
    the sum of positive integers is greater than or less than the sum of negative integers.

    """
    positive_numbers_sum = sum(number for number in numbers if number > 0)
    negative_numbers_sum = sum(number for number in numbers if number < 0)

    return_list = [negative_numbers_sum, positive_numbers_sum]

    if positive_numbers_sum > abs(negative_numbers_sum):
        return_list.append('The positives are stronger than the negatives')
    else:
        return_list.append('The negatives are stronger than the positives')

    return return_list


input_numbers = [int(x) for x in input().split()]
output_string = positive_vs_negative(input_numbers)
print(*output_string, sep='\n')
