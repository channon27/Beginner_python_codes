is_valid = True 

password = input("Enter your password: " )

if len(password) < 8:
    is_valid = False
    print("Error: Too short!")

if "@" not in password:
    is_valid = False
    print("Error: Needs '@' symbol")

if is_valid == True:
    print ("Succses")
