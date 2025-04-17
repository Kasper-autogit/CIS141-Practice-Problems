''' 4. Create a program that prompts the user for their birth year and displays a message that says 
"You are ___ old". Use an f-string in your solution to this problem.
'''
#ask user for birth year
birth_year = int(input("Enter your birth year"))
#add current year
current_year = 2025
#math
age = current_year - birth_year
#display the results using f-string
print(f"you are {age} years old.")
