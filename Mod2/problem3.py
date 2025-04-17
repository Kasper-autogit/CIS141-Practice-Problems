'''3. Create a program that prompts for the side lengths of a triangle and computes 
the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
'''
# Ask the user for the three side lengths
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Show the result
print("The area of the triangle is:", area)
