from collections import deque

# Initialize deque for bees and symbols, and a list for nectar
bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

# Initialize a variable to keep track of total honey made
total_honey = 0

# Define functions for each operation
functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,  # Handling division by zero
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}

# Process bees and nectar
while bees and nectar:
    curr_bee = bees.popleft()  # Take the next bee
    curr_nectar = nectar.pop()  # Take the last nectar

    # If the nectar is less than the bee's value, put the bee back
    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
    else:
        # Calculate honey made and add to total
        total_honey += abs(functions[symbols.popleft()](curr_bee, curr_nectar))

# Output results
print(f"Total honey made: {total_honey}")

# Print any remaining bees
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

# Print any remaining nectar
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
