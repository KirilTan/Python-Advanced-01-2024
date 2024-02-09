def math_operations(*numbers, **kwargs):
    """
    This function performs basic mathematical operations on a variable number of numbers and keyword arguments.

    Parameters:
        numbers: A list of numbers to perform operations on.
        kwargs: A dictionary of keyword arguments to perform operations on. The keys of the dictionary should be one of the following: "a", "s", "d", or "m", which represent addition, subtraction, division, and multiplication, respectively. The values of the dictionary should be numbers.

    Returns:
        str: A string containing the results of the mathematical operations, in the format "key: value", where "key" is one of the keys of the "kwargs" dictionary and "value" is the result of the operation. The results are sorted in decreasing order of magnitude and alphabetical order of the keys.

    Raises:
        ValueError: If the input arguments are of an invalid type.
    """
    keys = list(kwargs.keys())  # [a, s, d, m]

    for i in range(len(numbers)):
        key = keys[i % 4]  # 0, 1, 2, 3

        if key == "a":
            kwargs[key] += numbers[i]
        elif key == "s":
            kwargs[key] -= numbers[i]
        elif key == "d":
            if numbers[i] != 0:
                kwargs[key] /= numbers[i]
        elif key == "m":
            kwargs[key] *= numbers[i]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return "\n".join(f"{k}: {v:.1f}" for k, v in kwargs)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
