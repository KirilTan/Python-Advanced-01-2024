from collections import deque

# Initial input
water = int(input())
queue = deque()

# Adding people to queue
name = input()
while not name == "Start":
    queue.append(name)
    name = input()

# Performing actions
command = input()
while not command == "End":
    data = command.split()

    # Refilling the dispenser
    if len(data) > 1:
        water += int(data[1])

    # Removing person from queue and poring water if available
    if len(data) == 1:
        water_requested = int(data[0])
        person = queue.popleft()

        # Checking if there is enough water
        if water >= water_requested:
            water -= water_requested
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

    command = input()

# Final output - water left
print(f"{water} liters left")
