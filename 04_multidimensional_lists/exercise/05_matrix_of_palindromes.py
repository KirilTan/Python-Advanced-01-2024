def print_matrix_pattern(rows: int, columns: int):
    """
    Prints a matrix palindrome pattern based on the given rows and columns.

    Each element in the matrix is composed of three characters.
    The first and third characters are the same and based on the row index,
    while the middle character is based on the column index.

    Args:
    rows (int): The number of rows in the matrix.
    columns (int): The number of columns in the matrix.
    """
    start_char = ord('a')  # ASCII value for 'a'

    for row in range(rows):
        for col in range(columns):
            # Generate each character based on the row and column indices
            first_and_third_char = chr(start_char + row)
            middle_char = chr(start_char + row + col)
            print(first_and_third_char + middle_char + first_and_third_char, end=" ")
        print()  # Newline after each row


def main():
    rows, columns = [int(num) for num in input().split()]
    print_matrix_pattern(rows, columns)


if __name__ == '__main__':
    main()
