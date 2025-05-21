'''
#1. Write a function called count_vowels(input) that takes a string
and returns the number of vowels (a, e, i, o, u) in it.
'''

def count_vowels(input):
    vowels = "aeiouAEIOU"
    return sum(1 for char in input if char in vowels)
    
    
print("Vowel Count (Hello, World):", count_vowels("Hello, World"))  
