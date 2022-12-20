#Leer 10 enteros. Guardar en otra lista los elementos pares de la primera, y a continuación los elementos impares.
#Ejemplo:
#[9, 5, 10, 4, 2, 7, 2, 2, 10, 5]
#[10,4,2,2,2,10,9,5,7,5]

from random import randint
lista=[]
lista2=[]
for i in range(10):
  lista.append(randint(0,15))
for numero in lista:
	if numero % 2 == 0:
		lista2.append(numero)
for numero in lista:
	if not numero % 2 == 0:
		lista2.append(numero)

print(lista)
print(lista2)