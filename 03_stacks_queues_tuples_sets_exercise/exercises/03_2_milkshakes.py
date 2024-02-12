from collections import deque


def make_milkshakes(chocolates: list, cups_of_milk: deque) -> int:
    """
    Makes milkshakes by matching chocolates with cups of milk.

    Args:
        chocolates (list): List of integers representing chocolates.
        cups_of_milk (deque): Deque of integers representing cups of milk.

    Returns:
        int: The number of milkshakes made.
    """

    milkshakes = 0

    while milkshakes < 5 and chocolates and cups_of_milk:
        current_chocolate = chocolates.pop()
        current_cup_of_milk = cups_of_milk.popleft()

        # Skip if either chocolate or milk is not positive
        if current_chocolate <= 0 and current_cup_of_milk <= 0:
            continue
        elif current_chocolate <= 0:
            cups_of_milk.appendleft(current_cup_of_milk)
            continue
        elif current_cup_of_milk <= 0:
            chocolates.append(current_chocolate)
            continue

        # Make a milkshake if chocolate and milk match
        if current_chocolate == current_cup_of_milk:
            milkshakes += 1
        else:
            cups_of_milk.append(current_cup_of_milk)
            chocolates.append(current_chocolate - 5)

    return milkshakes


def main():
    """
    The main function that handles user input and outputs the results.
    """

    # User inputs
    chocolates = [int(x) for x in input().split(', ')]
    cups_of_milk = deque(int(x) for x in input().split(', '))

    # Make milkshakes
    milkshakes_made = make_milkshakes(chocolates, cups_of_milk)

    # Output results
    print("Great! You made all the chocolate milkshakes needed!") if milkshakes_made == 5 \
        else print("Not enough milkshakes.")

    print(f'Chocolate: {", ".join(map(str, chocolates))}') if chocolates \
        else print("Chocolate: empty")

    print(f'Milk: {", ".join(map(str, cups_of_milk))}') if cups_of_milk \
        else print("Milk: empty")


if __name__ == "__main__":
    main()
