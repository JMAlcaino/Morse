from wiktionaryparser import WiktionaryParser

def obtenir_infos_wiktionnaire(mot):
    parser = WiktionaryParser()
    parser.set_default_language("fr")
    result = parser.fetch(mot)
    print (parser)
    print ()
    print (result)

    if result:
        # Affichage d'un exemple d'information disponible
        for definition in result[0].get("definitions", []):
            print(f"Partie du discours : {definition.get('partOfSpeech')}")
            print(f"Définitions : {definition.get('text')}")
            print(f"Étymologie : {definition.get('etymology')}")
            print("-" * 40)
    else:
        print(f"Aucune information trouvée pour '{mot}'.")

mot = "abeille"
obtenir_infos_wiktionnaire(mot)
