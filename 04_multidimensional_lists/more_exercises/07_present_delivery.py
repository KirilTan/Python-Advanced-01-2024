def eat_cookie(presents_left: int, nice_kids: int) -> tuple:
    """
    This function takes two arguments: presents_left (an integer) and nice_kids (an integer).
    It iterates over a list of coordinates (represented as tuples) and checks if the square at the given coordinates
    contains an alphabetical character.
    If it does, it checks if the character is "V", which represents a present left by a nice kid.
    If it is, the function increments the nice_kids counter.
    Then, it replaces the character with a hyphen (-) and decrements the presents_left counter.
    The function continues until either the presents_left counter reaches zero or the loop completes.
    After the loop completes, the function returns a tuple containing the updated values of presents_left and nice_kids.

    Parameters:
    presents_left (int): The number of presents left after visiting each house.
    nice_kids (int): The number of nice kids visited so far.

    Returns:
    tuple: A tuple containing the updated values of presents_left and nice_kids.

    """
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighborhood[r][c].isalpha():
            if neighborhood[r][c] == "V":
                nice_kids += 1

            neighborhood[r][c] = "-"
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


presents = int(input())
size = int(input())

neighborhood = []
santa_pos = []

total_nice_kids = 0
nice_kids_visited = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):

    line = input().split()

    neighborhood.append(line)

    if 'S' in line:
        santa_pos = [row, line.index('S')]
        neighborhood[row][santa_pos[1]] = '-'

    total_nice_kids += line.count('V')

command = input()
while command != 'Christmas morning':
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]

    house = neighborhood[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_visited += 1
        presents -= 1
    elif house == "C":
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    neighborhood[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or nice_kids_visited == total_nice_kids:
        break

    command = input()

neighborhood[santa_pos[0]][santa_pos[1]] = 'S'

if not presents and nice_kids_visited < total_nice_kids:
    print('Santa ran out of presents!')

for row in range(size):
    print(' '.join(neighborhood[row]))

if total_nice_kids == nice_kids_visited:
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')
else:
    print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')
