def process_commands(commands, first_set, second_set):
    """
    Processes a series of commands to manipulate two sets.

    Args:
    commands (dict): A dictionary mapping command strings to lambda functions.
    first_set (set): The first set to be manipulated.
    second_set (set): The second set to be manipulated.
    """
    number_of_inputs = int(input())
    for _ in range(number_of_inputs):
        first_command, second_command, *data = input().split()
        command = first_command + " " + second_command
        commands[command](data)


def main():
    """
    Main function to execute the script.
    """
    # Define the set manipulation functions
    functions = {
        'Add First': lambda x: first_set.update(map(int, x)),
        'Add Second': lambda x: second_set.update(map(int, x)),
        'Remove First': lambda x: first_set.difference_update(map(int, x)),
        'Remove Second': lambda x: second_set.difference_update(map(int, x)),
        'Check Subset': lambda _: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
    }

    # Initialize the sets
    first_set = set(map(int, input().split()))
    second_set = set(map(int, input().split()))

    # Process the commands
    process_commands(functions, first_set, second_set)

    # Print the final sets
    print(*sorted(first_set), sep=', ')
    print(*sorted(second_set), sep=', ')


if __name__ == "__main__":
    main()
 