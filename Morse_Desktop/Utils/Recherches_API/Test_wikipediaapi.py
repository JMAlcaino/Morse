import wikipediaapi

def obtenir_definition_wikipedia(mot):
    user_agent = "MonProgramme/1.0 (jeanmarcalcaino@gmail.com)"  # Remplace par ton propre email ou identifiant
    wiki_fr = wikipediaapi.Wikipedia(user_agent=user_agent, language="fr")
    
    page = wiki_fr.page(mot)

    if page.exists():
        return page.summary.split("\n")[0]  # Première phrase de la définition
    else:
        return f"Aucune définition trouvée pour {mot}."

mot = "tartiflette"
definition = obtenir_definition_wikipedia(mot)
print(f"Définition de '{mot}' : {definition}")


# Ce script utilise l'API Wikipedia pour obtenir la définition d'un mot en français. Il crée une instance de Wikipedia en français et récupère la page correspondant au mot donné. Ensuite, il extrait la première phrase de la définition de la page et l'affiche à l'utilisateur.
# Il fonctionne très bien pour les mots courants, mais il peut ne pas trouver de définition pour des mots plus rares ou techniques.
# Pour l'utiliser, remplace l'adresse email dans la variable user_agent par ton propre adresse ou identifiant.
# Pour obtenir des définitions en d'autres langues, tu peux changer le paramètre language de l'instance Wikipedia.
# Pour obtenir des définitions plus détaillées, tu peux modifier la façon dont la définition est extraite de la page.
# Pour obtenir des informations supplémentaires sur la page, tu peux explorer les autres méthodes et attributs de l'objet page.

# Voir comment obtenir d'autres informations sur le mot/verbe/nom/adjectif dans la documentation de l'API Wikipedia.
# https://pypi.org/project/Wikipedia-API/

