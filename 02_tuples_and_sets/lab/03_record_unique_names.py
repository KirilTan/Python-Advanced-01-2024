number_of_inputs = int(input())
names = set()
for _ in range(number_of_inputs):
    name = input()
    names.add(name)

for name in names:
    print(name)
