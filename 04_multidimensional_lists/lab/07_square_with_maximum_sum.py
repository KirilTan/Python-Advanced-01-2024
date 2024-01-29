rows, columns = map(int, input().split(', '))

matrix = []
for row in range(rows):
    numbers = [int(num) for num in input().split(', ')]
    matrix.append(numbers)

max_sum = float('-inf')
max_sum_sub_matrix = []

for row_index in range(rows-1):
    for column_index in range(columns-1):
        el_1 = matrix[row_index][column_index]
        el_2 = matrix[row_index][column_index+1]
        el_3 = matrix[row_index+1][column_index]
        el_4 = matrix[row_index+1][column_index+1]
        sum_el = el_1 + el_2 + el_3 + el_4

        if max_sum < sum_el:
            max_sum = sum_el
            max_sum_sub_matrix = [
                [el_1, el_2],
                [el_3, el_4]
            ]

print(*max_sum_sub_matrix[0])
print(*max_sum_sub_matrix[1])
print(max_sum)
