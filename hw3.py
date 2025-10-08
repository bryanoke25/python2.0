import random
score = 0
for i in range(0, 10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    result = num1 * num2
    print(f"what is {num1} * {num2}?")
    answer = int(input("the answer is : "))
    if result == answer:
        print("well done you got it right")
        score += 1
    else:
        print("Nope you got it wrong.")
        break
    print(f"score : {score}")