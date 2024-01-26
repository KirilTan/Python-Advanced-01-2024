user_input_numbers = tuple([float(x) for x in input().split()])

numbers_occurrences = {}

for number in user_input_numbers:
    if number not in numbers_occurrences:
        numbers_occurrences[number] = user_input_numbers.count(number)

for number, occurrences in numbers_occurrences.items():
    print(f"{number} - {occurrences} times")
