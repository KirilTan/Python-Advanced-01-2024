num_of_inputs = int(input())

my_list = []

for _ in range(num_of_inputs):
    sub_list = [int(x) for x in input().split(', ')]
    my_list.extend(sub_list)
print(my_list)

# matrix = [[int(x) for x in input().split(', ')] for _ in range(num_of_inputs)]
# flattened_matrix = [x for y in matrix for x in y]
# print(flattened_matrix)
