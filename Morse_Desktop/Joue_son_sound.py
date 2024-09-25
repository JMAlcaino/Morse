'''

Script qui permet de produire le son en Morse du S.O.S --> . . . _ _ _ . . .
Pour servir dans le programme de Morse

Utilise les bibliothèques : 'os', 'pygame' et 'time'
Utilise les sons en.wav sauvagardés dans un répepertoire

'''


from os import environ                              # La méthode 'environ' est utilisée pour supprimer le 'prompt' de pygame qui sinon s'affiche au chargement de la librairie 
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'         # Cache le 'prompt' 

import pygame                                      # Importation de 'pygame' pour l'utilisation des méthodes de production de sons ou musiques
import time                                         # Importation de 'time' pour la méthode 'sleep' qui permet d'attendre un certain temps

pygame.init()                                       # Initialisation de pygame

#pygame.mixer.Sound.play(pygame.mixer.Sound("/media/jma/EDEA-20AC/Programmation_Python/Projet_Desktop_Morse/Doc_Utils/Morse_point.wav"))
#time.sleep(0.23)
#pygame.mixer.Sound.play(pygame.mixer.Sound("/media/jma/EDEA-20AC/Programmation_Python/Projet_Desktop_Morse/Doc_Utils/Morse_trait.wav"))
#time.sleep(0.42)

point = pygame.mixer.Sound("/media/jma/EDEA-20AC/Programmation_Python/Projet_Desktop_Morse/Doc_Utils/Morse_point.wav")
trait = pygame.mixer.Sound("/media/jma/EDEA-20AC/Programmation_Python/Projet_Desktop_Morse/Doc_Utils/Morse_trait.wav")
point.play()
time.sleep(0.23)
trait.play()
time.sleep(0.42)

#def thii():                                        # Définition de la fonction pour jouer 3 fois le son du 'point' en Morse
#   for s in range(3):                              # Boucle de répétition pour trois itérations
#        pygame.mixer.music.load("/media/jma/EDEA-20AC/Programmation_Python/Projet_Desktop_Morse/Doc_Utils/Morse_point.wav")   # Charge le son à partir du path/fichier.wav
#        pygame.mixer.music.play(point)                   # Joue le son précédemment chargé
#       time.sleep (0.23)                           # Attend 0.23 seconde avant de boucler - Ce temps a été testé pour refléter la réalité le plus possible

#def thaa():
#   for t in range(3):                              # Définition de la fonction pour jouer 3 fois le son du 'trait' en Morse
#        pygame.mixer.music.load("/media/jma/EDEA-20AC/Programmation_Python/Projet_Desktop_Morse/Doc_Utils/Morse_trait.wav")
#       pygame.mixer.music.play(trait)
#       time.sleep(0.42)                            # Attend 0.42 seconde avant de boucler - Ce temps a été testé pour refléter la réalité le plus possible
        
#thii()
#thaa()
#thii()
