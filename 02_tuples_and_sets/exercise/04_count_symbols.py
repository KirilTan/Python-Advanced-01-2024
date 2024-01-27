# Option 1
occurrences = {}
for symbol in input():
    occurrences[symbol] = occurrences.get(symbol, 0) + 1
for symbol, count in sorted(occurrences.items()):
    print(f'{symbol}: {count} time/s')

# Option 2
# from collections import OrderedDict
#
# input_string = input()
#
# letter_occurrences = {}
# for letter in input_string:
#     if letter not in letter_occurrences.keys():
#         letter_occurrences[letter] = 1
#     else:
#         letter_occurrences[letter] += 1
#
# letter_occurrences = OrderedDict(sorted(letter_occurrences.items()))
#
# for letter, count in letter_occurrences.items():
#     print(f'{letter}: {count} time/s')
