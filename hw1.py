import random
num = random.randint(1, 100)
play_again = True
while play_again:
    guess = int(input("guess a number : "))

    if guess < num:
        print("your guess is smaller then the number. Try again")

    elif guess > num:
        print("your guess is bigger then the number. Try again")

    else:
        print("crongragulations! You got it right!")
        user = input("do you want to play again? : ")
        if user == "yes":
            num = random.randint(1, 100)
        else:
            play_again = False
        
            

