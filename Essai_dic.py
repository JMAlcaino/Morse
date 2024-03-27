
# Morse Code dictonnary definition
morse_code = {'a':[1,1,2,2],
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
       '9':[2,2,2,2,1]}

'''
Dictionnary testing instructions

# Morse Code dictionnary's description with 'for' loops 
print('le dic morse_code contient : ',morse_code)
print()

# Examples with some keys
print ('valeur de a : ', morse_code.get('a'))
print ('valeur de b : ',morse_code.get('b'))
print ('valeur de q : ',morse_code.get('q'))
print ('valeur de 3 : ',morse_code.get('3'))
print()

print('les clés du dic par boucle for : ')
for cle in morse_code.keys():
    print (cle)
print()

print('les valeurs du dic par boucle for :')
for val in morse_code.values():
    print (val)
print()

print ('clés et valeurs du dic en tuples par boucle for : ')
for it in morse_code.items():
    print (it)   
print()

print('clés et valeurs du dic directes par boucle for : ')
for cle, val in morse_code.items():
    print(cle,' --> ',val)
print()

'''

# Value of a letter/number given by the user
print('* Morse coding of a letter/number given by the user \n')
letter = input('letter/number ?..')
if letter in morse_code:
    code_list = morse_code.get(letter)
    print (letter,'-->',code_list)
    for code in code_list:
        print (code, end="  ")
    
else:
    print ('Invalid Input')






