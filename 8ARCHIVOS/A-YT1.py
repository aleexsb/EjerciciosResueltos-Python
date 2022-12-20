#ARCHIVOS (w a r)

#SI EL ARCHIVO NO EXISTE CON LA w O CON LA a CREA UNO NUEVO.

#EL APPEND CREA Y AGREGA

#EL WRITE CREA O SOBREESCRIBE ARCHIVO .TXT

#EL READ SOLO LEE

#TANTO EL APPEND COMO EL WRITE SE ESCRIBE .WRITE()
#EL READ SE ESCRIBE .READ

#SIEMPRE AL FINAL DE CADA UNO TENE QUE HABER UN .CLOSE()


def crearArchivo():
    archivo=open('agenda.txt','w')
    archivo.close()

crearArchivo()
print('El archivo se ha creado')

-------------------------

def escribir():
    archivo=open('agenda.txt','a')
    cadena=input('Escriba un texto: ')
    archivo.write(cadena+'\n') #GUARDA LA CADENA DENTRO DEL ARCHIVO
    archivo.close
    
escribir()
print('Archivo escrito')

--------------------------

def leer():
    archivo=open('agenda.txt','r')
    linea=archivo.readline()
    while(linea):#UNA VEZ QUEW NO DETECTE MAS TEXTO FINALIZA EL PROGRAMA
        print(linea)
        linea=archivo.readline()
    archivo.close()
leer()
print('Archivo leido')


