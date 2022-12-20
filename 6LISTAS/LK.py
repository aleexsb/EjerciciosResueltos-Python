#Ejercicio11.Leer 10 enteros, guardarlos en una lista. Leer N y buscarlo en la lista. Se debe mostrar la posición en que se encuentra. Si no está, indicarlo con un mensaje.
from random import randint
lista = []
for i in range(10):
	lista.append(randint(1,10))
print(lista)

seIngreso = input('Ingrese un valor a buscar: ')
try:
	seIngreso = int(seIngreso)
except:
	pass

if seIngreso in lista:
	posicion = lista.index(seIngreso)
	print('Está en la posicion: '+str(posicion))
else:
	print('Ese valor no está en la lista')


#Resolviendo para multiples casos del mismo valor

from random import randint
lista = []
for i in range(10):
	lista.append(randint(1,10))
print(lista)

seIngreso = input('Ingrese un valor a buscar: ')
try:
	seIngreso = int(seIngreso)
except:
	pass

if seIngreso not in lista:
	print('No se encontró el valor en la lista.')
else:
	for i in range(len(lista)):#0,1,2,3,4,5,6,7,8,9
		if lista[i] == seIngreso:
			print('Posicion: '+str(i))