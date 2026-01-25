# Currency converter
opt = input("Convert and budget or just budget (enter 'convert' or 'budget'): ")
if opt == "convert":
    money = float(input("Enter amount of money you have remaining (GBP): "))
    days = float(input("Enter days left on holiday: "))
    print (money/days*1.36, "USD per day")
else:
    money2 = float (input("Enter amount of money you have remaining (USD): "))
    days2 = float(input("Enter days left on holiday: "))
    print (money2/days2,"USD per day")
    



