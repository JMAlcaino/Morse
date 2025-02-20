import requests
import random

def get_random_noun_or_verb():
    # Requête pour obtenir des noms
    response_nouns = requests.get("https://api.datamuse.com/words?ml=&md=p&max=1000&v=fr")
    # Requête pour obtenir des verbes
    response_verbs = requests.get("https://api.datamuse.com/words?ml=&md=p&max=1000&v=fr")

    if response_nouns.status_code == 200 and response_verbs.status_code == 200:
        nouns = [word['word'] for word in response_nouns.json() if 'n' in word['tags']]
        verbs = [word['word'] for word in response_verbs.json() if 'v' in word['tags']]
        
        # Combiner les noms et les verbes
        words = nouns + verbs
        return random.choice(words)
    else:
        return None

random_word = get_random_noun_or_verb()
if random_word:
    print(f"Mot au hasard : {random_word}")
else:
    print("Impossible de récupérer un mot.")