board_size = int(input())
board = [list(input()) for _ in range(board_size)]

a = [-2, 2, -1, 1]  # Possible moves for the knight
legal_moves = [(x, y) for x in a for y in a if abs(x) + abs(y) == 3]  # Legal moves for the knight

removed_knights = 0

while True:
    max_attacks = 0
    strongest_knight_pos = []  # Knight with the highest number of attacks

    for row in range(board_size):
        for col in range(board_size):

            # Find the knight and counts the number of attacks it can make
            if board[row][col] == 'K':
                attacks = 0

                for pos in legal_moves:
                    row_pos = row + pos[0]
                    col_pos = col + pos[1]

                    if 0 <= row_pos < board_size and 0 <= col_pos < board_size:
                        if board[row_pos][col_pos] == 'K':
                            attacks += 1

                # Check if it is the strongest knight
                if attacks > max_attacks:
                    max_attacks = attacks
                    strongest_knight_pos = [row, col]

    # Remove the strongest knight from the board and add it to the removed_knights variable
    if strongest_knight_pos:
        r, c = strongest_knight_pos
        board[r][c] = '0'
        removed_knights += 1

    # No more attacks for the knights -> end the program
    else:
        break

# Output -> the number of removed knights
print(removed_knights)
