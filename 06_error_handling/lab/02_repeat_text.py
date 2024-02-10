input_text = input()

try:
    n = int(input())
    print(n * input_text)
except ValueError:
    print('Variable times must be an integer')
