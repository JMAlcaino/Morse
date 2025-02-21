# Test of the function choose_random_word
# Uses the file 'D:/Python/Morse/Needed/english_words_list.txt' to choose a random word
#--> works well, returns simple and non-conjugated words.
#--> to be used for the rest of the project.
#--> note that the file 'english_words_list.txt' is a text file containing a list of englishes words, one word per line.


import random

def choose_random_word(file_path):
    # Opens the file in read mode with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        # Reads all lines and stores them in a list (each line represents a word)
        words = file.read().splitlines()

    # Tests...
    #   print (words) --> to verify that the list is well created
    #   print (type(words)) --> to verify that the type of 'words' is a list

    # Returns a randomly chosen word from the list
    return random.choice(words)

# Main
random_word = choose_random_word('D:/Python/Morse/Needed/english_words_list.txt')  # Send the path of the file containing the list of words to the function
print("Chosen word:", random_word)