def get_primary_diagonal(matrix: list) -> list:
    """
    Returns the primary diagonal of a square matrix.
    The primary diagonal starts at (0:0) and ends at (n:n) where n is the length of the matrix.

    Parameters:
        matrix (list): A list of lists representing a square matrix.

    Returns:
        list: The primary diagonal of the square matrix.

    """
    return [matrix[index][index] for index in range(len(matrix))]


def get_secondary_diagonal(matrix: list) -> list:
    """
    Returns the secondary diagonal of a square matrix as a list.
    The secondary diagonal starts at (0;-n) and ends at (0:n) where n is the length of the matrix.

    Parameters:
        matrix (list): A list of lists representing a square matrix.

    Returns:
        list: The secondary diagonal of the square matrix.

    """
    return [matrix[index][-index - 1] for index in range(len(matrix))]


def main():
    """
    Main function.

    """
    input_matrix = [[int(num) for num in input().split(', ')] for _ in range(int(input()))]

    primary_diagonal = get_primary_diagonal(input_matrix)
    sum_primary_diagonal = sum(primary_diagonal)

    secondary_diagonal = get_secondary_diagonal(input_matrix)
    sum_secondary_diagonal = sum(secondary_diagonal)

    print(f'Primary diagonal: {(", ".join(str(num) for num in primary_diagonal))}. Sum: {sum_primary_diagonal}')
    print(f'Secondary diagonal: {(", ".join(str(num) for num in secondary_diagonal))}. Sum: {sum_secondary_diagonal}')


if __name__ == '__main__':
    main()
