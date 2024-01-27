def get_range_numbers(range_str: str) -> set:
    """
    Converts a range string to a set of numbers.

    Args:
    range_str (str): The range string in the format "start,end".

    Returns:
    set: A set of numbers representing the range.
    """
    start, end = map(int, range_str.split(','))
    return set(range(start, end + 1))


def find_longest_intersection(num_inputs: int) -> tuple:
    """
    Finds the longest intersection among the given number of range inputs.

    Args:
    num_inputs (int): The number of range inputs to process.

    Returns:
    tuple: The longest intersection set and its length.
    """
    longest_intersection = set()

    for _ in range(num_inputs):
        first_range, second_range = input().split('-')
        intersection = get_range_numbers(first_range).intersection(get_range_numbers(second_range))

        if len(intersection) > len(longest_intersection):
            longest_intersection = intersection

    return longest_intersection, len(longest_intersection)


def main():
    """
    Main function to execute the script.
    """
    number_of_inputs = int(input())
    longest_intersection, length = find_longest_intersection(number_of_inputs)

    intersection_str = ', '.join(map(str, longest_intersection))
    print(f"Longest intersection is [{intersection_str}] with length {length}")


if __name__ == "__main__":
    main()
