def file_count(file_name: str) -> int or str:
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
    try:
        with open(file_name, 'r') as file:
            total_count = 0

            for line in file:
                try:
                    total_count += int(line)
                except ValueError:
                    print(f'The line "{line}" is not an integer')
            return total_count

    except FileNotFoundError:
        return f'The file "{file_name}" cannot be found'


while True:
    current_file = input('Please write next file\'s name or "Quit" to exit the program: ')
    if current_file == 'Quit':
        break
    print(file_count(current_file))
