'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

file_name = "hiking_log.txt"

with open(file_name, "a") as file:
    while True:
        hike_name = input("Enter hike name (or 0 to stop): ").strip()
        if hike_name == "0":
            break
        distance = input("Enter distance in miles: ").strip()
        file.write(f"{hike_name} - {distance} miles\n")
        print("Hike logged!\n")

print("\nHiking Log Entries:")
with open(file_name, "r") as file:
    print(file.read())
