print("Welcome to this World of colors:!What would you like to do with them?")
rainbow = ['Red' , 'Orange' , 'Yellow' , 'Green' , 'Blue' , 'Purple' ,  'Pink' ,  'Brown',  'Black' , 'Gray']
while True:
    print("1. See the rainbow!")
    print("2. Add on to the rainbow!")
    print("3. Take away any unwanted colors from your raibow!.")
    print("4. Say goodbye to the rainbow!.")
   
    user_choice = int(input("Decide which option will suit you most for manufacturing your rainbow! : "))

    if user_choice == 1:
        num = 1
        for r in rainbow:
            print(f"{num}. {r}")
            num+=1

    elif user_choice == 2:
        user_rainbow_add = str(input("Which color would u like to be added to the existing rainbow? :  "))
        rainbow.append(user_rainbow_add)
    elif user_choice == 3:
        user_rainbow_remove = str(input("Which color is undesirable and you would like to remove? : "))
        if user_rainbow_remove in rainbow:
          rainbow.remove(user_rainbow_remove)
        else:
            print("This color has not been added. Please review your colors and choose again")
    elif user_choice == 5:
        print("The rainbow is now residing, till next time!")
        break