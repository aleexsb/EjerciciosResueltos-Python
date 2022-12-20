#Ejercicio6.
#Escribir un programa que pueda listar todas las carpetas y archivos del cwd por separado.

import os
archivosLista = []
carpetasLista = []

for elemento in os.listdir():
	if os.path.isfile(elemento):
		archivosLista.append(elemento)
	else:
		carpetasLista.append(elemento)
        
print('Archivos: ')
print(archivosLista)
print()
print('Carpetas:')
print(carpetasLista)