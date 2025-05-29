'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas. Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''


with open("poll.txt", "w") as file:
    file.write("yea,nay,yea,yea,nay,nay,yea")

with open("poll.txt", "r") as file:
    votes = file.read().strip().lower().split(',')

# Count votes
yea_count = votes.count("yea")
nay_count = votes.count("nay")

# Print results
print(f"Yea votes: {yea_count}")
print(f"Nay votes: {nay_count}")

