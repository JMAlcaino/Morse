#!/usr/bin/env python3
'''
############################################################################################################
 
 Filename     : Morse_desktop_v1-0.py                                                                              
 Description  : This program is the same as the GPIO/Electronic version but works only on the desktop(console
                or window). The GPIO and the electronic board are not used.
                Coding and decoding Morse code from a letter/number, a word or a sentence on the screen.
                Use of the mouse or the keyboard to enter Morse code.
                Learning mode available to test the knowledges.
 author       : Alcaïno Jean-Marc                                                                          
 modification : 2024/03/24                                                                             
 version      : V 1.0   Algorythms test version for developpement. 
 
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
 


############################################################################################################

Future ehancements :  '-' = to be done    '/' = in developpement    'X' = finished

 X Coding and decoding words  --> in dev with the 'def code(ltr):' function
 X Coding and decoding sentences --> in dev with the 'def code(ltr):' function
 - Write the decoded sentence in Morse signs
 - Showing the time for coding and decoding 
 - Morse code learning mode.
 - Keyboard/Mouse impulsions coding/decoding.
 - Add a sound when decoding and when key/mouse pressed to input something to decode or in learning mode
 - Decode a real radio reception by SDR
 - GUI for the user
 
############################################################################################################

 '''

# Libraries import
from os import environ                          # Import 'os' 'environ' method to avoid the prompt display from 'pygagme' library 
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'     # Hide the 'pygame's prompt when loaded

import time                                     # Import 'time' library
import sys                                      # Import 'sys' library  --> maybe not used in the desktop version (to be seen)
import pygame                                   # Import 'pygame' library to use the music's playing methods

pygame.init()                                   # 'pygame' initialisation

# Variables definitions

point = pygame.mixer.Sound("/media/jma/EDEA-20AC/Programmation_Python/Projet_Desktop_Morse/Doc_Utils/Morse_point.wav")   # Load the 'point' Morse sound in the pygame's mixer module
line = pygame.mixer.Sound("/media/jma/EDEA-20AC/Programmation_Python/Projet_Desktop_Morse/Doc_Utils/Morse_trait.wav")    # Load the 'line' Morse sound in the pygame's mixer module

# Morse Code dictonnary definition
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
       ' ':[1,1,1,1,1,1,1]}
    
# Functions definition

def generique(title):                                       # Function to display the script title even how long it is
    lg = len(title) + 8                                     # 3 spaces before and after the title + 2 for the '#' at the beginning and at the end of the table
    print(lg * "#")
    print("#" + (lg - 2) * " " + "#")
    print("#   " + title + "   #")
    print("#" + (lg - 2) * " " + "#")
    print(lg * "#")
    
def menu_title(title):                                      # Function to display the menu title even how long it is
    lg = len(title) + 8                                     # 3 spaces before and after the title + 2 for the '°' at the beginning and at the end of the table
    print()
    print(lg * "°")
    print("°" + (lg - 2) * " " + "°")
    print("°   " + title + "   °")
    print("°" + (lg - 2) * " " + "°")
    print(lg * "°")
   
def menu():
    while True:                                             # While True loop for the menu choice                       
        try:                                                # Exception try for the choice menu
            print ('\n   Choose an activity in this menu... \n')
            print ('     1 - Code a letter')
            print ('     2 - Impulse a letter')
            print ('     3 - Code a word')
            print ('     4 - Impulse a word')
            print ('     5 - Code a sentense')
            print ('     6 - Impulse a sentence')
            print ('     7 - Learning mode \n')
            print ('     8 - Quit \n')
            menu_ch = int(input ('   Your choice ...'))     # User choice
            if menu_ch == 1:
                menu_title('Code a letter/number')          # Execute 'menu_title' function to display the menu's choice title
                code_ltr()                                  # Execute code_ltr() function 
            elif menu_ch == 2:
                menu_title('Impulse a letter/number')       # Execute 'menu_title' function to display the menu's choice title
                impulse_ltr()                               # Execute impulse_ltr() function
            elif menu_ch == 3:
                menu_title('Code a word')                   # Execute 'menu_title' function to display the menu's choice title
                code_wrd()                                  # Execute code_wrd() function
            elif menu_ch == 4:
                menu_title('Impulse a word')                # Execute 'menu_title' function to display the menu's choice title 
                impulse_wrd()                               # Execute impulse_wrd() function
            elif menu_ch == 5:
                menu_title('Code a sentence')               # Execute 'menu_title' function to display the menu's choice title
                code_stc()                                  # Execute code_stc() function
            elif menu_ch == 6:
                menu_title('Impulse a sentence')            # Execute 'menu_title' function to display the menu's choice title
                impulse_stc()                               # Execute impulse_stc() function
            elif menu_ch == 7:
                menu_title('Learn the Morse Code')          # Execute 'menu_title' function to display the menu's choice title
                learn_mode()                                # Execute learn_mode() function
            elif menu_ch == 8:
                destroy()                                   # Execute destroy() function
            else:
                print("\n--> Your choice is invalid, try again...\n")
                continue
        except ValueError:                                  # Choice's error
            print("\n--> Your choice is invalid, try again...\n")
    
def try_again():                                            # Function for the choice option to continue or not
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

        
def code(character):                                         # Function to code a character from a single letter, a word or a sentence
    code_list = morse_code.get(character)                    # Extract the list of codes (values of 1 or 2) wich is value of the dictionnary key
    print(character)
    for code in code_list:                                   # For the number of item in the letter
        if code == 1:                                        # If the item == 1 -> blinks for .25" for the '.' in Morse code
            print ('Point...')                               # Print information on terminal
            point.play()
            time.sleep(0.25)
        else:                                                # code==2 
            print ('Trait...')                               # Print information on terminal
            line.play()
            time.sleep(0.42)
    time.sleep(0.75)

def code_ltr():                                              # Function to code in Morse a letter, a word, a sentence or some numbers
    while True:
        try:
            sentence = input("\n Imput either a letter, a word, a sentence or a number...")  # The user enter what he wants to becoded
            lng = len(sentence)                              # The lenght is needed to exctract each sentence's character         
            for character in sentence:   
                if character in morse_code:                  # Take a look in 'morse_code' dictionnary if the character 'ltr' exists
                    code(character)                          # Jump to the function 'code()' with the extracted 'character' from the sentence
                else:
                    print("\n--> You typed an invalid character, try again...\n") # Typing test
                    continue                                 
        except ValueError:                                   # Error in the choice
            print("\n--> You typed an invalid character, try again...\n")
            break                                            # Exit the while/true loop
        try_again()                                          
                
             
def impulse_ltr():                                           # Function to code in Morse a letter impulsed by the user with the button (to be developped)
    print('\n Impulse a letter - Not available for now, in developpement...\n')
    return None

def code_wrd():                                              # Function to code in Morse a word given by the user
    print('\n Coding a word - Not available for now, in developpement...\n')
    return None

def impulse_wrd():                                           # Function to code in Morse a word impulsed by the user with the button (to be developped)
    print('\n Impulse a word - Not available for now, in developpement...\n')
    return None

def code_stc():                                              # Function to code in Morse a sentence given by the user
    print('\n Coding a sentence - Not available for now, in developpement...\n')
    return None

def impulse_stc():                                           # Function to code in Morse a sentence impulsed by the user with the button (to be developped)
    print('\n Impulse a sentence - Not available for now, in developpement...\n')
    return None

def learn_mode():                                            # Function to learn Morse coding/decoding
    print('\n Learning Mode - Not available for now, in developpement...\n')
    return None

def destroy():                                               # Quit choice function
    while True:
        try:
            print()
            answer = input('Do you really want to quit ? y/n...')
            if answer == 'y' or answer == 'Y':
                print('\nEnd of the Morse program. See you soon... \n')
                sys.exit()                                   # Use the exit method from the sys library to quit
            if answer == 'n' or answer == 'N':
                print()
                return None                                  # Restart the main program
        except ValueError:                                   # Error in the choice
            print("\n--> Your choice is invalid, try again...\n")
        else:
            print("\n--> Your choice is invalid, try again...\n")
            pass
        


# Main Program

if __name__ == '__main__':                                   # Program main entrance
        
    generique ("MORSE - Coding and decoding Morse code")     # Execute the generique function
    
    print()
    print ('Program is starting ... \n')
    print()
    
    menu()                                                   # Execute the 'menu' function --> choice of the activity
    





'''
Developper notes / Mes notes de développement

* code pour récupérer les éléments de la liste associée à la lettre
 # Value of a letter/number given by the user
 print('* Morse coding of a letter/number given by    the user \n')
 letter = input('letter/number ?..')
 if letter in morse_code:
     code_list = morse_code.get(letter)
     print (letter,'-->',code_list)
     for code in code_list:
         print (code, end="  ")
    
 else:
    print ('Invalid Input')

------------------------------------------------

* Faire une fonction(def) pour le test y/n ça sera plus facile pour les choix finaux de chaque modules de coding/decoding. 
 --> ok ça marche avec le menu de départ en fonction...

------------------------------------------------

* Commenter les nouvelles fonctions et les différents éléments de code faits
 --> fait

------------------------------------------------

* Faire la fonction de codage d'un mot. Attention aux intervalles entre chaque lettre.

------------------------------------------------

* Voir utilisation de la Lib gpiozero à la place de rpi.gpio pour la compatibilité avec le Rasprberry 5 --> conversion du programme avec cette lib...
 --> l'ancien code avec la librairie 'RPi.GPIO' est conservé avec le signe '##' en début de ligne

------------------------------------------------

'''
