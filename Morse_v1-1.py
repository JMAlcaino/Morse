#!/usr/bin/env python3
'''
############################################################################################################
 
 Filename     : Morse_v1-1.py                                                                              
 Description  : Blinks a led in fonction of a word done by the user in Morse style                         
                Using the GPIO with a led pinned on the pin 11 (GPIO17)                                    
 auther       : Alcaïno Jean-Marc                                                                          
 modification : 2023/11/16                                                                                 
 version      : V 1.1
 
############################################################################################################

 Version note :
 
 - Comments and program structure's update
 - Uses True and False arguments instead of GPIO.HIGH and GPIO.LOW
 - Test of ON and OFF led blink to study the effect of time.sleep() method on durations vs Morse code and their display for testing
    -> '.'  = 0.25"
    
    -> '-'  = 0.75" (same as three '.')
    
    -> ' '  = 0.25" (gap between two impulsions for a letter -> same as one '.')
    
    -> '_'  = 0.75" (gap between two letters of the same word -> same as one '-')
    
    -> '/'  = 1.75" (space between two words -> same as seven '.')
- Code table for each character defined by a list.
- Definition of new functions for decoding Morse code table, user menu, exceptions for bad entries...

############################################################################################################

Future ehancements :

 - Morse code learning mode.
 - Impulsions decoding.
 - Add a button on the board to impulse a code.
 - Add a speaker to play the impulsion.
 - Code and decode mode.
 - Decode a real radio reception by SDR
 
############################################################################################################
 
 Electronic scheme :
 
 [GPIO17 (pin 11)]----[R1-220 Ohm]----[Red Led]----[GPIO Gnd]
 
############################################################################################################
 '''

# Libraries import

import RPi.GPIO as GPIO                         # import GPIO control library
import time                                     # import time library


# Variables definition

ledPin = 11    # define ledPin

# Letters coding table
A = [".","-"]
B = ["b","-",".",".","."]
C = ["c","-",".","-","."]
D = ["d","-",".","."]
E = ["e","."]
F = ["f",".",".","-","."]
G = ["g","-","-","."]
H = ["h",".",".",".","."]
I = ["i",".","."]
J = ["j",".","-","-","-"]
K = ["k","-",".","-"]
L = ["l",".","-",".","."]
M = ["m","-","-"]
N = ["n","-","."]
O = ["o","-","-","-"]
P = ["p",".","-","-","."]
Q = ["q","-","-",".","-"]
R = ["r",".","-","."]
S = ["s",".",".","."]
T = ["t","-"]
U = ["u",".",".","-"]
V = ["v",".",".",".","-"]
W = ["w",".","-","-"]
X = ["x","-",".",".","-"]
Y = ["y","-",".","-","-"]
Z = ["z","-","-",".","."]
    
# Numbers coding table
N0 = ["0","-","-","-","-","-"]
N1 = ["1",".","-","-","-","-"]
N2 = ["2",".",".","-","-","-"]
N3 = ["3",".",".",".","-","-"]
N4 = ["4",".",".",".",".","-"]
N5 = ["5",".",".",".",".","."]
N6 = ["6","-",".",".",".","."]
N7 = ["7","-","-",".",".","."]
N8 = ["8","-","-","-",".","."]
N9 = ["9","-","-","-","-","."]
    
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
    GPIO.setup(ledPin, GPIO.OUT)                # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)               # make ledPin output LOW level 
    print ()

def loop():                                     # function for the blinking sequence
    #while True:
        for i in A:
            if A[i]==('.'):
                ts=0.25
            else:
                ts=0.75
        GPIO.output(ledPin,True)                # make ledPin output at True level to turn on led
        print ('led turned on >>>')             # print information on terminal
        time.sleep(ts)                        # wait for 1/4 second
        GPIO.output(ledPin,False)               # make ledPin output at Falselevel to turn off led
        print ('led turned off <<<')            # print information on terminal
        time.sleep(0.75)                        # wait for 3/4 second

def destroy():                                  # function to reset the Raspberry's GPIO
    GPIO.cleanup()                              # release all GPIO


# Main Program

if __name__ == '__main__':                      # program entrance
    
    setup()                                     # execute the setup function
    
    generique ("MORSE - Coding and decoding Morse code")    # execute the generique function
    print()
    print ('Blink the led using pin%d'%ledPin + '\n')
    print ('Program is starting ... \n')
    print ('Press CTRL-c to end ... \n')
    
    try:                                        # exception try
        loop()                                  # execute loop function
    except KeyboardInterrupt:                   # exception : press ctrl-c to end the program.
        destroy()                               # execute the destroy function

