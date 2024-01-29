matrix = [[int(num) for num in input().split()] for num in range(int(input()))]
# print(*matrix, sep='\n')

# diagonal_sum = 0
# for index in range(len(matrix)):
#     diagonal_sum += matrix[index][index]
# print(diagonal_sum)

diagonal_sum = sum(matrix[index][index] for index in range(len(matrix)))
print(diagonal_sum)
