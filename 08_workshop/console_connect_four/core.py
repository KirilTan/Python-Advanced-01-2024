from typing import List

class OutOfBoundsException(Exception):
    pass


class ColumnFullException(Exception):
    pass


def make_board(rows: int, cols: int) -> List[list[int]]:
    """
    This function creates a 2D list of size rows x cols, where each element is initialized to 0.

    Args:
        rows (int): the number of rows in the board
        cols (int): the number of columns in the board

    Returns:
        List[list[int]]: a 2D list of size rows x cols, where each element is initialized to 0
    """
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    return matrix


def move_player(board: List[list[int]], player: int, col_to_move: int) -> tuple[int, int]:

    board_rows, board_cols = len(board), len(board[0])

    col_index_to_move = col_to_move - 1
    row_index_to_move = board_rows - 1

    # Check if column is out of bounds
    if col_to_move <= 0 or col_to_move > board_rows + 1:
        raise OutOfBoundsException

    # Check if column is already full
    if board[0][col_index_to_move] != 0:
        raise ColumnFullException

    while True:
        if board[row_index_to_move][col_index_to_move] == 0:
            return row_index_to_move, col_index_to_move
        row_index_to_move -= 1


def display_board(board: List[list[int]]) -> None:
    for row in range(len(board)):
        print(*board[row], sep=' ')




