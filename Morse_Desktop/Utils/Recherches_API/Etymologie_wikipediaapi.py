import wikipediaapi

def obtenir_etymologie(mot):
    user_agent = "MonProgramme/1.0 (contact@exemple.com)"
    wiki_fr = wikipediaapi.Wikipedia(user_agent=user_agent, language="fr")
    page = wiki_fr.page(mot)
    print (page)
    
    if not page.exists():
        return f"Aucune page trouvée pour '{mot}'."
    
    # Parcourir les sections pour trouver "Étymologie"
    for section in page.sections:
        if section.title.lower() == "étymologie":
            return section.text
    return f"Aucune étymologie trouvée pour '{mot}'."

mot = "triangle"
etymologie = obtenir_etymologie(mot)
print(f"Étymologie de '{mot}' : {etymologie}")
