direction_mapper = {  # Direction : row, column to move
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Variables
matrix = []
player_pos = []
qty_needed = 20  # Tons of fish needed
qty_collected = 0  # Tons of fish collected

# Create the matrix
n = int(input())
for row in range(n):

    matrix.append(list(input()))

    if 'S' in matrix[row]:  # Player's position
        player_pos = [row, matrix[row].index('S')]
        matrix[player_pos[0]][player_pos[1]] = '-'

# Take commands from the user
ship_destroyed = False

command = input()
while command != 'collect the nets':

    # Move the player
    r, c = (
        player_pos[0] + direction_mapper[command][0],
        player_pos[1] + direction_mapper[command][1]
    )

    # Check if the position is valid. If it is not, move the player to the opposite side of the one he was on
    if r < 0:
        r = n - 1  # Move player to the bottom row
    elif r >= n:
        r = 0  # Move player to the top row
    if c < 0:
        c = n - 1  # Move player to the rightmost column
    elif c >= n:
        c = 0  # Move player to the leftmost column

    # Move the player to the new position
    player_pos = [r, c]

    # Player finds fish
    if matrix[r][c].isnumeric():
        qty_collected += int(matrix[r][c])
        matrix[r][c] = '-'
    # Player goes in a whirlpool
    elif matrix[r][c] == 'W':
        ship_destroyed = True
        break

    command = input()

if ship_destroyed:
    r, c = player_pos[0], player_pos[1]
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
          f"Last coordinates of the ship: [{r},{c}]")
elif qty_collected >= qty_needed:
    print('Success! You managed to reach the quota!')
elif qty_collected < qty_needed:
    lack_of_fish = qty_needed - qty_collected
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {lack_of_fish} tons of fish more.")

if not ship_destroyed and qty_collected > 0:
    print(f"Amount of fish caught: {qty_collected} tons.")

if not ship_destroyed:
    # Put the player back in the matrix
    matrix[player_pos[0]][player_pos[1]] = 'S'
    for row in matrix:
        print(''.join(row))
