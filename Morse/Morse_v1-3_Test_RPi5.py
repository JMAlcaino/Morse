#!/usr/bin/env python3
'''
############################################################################################################
 
 Filename     : Morse_v1-3_Test.py                                                                              
 Description  : Blinks a led in fonction of a word done by the user in Morse style                         
                Using the GPIO with a led pinned on the pin 11 (GPIO17)                                    
 auther       : Alcaïno Jean-Marc                                                                          
 modification : 2023/12/05                                                                                
 version      : V 1.3    Algorythms test version for developpement. Dictionnary use for the code table.
 
############################################################################################################

 Versions notes :
 
 * V1.3
- New Morse code table using a dictionnary instead of a list
- Using the dictionnary for the coding and the blink 
- Creation of 'Coding a word' algorythm 
 
 * V1.2
- Code table for each character defined by a list - the '.' is '1' in the table, '-' is '2' (tee/taaa)
- Definition of new functions for decoding Morse code table, user menu, exceptions for bad entries...

 * V 1.1 :
 - Comments and program structure's update
 - Uses True and False arguments instead of GPIO.HIGH and GPIO.LOW
 - Test of ON and OFF led blink to study the effect of time.sleep() method on durations vs Morse code and their display for testing
    -> '.'  = 0.25"
    
    -> '-'  = 0.50" (same as two '.')
    
    -> ' '  = 0.25" (gap between two impulsions for a letter -> same as one '.')
    
    -> '_'  = 0.75" (gap between two letters of the same word -> same as one '-')
    
    -> '/'  = 1.50" (space between two words -> same as five '.')

 * V 1.0 :
 - Developpement of a Morse code program from a little led blinking program using the Raspberry's GPIO.

############################################################################################################

Future ehancements :

 - Coding and decoding words
 - Coding and decoding sentences
 - Morse code learning mode.
 - Impulsions decoding.
 - Add a button on the board to impulse a code - Electronic ehancement
 - Add a speaker to play the impulsion - Electronic ehancement
 - Decode a real radio reception by SDR
 - GUI for the user
 
############################################################################################################
 
 Electronic scheme :
 
 [GPIO17 (pin 11)]----[R1-220 Ohm]----[Red Led]----[GPIO Gnd]
 
############################################################################################################
 '''

# Libraries import

import gpiod as GPIO                            # import GPIO control library (for RPi 5)
import time                                     # import time library
import sys                                      # import sys library


# Variables definition

ledPin = 11    # define ledPin

# Morse Code dictonnary definition
morse_code = {'a':[1,1,2,2],
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
       '9':[2,2,2,2,1]}
    
# Functions definition

def generique(title):                           # function to display the script title even how long it is
    lg = len(title) + 8                         # 3 spaces before and after the title + 2 for the '#' at the beginning and at the end of the table
    print(lg * "#")
    print("#" + (lg - 2) * " " + "#")
    print("#   " + title + "   #")
    print("#" + (lg - 2) * " " + "#")
    print(lg * "#")

def setup():                                    # function to setup the Raspeberry's GPIO
    GPIO.setmode(GPIO.BOARD)                    # use PHYSICAL GPIO Numbering
    GPIO.setwarnings(False)                     # disable the GPIO warnings as the RunTimeWarning (channel in use)
    GPIO.setup(ledpin, GPIO.OUT)                # set the ledPin to OUTPUT mode
    GPIO.output(ledpin, GPIO.LOW)               # make ledPin output LOW level
    print ()
    
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
            menu_ch = int(input ('   Your choice ...'))     # user choice
            if menu_ch == 1:
                code_ltr()                                  # execute code_ltr() function 
            elif menu_ch == 2:
                impulse_ltr()                               # execute impulse_ltr() function
            elif menu_ch == 3:
                code_wrd()                                  # execute code_wrd() function
            elif menu_ch == 4:
                impulse_wrd()                               # execute impulse_wrd() function
            elif menu_ch == 5:
                code_stc()                                  # execute code_stc() function
            elif menu_ch == 6:
                impulse_stc()                               # execute impulse_stc() function
            elif menu_ch == 7:
                learn_mode()                                # execute learn_mode() function
            elif menu_ch == 8:
                destroy()                                   # execute destroy() function
            else:
                print("\n--> Your choice is invalid, try again...\n")
                continue
        except ValueError:                                  # error in the choice
            print("\n--> Your choice is invalid, try again...\n")
    
def try_again():
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
                
        except ValueError:                                  # error in the choice
            print("\n--> Your choice is invalid, try again...\n")
            break

    


def code_ltr():                                 # function to code in Morse a letter given by the user
    generique('Code a letter/number')
    while True:
        try:
            ltr = input("\n Input a letter '(a to z)' or a number '(1 to 0)'")  # input of a character
            if ltr in morse_code:
                code_list = morse_code.get(ltr)
    
                for code in code_list:                               # for the number of item in the letter
                    print(code)
                    if code == 1:                              # if the item = 1 -> blinks for .25" for the '.' in Morse code
                        GPIO.output(ledPin,True)            # make ledPin output at True level to turn on led
                        print ('led turned on >>>')         # print information on terminal
                        time.sleep(0.25)                    # wait for 1/4 second
                    else:
                        GPIO.output(ledPin,True)            # make ledPin output at True level to turn on led
                        print ('led turned on >>>')         # print information on terminal
                        time.sleep(0.5)                     # the item = 2 -> blinks for 0.5" for the'-' in Morse code
                        GPIO.output(ledPin,False)               # make ledPin output at Falselevel to turn off led
                        print ('led turned off <<<')            # print information on terminal
                        time.sleep(.25)                         # wait for 0.75" interval between two impulsions
            else:
                print("\n--> Your choice is invalid, try again...\n")
                continue
        except ValueError:                                  # error in the choice
            print("\n--> Your choice is invalid, try again...\n")
            break
        try_again()
                
            
#        else:
#            print("\n--> Your choice is invalid, try again...\n")
#           pass
 
def impulse_ltr():                              # function to code in Morse a letter impulsed by the user with the button (to be developped)
    print('\n Impulse a letter - Not available for now, in developpement...\n')
    return None

def code_wrd():                                 # function to code in Morse a word given by the user
    print('\n Coding a word - Not available for now, in developpement...\n')
    return None

def impulse_wrd():                               # function to code in Morse a word impulsed by the user with the button (to be developped)
    print('\n Impulse a word - Not available for now, in developpement...\n')
    return None

def code_stc():                                  # function to code in Morse a sentence given by the user
    print('\n Coding a sentence - Not available for now, in developpement...\n')
    return None

def impulse_stc():                               # function to code in Morse a sentence impulsed by the user with the button (to be developped)
    print('\n Impulse a sentence - Not available for now, in developpement...\n')
    return None

def learn_mode():                                # function to learn Morse coding/decoding
    print('\n Learning Mode - Not available for now, in developpement...\n')
    return None

def destroy():                                              # quit choice function
    while True:
        try:
            print()
            answer = input('Do you really want to quit ? y/n...')
            if answer == 'y' or answer == 'Y':
                GPIO.cleanup()                              # release all GPIO (reset Raspeberry's GPIO
                print('\nEnd of the Morse program. See you soon... \n')
                sys.exit()                                  # use the exit method from the sys library to quit
            if answer == 'n' or answer == 'N':
                print()
                return None                                 # restart the main program
        except ValueError:                                  # error in the choice
            print("\n--> Your choice is invalid, try again...\n")
        else:
            print("\n--> Your choice is invalid, try again...\n")
            pass
        


# Main Program

if __name__ == '__main__':                                  # program main entrance
    
    setup()                                                 # execute the setup function
    
    generique ("MORSE - Coding and decoding Morse code")    # execute the generique function
    
    print()
    print ('Program is starting ... \n')
    print ('It will blink the led using GPIO pin%d'%ledPin + '\n')
    print()
    menu()
    
'''
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
            menu_ch = int(input ('   Your choice ...'))     # user choice
            if menu_ch == 1:
                code_ltr()                                  # execute code_ltr() function 
            elif menu_ch == 2:
                impulse_ltr()                               # execute impulse_ltr() function
            elif menu_ch == 3:
                code_wrd()                                  # execute code_wrd() function
            elif menu_ch == 4:
                impulse_wrd()                               # execute impulse_wrd() function
            elif menu_ch == 5:
                code_stc()                                  # execute code_stc() function
            elif menu_ch == 6:
                impulse_stc()                               # execute impulse_stc() function
            elif menu_ch == 7:
                learn_mode()                                # execute learn_mode() function
            elif menu_ch == 8:
                destroy()                                   # execute destroy() function
            else:
                print("\n--> Your choice is invalid, try again...\n")
                continue
        except ValueError:                                  # error in the choice
            print("\n--> Your choice is invalid, try again...\n")
'''
        
            
