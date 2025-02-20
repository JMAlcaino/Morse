import requests
import random

def get_random_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1&lang=fr")
    if response.status_code == 200:
        words = response.json()
        return words[0]
    else:
        return None

random_word = get_random_word()
if random_word:
    print(f"Mot au hasard : {random_word}")
else:
    print("Impossible de récupérer un mot.")



# Ce script utilise l'API Random Word pour obtenir un mot aléatoire en français. Il envoie une requête GET à l'URL de l'API et récupère le mot aléatoire retourné. Ensuite, il affiche ce mot à l'utilisateur.
# Il fonctionne très bien le seul souci est qu'il renvoit des verbes conjugués trop souvent et cela n'est pas opyimal pour l'apprentissage du code Morse.