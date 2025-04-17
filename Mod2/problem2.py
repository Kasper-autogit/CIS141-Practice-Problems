''' 2. Create a program that prompts for 2 numbers and then outputs the
addition, subtraction, multiplication, and division '
of the first number by the second number.
'''
# prompt the user for the 2 numbers
num1 = float(input("Pick 1 number! And we'll do the rest!"))
num2 = float(input("Pick a 2nd number!"))
#Math
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
divistion = num1 / num2 
#math results
print("Results!")
print("Addition", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Divistion", divistion)
