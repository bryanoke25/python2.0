stuff = {"Pen" : "writing", }

while True:
    print("1)add.")
    print("2)check a word.")
    print("3)delete.")
    print("4)see all.")
    print("5)just leave.")

    choice = int(input("choose one of the above : "))

    if choice == 1:
        thing = str(input("add a thing : "))
        use = str(input("give a use: "))
        stuff[thing]=use
        print(stuff)

    elif choice == 2:
        option = str(input("What do you want to check : "))
        if option in stuff:
         print(stuff[option])
        else:
            print("thing not in the stuff folder")

        

        

    elif choice == 3:
        del_thing = str(input("What you want to delte : "))
        del stuff[del_thing]
        print(stuff)

    elif choice == 4:
        print(stuff) 

    elif choice == 5:
        break
    else:
        print("that not there.")

    

        