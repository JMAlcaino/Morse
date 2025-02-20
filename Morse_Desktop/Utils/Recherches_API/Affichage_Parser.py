from wiktionaryparser import WiktionaryParser
import pprint

def debug_infos(mot):
    parser = WiktionaryParser()
    parser.set_default_language("fr")
    data = parser.fetch(mot)
    pprint.pprint(data)  # Affiche joliment la structure
    return data

mot = "chat"
debug_infos(mot)
