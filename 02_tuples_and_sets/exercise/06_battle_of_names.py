num_inputs = int(input())

odd_set = set()
even_set = set()

for index in range(num_inputs):
    index += 1
    name = input()
    name_value = sum(ord(letter) for letter in name) // index

    if name_value % 2 == 0:
        even_set.add(name_value)
    else:
        odd_set.add(name_value)

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_odd_set == sum_even_set:
    union = odd_set.union(even_set)
    print(*union, sep=', ')
elif sum_odd_set > sum_even_set:
    symmetric_difference = odd_set.difference(even_set)
    print(*symmetric_difference, sep=', ')
else:
    different_values = odd_set.symmetric_difference(even_set)
    print(*different_values, sep=', ')
