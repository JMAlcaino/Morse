# Test de la fonction choisir_mot_aleatoire
# Utilise le fichier 'D:/Python/Morse/Needed/french_words_list.txt' pour choisir un mot aléatoire
#--> fonctionne bien, renvoit des mots simples et non conjugués.
#--> à utiliser pour la suite du projet.
#--> à noter que le fichier 'french_words_list.txt' est un fichier texte contenant une liste de mots en français, un mot par ligne.


import random

def choisir_mot_aleatoire(chemin_fichier):
    # Ouvre le fichier en mode lecture avec l'encodage UTF-8
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        # Lit toutes les lignes et les stocke dans une liste (chaque ligne représente un mot)
        mots = fichier.read().splitlines()
    # Retourne un mot choisi aléatoirement dans la liste
    return random.choice(mots)

# Exemple d'utilisation : suppose que ton fichier 'mots_francais.txt' se trouve dans le même répertoire que ton script.
mot_aleatoire = choisir_mot_aleatoire('D:/Python/Morse/Needed/french_words_list.txt')
print("Mot choisi :", mot_aleatoire)
