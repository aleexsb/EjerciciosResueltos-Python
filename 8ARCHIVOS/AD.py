#Ejercicio5.Escribe un programa que pueda abrir un archivo y:
#a) Contar la cantidad de palabras.
#b) Encontrar la palabra más larga.
#c) Contar la frecuencia de cada palabra.

import os
from pprint import pprint
dicPalabras = {}
ruta = os.path.join('.','soneto29.txt')
if os.path.exists(ruta):
	spamFile = open(ruta)
	spamContenido = spamFile.read()
	spamFile.close()
	#print(spamContenido)
	#print()
	palabrasLista = spamContenido.split()
	cantPalabras = len(palabrasLista)
	maxLetras = 0
	palabraMasLarga = []
	for palabra in palabrasLista:
		letrasPalabra = len(palabra.strip('.').strip(','))
		if letrasPalabra >= maxLetras:
			if letrasPalabra > maxLetras:
				palabraMasLarga = []
			maxLetras = letrasPalabra
			palabraMasLarga.append(palabra.strip('.').strip(','))
		dicPalabras[palabra.strip('.').strip(',').lower()] = dicPalabras.get(palabra.strip('.').strip(',').lower(),0)+1
	print(f'a) El Soneto tiene: {cantPalabras} palabras')
	print(f'b) La palabra más larga es:{palabraMasLarga}')
	print(f'c) Frecuencia de cada palabra:')
	pprint(dicPalabras)
	
else:
	print('Error')