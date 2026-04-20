import time
import random
import json
import os
try:
    with open("game/leaderboard","r") as f:
        data = json.load(f)
except (FileNotFoundError,json.JSONDecodeError):
    data = {}
BOLD = '\033[1m'
END = '\033[0m'

game_state = {
    "player_hp" : 100,
    "sheild" : 20,
    "boss_hp": 500,
    "gold": 10,
    "inventory":[],
    "karma":0
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
    global usr_name
    usr_name = input("Hello traveler, what is your name? ")
    print(f"Welcome {usr_name}, and goodluck on your travels.") 
    if usr_name =="ADMIN_USER2707":
        game_state["gold"] = 999999
        game_state["sheild"] = 999999
        game_state["player_hp"] = 999999
        game_state["inventory"].append("Starforged blade")
    else:
        print("Here is a gift for you: A Health potion!")
        game_state["inventory"].append("Health potion")
        pause()
def status_check():
    print("-"*20)
    print(f"HP: {game_state['player_hp']}  | Gold: {game_state['gold']}   | Sheild: {game_state['sheild']}   | Inventory: {game_state['inventory']}")
def shop():
    shop_data ={
        "1": ["Health potion",20,"item"],
        "2": ["Mega potion",25,"item"],
        "3": ["Mini sheild potion",30,"item"],
        "4": ["Big sheild potion",35,"item"],
        "5": ["Sword crate",25,"crate"],
        "6": ["Exit",0,"Exit"]
    }
    while True:
        print(f"Welcome to the shop you have {game_state['gold']} gold to spend.")
        print("What would you like to buy?")
        print("1.Health potion (20 Gold)")
        print("2.Mega potion (25 Gold)")
        print("3.Mini sheild potion (30 Gold)")
        print("4.Big sheild potion (35 Gold)")   
        print("5.Sword crate(25 Gold)") 
        print("6.Exit") 
        pause() 
        purchase = input("1,2,3,4,5,6: ")
        if purchase in shop_data:
                if game_state["karma"] >= 40:
                    item_info =shop_data[purchase]
                    name = item_info[0]
                    price = int(item_info[1]*0.8)
                    category = item_info[2]
            
                elif game_state["karma"] <= -40:
                    item_info =shop_data[purchase]
                    name = item_info[0]
                    price = int(item_info[1]*1.3)
                    category = item_info[2]
                
                else:
                    item_info =shop_data[purchase]
                    name = item_info[0]
                    price = item_info[1]
                    category = item_info[2]

                if game_state["gold"] >= price and len(game_state["inventory"]) <3:
                    game_state["gold"] -= price
                    if category == "item":
                        print(f"You purchased a {name}!")
                        game_state["inventory"].append(name)
                    elif category == "crate":
                        swords =["Wooden stick" , "Wooden sword" , "Iron sword" , "Starforged blade"]
                        weights =[60 , 30 , 7 , 3]
                        new_sword = random.choices(swords, weights=weights,k=1)[0]
                        print(f"Inside you got a {BOLD}{new_sword}{END}!")
                        if new_sword not in game_state["inventory"]:
                            game_state["inventory"].append(new_sword)
                            print(f"You equip the {new_sword}")
                    elif category == "Exit":
                        print("Goodbye.")
                        break
                else:
                    print("You don't have enough gold , or your pockets are full")
        else:
            print("Wow! 6 options and you decicde to pick not existing ones.")
def alive_check():
    if game_state["player_hp"] <= 0 and game_state["sheild"] <= 0:
     game_over()
def lvl1_n():
    pause()
    clear()
    status_check()
    print(f"{BOLD} ---LEVEL 1: THE TANGLED WILDS--- {END}") 
    print("You wake up on a cold bed of moss. The trees above are thick and twisted.")
    print("You check your pockets: 10 gold and a small potion. Better than nothing.")
    print("As you stand up, a starving Wolf emerges from the shadows, growling.") 
    print("What do you do?") 
    pause()
    while True:
        ans1 = input("Option 1. Fight!   Option 2. Distract: ") 
        if ans1 =="1":
            attack(enemy_hp=20)
            time.sleep(1)
            game_state["gold"] += 20
            print(f"{BOLD}LEVEL PASSED! {END}")
            game_state["karma"] -= 20
            break
        elif ans1 =="2":
            take_damage(damage=15)
            game_state["karma"] += 20
            break
        else:
            game_state["player_hp"] -= 15
            print("If you're seeing this,you've done something wrong. well done")
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
def lvl2_N():
    True
    while True:
        pause()
        clear()
        status_check()
        print(f"{BOLD}---LEVEL 2: THE WHISPERING BRIDGE---{END}")
        print("A thick fog rolls in. Ahead , a bridge made of shimmering light crosses a bottomles pit.")
        print("A tall, hooded figure blocks the path. It speaks in two voices at once.")
        print("To cross, you must pay. Give me 30 gold, or answer the riddle for free.")
        print("What do you do?")
        pause()
        qu2 = input("Option (1). Pay  |  Option (2). Try the riddle: ")
        if qu2 == "1":
            if game_state["gold"] < 30:
                print("You check your pockets and you dont have enough gold.")
                print("The figure screams and you fall.")
                pause()
                print("You manage to scramble accros but you are badly hurt.")
                print("-30HP")
                take_damage(damage=30)
                game_state["karma"] -= 10
                break
            else:
                print("You hand over the gold and the figure disapears into the fog.")
                print(f"{BOLD}LEVEL PASSED!{END}")
                game_state["karma"] -= 10
                break
        elif qu2 == "2":
            print("The figure whispers:")
            print("I have cities but no houses.")
            print("I have mountains but no trees.")
            print("I have water but no fish.")
            rid = input("What am I? ").lower().strip()
            if rid == "map":
                print("The figure let out a hollow laugh.  'Correct , Pass traveler.")
                print(f"{BOLD}LEVEL PASSED!{END}")
                game_state["karma"] += 5
                break
            else:
                print("The figure tilts his head.  'Incorrect'")
                print("It strikes you with a staff of shadows!")
                time.sleep(1)
                print("-30HP")
                take_damage(damage=30)
                print("You barely make it to the other side gasping for air.")
                game_state["karma"] -= 15
                break
        else:
            print("The town wizard sighs. 'It's 1, 2, or 3, kid. It's not alchemy.'")
def lvl2_G():
    pause()
    clear()
    print(f"{BOLD}---LEVEL 2-G: THE BRIDGE OF SERENITY---{END}")
    print("The air turns sweet with the scent of mountain lavender as the mist parts.")
    print("Before you lies a bridge of pale marble, glowing softly above a sea of white clouds.")
    print("An old monk in tattered saffron robes sits by the path, fumbling with a cold brass lantern.")
    print("'Kind traveler,' he rasps, 'the light has failed me, and the road ahead is long.'")
    pause()
    print("1. Take his hand and guide him through the fog.")
    print("2. Give him a Health Potion to restore his strength.")
    print("3. Snatch his heavy coin purse and shove him aside.")
    pause() 
    
    choice = input("What do you do? ")
    while True:
        if choice == "1":
            print("\nYou lead him across. He hums a melody that makes your old wounds knit together.")
            game_state["karma"] += 10
            game_state["player_hp"] = min(100, game_state["player_hp"] + 15)
            print(f"{BOLD}The monk's blessing heals you! +15 HP{END}")
            break
        elif choice == "2":
            if "Health potion" in game_state["inventory"]:
                game_state["inventory"].remove("Health potion")
                print("\nThe monk drinks and glows with vigor. He presses a silk pouch of gold into your hand.")
                game_state["karma"] += 20
                game_state["gold"] += 45
                print(f"{BOLD}A generous trade! +45 Gold{END}")
                break
            else:
                print("\nYou have no potions to give, so you guide him across the marble path instead.")
                game_state["karma"] += 5
                break
        elif choice == "3":
            print("\nYou wrench the gold from his hands. The sky bruises purple as a bolt of divine lightning strikes!")
            game_state["karma"] -= 25
            game_state["gold"] += 65
            take_damage(damage=20)
            print(f"{BOLD}You take what you want, but the spirits are angry. +65 Gold | -20 HP{END}")
            alive_check()
            break
        else:
            print("Oh, a rebel! Choosing Option 4 when there are only 3. How's that working out for you?")
        alive_check()
        print(f"{BOLD}LEVEL PASSED!{END}")
def lvl2_B():
    pause()
    clear()
    print(f"{BOLD}---LEVEL 2-B: THE OBSIDIAN TOLL---{END}")
    print("The air grows thick with the stench of sulfur and charred bone.")
    print("A bridge of jagged black glass spans a river of slow-moving lava.")
    print("A scarred Mercenary stands guard, sharpening a wicked-looking blade.")
    print("'Blood or gold, traveler,' he sneers. 'Nothing crosses this bridge for free.'")
    pause() 
    print("1. Hand over a 'tribute' (15HP) to let you pass unchallenged.")
    print("2. Attack the Mercenary to take his loot (Hard Fight).")
    print("3. Try to pay his debt with 40 Gold to spare him and change your path.")
    pause() 
    choice = input("What is your move? ")
    while True:
        if choice == "1":
            print("\nYou let the Mercenary draw blood from your arm as a dark ritual.")
            print("He laughs, stepping aside as the obsidian bridge glows a sickly red.")
            game_state["karma"] -= 10
            take_damage(damage=15)
            print(f"{BOLD}You paid in blood. -15 HP | -10 Karma{END}")
            alive_check()
            break
        elif choice == "2":
            print("\nYou draw your steel! The Mercenary is a seasoned killer.")
            enemy_hp = 80 # Harder than the neutral wolf or shadow
            while enemy_hp > 0:
                enemy_hp = attack(enemy_hp)
                if enemy_hp > 0:
                    print("The Mercenary counters with a brutal strike!")
                    take_damage(damage=30)
            print(f"{BOLD}You stand over his body and raid his pockets. +55 Gold | -20 Karma{END}")
            game_state["gold"] += 55
            game_state["karma"] -= 20
            break
        elif choice == "3":
            if game_state["gold"] >= 40:
                game_state["gold"] -= 40
                print("\nYou offer him enough gold to quit this life of murder.")
                print("He looks stunned, lowers his sword, and walks away into the haze.")
                game_state["karma"] += 25
                print(f"{BOLD}A spark of light in the dark. -40 Gold | +25 Karma{END}")
                break
            else:
                print("\nYou reach for your gold, but you're too poor. He takes it as an insult!")
                print("The Mercenary lunges at you!")
                time.sleep(1)
                # Forced fight because the player failed the 'Good' check
                take_damage(damage=20)
                print("-20 HP from the surprise attack!")
                alive_check()
                break
        else:
            print("I've lived through a thousand playthroughs, and never have I seen someone try to do... whatever it is you just typed.")
        print(f"{BOLD}LEVEL PASSED!{END}")
def lvl3_N():
    pause()
    clear()
    status_check()
    print(f"{BOLD}---LEVEL 3: THE ECHOING HALL---{END}")
    print("The air here is freezing. You see your own breath misting in the air.")
    print("A shadow reflection rises from the floor. It looks exactly like you?")
    print("The reflection charges! What do you do?")
    pause()
    while True:
        qu3 = input("Option (1). Stand your ground and fight!  |  Option (2). Try to reason with it. ")
        enemy_hp = 60
        if qu3 == "1":
            print("You draw your weapon! The shadow mimics your every move.")
            game_state["karma"] -= 20
            while enemy_hp > 0:
                time.sleep(1)
                enemy_hp = attack(enemy_hp=enemy_hp)
                time.sleep(1)
                if enemy_hp > 0:
                    print(f"The shadow has {enemy_hp}HP left and strikes back!")
                    time.sleep(1)
                    take_damage(damage=25)
                    print(f"You took 15 damage!|Current HP: {game_state['player_hp']}|Current Shield:{game_state['sheild']}")
                    time.sleep(1)
                    alive_check()
                    
                else:
                    print(f"{BOLD}THE SHADOW DISOLVES!{END}")
                    game_state["gold"] += 35
                    print("You found 35 gold in the dark.")
                    time.sleep(1)
                    print(f"{BOLD}LEVEL PASSED!{END}")
                    break
        elif qu3 == "2":
            print ("You try to run, but the doors have vanished. There is no escape!")
            game_state["karma"] += 20
            break
        else:
            print("Error 404: Player's sense of direction not found.")
def lvl3_G():
    pause()
    clear()
    status_check()
    print(f"{BOLD}---LEVEL 3-G: THE HALL OF ANCESTORS---{END}")
    print("The air is thick with golden incense, but the floor is littered with the bones of unworthy knights.")
    print("A colossal Spirit of a High Priest stands before the exit, his eyes burning like white stars.")
    print("'Only the pure or the penitent may pass,' he booms. 'Prove your worth, or be purged.'")
    print("He raises a glowing palm, ready to strike.")
    pause() 
    print("1. Kneel and offer 25 Gold as a tithe to the temple.")
    print("2. Attempt to walk through his holy fire to prove your courage.")
    print("3. Blow a handful of sulfur into the Spirit's face and run!")
    pause() 
    qu3g = input("What is your choice? ")
    while True:
        if qu3g == "1":
            if game_state["gold"] >= 25:
                game_state["gold"] -= 25
                game_state["karma"] += 15
                print("\nThe Priest lowers his hand. 'Your humility is your shield, traveler.'")
                print(f"{BOLD}The path opens. -25 Gold | +15 Karma{END}")
            else:
                print("\nYou have no gold! The Priest strikes you for your empty promises.")
                take_damage(damage=35)
                print(f"{BOLD}HOLY BLAST! -35 Damage{END}")
                alive_check()
                break
        elif qu3g == "2":
            print("\nYou step into the white flames. It is a test of will.")
            # 50/50 chance of a blessing or a burn
            if random.randint(1, 2) == 1:
                print("The fire feels like cool water. Your spirit is strengthened!")
                game_state["player_hp"] = min(100, game_state["player_hp"] + 20)
                game_state["karma"] += 20
                print(f"{BOLD}+20 HP | +20 Karma{END}")
            else:
                print("The flames sear your flesh! You weren't as pure as you thought.")
                game_state["player_hp"] -= 30
                print(f"{BOLD}CRITICAL BURN! -30 HP{END}")
                alive_check()
                break
        elif qu3g == "3":
            print("\nThe sulfur reacts with the holy mist, causing a violent explosion!")
            print("You scramble through the exit as the hall collapses behind you.")
            game_state["gold"] += 40
            game_state["karma"] -= 25
            take_damage(damage=25)
            print(f"{BOLD}+40 Gold | -25 HP from debris | -25 Karma{END}")
            alive_check()
            break
        else:
            print("The gods gave you three paths. You chose to walk into a brick wall. Please try again.")
        print(f"{BOLD}LEVEL PASSED!{END}")
def lvl3_B():
    pause()
    clear() 
    status_check()
    print(f"{BOLD}---LEVEL 3-B: THE PIT OF PENANCE---{END}")
    print("The walls here are stained with soot, and the floor is a grate over a bottomless drop.")
    print("A Tormented Soul rises from the steam, its face twisted in a silent scream.")
    print("'You carry the scent of a sinner,' it hisses, reaching out with spectral claws.")
    print("The air grows freezing cold as the spirit prepares to drain your life.")
    pause() 
    print("1. Sacrifice your memories (Lose 20HP) to satisfy its hunger.")
    print("2. Fight the Soul to steal its necrotic essence (Hard Fight).")
    print("3. Pray for its release and offer 50 Gold to hallow the ground.")
    pause() 
    qu3b = input("What is your choice? ")
    while True:
        if qu3b == "1":
            print("\nYou stand still as the ghost passes through you, chilling your very soul.")
            print("The pain is agonizing, but the spirit vanishes into the floor.")
            game_state["karma"] -= 10
            take_damage(damage=20)
            print(f"{BOLD}-20 HP | -10 Karma{END}")
            break
        elif qu3b == "2":
            print("\nYou strike at the mist! The Soul shrieks, lashing out with icy hate.")
            enemy_hp = 90
            while enemy_hp > 0:
                enemy_hp = attack(enemy_hp)
                if enemy_hp > 0:
                    print("The Soul claws at your chest!")
                    take_damage(damage=25)
                    alive_check()
            print(f"{BOLD}The Soul dissipates. You find a dark gem in the ashes! +75 Gold{END}")
            game_state["gold"] += 75
            game_state["karma"] -= 20
            break
        elif qu3b == "3":
            if game_state["gold"] >= 50:
                game_state["gold"] -= 50
                game_state["karma"] += 35
                print("\nYou scatter gold across the grate while reciting an old blessing.")
                print("The Soul stops screaming. It glows with a soft light and fades peacefully.")
                print(f"{BOLD}The curse lifts. -50 Gold | +35 Karma{END}")
                break
            else:
                print("\nYou don't have enough gold to hallow this place! The Soul is insulted.")
                print("It lunges, tearing into your armor!")
                take_damage(damage=30)
                alive_check()
                break
        else:
            print("I spent weeks coding this world, and you're trying to invent a fourth option? The audacity.")   
        print(f"{BOLD}LEVEL PASSED!{END}")
def lvl4_N():
    pause()
    clear()
    status_check()
    print(f"{BOLD}---LEVEL 4: THE ALCHEMIST'S ARCHIVE---{END}")
    print("The air smells of sulfur and old parchment.")
    print("A desk sits in the centre, with two glowing vials.")
    print("A magical voice echos 'One will heal your soul... The other fills your pockets.'")
    print("Behind the desk, a massive stone door is locked by a riddle of weight.")
    pause() 
    qu4 = input("Option (1). Drink the red vial | Option (2). Drink the gold vial | Option (3). Inspect the door: ")
    if qu4 =="1":
        print("You feel a surge of enegy! Your skin feels like energy.")
        time.sleep(1)
        if game_state["player_hp"] <=50:
            game_state["player_hp"] += 50
        elif game_state["player_hp"] >=50:
            game_state["player_hp"] =+ 100
        print(f"{BOLD}Your HP was boosted!{END}")
        print("The stone door opens slowly. You are ready for what comes next...")
        game_state["karma"] += 10
    elif qu4 =="2":
        print("The liquid tastes like honey and coins. You feel heavier.")
        game_state["gold"] += 75
        print(f"{BOLD}+100 Gold found!{END}")
        print("But as you take the gold , a trap triggers! Darts fly from the walls.")
        take_damage(damage=25)
        print("You took 20 damage escaping the room.")
        pause() 
        alive_check()
        game_state["karma"] -= 15
    elif qu4 == "3":
        print("You ignore the potions and look to the door.")
        print("It says: 'To pass without a key, you must give what you cannot keep.")
        choice = input("Will you give 15HP to the door? (yes/no)")
        if choice =="yes":
            game_state["player_hp"] -= 15
            alive_check()
            print("The door drinks your life. It begins to make noise...")
            time.sleep(2)
            print("The door remains shut. You have no choice but to pick a vial.")
            lvl4_N()
        else:
            print("OK. You just continue...")
    else:
        print("Your character stares blankly into the void, unsure of how to perform an action that doesn't exist.")
        lvl4_N()
        return
    print(f"{BOLD}LEVEL PASSED! THE BOSS DOOR LIES AHEAD...{END}")
    time.sleep(2)
def lvl4_G():
    pause()
    clear()
    status_check()
    print(f"{BOLD}---LEVEL 4-G: THE SANCTUARY OF CURES---{END}")
    print("The Archive is filled with the scent of dried roses and ancient parchment.")
    print("A Kind Alchemist is busy mixing a glowing blue elixir in a crystal flask.")
    print("'Ah, a traveler of light!' he beams. 'I have a gift for you, but my supplies are low.'")
    print("Behind him, a massive door of white oak waits for a selfless key.")
    pause() 
    print("1. Donate 30 Gold to help his research for a blessing.")
    print("2. Offer a bit of your 'Life Spark' (10HP) to power the elixir.")
    print("3. Smash his flasks and steal his secret stash of gold.")
    pause() 
    qu4g = input("Choice: ")
    while True:
        if qu4g == "1":
            if game_state["gold"] >= 30:
                game_state["gold"] -= 30
                game_state["karma"] += 15
                print("\n'Your generosity saves lives!' He splashes you with a potion of protection.")
                game_state["sheild"] = min(100, game_state["sheild"] + 40)
                print(f"{BOLD}+40 Shield | +15 Karma{END}")
                break
            else:
                print("\nYou reach for gold but find none. He sighs and gives you a small bandage instead.")
                game_state["player_hp"] = min(100, game_state["player_hp"] + 5)
                game_state["karma"] += 5
                break
        elif qu4g == "2":
            print("\nYou let the Alchemist draw a drop of glowing energy from your palm.")
            print("The elixir turns brilliant gold, and he shares a draught of it with you.")
            game_state["karma"] += 20
            take_damage(damage=10)
            game_state["player_hp"] = min(100, game_state["player_hp"] + 40)
            print(f"{BOLD}The potion surges through you! +40 HP (Net +30) | +20 Karma{END}")
            break
        elif qu4g == "3":
            print("\nYou shatter the glass! The Alchemist flees in terror as you raid the shelves.")
            game_state["gold"] += 90
            game_state["karma"] -= 35
            print("In the chaos, a cloud of toxic fumes burns your lungs.")
            take_damage(damage=20)
            print(f"{BOLD}+90 Gold | -20 HP from fumes | -35 Karma{END}")
            alive_check()
            break
        else:
            print("A passing squirrel judges your inability to follow simple instructions.")
        print(f"{BOLD}LEVEL PASSED! THE FINAL BOSS AWAITS...{END}")
def lvl4_B():
    pause()
    clear()
    status_check()
    print(f"{BOLD}---LEVEL 4-B: THE POISONER'S LAB---{END}")
    print("The air here is green and heavy with the smell of rotted meat and acid.")
    print("A Mad Chemist cackles as he stirs a cauldron of bubbling, black sludge.")
    print("'More ingredients for the pot!' he shrieks, pointing a jagged syringe at you.")
    print("The door behind him is barred by rusted iron chains that pulse with dark energy.")
    pause() 
    print("1. Throw a 'Volatile Potion' at the door to blast it open.")
    print("2. Fight the Chemist to take his 'Master Key'.")
    print("3. Pour your own Health Potion into the cauldron to purify the room.")
    pause() 
    qu4b = input("Choice: ")
    while True:
        if qu4b == "1":
            print("\nThe explosion is deafening! The chains shatter, but the blast catches you too.")
            game_state["karma"] -= 10
            take_damage(damage=25)
            print(f"{BOLD}The door is open, but you are scorched. -25 HP | -10 Karma{END}")
            alive_check()
            break
        elif qu4b == "2":
            print("\nYou charge the Mad Chemist! He splashes acid at your face.")
            enemy_hp = 110
            while enemy_hp > 0:
                enemy_hp = attack(enemy_hp)
                if enemy_hp > 0:
                    print("The Chemist stabs with his syringe!")
                    take_damage(damage=30)
                    alive_check()
            print(f"{BOLD}He falls into his own brew. You find a heavy purse on his belt. +85 Gold{END}")
            game_state["gold"] += 85
            game_state["karma"] -= 20
            break
        elif qu4b == "3":
            if "Health potion" in game_state["inventory"]:
                game_state["inventory"].remove("Health potion")
                game_state["karma"] += 40
                print("\nThe black sludge turns to clear water. The Chemist gasps and regains his sanity.")
                print("'Thank you... I was lost.' He unlocks the door and hands you 20 Gold.")
                game_state["gold"] += 20
                print(f"{BOLD}Room Purified! +20 Gold | +40 Karma{END}")
                break
            else:
                print("\nYou have no potion! The Chemist laughs at your failed gesture and strikes.")
                take_damage(damage=35)
                alive_check()
                break
        else:
            print("You try to perform the forbidden action. The universe glitches for a second, then politely asks you to pick a real choice.")
        print(f"{BOLD}LEVEL PASSED! PREPARE FOR THE END...{END}")
def boss_lvl():
    pause()
    clear()
    status_check()
    print(f"{BOLD}---FINAL LEVEL: THE THRONE OF THE VOID---{END}")
    print("The air is heavy. Lightning ripples accros a black sky.")
    print("Before the great gates stands a giant staue made of rusted armour and a blue flame.")
    print(f"{BOLD}The gatekeeper has appered!{END}")
    pause() 
    print(f"{BOLD}---PART 1: THE BOSS GUARD---{END}")
    print("Gatekeeper:'No one shall disturb the masters slumber!")
    pause() 
    enemy_hp = 75
    while enemy_hp > 0 and game_state["player_hp"] > 0:
        print(f"You:({game_state['player_hp']}) VS Enemy:({enemy_hp})")
        action = input("Do you (1).Attack  |  (2). Use item ")
        if action =="1":
            enemy_hp = attack(enemy_hp=enemy_hp)
            if enemy_hp > 0:
                    take_damage(damage=25)
                    time.sleep(1)
                    print("The gatekeeper swings his flame-sword! You take -15 damage!")
                    time.sleep(1)
        elif action =="2":
            use_item()
            print("The gatekeeper attcks when your distracted!")
            take_damage(damage=10)
        else:
            print("Indecision is deadly! The gatekeeper strikes!")
            take_damage(damage=25)
        alive_check()
    print(f"{BOLD}---PART 2: THE VOID ALTAR---{END}")
    print("In the centre of the hall is a glowing altar.")
    print(f"Curently you have: {game_state['gold']} Gold.")
    print("A voice whispers:'Offer your riches to surive the end...")
    pause() 
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
        print("The altar flickers... Time resets.")
        time.sleep(1)
        boss_lvl()
        return
    print(f"{BOLD}---PART 3: THE FINAL BOSS---{END}")
    print(f"{BOLD}THE VOID SOVEREIGN RISES FROM THE THRONE!{END}")
    print("So... a mortal has made it this far. Let's see if you can bleed.")
    pause()
    enemy_hp2 = 125
    while enemy_hp2 >0:
            enemy_hp2 = attack(enemy_hp=enemy_hp2)
            time.sleep(2)
            if enemy_hp2 > 0:
                take_damage(damage=25)
                print("THE VOID SOVEREIGN HAS HIT YOU!")
                alive_check()
    time.sleep(3)
    print(f"{BOLD}THE SOVEREIGN FALLS!! The darknes fades...{END}")
    time.sleep(2)
    print("The world begins to brighten. You have saved the realm.")
    time.sleep(2)
    print(f"{BOLD}CONGRATULATIONS! YOU HAVE COMPLETED THE GAME!{END}")
    time.sleep(5)
    exit()
def save_to_leaderboard():
    # 1. Calculate the score
    p_score = game_state["gold"] * 2
   
    # 2. Try to load existing data first so we can add to it
    try:
        with open("leaderboard.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # 3. Add the current player's score to the data dictionary
    data[usr_name] = p_score

    # 4. Save the updated dictionary back to the file
    with open("leaderboard.json", "w") as f:
        json.dump(data, f)

    # 5. Display the neat leaderboard
    print("\n" + "="*30)
    print("      GLOBAL LEADERBOARD")
    print("="*30)
   
    # Sort by score (item[1]) in descending order
    sorted_leaderboard = sorted(data.items(), key=lambda item: item[1], reverse=True)
   
    for position, (name, score) in enumerate(sorted_leaderboard, start=1):
        # The :<15 creates padding for a neat column look
        print(f"{position}. {name:<15} | {score} points")
    print("="*30)
def take_damage(damage=25):
    if game_state["sheild"] >= damage:
        game_state["sheild"] -= damage
    elif game_state["sheild"] < damage and game_state["sheild"] > 0:
        current_sheild = game_state["sheild"]
        game_state["sheild"] = 0
        remaining = damage - current_sheild
        game_state["player_hp"] -= remaining
    else:
        game_state["player_hp"] -= damage
        alive_check()
def run():

    intro()
    lvl1_n()
    status_check()
    traveling1()
    alive_check()
    shop()
    use_item()
    if game_state["karma"] >= 40:
        lvl2_G()
    elif game_state["karma"] <= -40:
        lvl2_B()
    else:
        lvl2_N()
    alive_check()
    shop()
    use_item()
    if game_state["karma"] >= 40:
        lvl3_G()
    elif game_state["karma"] <= -40:
        lvl3_B()
    else:
        lvl3_N()
    traveling1()
    alive_check()
    shop()
    use_item()
    if game_state["karma"] >= 40:
        lvl4_G()
    elif game_state["karma"] <= -40:
        lvl4_B()
    else:
        lvl4_N()
    alive_check()
    shop()
    use_item()
    boss_lvl()
    save_to_leaderboard()
def pause():
    time.sleep(0.5)
    input(f"{BOLD}[Press Enter to continue]{END}")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
run() 
