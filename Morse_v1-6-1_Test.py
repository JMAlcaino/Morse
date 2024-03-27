#!/usr/bin/env python3
'''
############################################################################################################
 
 Filename     : Morse_v1-6_Test.py                                                                              
 Description  : lights a led in fonction of a letter, a word or a sentence done by the user in Morse style                         
                Using the GPIO with a led pinned on the pin 11 (GPIO17)
                this program is for all Raspberry Pi with 40 pins GPIO
 auther       : Alcaïno Jean-Marc                                                                          
 modification : 2024/02/23                                                                                
 version      : V 1.5   Algorythms test version for developpement. GPIO activation by the gpiozero library
                        instead of rpi-gpio
 
############################################################################################################

 Versions notes :
 
 * V1.6 :
 - More simple code which use only one morse code function even the user enter a letter, a word or a sentence.
 
 * V1.5 :
 - new 'code()' function which can code a letter or a word or a sentence. Only one function for the Morse coding
 - space, ponctuations and signs added to the 'morse_code' dictionnary. The space ' ' is same as 7 '.' --> 1.50" time sleep
 
 * V1.4 :
- importation of the 'gpiozero' library
- keep of the 'rpi.gpio' code for a possible use (lines to use for noted '##' in the begining)
- Menu title function added for a different display instead of the program's one
 
 * V1.3 :
- New Morse code table using a dictionnary instead of a list
- Using the dictionnary for the coding and the blink 
- Creation of 'Coding a word' algorythm 
 
 * V1.2 :
- Code table for each character defined by a list - the '.' is '1' in the table, '-' is '2' (tee/taaa)
- Definition of new functions for decoding Morse code table, user menu, exceptions for bad entries...

 * V 1.1 :
 - Comments and program structure's updated
 - Uses True and False arguments instead of GPIO.HIGH and GPIO.LOW
 - Test of ON and OFF led blink to study the effect of time.sleep() method on durations vs Morse code and their display for testing
    -> '.'  = 0.25"
    
    -> '-'  = 0.50" (same as two '.')
    
    -> ' '  = 0.25" (gap between two impulsions for a letter -> same as one '.')
    
    -> between two letters  = 0.75" (gap between two letters of the same word -> same as three '.')
    
    -> between two words = 1.50" (space between two words -> same as seven '.')

 * V 1.0 :
 - Developpement of a Morse code program from a little led blinking program using the Raspberry's GPIO.

############################################################################################################

Future ehancements :

 - Coding and decoding words  --> in dev with the 'def code(ltr):' function
 - Coding and decoding sentences --> in dev with the 'def code(ltr):' function
 - Morse code learning mode.
 - Impulsions decoding.
 - Add a button on the board to impulse a code - Electronic ehancement
 - Add a buzzer to play the impulsion - Electronic ehancement
 - Decode a real radio reception by SDR
 - GUI for the user
 
############################################################################################################
 
 Electronic scheme :
 
 [GPIO17 (pin 17 BCM numbering) (pin 11 in board numbering)]--->[R1-220 Ohm]--->[Red Led]--->[GPIO Gnd]
 
############################################################################################################
 '''

# Libraries import

##import RPi.GPIO as GPIO                       # import RPi.GPIO control library  --> actually it can't be used with Rpi 5
import gpiozero as GPIO                         # import GPIO control
import time                                     # import time library
import sys                                      # import sys library


# Variables definition

##ledPin = 11                                   # define ledPin
ledPin = 17                                     # define ledPin GPIO output - 'gpiozero' uses the Broadcom (BCM) pins numbering
redLed = GPIO.LED(ledPin)                       # define the led with the regular class 'LED' in API-Output devices of the 'gpiozero' library

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

def generique(title):                                       # function to display the script title even how long it is
    lg = len(title) + 8                                     # 3 spaces before and after the title + 2 for the '#' at the beginning and at the end of the table
    print(lg * "#")
    print("#" + (lg - 2) * " " + "#")
    print("#   " + title + "   #")
    print("#" + (lg - 2) * " " + "#")
    print(lg * "#")
    
def menu_title(title):                                      # function to display the menu title even how long it is
    lg = len(title) + 8                                     # 3 spaces before and after the title + 2 for the '°' at the beginning and at the end of the table
    print()
    print(lg * "°")
    print("°" + (lg - 2) * " " + "°")
    print("°   " + title + "   °")
    print("°" + (lg - 2) * " " + "°")
    print(lg * "°")

##def setup():                                              # function to setup the Raspeberry's GPIO  --> it's not necessary to setup the GPIO with 'gpiozero' lib
##    GPIO.setmode(GPIO.BOARD)                              # use PHYSICAL GPIO Numbering
##    GPIO.setwarnings(False)                               # disable the GPIO warnings as the RunTimeWarning (channel in use)
##    GPIO.setup(ledPin, GPIO.OUT)                          # set the ledPin to OUTPUT mode
##    GPIO.output(ledPin, GPIO.LOW)                         # make ledPin output LOW level
##    print ()
    
def menu():
    while True:                                             # while True loop for the menu choice                       
        try:                                                # exception try for the choice menu
            print ('\n   Choose an activity in this menu... \n')
            print ('     1 - Code a letter')
            print ('     2 - Impulse a letter')
            print ('     3 - Code a word')
            print ('     4 - Impulse a word')
            print ('     5 - Code a sentense')
            print ('     6 - Impulse a sentence')
            print ('     7 - Learning mode \n')
            print ('     8 - Quit \n')
            menu_ch = int(input ('   Your choice --> '))     # user choice
            if menu_ch == 1:
                menu_title('Code a letter/number')          # execute 'menu_title' function to display the menu's choice title
                code_ltr()                                  # execute code_ltr() function 
            elif menu_ch == 2:
                menu_title('Impulse a letter/number')       # execute 'menu_title' function to display the menu's choice title
                impulse_ltr()                               # execute impulse_ltr() function
            elif menu_ch == 3:
                menu_title('Code a word')                   # execute 'menu_title' function to display the menu's choice title
                code_wrd()                                  # execute code_wrd() function
            elif menu_ch == 4:
                menu_title('Impulse a word')                # execute 'menu_title' function to display the menu's choice title 
                impulse_wrd()                               # execute impulse_wrd() function
            elif menu_ch == 5:
                menu_title('Code a sentence')               # execute 'menu_title' function to display the menu's choice title
                code_stc()                                  # execute code_stc() function
            elif menu_ch == 6:
                menu_title('Impulse a sentence')            # execute 'menu_title' function to display the menu's choice title
                impulse_stc()                               # execute impulse_stc() function
            elif menu_ch == 7:
                menu_title('Learn the Morse Code')          # execute 'menu_title' function to display the menu's choice title
                learn_mode()                                # execute learn_mode() function
            elif menu_ch == 8:
                destroy()                                   # execute destroy() function
            else:
                print("\n--> Your choice is invalid, try again...\n")
                continue
        except ValueError:                                  # error in the choice
            print("\n--> Your choice is invalid, try again...\n")
    
def try_again():                                            # function for the choice option to continue or not
    print()
    while True:
        try:
            again = input('Do it again ? y/n --> ')
            if again == 'y':
                return None
            if again == 'n':
                menu()
            else:
                print("\n--> Your choice is invalid, try again...\n")
                continue
                
        except ValueError:                                   # error in the choice
            print("\n--> Your choice is invalid, try again...\n")
            break


        
def code(ltr):                                               # function to code a character from a single letter, a word or a sentence
    code_list = morse_code.get(ltr)                          # extract the list of codes (1 and 2) wich is value of the dictionnary key
    
    for code in code_list:                               # for the number of item in the letter
        print(code)
        if code == 1:                                    # if the item == 1 -> blinks for .25" for the '.' in Morse code
##      GPIO.output(ledPin,True)                     # make ledPin output at True level to turn on led --> RPi.GPIO library
            redLed.on()
            print ('led turned on >>>')                  # print information on terminal
            time.sleep(0.25)                             # the item == 1 -> blinks for 0.25" for the'.' in Morse code
##          GPIO.output(ledPin,False)                    # make ledPin output at Falselevel to turn off led --> RPi.GPIO library
            redLed.off()                                 # switch 'off' the led with the function 'off' of the class 'LED' from 'gpiozero' library
            print ('led turned off <<<')                 # print information on terminal
            time.sleep(.25)                              # wait for 0.75" interval between two impulsions
        else:                                            # code==2 
##          GPIO.output(ledPin,True)                     # make ledPin output at True level to turn on led --> RPi.GPIO library
            redLed.on()
            print ('led turned on >>>')                  # print information on terminal
            time.sleep(0.5)                              # the item == 2 -> blinks for 0.5" for the'-' in Morse code
##          GPIO.output(ledPin,False)                    # make ledPin output at Falselevel to turn off led --> RPi.GPIO library
            redLed.off()                                 # switch 'off' the led with the function 'off' of the class 'LED' from 'gpiozero' library
            print ('led turned off <<<')                 # print information on terminal
            time.sleep(.25)                              # wait for 0.75" interval between two impulsions

def code_ltr():                                              # function to code in Morse a letter given by the user
    while True:
        try:
            ltr = input("\n Input a letter '(a to z)' or a number '(1 to 0)'")  # input of a character
            if ltr in morse_code:                            # take a look in 'morse_code' dictionnary if the character 'ltr' exists
                code(ltr)
            else:
                print("\n--> You typed an invalid character, try again...\n")
                continue
        except ValueError:                                   # error in the choice
            print("\n--> You typed an invalid character, try again...\n")
            break
        try_again()
                
             
def impulse_ltr():                                           # function to code in Morse a letter impulsed by the user with the button (to be developped)
    print('\n Impulse a letter - Not available for now, in developpement...\n')
    return None

def code_wrd():                                              # function to code in Morse a word given by the user
    print('\n Coding a word - Not available for now, in developpement...\n')
    return None

def impulse_wrd():                                           # function to code in Morse a word impulsed by the user with the button (to be developped)
    print('\n Impulse a word - Not available for now, in developpement...\n')
    return None

def code_stc():                                              # function to code in Morse a sentence given by the user
    print('\n Coding a sentence - Not available for now, in developpement...\n')
    return None

def impulse_stc():                                           # function to code in Morse a sentence impulsed by the user with the button (to be developped)
    print('\n Impulse a sentence - Not available for now, in developpement...\n')
    return None

def learn_mode():                                            # function to learn Morse coding/decoding
    print('\n Learning Mode - Not available for now, in developpement...\n')
    return None

def destroy():                                               # quit choice function
    while True:
        try:
            print()
            answer = input('Do you really want to quit ? y/n --> ')
            if answer == 'y' or answer == 'Y':
##              GPIO.cleanup()                               # release all GPIO (reset Raspeberry's GPIO) used with rpi.gpio library
                print('\nEnd of the Morse program. See you soon... \n')
                sys.exit()                                   # use the exit method from the sys library to quit
            if answer == 'n' or answer == 'N':
                print()
                return None                                  # restart the main program
        except ValueError:                                   # error in the choice
            print("\n--> Your choice is invalid, try again...\n")
        else:
            print("\n--> Your choice is invalid, try again...\n")
            pass
        


# Main Program

if __name__ == '__main__':                                   # program main entrance
    
##    setup()                                                # execute the 'setup' function  --> not usefull with 'gpiozero' lib
    
    generique ("MORSE - Coding and decoding Morse code")     # execute the generique function
    
    print()
    print ('Program is starting ... \n')
    print ('It will light the red led using GPIO pin%d'%ledPin)
    print ('using the Broadcom (BCM) numbering for the GPIO pins')
    print()
    
    menu()                                                   # execute the 'menu' function --> choice of the activity
    





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