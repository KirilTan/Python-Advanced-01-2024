from math import log

result = 0
number = int(input())

try:
    base = int(input())
    result = log(number, base)
except ValueError:
    result = log(number)
finally:
    print("{:.2f}".format(result))

