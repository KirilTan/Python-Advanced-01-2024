def biggest_sum_3x3(rows: int, columns: int, matrix: list) -> int and list:
    """
    This function takes a 2D list of integers as input and returns the largest sum of any 3x3 sub-matrix in the list.

    Parameters:
    -----------
    rows: int
        The number of rows in the 2D list.
    columns: int
        The number of columns in the 2D list.
    matrix: list
        A 2D list of integers.

    Returns:
    --------
    biggest_matrix_sum: int
        The largest sum of any 3x3 sub-matrix in the list.
    biggest_matrix: list
        A list containing the 3x3 sub-matrix with the largest sum.

    """
    biggest_matrix = []
    biggest_matrix_sum = float("-inf")

    for row in range(rows - 2):
        for col in range(columns - 2):
            first_row = matrix[row][col:col + 3]
            second_row = matrix[row + 1][col:col + 3]
            third_row = matrix[row + 2][col:col + 3]

            current_sum = sum(first_row) + sum(second_row) + sum(third_row)

            if current_sum > biggest_matrix_sum:
                biggest_matrix_sum = current_sum
                biggest_matrix = [first_row, second_row, third_row]

    return biggest_matrix_sum, biggest_matrix


def main():
    """
    This function is the main function of the code. It takes input from the user and calls the 
    biggest_sum_3x3 function to find the largest sum of any 3x3 sub-matrix in the list.

    """
    rows, columns = [int(num) for num in input().split()]
    matrix = [[int(num) for num in input().split()] for _ in range(rows)]

    biggest_matrix_sum, biggest_matrix = biggest_sum_3x3(rows, columns, matrix)
    print('Sum =', biggest_matrix_sum)
    [print(*row) for row in biggest_matrix]


if __name__ == '__main__':
    main()
