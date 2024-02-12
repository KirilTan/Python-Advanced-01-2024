from functools import reduce
from math import floor

expression = input().split()  # [6, 5, 4, 5, +]

idx = 0

functions = {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
}

while idx < len(expression):
    element = expression[idx]

    if element in "/*+-":
        expression[0] = functions[element](idx)
        [expression.pop(1) for _ in range(idx)]  # pop everything including the symbol
        idx = 1

    idx += 1

print(floor(int(expression[0])))
