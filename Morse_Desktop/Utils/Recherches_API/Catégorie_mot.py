from wiktionaryparser import WiktionaryParser

def verifier_categorie(mot):
    parser = WiktionaryParser()
    parser.set_default_language("french")
    data = parser.fetch(mot)
    
    if data:
        # Parcourir les entrées et leurs définitions
        for entry in data:
            for definition in entry.get("definitions", []):
                pos = definition.get("partOfSpeech", "").lower()
                # Vérifie selon la valeur renvoyée par WiktionaryParser
                if pos in ["nom", "noun"]:
                    return "Nom commun"
                elif pos in ["verbe", "verb"]:
                    return "Verbe à l'infinitif"
        return "Catégorie non déterminée"
    else:
        return "Aucune donnée trouvée pour ce mot"

# Exemple d'utilisation
mot = "chat"
categorie = verifier_categorie(mot)
print(f"Le mot '{mot}' est un {categorie}.")

