direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

n = int(input())
matrix = []
player_pos = []

# Initialize game settings
starting_armour = 300
total_enemies = 0

# Create the matrix and count game elements
for row in range(n):
    row_data = list(input())
    matrix.append(row_data)
    if 'J' in row_data:
        player_pos = [row, row_data.index('J')]
        matrix[player_pos[0]][player_pos[1]] = '-'
    total_enemies += row_data.count('E')

remaining_armour = starting_armour
mission_accomplished = False
shot_down = False

while not (shot_down or mission_accomplished):
    command = input()
    new_r, new_c = player_pos[0] + direction_mapper[command][0], player_pos[1] + direction_mapper[command][1]

    if 0 <= new_r < n and 0 <= new_c < n:  # Check if new position is within the matrix
        player_pos = [new_r, new_c]  # Move the player
        cell = matrix[new_r][new_c]

        if cell == 'E':
            remaining_armour -= 100
            total_enemies -= 1
            if total_enemies == 0:
                mission_accomplished = True
        elif cell == 'R':
            remaining_armour = min(remaining_armour + 300, starting_armour)  # Repair, but do not exceed starting armour

        if remaining_armour <= 0:
            shot_down = True

        matrix[new_r][new_c] = '-'  # Clear the cell after moving or encountering an item


if mission_accomplished and not shot_down:
    print("Mission accomplished, you neutralized the aerial threat!")
else:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{player_pos[0]}, {player_pos[1]}]!")

# Place the player back for final matrix display
matrix[player_pos[0]][player_pos[1]] = 'J'
for row in matrix:
    print(''.join(row))
