# Currency converter
valid = True
while valid == True:
    opt = input("Convert and budget (1) or just budget (2) (Enter '1' or '2'): ")
    if opt == "1":
        money = float(input("Enter amount of money you have remaining (GBP): "))
        days = float(input("Enter days left on holiday: "))
        print (money/days*1.36, "USD per day")
        Try_again = False
        while True:
            try2 = input("Would you like to play again? Yes (1) No (2) ")
            if try2 =="1":
                break
            elif try2 =="2":
                print("Goodbye!")
                exit()
            else:    
                print("Error! Enter 1 or 2. Try again")
                
    elif opt == "2":
        money2 = float (input("Enter amount of money you have remaining (USD): "))
        days2 = float(input("Enter days left on holiday: "))
        print (money2/days2,"USD per day")
        Try_again = False
        while True:
            try2 = input("Would you like to play again? Yes (1) No (2) ")
            if try2 =="1":
                break
            elif try2 =="2":
                print("Goodbye!")
                exit()
            else:    
                print("Error! Enter 1 or 2. Try again")



    



