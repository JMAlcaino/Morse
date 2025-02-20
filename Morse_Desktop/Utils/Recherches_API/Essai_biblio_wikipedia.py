import wikipedia
 
wikipedia.set_lang("fr")
 
summary_fr = wikipedia.summary("Ardennes", sentences=10)
my_page = wikipedia.page("Ardennes")
 
print(summary_fr)
print (my_page.url)