rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

equal_blocks = 0

for row in range(rows - 1):
    for column in range(cols - 1):
        symbol = matrix[row][column]

        if symbol == matrix[row + 1][column] and symbol == matrix[row][column + 1] and symbol == matrix[row + 1][column + 1]:
            equal_blocks += 1

print(equal_blocks)
