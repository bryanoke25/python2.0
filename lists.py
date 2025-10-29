print("Welcome to your lists. Please select on option")
tasks = []
while True:
    print("1. view your list.")
    print("2. add an item to your list.")
    print("3. remove an item from your list.")
    print("4. update an item in your list.")
    print("5 close the list.")
    user_choice = int(input("enter from the following : "))

    if user_choice == 1:
        num = 1
        for t in tasks:
            print(f"{num}. {t}")
            num+=1

    elif user_choice == 2:
        user_add = str(input("What do you want to add :  "))
        tasks.append(user_add)
    elif user_choice == 3:
        user_remove = str(input("What would you like to remove"))
        if user_remove in tasks:
          tasks.remove(user_remove)
        else:
            print("Element not found in tasks")
    elif user_choice == 5:
        print("It will now close")
        break

    
    

    
