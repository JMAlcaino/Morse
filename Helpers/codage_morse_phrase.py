# Test d'algorythme de lecture d'une lettre, mot ou phrase pour codage en morse

# Morse Code dictonnary definition
morse_code = {
       'a':[1,1,2,2],
       'b':[2,2,1,2],
       'c':[2,1,1,1],
       'd':[2,1,2,1],
       'e':[1],
       'f':[1,1,2,1],
       'g':[2,2,1],
       'h':[1,1,1,1],
       'i':[1,1],
       'j':[1,2,2,2],
       'k':[2,1,2],
       'l':[1,2,1,1],
       'm':[2,2],
       'n':[2,1],
       'o':[2,2,2],
       'p':[1,2,2,1],
       'q':[2,2,1,2],
       'r':[1,2,1],
       's':[1,1,1],
       't':[2],
       'u':[1,1,2],
       'v':[1,1,1,2],
       'w':[1,2,2],
       'x':[2,1,1,2],
       'y':[2,1,2,2],
       'z':[2,2,1,1],
       '0':[2,2,2,2,2],
       '1':[1,2,2,2,2],
       '2':[1,1,2,2,2],
       '3':[1,1,1,2,2],
       '4':[1,1,1,1,2],
       '5':[1,1,1,1,1],
       '6':[2,1,1,1,1],
       '7':[2,2,1,1,1],
       '8':[2,2,2,1,1],
       '9':[2,2,2,2,1],
       '.':[1,2,1,2,1,2],
       ',':[2,2,1,1,2,2],
       '?':[1,1,2,2,1,1],
       "'":[1,2,2,2,2,1],
       '!':[2,1,2,1,2,2],
       '/':[2,1,1,2,1],
       '(':[2,1,1,2,1],
       ')':[2,1,2,2,1,2],
       '&':[1,2,1,1,1],
       ':':[2,2,2,1,1,1],
       ';':[2,1,2,1,2,1],
       '=':[2,1,1,1,2],
       '+':[1,2,1,2,1],
       '-':[2,1,1,1,1,2],
       '_':[1,1,2,2,1,2],
       '"':[1,2,1,1,2,1],
       '$':[1,1,1,2,1,1,2],
       '@':[1,2,2,1,2,1],
       ' ':[1,1,1,1,1,1,1]}

phr=input("entrez un mot ou phrase...")                # entrée de la phrase

# codage
indice=0                                               # indice juste pour voir si on lit bien la bonne lettre
for ltr in phr:                                        # boucle pour chaque lettre 'ltr' dans la phrase 'phr'
    if ltr in morse_code:                              # boucle de recherche du caractère dans le dictionnaire 'morse_code'
        code_list = morse_code.get(ltr)                # récupère la liste qui est en valeur de la clé 'ltr'
    print (ltr,indice,code_list)                       # écrit la lettre 'ltr' son 'indice' dans la phrase 'phr' et la liste associée 'code_list'
    code_list = [1,1,1]                                # pour le temps de pause entre deux lettre en morse --> 0.75" soient 3 '.'  Attention c'est une pause pas des bips (time.sleep)
    print (code_list) 
    indice+=1                                          # pour la boucle des indices
        
    
  
