direction_mapper = {  # Direction : row, column to move
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
}

n = int(input())

matrix = []
player_pos = []

# Create the matrix
for row in range(n):
    matrix.append(list(input()))

    if 'G' in matrix[row]:  # Player's position
        player_pos = [row, matrix[row].index('G')]
        matrix[player_pos[0]][player_pos[1]] = '-'

player_money = 100  # Initial entering the game bonus
jackpot_won = False

command = input()
while not jackpot_won:

    # Check if the player's money is negative. If so, terminate the game.
    if player_money < 0:
        print('Game over! You lost everything!')
        exit()

    if command == 'end':
        break

    # Take command from the user
    direction = command

    # Calculate new player position
    r, c = (
        player_pos[0] + direction_mapper[direction][0],
        player_pos[1] + direction_mapper[direction][1]
    )

    # Check if his position is within the matrix's boundaries and if his winning are positive.
    # If either is not, terminate the game.
    if not (0 <= r < n and 0 <= c < n):
        print('Game over! You lost everything!')
        exit()

    # Move the player to the new position
    player_pos = [r, c]

    # Check if something is collected
    if matrix[r][c] == 'W':  # Add 100 to player_money
        player_money += 100

    elif matrix[r][c] == 'P':  # Subtract 200 from player_money
        player_money -= 200

    elif matrix[r][c] == 'J':  # Add 100_000 to player_money
        player_money += 100_000
        jackpot_won = True

    matrix[r][c] = '-'

    command = input()

# Update matrix to include the player's position
matrix[player_pos[0]][player_pos[1]] = 'G'

# Output

if jackpot_won:  # If player wins the Jackpot
    print('You win the Jackpot!')

print(f'End of the game. '  # Collected money
      f'Total amount: {player_money}$')

for row in matrix:  # Print the matrix
    print(''.join(row))
