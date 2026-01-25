is_valid = False #switch is off
while is_valid == False: #when switch is off run code 
  is_valid = True # switch is on 
  password = input("Enter your password: " ) 

  if len(password) < 8:
    is_valid = False
    print("Error: Too short!")

  if len(password) > 25:
    is_valid = False
    print("Error: Too long!")
  
  if password.islower():
    is_valid = False
    print("Error: Needs at least one uppercase character" )

  #checking if any charcater is a digit 
  has_digit = False
  for char in password: #for evey charcter hceck if any has a digit 
    if char.isdigit():
      has_digit = True

  if has_digit == False:
    is_valid = False
    print("Error: Needs at least one number!")
      
    if "@" not in password and "!" not in password and "?" not in password:
      is_valid = False
      print("Error: Needs a symbol!")
    
    if is_valid == True: #if all other 'ifs' have been ingored the witch will stay on meaning the loop ends 
      print("Success")
