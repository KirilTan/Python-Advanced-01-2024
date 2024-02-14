from core import execute_expression

expression = input()

result = execute_expression(expression)
print('{:.2f}'.format(result))