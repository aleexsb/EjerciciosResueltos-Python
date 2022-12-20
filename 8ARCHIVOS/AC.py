#ESCRIBIR UN PROGRAMA CON LA OPCION PARA LEER Y MOSTRAR LAS PRIMERAS n LINEAS DE UN ARCHIVO 
#Y OTRA OPCION PARA LEER Y MOSTRAR LAS ULTIMAS n LINEAS DE UN ARCHIVO.
#n SE LE PIDE AL USUARIO Y EL ARCHIVO TAMBIEN

import os

lista=os.listdir()  #-->MUESTRA EL DIRECTORIO (ARCHIVOS Y CARPETAS)
print(f'{lista}\n')
      
seleccion=input('Seleccione el archivo con el que desea trabajar: ') 
#QUE CAMBIA QUE NO ESTE .\ ??

if os.path.exists(seleccion):
    File=open(seleccion,'r')
    Contenido=File.readlines() 
    #.readlines tranforma la cadena en una lista, sino dejar .read
    File.close()
    print(f'El archivo posee {len(Contenido)} lineas'.center(40,'*')+'\n')
    primera=int(input('Elija la primera linea que desea leer: '))
    print(Contenido[primera-1]) #-->RESTO 1 PORQUE LA LISTA COMIENZA DESDE EL 0
    ultima=int(input('Elija la ultima linea que desea leer: '))
    print(Contenido[ultima-1])
else:
    print('No encontre el archivo')

print('Fin del programa')

