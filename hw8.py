while True:
    choice = str(input("Enter a word: "))
    if choice[:] == choice[: :-1]:
        print("It is a palindrome")
    else:
        print("it is not a palindrome")