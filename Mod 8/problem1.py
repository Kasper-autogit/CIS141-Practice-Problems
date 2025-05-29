'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it. Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''
with open('gardening_tips.txt', 'w') as file:
    file.write("Water your plants early in the morning.\n")
    file.write("Use compost to enrich your soil.\n")
    file.write("Get a lot of sun.\n")
with open('gardening_tips.txt', 'r') as file:
    for line in file:
        print("Tip:", line.strip())
