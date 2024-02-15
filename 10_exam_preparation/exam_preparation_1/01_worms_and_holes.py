from collections import deque

# User input - worms and holes
worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

# Variables needed
starting_worms = len(worms)
matches_count = 0

while worms and holes:  # Stop matching if there are no more worms or holes

    # Start with the last worm and the first hole
    current_worm = worms.pop()
    current_hole = holes.popleft()

    # If the worm value becomes equal to or below 0 remove it from the sequence before trying to match it with the hole
    if current_worm <= 0:
        holes.appendleft(current_hole)
        continue

    # If their values are equal, remove the worm and the hole
    if current_worm == current_hole:
        matches_count += 1
        continue
    else:  # Otherwise remove the whole and decrease the value of the worm by 3
        current_worm -= 3
        worms.append(current_worm)

# Output

# First line
if matches_count > 0:
    print('Matches:', matches_count)
else:
    print('There are no matches.')

# Second line
if matches_count == starting_worms:
    print(f'Every worm found a suitable hole!')
elif not worms:
    print('Worms left: none')
elif worms:
    print(f'Worms left: {", ".join(map(str, worms))}')

# Third line
if not holes:
    print('Holes left: none')
elif holes:
    print(f'Holes left: {", ".join(map(str, holes))}')
