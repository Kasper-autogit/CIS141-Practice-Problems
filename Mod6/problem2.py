'''#2. Create a list of strings. 
Write code that counts how many times the word 
"Olympic" appears in the list, 
and then print the count.'''

word = ["Olympic", "College", "Washington", "Fishing"]
olympic_count = 0
for element in word:
    if element == "Olympic":
        olympic_count += 1
print("Count of 'Olympic':", olympic_count)
