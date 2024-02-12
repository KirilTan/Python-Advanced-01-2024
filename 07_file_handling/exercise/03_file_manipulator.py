import os

user_input = input()
while user_input != 'End':
    command, *info = user_input.split('-')

    if command == 'Create':
        file_name = info[0]
        with open(file_name, 'w') as _:
            pass
        print(f'{file_name} created')

    elif command == 'Add':
        file_name, content = info[0], info[1]
        try:

            with open(file_name, 'a') as file:
                file.write(content + '\n')
                print(f'{content} added to {file_name}')

        except FileNotFoundError:
            print('An error occurred!')
            print(f'{file_name} not found')

    elif command == 'Replace':
        file_name, old_content, new_content = info[0], info[1], info[2]

        try:

            with open(file_name, 'r+') as file:
                text = file.read()
                text = text.replace(old_content, new_content)

                file.seek(0)
                file.write(text)
                file.truncate()
            print(f'{old_content} replaced with {new_content} in {file_name}')

        except FileNotFoundError:
            print('An error occurred!')
            print(f'{file_name} not found')

    elif command == 'Delete':
        file_name = info[0]

        try:

            os.remove(file_name)
            print(f'{file_name} deleted')

        except FileNotFoundError:
            print('An error occurred!')
            print(f'{file_name} not found')

    user_input = input()
