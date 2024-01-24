from collections import deque
from datetime import datetime, timedelta

robots = {}  # robot_name: [time_for_completion, time_till_free]

for r in input().split(";"):
    name, time_needed = r.split("-")  # "ROB-15" -> name = ROB, time_needed = 15
    robots[name] = [int(time_needed), 0]


factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(seconds=1)
    product = products.popleft()

    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:  # Robot is still working
            robots[name][1] -= 1  # Remove 1 second from the robot's time till free

        if value[1] == 0:  # Robot is free
            free_robots.append([name, value])  # Robot added to the list of free robots

    if not free_robots:  # No free robots
        products.append(product)  # Product added back to the list of products
        continue

    robot_name, data = free_robots[0]  # robots_name = "Rob", data = [15, 0]
    robots[robot_name][1] = data[0]  # {"Rob": [15, 15]}

    print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")
