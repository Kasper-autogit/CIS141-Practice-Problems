'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''


with open("song_lyrics.txt", "w") as file:
    file.write("Let it be, let it be, let it be, oh let it be\n")
    file.write("Whisper words of wisdom, let it be\n")

with open("song_lyrics.txt", "r") as file:
    lyrics = file.read().lower()

words_to_count = []
for i in range(5):
    word = input(f"Enter word {i+1} to count: ").lower()
    words_to_count.append(word)

word_count = {}
for word in words_to_count:
    count = lyrics.count(word)
    word_count[word] = count

print("Word Frequencies:", word_count)
