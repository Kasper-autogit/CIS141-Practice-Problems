'''#3. Create a list of strings. 
Write code to create a new list that includes only the strings longer than three characters.
Print the resulting filtered list.
'''

strings = ["fun", "fishing", "fat", "loud one", "star", "galaxy"]
long_strings = []
for s in strings:
    if len(s) > 3:
        long_strings.append(s)
print("Strings longer than three characters:", long_strings)
