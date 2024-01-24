# Function definition from the previous step
def is_balanced(parentheses: str) -> str:
    """
    This function takes a string of parentheses and determines if the parentheses are balanced or not.

    Parameters:
    parentheses (str): The string of parentheses to be checked.

    Returns:
    str: Returns "YES" if the parentheses are balanced, and "NO" if they are not.

    """
    stack = []
    # Mapping of opening and closing parentheses
    parentheses_map = {'(': ')', '[': ']', '{': '}'}

    for parenthesis in parentheses:
        # If it's an opening parenthesis, push onto stack
        if parenthesis in parentheses_map:
            stack.append(parenthesis)
        # If it's a closing parenthesis
        else:
            # If stack is empty or doesn't match the opening, return "NO"
            if not stack or parentheses_map[stack.pop()] != parenthesis:
                return "NO"

    # If stack is empty, parentheses are balanced
    return "YES" if not stack else "NO"


sequence = input()
result = is_balanced(sequence)
print(result)
