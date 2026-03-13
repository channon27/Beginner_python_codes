True
while True:
  try:
    num1 = float(input("Enter your first number: "))
    inp = input("What would you like to do (+,-,*,/): ")
    num2 = float(input("Enter your seccond number: "))
    if inp == "+":
      print(num1 + num2)
    elif inp == "-":
      print(num1 - num2)
    elif inp == "*":
      print(num1 * num2)
    elif inp == "/":
      print(num1 / num2)
    else:
      print("Error! Enter a valid input!")
      True
      continue
  except:
    ValueError
    print("Error! Thats not valid!")
    True
    continue
  inp2 = input("Would you like to preform another calculation? (Enter '1' for yes , or '2' for no) ")
  if inp2 == "1":
    True
  if inp2 == "2":
    print("Goodbye!")
    False
    break
