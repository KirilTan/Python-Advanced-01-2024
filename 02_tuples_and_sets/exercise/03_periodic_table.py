number_of_inputs = int(input())

unique_elements = set()
for _ in range(number_of_inputs):
    input_elements = input().split()
    unique_elements.update(input_elements)

print(*unique_elements, sep='\n')
