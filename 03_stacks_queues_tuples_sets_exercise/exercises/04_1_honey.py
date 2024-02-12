from collections import deque


def calc(x: int, operator: str, y: int) -> int or float:

    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        if y == 0:
            return 0
        return x / y
    else:
        raise ValueError(f"Unsupported operator: {operator}")


working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while nectar and working_bees:

    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    # Step 1 - Take the first bee and try to match it with the last nectar
    if current_nectar >= current_bee:
        # Step 2 - Calculate the honey made
        symbol = symbols.popleft()
        honey_made = calc(current_bee, symbol, current_nectar)
        total_honey += abs(honey_made)

    elif current_nectar < current_bee:  # Nectar is discarded, check next nectar value for the same bee
        working_bees.appendleft(current_bee)

# Output
print(f'Total honey made: {total_honey}')
if working_bees:
    print(f'Bees left: {(", ".join([str(x) for x in working_bees]))}')
if nectar:
    print(f'Nectar left: {(", ".join([str(x) for x in nectar]))}')