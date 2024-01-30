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


def abs_diagonal_difference(matrix: list) -> int:
    """
    Returns the absolute difference between the primary and secondary diagonals of a square matrix.
    The primary diagonal starts at (0:0) and ends at (n:n) where n is the length of the matrix.
    The secondary diagonal starts at (0;-n) and ends at (0:n) where n is the length of the matrix.

    Parameters:
        matrix (list): A list of lists representing a square matrix.
    Returns:
        int: The absolute difference between the primary and secondary diagonals of the square matrix.
    """

    sum_primary_diagonal = sum(get_primary_diagonal(matrix))
    sum_secondary_diagonal = sum(get_secondary_diagonal(matrix))
    abs_difference = abs(sum_primary_diagonal - sum_secondary_diagonal)

    return abs_difference


def main():
    """
    Main function.

    """
    input_matrix = [[int(num) for num in input().split()] for _ in range(int(input()))]

    abs_difference = abs_diagonal_difference(input_matrix)
    print(abs_difference)


if __name__ == '__main__':
    main()
