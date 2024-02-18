import core

# Import the needed constants
ROWS = core.ROWS
COLS = core.COLS

# Make the playing board
board = core.make_board(rows=ROWS, cols=COLS)

# Playing the game
turns = 1
while True:
    player_to_move = 2 if turns % 2 == 0 else 1

    # User input
    try:
        column = int(input(f'Player {player_to_move} please choose a column to place your piece on: '))
    except ValueError:  # Check if the user entered a number
        print(f'Please enter a number between 1 and {COLS}')
        continue

    # Get placed piece's coordinates
    try:
        r, c = core.move_player(board=board, player=player_to_move, col_to_move=column)
    except core.OutOfBoundsException:  # Check if the user entered a number that is out of bounds
        print(f'Please enter a number between 1 and {COLS}')
        continue
    except core.ColumnFullException:  # Check if the column selected by the user is already full
        print(f'Column {column} is already full')
        continue

    # Update the board
    board[r][c] = player_to_move

    # Display the board
    core.display_board(board=board)

    # Check for a winner
    if core.is_winner(current_row_index=r, current_col_index=c, board=board):
        print()
        core.display_board(board=board)
        print(f'Player {player_to_move} wins!')
        exit()

    # Check if the board is full
    if core.is_board_full(turns=turns):
        core.display_board(board=board)
        print(f'The board is full!')
        exit()

    turns += 1

