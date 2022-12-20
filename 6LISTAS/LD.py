#Leer 10 números enteros, gaurdarlos en una lista. Debemos mostrarlos en el siguiente orden:
#el primero, el último, el segundo, el penúltimo, el tercero, el ante-penúltimo, etc.

from random import randint
lista=[]

for i in range(10):
	lista.append(randint(1,10))
print(lista)
for i in range(5):
	print(lista[i],end='  ')
	print(lista[-1-i],end='  ')