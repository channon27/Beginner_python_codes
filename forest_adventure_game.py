#database
import json
try:
    with open("leaderboard","r") as f:
        data = json.load(f)
except:
    data = {}

name = input("Enter username: ")
if name in data:
    print(f"You've played before! Your previous score was {data[name]}")
else:
    print("Hello new player!")
    data[name] = 0
#text game   
def add_points(player_name,database):
    database[player_name] += 10
def minus_points(player_name,database):
    database[player_name] -= 10    

BOLD = '\033[1m'
END = '\033[0m'

strike = 0
health = 100
Alive = True
while health > 0:
    print(f"Hello {name} Welcome to the text-based game!")
    print(f"You have {health} health remaining")
    print(f"{BOLD}----Level 1----{END}")
    lvl1 = input("You see a bear sleeping and you are hungry , What do you do? --- Option 1: Kill it for food (1) --- Option 2: Leave it be (2) ").lower().strip()
    if lvl1 == "1":
        print("Very bad choice. You woke the bear as you had no tools. --- Lose 50 health!")
        health = health - 50
        minus_points(name,data)
        print(f"You have {health} health remaining")
    elif lvl1 == "2":
        print("Good Choice! With your bear hands you would not have stood a chance.")
        add_points(name,data)
    else:
        print("Error! Enter a valid input! No points awarded!")
        strike = strike + 1
    if Alive == True:
        print(f"You have {health} health remaining")
        print(f"{BOLD}----Level 2----{END}")
        lvl2 = input("You find a cave on your travels ,What do you do? --- Option 1: Enter cave (1) --- Option 2: Ignore and continue (2) ").lower().strip()
        if lvl2 == "1":
            print("Good choice! In the cave you found a bed for the night , a open fire and plenty of food.")
            add_points(name,data)
        elif lvl2 == "2":
            health = health - 20 
            print("Bad choice. The cave had essentials to keep you alive. --- Lose 20 health!")
            minus_points(name,data)
        else:
            print("Error! Enter a valid input! No points awarded")
            strike = strike + 1
    if health <= 0 or strike >= 2:
        print(f"{BOLD}You died! ---GAME OVER---{END}")
        break
    if Alive == True:
        print(f"You have {health} health remaining")
        print(f"{BOLD}----Level 3----{END}")
        lvl3 = input("You see a abandoned cabin , What do you do? --- Option 1: Enter the cabin (1) --- Option 2: Ignore and continue (2) ").lower().strip()
        if lvl3 == "1":
            print("Very bad choice. An old man lives inside and hits you multipule times with his cane. --- Lose 50 health! ")
            health = health - 50
            print(f"You have {health} health remaining")
            minus_points(name,data)
        elif lvl3 == "2":
            print("Good choice! An old man lived iside who would have hit you with his cane.")
            add_points(name,data)
        else:
            print("Error! Enter a valid input! No points awarded")
            strike = strike + 1
    if health <= 0 or strike >= 2:
        print(f"{BOLD}You died! ---GAME OVER---{END}")
        break
    if Alive == True:
        print(f"You have {health} health remaining")
        print(f"{BOLD}----Level 4----{END}")
        lvl4 = input("You find a pond , What do you do? --- Option 1: Drink the water (1) --- Option 2: Ignore and continue (2) ").lower().strip()
        if lvl4 == "1":
            print("Bad choice. The water was contaminated and you get sick. --- Lose 20 health! ")
            health = health - 20
            minus_points(name,data)
        elif lvl4 == "2":
            print("Good choice! The water was contaminated.")
            add_points(name,data)
        else:
            print("Error! Enter a valid input! No points awarded")
            strike = strike + 1
    if health <= 0 or strike >= 2:
        print(f"{BOLD}You died! ---GAME OVER---{END}")
        print(f"Your score was: {data[name]}")
        break 
    else:
        print(f"{BOLD}You survived all the levels! ---!YOU WIN!---{END}")
        print(f"Your score was: {data[name]}")
        break      
save = input("Would you like to save to leaderboard? Yes(1)  No(2)")
def save_to_leaderboard():
    with open ("leaderboard","w") as f:
        json.dump(data,f)
        print("Game score saved to leaderboard!")
        print("\n---GLOBAL LEADERBOARD---")
        reverse = True
        sorted_leaderboard = sorted(data.items(), key=lambda item: item[1], reverse=True)
        for position, (player_name,player_score ) in enumerate(sorted_leaderboard, start= 1):
            print(f"{position}. {player_name}: {player_score}: points")
if save =="1":
    save_to_leaderboard()
elif save =="2":
    print("Not Saving!")
else:
    print("Error! Enter valid input! Not Saving!")
      
    