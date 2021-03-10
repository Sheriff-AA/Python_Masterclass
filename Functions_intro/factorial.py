def factorial(number: int) -> int:
    """
    Calculate factorial of number

    :param number: integer
    :return: factorial of `number`.
    """
    initial_number = 1
    for i in range(1, number + 1):
        initial_number *= i
    return initial_number


for num in range(36):
    print("{} factorial is {}".format(num, factorial(num)))
