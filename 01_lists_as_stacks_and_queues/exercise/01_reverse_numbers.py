from collections import deque

# Option 1 (Time = 0.05)
numbers = deque(input().split())

while numbers:
    print(numbers.pop(), end=" ")

# Option 2 (Time = 0.09)
numbers = deque(input().split())
numbers.reverse()
print(*numbers)

