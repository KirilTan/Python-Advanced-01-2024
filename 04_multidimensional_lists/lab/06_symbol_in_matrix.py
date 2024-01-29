matrix = [[el for el in input()] for el in range(int(input()))]
# print(*matrix, sep='\n')
symbol_to_find = input()

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == symbol_to_find:
            print(f'({row_index}, {col_index})')
            exit()
print(f'{symbol_to_find} does not occur in the matrix')
