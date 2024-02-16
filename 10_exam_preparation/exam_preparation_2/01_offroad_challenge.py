from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption = deque([int(x) for x in input().split()])
fuel_needed = deque([int(x) for x in input().split()])

current_altitude = 1
max_altitude = len(initial_fuel)

while initial_fuel and additional_consumption and fuel_needed:

    current_fuel = initial_fuel.pop()
    current_consumption = additional_consumption.popleft()
    current_fuel_needed = fuel_needed.popleft()

    consumption = current_fuel - current_consumption

    # Successfully climbed the hill
    if consumption >= current_fuel_needed:
        print(f'John has reached: Altitude {current_altitude}')
        current_altitude += 1
        continue

    # Failed to climb the hill, exit the loop
    print(f'John did not reach: Altitude {current_altitude}')
    current_altitude -= 1
    break

# Output
reached_top = (current_altitude == max_altitude)

reached_altitudes = [int(x) for x in range(1, current_altitude + 1)]
output_text = []
for altitude in reached_altitudes:
    output_text.append(f'Altitude {altitude}')


if reached_top:
    print('John has reached all the altitudes and managed to reach the top!')

elif not reached_top and current_altitude > 0:
    print('John failed to reach the top.')
    print(f'Reached altitudes: {", ".join(output_text)}')

elif not reached_top and current_altitude <= 0:
    print('John failed to reach the top.')
    print("John didn't reach any altitude.")
