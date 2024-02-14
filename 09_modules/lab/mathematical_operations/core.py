sign_mapper = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y
}


def execute_expression(expression: str):
    n1_txt, sign, n2_txt = expression.split()

    n1 = float(n1_txt)
    n2 = float(n2_txt)

    result = sign_mapper[sign](n1, n2)
    return result
