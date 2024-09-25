from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import time
pygame.init()
for s in range(3):
    pygame.mixer.music.load("/media/jma/EDEA-20AC/Programmation_Python/Projet_Desktop_Morse/Doc_Utils/Morse_point.wav")
    pygame.mixer.music.play()
    time.sleep (0.22)

for t in range(3):
    pygame.mixer.music.load("/media/jma/EDEA-20AC/Programmation_Python/Projet_Desktop_Morse/Doc_Utils/Morse_trait.wav")
    pygame.mixer.music.play()
    time.sleep(0.4)