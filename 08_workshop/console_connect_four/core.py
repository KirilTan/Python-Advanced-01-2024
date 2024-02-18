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
    """
    This function moves the player to the specified column on the tic-tac-toe board.

    Parameters:
        board (List[list[int]]): the tic-tac-toe board
        player (int): the player whose turn it is (1 for X, -1 for O)
        col_to_move (int): the column number (1-based) to move to

    Returns:
        tuple[int, int]: the row and column index of the player's new position on the board

    Raises:
        OutOfBoundsException: if the column number is out of bounds
        ColumnFullException: if the specified column is already occupied by another player
    """
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
    """
    This function prints out the tic-tac-toe board in a readable format.

    Parameters:
        board (List[list[int]]): the tic-tac-toe board to be printed

    Returns:
        None

    """
    for row in range(len(board)):
        print(*board[row], sep=' ')


def check_for_winner(board: List[list[int]]) -> bool:
    pass
