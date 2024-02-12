functions = {
    'Add First': lambda x: first_set.update(map(int, x)),
    'Add Second': lambda x: second_set.update(map(int, x)),
    'Remove First': lambda x: first_set.difference_update(map(int, x)),
    'Remove Second': lambda x: second_set.difference_update(map(int, x)),
    'Check Subset': lambda _: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
}

first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))

number_of_inputs = int(input())
for _ in range(number_of_inputs):
    # input_parts = input().split()
    # command, data = ' '.join(input_parts[:2]), input_parts[2:]

    first_command, second_command, *data = input().split()
    command = first_command + " " + second_command

    functions[command](data)

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
