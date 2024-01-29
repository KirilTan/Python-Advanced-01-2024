row, col = map(int, input().split(', '))

matrix = [[int(num) for num in input().split()] for num in range(row)]
# print(*matrix, sep='\n')

col_sum = []
for col_index in range(col):
    cur_col_sum = 0
    for row_index in range(row):
        cur_col_sum += matrix[row_index][col_index]
    col_sum.append(cur_col_sum)

print(*col_sum, sep='\n')
