import time
import random
import pygame
BOLD = '\033[1m'
END = '\033[0m'
game_state = {
    "player_hp" : 100,
    "sheild" : 0,
    "boss_hp": 500,
    "gold": 10,
    "inventory":[]
}
def add_item(item_name):
    if item_name in game_state["inventory"]:
        print(f"You allready have the {item_name}!")
    elif len(game_state["inventory"]) >= 3:
        print("Your inventory is full. Drop something first.")
    else:
        game_state["inventory"].append(item_name)
        print(f"Added {item_name} to your inventory.")
def use_item():
    print("Would you like to use one of your items?")
    print("NOTE |CASE SENSTIVE |")
    print("NOTE |ENTER 'no' TO EXIT |")
    print(f"You have {game_state['inventory']} ")
    item_name = input("What would you like to use? ")
    if item_name =="no":
        print("Goodbye.")
        return
    if item_name in game_state["inventory"]:
        if item_name == "Health potion":
            if game_state["player_hp"] > 80:
                print("You can't use that right now.")
            else:
                game_state["player_hp"] += 20 
                print("You drank a potion! +20HP!")
        elif item_name == "Mega potion":
            if game_state["player_hp"] > 50:
                print("You can't use that right now.")
            else:
                game_state["player_hp"] += 50 
                print("You drank a potion! +50HP!")
        elif item_name == "Mini sheild potion":
            if game_state["sheild"] > 80:
                print("You can't use that right now.")
            else:
                game_state["sheild"] += 25 
                print("You drank a Mini sheild potion! +25 Sheild!")
        elif item_name =="Big sheild potion":
            if game_state["sheild"] > 80:
                print("You can't use that right now.")
            else:
                game_state["sheild"] += 50 
                print("You drank a Big sheild potion! +50 Sheild!")
        else:
            use_item()
        game_state["inventory"].remove(item_name)
        print(f"{item_name} has been used!")
    else:
        print(f"You don't have a {item_name} to use!")
def attack(enemy_hp):
    damage = 20
    if "Starforged blade" in game_state["inventory"]:
        damage = 50
        print("Your one of a kind sword strikes with the force of a falling star!")
    elif "Iron sword" in game_state["inventory"]:
        damage = 35
        print("Your Iron sword hit hard.")
    elif "Wooden sword" in game_state["inventory"]:
        damage = 30
        print("Your wooden sword hits for extra.")
    elif "Wooden stick" in game_state["inventory"]:
        damage = 25
        print("Your wooden stick hits for a tiny bit extra.")

    enemy_hp -= damage
    print(f"You dealt {damage} damage to your enemy!")
    if enemy_hp <= 0:
        enemy_hp = 0
        print("Enemy killed!")
    return enemy_hp
def game_over():
    print(f"{BOLD} ----YOU DIED----{END}")
    print(f"{BOLD} ----GAME-OVER----{END}")
    quit()
def intro():
    usr_name = input("Hello traveler, what is your name? ")
    print(f"Welcome {usr_name}, and goodluck on your travels.")
    print("Here is a gift for you: A Health potion!")
    game_state["inventory"].append("Health potion")
def status_check():
    print("-"*20)
    print(f"HP: {game_state['player_hp']}  | Gold: {game_state['gold']}   | Sheild: {game_state['sheild']}   | Inventory: {game_state['inventory']}")
def shop():
    while True:
        print(f"Welcome to the shop you have {game_state['gold']} gold to spend.")
        print("What would you like to buy?")
        purchase = input("1.Health potion (20 Gold) , 2.Mega potion (25 Gold) , 3.Mini sheild potion (30 Gold) , 4.Big sheild potion (35 Gold) , 5.Sword crate(25 Gold) , 6.Exit  ")
        if purchase == "1":
            if game_state["gold"] >= 20 and len(game_state["inventory"]) < 3:
                print("You purchased a Health potion!")
                game_state["gold"] -= 20
                game_state["inventory"].append("Health potion")
                
            else:
                print("You can't buy anthing right now.")
                
        elif purchase == "2":
            if game_state["gold"] >= 25  and len(game_state["inventory"]) < 3:
                print("You purchased a Mega health potion!")
                game_state["gold"] -= 25
                game_state["inventory"].append("Mega potion")
                
            else:
                print("You can't buy anthing right now.")
                
        elif purchase == "3":
            if game_state["gold"] >= 30 and len(game_state["inventory"]) < 3:
                print("You purchased a Mini sheild potion!")
                game_state["gold"] -= 30
                game_state["inventory"].append("Mini sheild potion")
                
            else:
                print("You can't buy anthing right now.")
                
        elif purchase == "4":
            if game_state["gold"] >= 35 and len(game_state["inventory"]) < 3:
                print("You purchased a Big sheild potion!")
                game_state["gold"] -= 35
                game_state["inventory"].append("Big sheild potion")
                
            else:
                print("You can't buy anthing right now.")

        elif purchase == "5":
            if game_state["gold"] >= 25 and len(game_state["inventory"]) < 3:
                game_state["gold"] -= 25
                print("You crack open the glowing weapon crate...")
                time.sleep(2)
                swords =["Wooden stick" , "Wooden sword" , "Iron sword" , "Starforged blade"]
                weights =[60 , 30 , 7 , 3]
                new_sword = random.choices(swords, weights=weights,k=1)[0]
                print(f"Inside you got a {BOLD}{new_sword}{END}!")
                if new_sword not in game_state["inventory"]:
                    game_state["inventory"].append(new_sword)
                    print(f"You equip the {new_sword}")
                else:
                    print("The shopkeeper laughs. 'Come back again with more gold.'")
            else:
                print("You can't buy this right now.")
        elif purchase =="6":
            print("Goodbye.")
            False
            break
        else:
            print("Error! Enter a valid input (1,2,3,4,5)")
def alive_check():
    if game_state["player_hp"] <= 0:
     game_over()
def lvl1():
    status_check()
    print(f"{BOLD} ---LEVEL 1: THE TANGLED WILDS--- {END}") 
    time.sleep(3)
    print("You wake up on a cold bed of moss. The trees above are thick and twisted.")
    time.sleep(3)
    print("You check your pockets: 10 gold and a small potion. Better than nothing.")
    time.sleep(3)
    print("As you stand up, a starving Wolf emerges from the shadows, growling.") 
    time.sleep(3)
    print("What do you do?")  
    ans1 = input("Option 1. Fight!   Option 2. Distract: ") 
    if ans1 =="1":
        attack(enemy_hp=20)
        time.sleep(2)
        game_state["gold"] += 20
        print(f"{BOLD}LEVEL PASSED! {END}")
        time.sleep(2)
    elif ans1 =="2":
        game_state["player_hp"] -= 25
        print("You tried to distact the wolf but you triped and fell.")
    else:
        lvl1()
        return
def traveling1():
    events = [
        ["You found a berry bush!",10,0],
        ["A theif tripped you!",-15,-5],
        ["You found a shiny coin!",0,5],
        ["The sun feels good.",5,0]
    ]
    event = random.choice(events)
    print(f"\nEVENT: {event[0]}")
    if game_state["player_hp"] > 90:
        game_state["player_hp"] += event[1]
    game_state["gold"] += event[2]  
def lvl2 ():
    True
    while True:
        status_check()
        print(f"{BOLD}---LEVEL 2: THE WHISPERING BRIDGE---{END}")
        time.sleep(3)
        print("A thick fog rolls in. Ahead , a bridge made of shimmering light crosses a bottomles pit.")
        time.sleep(3)
        print("A tall, hooded figure blocks the path. It speaks in two voices at once.")
        time.sleep(3)
        print("To cross, you must pay. Give me 30 gold, or answer the riddle for free.")
        time.sleep(3)
        print("What do you do?")
        time.sleep(2)
        qu2 = input("Option (1). Pay  |  Option (2). Try the riddle: ")
        if qu2 == "1":
            if game_state["gold"] < 30:
                print("You check your pockets and you dont have enough gold.")
                time.sleep(3)
                print("The figure screams and you fall.")
                time.sleep(3)
                print("You manage to scramble accros but you are badly hurt.")
                print("-30HP")
                game_state["player_hp"] -= 30
                False
                break
            else:
                print("You hand over the gold and the figure disapears into the fog.")
                print(f"{BOLD}LEVEL PASSED!{END}")
                False
                break
        elif qu2 == "2":
            print("The figure whispers:")
            print("I have cities but no houses.")
            time.sleep(2)
            print("I have mountains but no trees.")
            time.sleep(2)
            print("I have water but no fish.")
            time.sleep(2)
            rid = input("What am I? ").lower().strip()
            if rid == "map":
                print("The figure let out a hollow laugh.  'Correct , Pass traveler.")
                print(f"{BOLD}LEVEL PASSED!{END}")
                False
                break
            else:
                print("The figure tilts his head.  'Incorrect'")
                print("It strikes you with a staff of shadows!")
                time.sleep(2)
                print("-30HP")
                print("You barely make it to the other side gasping for air.")
                False
                break
        else:
            True
def lvl3 ():
    status_check()
    print(f"{BOLD}---LEVEL 3: THE ECHOING HALL---{END}")
    time.sleep(3)
    print("The air here is freezing. You see your own breath misting in the air.")
    time.sleep(3)
    print("A shadow reflection rises from the floor. It looks exactly like you?")
    time.sleep(3)
    print("The reflection charges! What do you do?")
    time.sleep(2)
    qu3 = input("Option (1). Stand your ground and fight!  |  Option (2). Try to reason with it. ")
    enemy_hp = 60
    if qu3 == "1":
        print("You draw your weapon! The shadow mimics your every move.")
        while enemy_hp > 0:
            time.sleep(2)
            enemy_hp = attack(enemy_hp=enemy_hp)
            if enemy_hp > 0:
                print(f"The shadow has {enemy_hp}HP left and strikes back!")
                time.sleep(2)
                game_state["player_hp"] -= 15
                print(f"You took 15 damage! Current HP: {game_state['player_hp']}")
                time.sleep(2)
                alive_check()
                
            else:
                print(f"{BOLD}THE SHADOW DISOLVES!{END}")
                game_state["gold"] += 35
                print("You found 35 gold in the dark.")
                time.sleep(2)
                print(f"{BOLD}LEVEL PASSED!{END}")
    elif qu3 == "2":
        print ("You try to run, but the doors have vanished. There is no escape!")
        lvl3()
    else:
        lvl3()
        return
def lvl4 ():
    status_check()
    print(f"{BOLD}---LEVEL 4: THE ALCHEMIST'S ARCHIVE---{END}")
    time.sleep(3)
    print("The air smells of sulfur and old parchment.")
    time.sleep(3)
    print("A desk sits in the centre, with two glowing vials.")
    time.sleep(3)
    print("A magical voice echos 'One will heal your soul... The other fills your pockets.'")
    time.sleep(3)
    print("Behind the desk, a massive stone door is locked by a riddle of weight.")
    time.sleep(3)
    qu4 = input("Option (1). Drink the red vial | Option (2). Drink the gold vial | Option (3). Inspect the door: ")
    time.sleep(2)
    if qu4 =="1":
        print("You feel a surge of enegy! Your skin feels like energy.")
        time.sleep(2)
        if game_state["player_hp"] <=50:
            game_state["player_hp"] += 50
        elif game_state["player_hp"] >=50:
            game_state["player_hp"] =+ 100
        print(f"{BOLD}Your HP was boosted!{END}")
        time.sleep(2)
        print("The stone door opens slowly. You are ready for what comes next...")
    elif qu4 =="2":
        print("The liquid tastes like honey and coins. You feel heavier.")
        time.sleep(2)
        game_state["gold"] += 75
        print(f"{BOLD}+100 Gold found!{END}")
        time.sleep(2)
        print("But as you take the gold , a trap triggers! Darts fly from the walls.")
        time.sleep(2)
        game_state["player_hp"] -= 20
        print("You took 20 damage escaping the room.")
        alive_check()
    elif qu4 == "3":
        print("You ignore the potions and look to the door.")
        time.sleep(2)
        print("It says: 'To pass without a key, you must give what you cannot keep.")
        time.sleep(2)
        choice = input("Will you give 15HP to the door? (yes/no)")
        if choice =="yes":
            game_state["player_hp"] -= 15
            print("The door drinks your life. It begins to make noise...")
            time.sleep(2)
            print("The door remains shut. You have no choice but to pick a vial.")
            lvl4()
    else:
        lvl4()
        return
    print(f"{BOLD}LEVEL PASSED! THE BOSS DOOR LIES AHEAD...{END}")
    time.sleep(2)
def boss_lvl():
    status_check()
    print(f"{BOLD}---FINAL LEVEL: THE THRONE OF THE VOID---{END}")
    time.sleep(3)
    print("The air is heavy. Lightning ripples accros a black sky.")
    time.sleep(3)
    print("Before the great gates stands a giant staue made of rusted armour and a blue flame.")
    time.sleep(2)
    print(f"{BOLD}The gatekeeper has appered!{END}")
    time.sleep(2)
    print(f"{BOLD}---PART 1: THE BOSS GUARD---{END}")
    time.sleep(2)
    print("Gatekeeper:'No one shall disturb the masters slumber!")
    time.sleep(2)
    enemy_hp = 100
    while enemy_hp > 0 and game_state["player_hp"] > 0:
        print(f"You:({game_state['player_hp']}) VS Enemy:({enemy_hp})")
        action = input("Do you (1).Attack  |  (2). Use item ")
        if action =="1":
            enemy_hp = attack(enemy_hp=enemy_hp)
            if enemy_hp > 0:
                game_state["player_hp"] -= 15
                time.sleep(2)
                print("The gatekeeper swings his flame-sword! You take -15 damage!")
                time.sleep(2)
        elif action =="2":
            use_item()
            print("The gatekeeper attcks when your distracted!")
            game_state["player_hp"]-=10
        else:
            print("Indecision is deadly! The gatekeeper strikes!")
            game_state["player_hp"] -=5
        alive_check()
    print(f"{BOLD}---PART 2: THE VOID ALTAR---{END}")
    time.sleep(2)
    print("In the centre of the hall is a glowing altar.")
    time.sleep(1)
    print(f"Curently you have: {game_state['gold']} Gold.")
    time.sleep(2)
    print("A voice whispers:'Offer your riches to surive the end...")
    altar = input("Option (1) Offer 50 gold for life essence | Option (2) Keep your gold and move on.")
    if altar =="1":
        if game_state["gold"] >= 50:
            game_state["gold"] -= 50
            game_state["player_hp"] =+100
            print(f"{BOLD}Your wounds knit together. HP boosted!{END}")
            status_check()
        else:
            print("The altar rejects you, you are too poor.")
    elif altar =="2":
        print("You walk past the altar. You feel a chill down your spine.")
    else:
        print("Impressive. You've selected an answer that doesnt exist.")
        time.sleep(2)
        print("The altar flickers... Time resets.")
        boss_lvl()
        return
    print(f"{BOLD}---PART 3: THE FINAL BOSS---{END}")
    print("\n"+"=*40")
    time.sleep(2)
    print(f"{BOLD}THE VOID SOVEREIGN RISES FROM THE THRONE!{END}")
    time.sleep(2)
    print("So... a mortal has made it this far. Let's see if you can bleed.")
    enemy_hp2 = 150
    while enemy_hp2 > 0 and game_state["player_hp"] > 0:
            enemy_hp = attack(enemy_hp=enemy_hp2)
            time.sleep(2)
            if enemy_hp2 > 0:
                game_state["player_hp"] -= 20
                print("THE VOID SOVEREIGN HAS HIT YOU!")
                alive_check()
    time.sleep(4)
    print(f"{BOLD}THE SOVEREIGN FALLS!! The darknes fades...{END}")
    time.sleep(3)
    print("The world begins to brighten. You have saved the realm.")
    time.sleep(2)
    print(f"{BOLD}CONGRATULATIONS! YOU HAVE COMPLETED THE GAME!{END}")
    time.sleep(5)
    exit()



intro()
lvl1()
traveling1()
alive_check()
shop()
use_item()
lvl2()
alive_check()
shop()
use_item()
lvl3()
traveling1()
alive_check()
shop()
use_item()
lvl4()
alive_check()
shop()
use_item()
boss_lvl()
