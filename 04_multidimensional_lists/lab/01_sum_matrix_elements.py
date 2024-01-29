row, col = map(int, input().split(', '))

matrix = []
matrix_sum = 0

for _ in range(row):
    current_list = [int(x) for x in input().split(', ')]
    matrix.append(current_list)
    matrix_sum += sum(current_list)

print(matrix_sum)
print(matrix)