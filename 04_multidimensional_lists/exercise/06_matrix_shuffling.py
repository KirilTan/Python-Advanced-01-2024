def check_indices_valid(indices: list, valid_rows: range, valid_cols: range) -> bool:
    """
    Check if the provided indices are valid within the matrix.

    Args:
        indices (list): List of integers representing row and column indices.
        valid_rows (range): Valid range for row indices.
        valid_cols (range): Valid range for column indices.

    Returns:
        bool: True if indices are valid, False otherwise.
    """
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def swap_elements(command: str, indices: list, matrix: list[list], valid_rows: range, valid_cols: range) -> None:
    """
    Swap two elements in the matrix based on the given indices if the command is valid.

    Args:
        command (str): The command to execute ('swap' or 'END').
        indices (list): The list of indices to swap.
        matrix (list of list): The matrix where the elements will be swapped.
        valid_rows (range): Range representing valid row indices.
        valid_cols (range): Range representing valid column indices.
    """
    if len(indices) == 4 and check_indices_valid(indices, valid_rows, valid_cols) and command == "swap":
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in matrix:
            print(*row)
    else:
        print("Invalid input!")


def main():
    """
    Main function to run the matrix swapping operation.
    """
    rows, cols = map(int, input().split())
    matrix = [input().split() for _ in range(rows)]

    valid_rows = range(rows)
    valid_cols = range(cols)

    while True:
        command_input = input().split()
        command_type = command_input[0]

        if command_type == "END":
            break

        coordinates = [int(x) if x.isdigit() else x for x in command_input[1:]]
        swap_elements(command_type, coordinates, matrix, valid_rows, valid_cols)


if __name__ == '__main__':
    main()
