n = int(input())
commands = input().split()

matrix = []
miner_pos = []
collected_coal = 0
total_coal = 0

directions = {
    # Direction : row, column to move
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

# Find miner's position and total coal
for row in range(n):
    matrix.append(input().split())

    if 's' in matrix[row]:
        miner_pos = [row, matrix[row].index('s')]
        matrix[miner_pos[0]][miner_pos[1]] = '*'

    total_coal += matrix[row].count('c')

# Start iteration through all commands
for command in commands:

    # Move miner
    r, c = (miner_pos[0] + directions[command][0],
            miner_pos[1] + directions[command][1])

    # Check if the position is valid
    if not (0 <= r < n and 0 <= c < n):
        continue  # Skip invalid command

    # Move miner to the new position
    miner_pos = [r, c]

    # Miner finds coal
    if matrix[r][c] == 'c':

        collected_coal += 1
        matrix[r][c] = '*'

        # Check if the miner has collected enough coal
        if total_coal == collected_coal:
            print(f'You collected all coal! ({r}, {c})')
            break

    # Miner exits the game
    elif matrix[r][c] == 'e':
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = '*'

else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
