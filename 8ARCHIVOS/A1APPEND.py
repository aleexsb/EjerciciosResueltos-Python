import os

direccion='./spam.txt'
if os.path.exists(direccion):
    spam_file=open(direccion,'a') # LA a NOS DEJA AGREGAR O CREAR
    spam_file.write('\nHola mundo!')
    spam_file.close()

