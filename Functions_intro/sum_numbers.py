def sum_numbers(*numbers: float) -> float:
    """
    Sum group of numbers.
    :param numbers: A tuple of numbers to sum together
    :return: Sum of the numbers in tuple `numbers`
    """
    start = 0
    for num in numbers:
        start += num
    return start


value = sum_numbers(12.5, 3.147, 98.1)
print(value)
