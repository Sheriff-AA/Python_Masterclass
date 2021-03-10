import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin)

    The function will continue looping, and prompting
    the user until a valid `int` is entered

    :param prompt: The string that the user will see,
        when they are prompted to enter the value
    :return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("Invalid input, Try again")


highest = 100
ans = random.randint(1, highest)
print(ans)

print("Guess the lucky number between 1 and {}: ".format(highest))
guess = 0

while guess != ans:
    guess = get_integer(": ")
    if guess == ans:
        print("That is correct!")
        break
    elif guess == 0:
        print("Game over")
        break
    elif guess > ans:
        print("Guess lower")
    elif guess < ans:
        print("Guess higher")

# if ans != guess:
#     if guess > ans:
#         print("Guess lower")
#     else:
#         print("Guess higher")
#     guess = int(input())
#     if guess == ans:
#         print("That is correct!")
#     else:
#         print("Oops! That is also wrong")
# else:
#     print("That is correct!")

# if guess > ans:
#     print("Guess lower")
#     guess = int(input())
#     if guess == ans:
#         print("You guessed it correctly")
#     else:
#         print("Oops! that is wrong")
# elif guess < ans:
#     print("Guess higher")
#     guess = int(input())
#     if guess == ans:
#         print("You guessed it correctly")
#     else:
#         print("Oops! that is wrong")
# else:
#     print("You got it right")
