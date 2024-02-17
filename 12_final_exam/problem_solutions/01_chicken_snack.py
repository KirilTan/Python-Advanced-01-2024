from collections import deque

# Input
money = [int(x) for x in input().split()]
prices = deque([int(x) for x in input().split()])

# Variables
change = 0
food_bought = 0

# Logic
while money and prices:

    current_money = money.pop()  # Start with the last element from money
    current_price = prices.popleft()  # Start with the first element from prices
    difference = current_money - current_price  # Calculate difference

    # If their values are equal:
    if current_money == current_price:

        # Buys food
        food_bought += 1

        continue  # Remove both

    # If current_money is bigger than current_price:
    elif current_money > current_price:

        # Buys food
        food_bought += 1

        # Add difference to change
        change += difference

        # Increase the next amount of money value in the sequence by the resulting difference
        if money:
            money[-1] += difference
        continue

    # If current_money is smaller than current_price:
    elif current_money < current_price:
        continue  # Remove both

# Output
if food_bought >= 4:
    print(f'Gluttony of the day! Henry ate {food_bought} foods.')
elif food_bought > 0:
    print(f'Henry ate: {food_bought} {"food" if food_bought==1 else "foods"}.')
elif food_bought == 0:
    print('Henry remained hungry. He will try next weekend again.')
