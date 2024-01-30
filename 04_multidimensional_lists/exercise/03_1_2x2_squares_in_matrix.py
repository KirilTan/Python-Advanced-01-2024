rows, columns = [int(num) for num in input().split()]
string_matrix = [[el for el in input().split()] for _ in range(rows)]

# Example:
# 3 4
# A B B D
# E B B B
# I J B B

sub_matrix_with_same_values = 0

for row_index in range(rows - 1):
    for column_index in range(columns - 1):

        sub_matrix = [                                                                                      # [
            string_matrix[row_index][column_index], string_matrix[row_index][column_index + 1],             # [A], [B],
            string_matrix[row_index + 1][column_index], string_matrix[row_index + 1][column_index + 1]      # [E], [B]
        ]                                                                                                   # ]

        first_element = sub_matrix[0][0]                                                                    # [A]

        is_valid = True
        for row in sub_matrix:
            if any(element != first_element for element in row):
                is_valid = False
                break
        if is_valid:
            sub_matrix_with_same_values += 1

print(sub_matrix_with_same_values)
