'''3. Prompt the user for a sentence and a word to try to find in that sentence. 
Have the program print out whether the word was found in the sentence. (i.e. True or False)'''
sentence = input("Enter a sentence")
check_word = input("Enter a word to search for in the sentence")
print(check_word in sentence)
