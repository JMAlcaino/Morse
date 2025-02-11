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