from collections import deque

# Option 1 (Time = 0.05)

my_stack = deque()

number_of_inputs = int(input())

for _ in range(number_of_inputs):
    current_input = [int(x) for x in input().split()]
    current_command = current_input[0]

    if current_command == 1:  # Push the number (integer) into the stack
        current_number = current_input[1]
        my_stack.append(current_number)

    elif current_command == 2:  # Delete the number at the top of the stack
        if my_stack:
            my_stack.pop()

    elif current_command == 3:  # Print the biggest number in the stack
        if my_stack:
            print(max(my_stack))

    elif current_command == 4:  # Print the smallest number in the stack
        if my_stack:
            print(min(my_stack))

my_stack.reverse()
print(*my_stack, sep=", ")
