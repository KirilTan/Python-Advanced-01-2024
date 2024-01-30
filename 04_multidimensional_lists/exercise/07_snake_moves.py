from collections import deque


def word_snake(word: list, rows: int, columns: int) -> list:
    """
    This function takes a list of characters (representing a word), a number of rows, and a number of columns
    and returns a list of rows, where each row is a string of the given number of columns, with the characters
    from the word wrapped around in a snake pattern.

    Parameters:
        word (list): A list of characters representing the word to be wrapped.
        rows (int): The number of rows in the output list.
        columns (int): The number of columns in each row of the output list.

    Returns:
        list: A list of rows, where each row is a string of the given number of columns,
        with the characters from the word wrapped around in a snake pattern.

    """

    new_word = []

    word_copy = deque(word)
    for row in range(rows):

        # Extend the word_copy so that it can fit in the current_tow
        while len(word_copy) < columns:
            word_copy.extend(word)

        # If the current row is even, add the characters from the word_copy to the new_word
        if row % 2 == 0:
            new_word.append(''.join([str(word_copy.popleft()) for _ in range(columns)]),)
        # If the current row is odd, add the characters from the word_copy to the new_word starting from the end
        else:
            new_word.append(''.join([str(word_copy.popleft()) for _ in range(columns)][::-1]))

    return new_word


def main():
    """
    This function is the main function of the code. It takes input from the user, calls the word_snake function,
    and prints the output.

    """
    # User input
    rows, columns = [int(num) for num in input().split()]
    word = list(input())

    # Call the word_snake function
    new_word = word_snake(word, rows, columns)

    # Output
    print(*new_word, sep="\n")


if __name__ == "__main__":
    main()
