from collections import deque

# pumps = deque([[int(x) for x in input().split()] for _ in range(int(input()))])  # 0.05
pumps = deque()
number_of_pumps = int(input())
for _ in range(number_of_pumps):
    current_pump = [int(x) for x in input().split()]
    pumps.append(current_pump)

pumps_copy = pumps.copy()
gas_in_tank = 0
index = 0

while pumps_copy:
    petrol, distance = pumps_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pumps.rotate(-1)
        pumps_copy = pumps.copy()
        index += 1
        gas_in_tank = 0

print(index)  # 0.09
