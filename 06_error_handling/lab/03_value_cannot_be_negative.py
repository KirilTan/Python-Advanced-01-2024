class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    try:
        number = float(input())
        if number < 0:
            raise ValueCannotBeNegative('Number cannot be negative')
    except ValueError:
        print('Variable number must be a floating value')