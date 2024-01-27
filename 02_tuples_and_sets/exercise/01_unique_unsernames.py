# Option 1
number_of_inputs = int(input())

names = set()
for _ in range(number_of_inputs):
    name = input()
    names.add(name)

print(*names, sep='\n')

# Option 2
# names = {input() for _ in range(int(input()))}
# print(*names, sep='\n')

# Option 3
# print(*{input() for _ in range(int(input()))}, sep='\n')
