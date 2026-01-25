#text game
BOLD = '\033[1m'
END = '\033[0m'
health = 100
Alive = True
while health > 0:
    usr_nm = input("Enter your user name: ")
    print (f"Hello {usr_nm}!  Welcome to the text based game!")
    print(f"You have {health} health remaining")
    print(f"{BOLD}----Level 1----{END}")
    lvl1 = input("You see a bear sleeping and you are hungry , What do you do? --- Option 1: Kill it for food (kill) --- Option 2: Leave it be (leave) ")
    if lvl1 == "kill":
        print("Very bad choice. You woke the bear as you had no tools. --- Lose 50 health!")
        health = health - 50
        print(f"You have {health} health remaining")
    if lvl1 == "leave":
        print("Good Choice! With your bear hands you would not have stood a chance.")
        print(f"You have {health} health remaining")
    if Alive == True:
        print(f"{BOLD}----Level 2----{END}")
        lvl2 = input("You find a cave on your travels ,What do you do? --- Option 1: Enter cave (enter) --- Option 2: Ignore and continue (ignore) ")
        if lvl2 == "enter":
            print("Good choice! In the cave you found a bed for the night , a open fire and plenty of food.")
        print(f"You have {health} health remaining")
        if lvl2 == "ignore":
            health = health - 20 
            print("Bad choice. The cave had essentials to keep you alive. --- Lose 20 health!")
            print(f"You have {health} health remaining")
    if health <= 0:
        print(f"{BOLD}You died! ---GAME OVER---{END}")
        break
    if Alive == True:
        print(f"{BOLD}----Level 3----{END}")
        lvl3 = input("You see a abandoned cabin , What do you do? --- Option 1: Enter the cabin (enter) --- Option 2: Ignore and continue (ignore) ")
        if lvl3 == "enter":
            print("Very bad choice. An old man lives inside and hits you multipule times with his cane. --- Lose 50 health! ")
            health = health - 50
            print(f"You have {health} health remaining")
        if lvl3 == "ignore":
            print("Good choice! An old man lived iside who would have hit you with his cane.")
            print(f"You have {health} health remaining")
    if health <= 0:
        print(f"{BOLD}You died! ---GAME OVER---{END}")
        break
    if Alive == True:
        print(f"{BOLD}----Level 4----{END}")
        lvl4 = input("You find a pond , What do you do? --- Option 1: Drink the water (drink) --- Option 2: Ignore and continue (ignore) ")
        if lvl4 == "drink":
            print("Bad choice. The water was contaminated and you get sick. --- Lose 20 health! ")
            health = health - 20
        if lvl4 == "ignore":
            print("Good choice! The water was contaminated.")

    if health <= 0:
        print(f"{BOLD}You died! ---GAME OVER---{END}")
        break 
    else:
        print(f"{BOLD}You survived all the levels! ---!YOU WIN!---{END}")
        break      
    