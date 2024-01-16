from collections import deque

names = deque(input().split())
n = int(input())
current_turn = 1

while len(names) > 1:
    current_kid = names.popleft()

    if current_turn != n:
        current_turn += 1
        names.append(current_kid)

    else:
        print(f"Removed {current_kid}")
        current_turn = 1

print(f"Last is {names[0]}")
