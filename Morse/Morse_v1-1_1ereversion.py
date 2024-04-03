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
 - Uses GPIO.True and GPIO.False methods instead of GPIO.HIGH and GPIO.LOW
 - Test of ON and OFF led blink to study the effect of time.sleep() method on durations vs Morse code and their display for testing
    -> '.'  = 0.25"
    
    -> '-'  = 0.75" (same as three '.')
    
    -> ' '  = 0.25" (gap between two impulsions for a letter -> same as one '.')
    
    -> '_'  = 0.75" (gap between two letters of the same word -> same as one '-')
    
    -> '/'  = 1.75" (space between two words -> same as seven '.')
- Definition of new functions for the Morse code table, user menu, exceptions for bad entries...

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

import RPi.GPIO as GPIO            # import GPIO control library
import time                        # import time library


# Variables definition

ledPin = 11    # define ledPin


# Functions definition

def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level 
    print ('Blink the led using pin%d'%ledPin)

def loop():
    while True:
        GPIO.output(ledPin, GPIO.True)          # make ledPin output at True level to turn on led
        print ('led turned on >>>')             # print information on terminal
        time.sleep(0.25)                        # Wait for 1/4 second
        GPIO.output(ledPin, GPIO.False)         # make ledPin output at Falselevel to turn off led
        print ('led turned off <<<')            # print information on terminal
        time.sleep(0.75)                        # Wait for 3/4 second

def destroy():
    GPIO.cleanup()                              # Release all GPIO


# Main Program

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

