def move(direction: str, steps: int) -> list:
    """
    Moves the player in the specified direction by the specified number of steps.

    Parameters
    ----------
    direction : str
        The direction in which to move, must be one of 'up', 'down', 'left', or 'right'.
    steps : int
        The number of steps to move in the specified direction.

    Returns
    -------
    list
        The new position of the player after moving. If the player attempts to move outside the board,
        their original position is returned.

    """
    r = player_pos[0] + (directions[direction][0] * steps)
    c = player_pos[1] + (directions[direction][1] * steps)

    # Check if the new player coordinates are valid.
    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return player_pos
    if field[r][c] == 'x':
        return player_pos

    # Valid coordinates -> return new coordinates
    return [r, c]


def shoot(direction: str) -> list:
    """
    Shoots the player in the specified direction.

    Parameters
    ----------
    direction : str
        The direction in which to shoot, must be one of 'up', 'down', 'left', or 'right'.

    Returns
    -------
    list
        The coordinates of the target that was hit, or None if no target was hit.

    """
    r = player_pos[0] + directions[direction][0]
    c = player_pos[1] + directions[direction][1]

    # Check if the player hits a target
    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5
field = []

total_targets = 0
targets_hit = 0
targets_hit_coord = []

player_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

# Create the field
for row in range(SIZE):
    field.append(input().split())

    # Find the player's position
    if 'A' in field[row]:
        player_pos = [row, field[row].index('A')]

    # Count the number of targets on the row and add them to the total
    total_targets += field[row].count('x')

# Iterate through the commands and execute them
for _ in range(int(input())):
    command_info = input().split()  # Take the command, e.g "move right 4", "shoot down"

    if command_info[0] == 'move':
        player_pos = move(command_info[1], int(command_info[2]))
    elif command_info[0] == 'shoot':
        current_target_hit_coord = shoot(command_info[1])

        # A target is hit -> add it to the list of targets that were hit
        if current_target_hit_coord:
            targets_hit_coord.append(current_target_hit_coord)
            targets_hit += 1

        # Check if all targets have been hit
        if targets_hit == total_targets:
            print(f'Training completed! All {total_targets} targets hit.')
            break

# Output the results
if targets_hit < total_targets:  # All targets have been hit
    print(f'Training not completed! {total_targets - targets_hit} targets left.')
# Coordinates of the targets that were hit
print(*targets_hit_coord, sep="\n")
