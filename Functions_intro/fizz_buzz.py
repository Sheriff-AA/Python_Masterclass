def fizz_buzz(number: int) -> str:
    """
    Play the game of fizz buzz.

    :param number: The number to check.
    :return: `fizz` for a number divisible by 3, `buzz`
        for a number divisible by 5, and `fizz buzz` for
        a number divisible by either.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


start_number = 1
while True:
    fizz_or_buzz = fizz_buzz(start_number)
    print(fizz_or_buzz)
    correct_number = start_number + 1
    correct_result = fizz_buzz(correct_number)
    users_input = correct_result

    if correct_number >= 100:
        print("Congratulations")
        break
    elif users_input != correct_result:
        print("YOU LOSE!")
        break
    else:
        start_number = correct_number + 1
    # print(start_number, correct_number)
