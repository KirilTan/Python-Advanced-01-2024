from collections import deque

command = input()
queue = deque([])

while not command == "End":

    if command == "Paid":
        while queue:
            print(queue.popleft())
        command = input()
        continue

    queue.append(command)
    command = input()

print(f"{len(queue)} people remaining.")
