'''#1. Create a list of integers (you get to pick!).
Write code to iterate through 
the list and calculate the sum of all even numbers. 
Print the resulting sum.'''

numbers = [10,5,7,2,11,12]
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
print("Sum of even numbers:", even_sum)
