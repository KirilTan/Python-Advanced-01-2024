from core import fibonacci_sequence, locate_number

instruction = input()
sequence = []

while instruction != 'Stop':

    command, *info = instruction.split()
    number = int(info[-1])

    if command == 'Create':
        sequence = fibonacci_sequence(number)
        print(*sequence)

    elif command == 'Locate':
        try:
            result = locate_number(number, sequence)

            text_to_print = f'The number {number} is located at index {result}'
            print(text_to_print)
        except ValueError:
            print(f'The number {number} is not in the sequence')
    instruction = input()
