#!/usr/bin/env python3
"""
############################################################################################################
 
 Filename     : Morse_desktop_v3-0-win.py                                                                              
 Description  : This program is the same as the GPIO/Electronic version but works only on the desktop(console
                or window). The GPIO and the electronic board are not used.
                Coding and decoding Morse code from a letter/number, a word or a sentence on the screen.
                Use of the mouse or the keyboard to enter Morse code.
                Learning mode available to test the knowledges.
 author       : Alcaïno Jean-Marc                                                                          
 modification : 2025/03/08                                                                            
 version      : V 3.0-win

 GitHub       :     https://github.com/JMAlcaino/Morse/tree/main/Morse_Desktop
 Author GitHub :    https://github.com/JMAlcaino

 See the file  :    https://github.com/JMAlcaino/Morse/blob/main/Morse_Desktop/Notes/Working_notes.txt for more informations about the project.
 Voir le fichier :  https://github.com/JMAlcaino/Morse/blob/main/Morse_Desktop/Notes/Notes_de_travail.txt pour plus d'informations sur le projet.
 
############################################################################################################

 Versions notes :

 * V 1.0 :
 - Keep the same program (Morse_V1-6-10_Test) as a base for developping.
 
 - ON and OFF printed to study the effect of time.sleep() method on durations vs Morse code and their display for testing
    -> '.'  = 0.25"
    
    -> '-'  = 0.50" (same as two '.')
    
    -> ' '  = 0.25" (gap between two impulsions for a letter -> same as one '.')
    
    -> between two letters  = 0.75" (gap between two letters of the same word -> same as three '.')
    
    -> between two words = 1.50" (space between two words -> same as seven '.')
    
 - new 'code()' function which can code a letter or a word or a sentence. Only one function for the Morse coding
 - space, ponctuations and signs added to the 'morse_code' dictionnary. The space ' ' is same as 7 '.' --> 1.50" time sleep
 
 - More simple code which use only one morse code function even the user enter a letter, a word or a sentence.
 
 
 * V 2.0 :
 - The 'pygame' library is used to play the Morse Code sounds
 
 
 * V 2.01 :
 - Print '.' and '-' of the Morse Code and the character associated
 
 
 * V 2.02 :
 - Suppression of the unused menus and associated fonctions. Obsolete ones since the 'code' function is able to code anything.
 - Morse coding sentence is writen on a single with official Morse Code's separators.
 
 * V 2.03 :
 - Timer to show how many times is coding's duration
 
 * V 2.03-win :
 - Windows 11 version  : the linux version is modified here to be executed on Windows
 - The Morse sounds path is modified to be reached from the D: volume. BE CAREFUL ! The path should be used with a "/" instead of a "\" --> ex: "D:/Python/Morse/Needed/Morse_point.wav"

 * V 3.0-win :
 - Begining of the 'learning mode' development
 - Random word choice for the learning mode (english or french) function included
 - The .txt files used for the random word choice are in the 'Needed' folder in the 'Morse' folder - They need to be in the same folder as the program or the path should be modified in the program
 - Some bugs fixed
 - Functions rewrited under the Python's PEP8 rules

############################################################################################################

Future ehancements :  '-' = to be done    '/' = in developpement    'X' = finished

 [X] Coding and decoding words  --> in dev with the 'def code(ltr):' function
 [X] Coding and decoding sentences --> in dev with the 'def code(ltr):' function
 [X] Write the coded sentence in Morse signs
 [X] Showing the time for coding and decoding 
 [/] Morse code learning mode.
 [X] Random word choice for the learning mode (english or french) from a list of words in a .txt file
 [-] Keyboard/Mouse impulsions coding/decoding (GUI dev)
 [-] Write the impulsed code in real characters on the same line
 [x] Play a sound when coding in Morse
 [-] Play a sound when key/mouse is pressed to input something to decode or in learning mode (GUI dev)
 [-] Decode a real radio reception by SDR
 [-] Integration with the 'Cypher' project and particularly with the 'Enigma' program  -> https://github.com/JMAlcaino/Cypher
 [-] GUI for the user
 [-] Pack all the program and the needed elements in a single executable file 
 
############################################################################################################

 """

# Libraries import

from os import environ                          # Import 'os' 'environ' method to avoid the prompt display from 'pygagme' library 
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'     # Hide the 'pygame's prompt when loaded

import time                                     # Import 'time' library
import sys                                      # Import 'sys' library  --> maybe not used in the desktop version (to be seen)
import pygame                                   # Import 'pygame' library to use the music's playing methods
import random

pygame.init()                                   # 'pygame' initialisation


# Constants definitions

point = pygame.mixer.Sound("D:/Python/Morse/Needed/Morse_point.wav")   # Load the 'point' Morse sound in the pygame's mixer module
line = pygame.mixer.Sound("D:/Python/Morse/Needed/Morse_trait.wav")    # Load the 'line' Morse sound in the pygame's mixer module
tmr = 0                                         # Set the variable 'tmr' - This variable will be set as global in the 'code()' function
                                                # and used to calculate the coding's elapse time


# Morse Code dictonnary definition
# The Morse Code's dictionary contains the letters, numbers, ponctuations and signs as keys and the Morse code as values

morse_code = {
       'a':[1,1,2,2],
       'b':[2,2,1,2],
       'c':[2,1,1,1],
       'd':[2,1,2,1],
       'e':[1],
       'f':[1,1,2,1],
       'g':[2,2,1],
       'h':[1,1,1,1],
       'i':[1,1],
       'j':[1,2,2,2],
       'k':[2,1,2],
       'l':[1,2,1,1],
       'm':[2,2],
       'n':[2,1],
       'o':[2,2,2],
       'p':[1,2,2,1],
       'q':[2,2,1,2],
       'r':[1,2,1],
       's':[1,1,1],
       't':[2],
       'u':[1,1,2],
       'v':[1,1,1,2],
       'w':[1,2,2],
       'x':[2,1,1,2],
       'y':[2,1,2,2],
       'z':[2,2,1,1],
       '0':[2,2,2,2,2],
       '1':[1,2,2,2,2],
       '2':[1,1,2,2,2],
       '3':[1,1,1,2,2],
       '4':[1,1,1,1,2],
       '5':[1,1,1,1,1],
       '6':[2,1,1,1,1],
       '7':[2,2,1,1,1],
       '8':[2,2,2,1,1],
       '9':[2,2,2,2,1],
       '.':[1,2,1,2,1,2],
       ',':[2,2,1,1,2,2],
       '?':[1,1,2,2,1,1],
       "'":[1,2,2,2,2,1],
       '!':[2,1,2,1,2,2],
       '/':[2,1,1,2,1],
       '(':[2,1,1,2,1],
       ')':[2,1,2,2,1,2],
       '&':[1,2,1,1,1],
       ':':[2,2,2,1,1,1],
       ';':[2,1,2,1,2,1],
       '=':[2,1,1,1,2],
       '+':[1,2,1,2,1],
       '-':[2,1,1,1,1,2],
       '_':[1,1,2,2,1,2],
       '"':[1,2,1,1,2,1],
       '$':[1,1,1,2,1,1,2],
       '@':[1,2,2,1,2,1],
       ' ':[]}


# Functions definition

def generique(title):
    """
    Display the title of the script even how long it is

    :param title: the title of the script
    """
    lg = len(title) + 8                                     # 3 spaces before and after the title + 2 for the '#' at the beginning and at the end of the table
    print(lg * "#")
    print("#" + (lg - 2) * " " + "#")
    print("#   " + title + "   #")
    print("#" + (lg - 2) * " " + "#")
    print(lg * "#")


def menu_title(title):
    """
    Display the title of the menu even how long it is

    :param title: the title of the menu
    """
    lg = len(title) + 8                                     # 3 spaces before and after the title + 2 for the '°' at the beginning and at the end of the table
    print()
    print(lg * "°")
    print("°" + (lg - 2) * " " + "°")
    print("°   " + title + "   °")
    print("°" + (lg - 2) * " " + "°")
    print(lg * "°")


def menu():
    """
    Display the menu of the script
    """
    while True:                                             # While True loop for the menu choice                       
        try:                                                # Exception try for the choice menu
            print ('\n   Choose an activity in this menu... \n')
            print ('     1 - Code in Morse')
            print ('     2 - Impulse in Morse')
            print ('     3 - Learning mode \n')
            print ('     4 - Quit \n')
            menu_ch = int(input ('   Your choice ...'))     # User choice
            if menu_ch == 1:
                menu_title('Code in Morse')                 # Execute 'menu_title' function to display the menu's choice title
                code_ltr()                                  # Execute code_ltr() function 
            elif menu_ch == 2:
                menu_title('Impulse in Morse')              # Execute 'menu_title' function to display the menu's choice title
                impulse_ltr()                               # Execute impulse_ltr() function
            elif menu_ch == 3:
                menu_title('Learn the Morse Code')          # Execute 'menu_title' function to display the menu's choice title
                learn_mode()                                # Execute learn_mode() function
            elif menu_ch == 4:
                destroy()                                   # Execute destroy() function
            else:
                print("\n--> Your choice is invalid, try again...\n")
                continue
        except ValueError:                                  # Choice's error
            print("\n--> Your choice is invalid, try again...\n")


def try_again():
    """
    Ask the user if he wants to continue or not
    """
    print()
    print()
    while True:
        try:
            again = input('Do it again ? y/n...')
            if again == 'y':
                return None
            if again == 'n':
                menu()
            else:
                print("\n--> Your choice is invalid, try again...\n")
                continue
                
        except ValueError:                                   # Choice's error
            print("\n--> Your choice is invalid, try again...\n")
            break


def sec2ydhms(ss):
    """
    Convert seconds into years, days, hours, minutes and seconds
    """
                                                             # using the native 'divmod' function --> (quotient, remainder) = (value 1 / value 2)
    (yy, ss) = divmod(ss, 31536000)                          # (yy 'years', ss (seconds) = divmod(ss (initial number of seconds / 31536000 (number of seconds in a year))                         
    (dd, ss) = divmod(ss, 86400)                             # 86400 --> number of seconds in a day
    (hh, ss) = divmod(ss, 3600)                              # 3600 --> number of seconds in an hour
    (mm, ss) = divmod(ss, 60)                                # 60 --> number of seconds in a minute
    return (yy, dd, hh, mm, ss)                              # send back the values of years, days, hours, minutes and seconds


def choose_random_word(file_path):                           # Function to choose a random word from a list of words
    """
    Choose a random word from a list of words

    :param file_path: the path of the file containing the list of words
    """
    with open(file_path, 'r', encoding='utf-8') as file:     # Reads all lines and stores them in a list (each line represents a word)    
        words = file.read().splitlines()
    return random.choice(words)                              # Returns a randomly chosen word from the list

       
def code(character):
    """
    Code a character from a single letter, a word or a sentence
    calulate the time of coding
    
    :param character: the character to code
    :return: the time of coding
    """
    global tmr                                               # Set the variable 'tmr' as global to be used in the function
    code_list = morse_code.get(character)                    # Extract the list of codes (values of 1 or 2) wich is value of the dictionnary key
    print ('', end=" ")                                      # This 'print' is needed to write the code on the same line
    if character == " ":                                     # Print a '/' if a space in detected in the sentence
        print (" /", end="")
        tmr = tmr + 0.75                                     # space character duration added to the timer
    for code in code_list:                                   # For the number of item in the letter
        if code == 1:                                        # If the item == 1 -> blinks for .25" for the '.' in Morse code
            print ('.', end="")                              # Print information on terminal and continue on the same line
            point.play()                                     # Play the point's sound with the 'play' pygame's method
            time.sleep(0.25)
            tmr = tmr + 0.25                                 # '.' duration added to the timer
        else:                                                # code==2 
            print ('-', end="")                              # Print information on terminal and continue on the same line
            line.play()                                      # Play the line's sound with the 'play' pygame's method
            time.sleep(0.42)
            tmr = tmr + 0.42                                 # '-' duration added to the timer
    time.sleep(0.75)                                         # Time between two letters in Morse Code
    tmr = tmr + 0.75                                         # Time between two letters added to the timer
    tmr = round(tmr)
    return tmr                                               # Return the timer to 'code_letter' function


def code_ltr():
    """
    Code a letter, a word, a sentence or a number in Morse code
    """
    while True:
        try:
            sentence = input("\n Imput either a letter, a word, a sentence or a number...")  # The user enter what he wants to becoded
            print()                                          # For lisibility        
            for character in sentence:   
                if character in morse_code:                  # Take a look in 'morse_code' dictionnary if the character 'ltr' exists
                    code(character)                          # Jump to the function 'code()' with the extracted 'character' from the sentence
                else:
                    print("\n--> You typed an invalid character, try again...\n") # Typing test
                continue
        except ValueError:                                   # Error in the choice
            print("\n--> You typed an invalid character, try again...\n")
            break                                            # Exit the while/true loop
        (years, days, hours, minutes, seconds) = sec2ydhms(tmr)       # Calls the 'sec2ajhms to convert the timer 'tmr' (tmr is a global variable
        print ("\n\nElapse coding time -->", minutes, "minutes", seconds, "seconds")    # Gives the elapse time converted in mm:ss
        try_again()
                
             
def learn_mode():                                            # Function to code in Morse a letter impulsed by the user with the button (to be developped)
    """
    Learn the Morse code

    This function is in developpement

    Will be used to code a letter impulsed by the user with the button or the mouse and display the Morse code on the screen
    Verify the Morse code with the user's input and give the result and if the impulsed time is correct or not
    The user can choose the language for the Morse code (English or French)
    The user can retry if the word's Morse code is not correct
    The user can chose to get the correct Morse code if he doesn't find it, get the next word or quit the learning mode

    :return: None
    """
    print('\n The learning mode is in developpement...\n\n')
    language = input('Choose the language for the Morse code : 1 - English / 2 - French...')  # Choose the language for the Morse code
    word_files = {                                                                            # Dictionnary with the path of the files containing the list of words
        '1': 'D:/Python/Morse/Needed/processed_english_1000_words.txt',
        '2': 'D:/Python/Morse/Needed/processed_french_1000_words.txt'
    }
    word = word_files.get(language)                          # Extract the path of the file containing the list of words                            
    if word:
        print(f'\n {["English", "French"][int(language) - 1]} is chosen...')  # Display the chosen language
        random_word = choose_random_word(word)               # Send the path of the file containing the list of words to the function
        print("\n Chosen word:", random_word)                # Display the chosen word
        print()
    else:
        print('\n Your choice is invalid, try again...')     # Error in the choice
        learn_mode()
    return None


def impulse_ltr():
    """
    Impulse a letter in Morse code
    
    This function is in developpement

    Will be used to code in Morse a letter impulsed by the user with the button or the mouse and display the Morse code on the screen

    :return: None
    """
    print('\n Impulse a letter - Not available for now, in developpement...\n')
    return None


def destroy():                                               # Quit choice function
    """
    Ask the user if he really wants to quit the program or not
    """
    while True:
        try:
            print()
            answer = input('Do you really want to quit ? y/n...').lower()  # The .lower() method is used to avoid the case sensitive
            if answer == 'y':
                print('\nEnd of the Morse program. See you soon... \n')
                sys.exit()                                   # Use the exit method from the sys library to quit
            elif answer == 'n':
                print()
                return None                                  # Restart the main program
            else:
                print("\n--> Your choice is invalid, try again...\n")
        except ValueError:                                   # Error in the choice
            print("\n--> Your choice is invalid, try again...\n")
        


# Main Program

if __name__ == '__main__':                                   # Program main entrance
        
    generique ("MORSE - Coding and decoding Morse code")     # Execute the generique function
    
    print()
    print ('Program is starting ... \n')
    print()
    
    menu()                                                   # Execute the 'menu' function --> choice of the activity to do