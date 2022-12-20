#ESCRIBIR UN PROGRAMA QUE SE PUEDA ABRIR UN ARCHIVO DE TEXTO Y MOSTRARLO

#SPAM.TXT

import os

if os.path.exists('./spam.txt'):
    spamFile=open('./spam.txt','r')
    spamContenido=spamFile.readlines() 
    #.readlines tranforma la cadena en una lista, sino dejar .read
    spamFile.close()
    print(spamContenido[0]) #-->AL SER UNA LISTA MUESTRA SOLO LA LINEA 1
else:
    print('No encontre el archivo')

#print(os.getcwd()) -->FUNCION PARA VER EL DIRECTORIO DE TRABAJO


#MOSTRAR LA CANTIDAD TOTAL DE LINEAS DEL TXT

print(len(spamContenido))

#USANDO CONTADOR

linea=0
for renglones in spamContenido:
    linea+=1
print(linea)





