file_name = 'text.txt'
invalid_file_name = 'invalid_file.txt'

try:
    file = open(file_name, 'r')
    print(f'File {file_name} found')
except FileNotFoundError:
    print(f'File {file_name} not found')


try:
    invalid_file = open(invalid_file_name, 'r')
    print(f'File {invalid_file_name} found')
except FileNotFoundError:
    print(f'File {invalid_file_name} not found')
