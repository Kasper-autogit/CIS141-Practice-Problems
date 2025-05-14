'''#5. Create a list of integers.
Use a loop to build a new list where each element is the square
of the corresponding element in the original list. 
Print the new list.
'''

list = [1, 2, 3, 4, 5]
squares = []
for element in list:
    squares.append(element ** 2)
print("Squares of the first list:", squares)
