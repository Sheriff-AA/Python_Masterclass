def palindrome_sentence(sentence):
    valid_letters = ""
    for letter in sentence:
        if letter.isalnum():
            valid_letters += letter

    return valid_letters[::-1].casefold() == valid_letters.casefold()


word = input("Enter a word to check: ")

if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not palindrome".format(word))
