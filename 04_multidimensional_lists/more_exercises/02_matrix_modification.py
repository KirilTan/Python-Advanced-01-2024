# Read the matrix
matrix = [[int(num) for num in input().split()] for _ in range(int(input()))]

# Define operations
functions = {
    "Add": lambda row, col, value: matrix[row][col] + value,
    "Subtract": lambda row, col, value: matrix[row][col] - value,
}

# Process commands
command = input()
while command != "END":
    command, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)

    # Check if indices are valid
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        result = functions[command](row, col, value)
        matrix[row][col] = result  # Update the specific element in the matrix
    else:
        print("Invalid coordinates")

    command = input()

# Print the updated matrix
for row in matrix:
    print(*row)
