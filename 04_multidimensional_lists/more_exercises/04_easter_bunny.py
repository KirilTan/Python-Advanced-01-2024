field_size = int(input())


field = []
bunny_pos = []
best_path = []

best_direction = None
max_collected_eggs = float('-inf')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Find the bunny's position
for row in range(field_size):
    field.append(input().split())

    if 'B' in field[row]:
        bunny_pos = [row, field[row].index('B')]

# Go over every possible direction
for direction, position in directions.items():
    # New position
    row, col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]
    ]

    path = []  # Current way
    collected_eggs = 0  # Current collected eggs

    # Check if the bunny is in the field in the given direction and if he is not on a trap
    while 0 <= row < field_size and 0 <= col < field_size and field[row][col] != 'X':

        collected_eggs += int(field[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    # Check if collected eggs is higher than max collected eggs
    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_path = path
        best_direction = direction

print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)
