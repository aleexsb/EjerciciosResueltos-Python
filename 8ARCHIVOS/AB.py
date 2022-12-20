#ESCRIBIR UN PROGRAMA QUE SE PUEDA AGREGAR TEXTO A UN ARCHIVO Y MOSTRARLO

import os

direccion='./spam.txt'
if os.path.exists(direccion):
    spam_file=open(direccion,'a') # LA a NOS DEJA AGREGAR
    texto=input('Escribe cualquier texto: ')
    spam_file.write('\n'+texto)
    spam_file.close()


#PARA PODER HACER UN PRINT HAY QUE PRIMERO LEERLO
    
if os.path.exists(direccion):
    spam_file=open(direccion,'r')
    spam_contenido=spam_file.read()
    spam_file.close()
    print(spam_contenido)

