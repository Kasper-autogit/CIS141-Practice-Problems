'''5. Write a program that continuously asks the user to input a number. 
If the user enters 0, immediately stop asking for more numbers. 
Otherwise, print the number they entered. Sample interaction:'''

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print("You entered", num)

