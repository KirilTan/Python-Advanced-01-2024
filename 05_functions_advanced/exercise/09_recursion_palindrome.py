def palindrome(word: str, index: int) -> str:
    """
    This function takes in a word and an index and determines if the word is a palindrome.

    Parameters:
        word (str): The word to be checked.
        index (int): The index of the current character being compared.

    Returns:
        str: A message indicating whether the word is a palindrome or not.

    """
    if index == len(word) // 2:
        return f'{word} is a palindrome'

    if word[index] != word[-index-1]:
        return f'{word} is not a palindrome'

    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
