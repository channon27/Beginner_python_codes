#simple python calc
print("welcome to the basic calculater")

# getting the first number from the user
num1_str = input("welcome to the basic calculater:") # this means that the first number to the calculater is what the user typed in from line 2 
num1 = float(num1_str) # this means it will regognise the number as a decimal to hlep with calculations

#now we get the opperations for the calc from  user
operation = input("enter your opperation (+,-,*,/):") #this means the operation for the calc is what the user entered

#getting the seccond number from user 
num2_str = input("enter the seccond number: ")
num2 = float(num2_str) # again this is telling us that it allows decimals 

result = None # this is like a checker if all of the elif ⬇ requiremnts arw not met it will not let you pass( end result would display ans none

if operation == "+":
    result = num1 + num2
