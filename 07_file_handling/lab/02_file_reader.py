def file_count(file_name: str) -> int:
    """
    This function opens a file and reads each line as an integer.
    The function then sums all the integers and returns the total count.

    Parameters:
        file_name (str): The name of the file to count the integers in.

    Returns:
        int: The total count of integers in the file.

    Raises:
        FileNotFoundError: If the file cannot be found.
        ValueError: If a line in the file is not an integer.
    """
    # Open the file and read each line as an integer
    with open(file_name, 'r') as current_file:
        total_count = 0
        for line in file:
            try:
                total_count += int(line)
            except ValueError:
                raise ValueError(f"Invalid integer: {line}") from None

    return total_count


file = 'numbers.txt'

print(file_count(file))
