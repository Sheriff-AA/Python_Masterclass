def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.

    :param x: An `int` to be passed as an argument.
    :param y: An `int` to be passed as an argument.
    :return: The product of x and y.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a string is palindrome.

    The function is case insensitive. It does not deal with
    sentences only words.

    :param string: The string that is collected from the argument.
    :return: True if the `str` is palindrome and False otherwise.
    """
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is palindrome.

    The function is case insensitive and collects any type of
    string literal. It ignores whitespace, capitalisation, and
    punctuations in the sentence.

    :param sentence: The string that is collected from the argument.
    :return: True if sentence is palindrome, False otherwise.
    """
    valid_letters = ""
    for letter in sentence:
        if letter.isalnum():
            valid_letters += letter

    return is_palindrome(valid_letters)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`"""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for i in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


sequence = fibonacci(6)
print(sequence)
