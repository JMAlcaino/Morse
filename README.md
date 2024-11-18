# Morse
Code, decode and learn Morse Code 

The project comes with two applications 
- A Python program/application using the Raspberry Pi 5's GPIO interface using an electronic board blinking a led.
- A Python program/application working on the desktop of any OS. The interface is done with the keyboard ou the mouse.

----------------------------------------------------------------------------------------------------------------------------

MORSE

 Filename          : Morse_Vx.x.py
 Description       : Lights a led in fonction of a letter, a word or a sentence done by the user in Morse style
                     Using the GPIO with a led pinned on the pin 11 (GPIO17)
                     This program is for all Raspberry Pi with 40 pins GPIO 
                     
 Author           : Alcaïno Jean-Marc
 
 First version    : 2023/12/18
 
 Last changes     : 2024/02/23
 
 Last version     : V 1.6   Algorythms test version for developpement. GPIO activation by the gpiozerolibrary instead of rpi-gpio

 WORK IN PROGRESS


 Versions notes :
 
 V1.6 
 - More simple code which use only one morse code function even the user enter a letter, a word or a sentence.
 
 V1.5 
 - new 'code()' function which can code a letter or a word or a sentence. Only one function for the Morse coding
 - space, ponctuations and signs added to the 'morse_code' dictionnary. The space ' ' is same as 7 '.' --> 1.50" time sleep
 
 V1.4 
- importation of the 'gpiozero' library
- keep of the 'rpi.gpio' code for a possible use (lines to use for noted '##' in the begining)
- Menu title function added for a different display instead of the program's one
 
 V1.3 
- New Morse code table using a dictionnary instead of a list
- Using the dictionnary for the coding and the blink 
- Creation of 'Coding a word' algorythm 
 
 V1.2 
- Code table for each character defined by a list - the '.' is '1' in the table, '-' is '2' (tee/taaa)
- Definition of new functions for decoding Morse code table, user menu, exceptions for bad entries...

 V 1.1 
 - Comments and program structure's updated
 - Uses True and False arguments instead of GPIO.HIGH and GPIO.LOW
 - Test of ON and OFF led blink to study the effect of time.sleep() method on durations vs Morse code and their display for testing
   
   '.'  = 0.25"
    
   '-'  = 0.50" (same as two '.')
    
   ' '  = 0.25" (gap between two impulsions for a letter -> same as one '.')
    
   between two letters  = 0.75" (gap between two letters of the same word -> same as three '.')
   
   between two words = 1.50" (space between two words -> same as seven '.')

 V 1.0 
 - Developpement of a Morse code program from a little led blinking program using the Raspberry's GPIO.

Future ehancements :

 - Coding and decoding words  --> in dev with the 'def code(ltr):' function
 - Coding and decoding sentences --> in dev with the 'def code(ltr):' function
 - Morse code learning mode.
 - Impulsions decoding.
 - Add a button on the board to impulse a code - Electronic ehancement
 - Add a buzzer to play the impulsion - Electronic ehancement
 - Decode a real radio reception by SDR
 - GUI for the user

------------------------------------------------------------------------------------------------------------------------------------------

MORSE_DESKTOP

 Filename          : Desktop_Morse_Vx.x.py
 
 Description       : Code, decode or learn Morse's code with some visual and auditive interface on any OS
 
 Author            : Alcaïno Jean-Marc
 
 First version     : 2024/03/26
 
 Last changes      : 2024/11/18
 
 Last version      : V 2.03 
                     Plays sounds as real Morse code - Morse sentence when decoding - Timer for the decoding's duration


 WORK IN PROGRESS
