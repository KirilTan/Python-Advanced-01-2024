from typing import List

# Constants
ROWS = 6
COLS = 7
MAXIMUM_CONNECTIONS = 4

DIRECTION_MAPPER = {
    "left": (0, -1),
    "up": (-1, 0),
    "main_diagonal": (-1, -1),
    "other_diagonal": (-1, 1),
}


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


def travel_direction(coordinates: tuple, current_row: int, current_col: int, element: int, sign: str, board: List[List[int]]) -> int:
    """
    This function counts the number of elements in a given direction from a given position on the board.

    Parameters:
        coordinates (tuple): a tuple containing the row and column directions
        current_row (int): the row index of the current position
        current_col (int): the column index of the current position
        element (int): the element to be counted
        sign (str): the sign to be used in the arithmetic expressions
        board (List[List[int]]): the tic-tac-toe board

    Returns:
        int: the number of elements in the given direction from the given position

    Raises:
        IndexError: if the row or column index is out of bounds
    """
    row_direction, col_direction = coordinates

    count = 0
    for i in range(1, MAXIMUM_CONNECTIONS):
        next_element_row_index = eval(f"{current_row} {sign} {row_direction} * {i}")
        next_element_col_index = eval(f"{current_col} {sign} {col_direction} * {i}")

        try:
            if board[next_element_row_index][next_element_col_index] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count
    return count


def is_winner(current_row_index: int, current_col_index: int, board: List[List[int]]) -> bool:
    """
    This function checks if the player with the given sign has won the game.

    Parameters:
        current_row_index (int): the row index of the current position
        current_col_index (int): the column index of the current position
        board (List[List[int]]): the tic-tac-toe board

    Returns:
        bool: True if the player with the given sign has won, False otherwise

    """
    for direction, coordinates in DIRECTION_MAPPER.items():
        searched_element = board[current_row_index][current_col_index]
        travel_direction_count = travel_direction(
            coordinates, current_row_index, current_col_index, searched_element, "+", board
        )
        travel_opposite_direction_count = travel_direction(
            coordinates, current_row_index, current_col_index, searched_element, "-", board
        )

        if travel_direction_count + travel_opposite_direction_count + 1 >= MAXIMUM_CONNECTIONS:
            return True
    else:
        return False


def is_board_full(turns: int) -> bool:
    """
    This function checks if the board is full.

    Parameters:
        turns (int): the number of turns played so far

    Returns:
        bool: True if the board is full, False otherwise
    """
    return ROWS * COLS <= turns
