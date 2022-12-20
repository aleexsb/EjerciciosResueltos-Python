#Leer por teclado una serie de 10 números enteros. La aplicación debe indicarnos si los números están ordenados de forma creciente, decreciente, o si están desordenados.

from random import randint
cantNum = 3
lista = []
print('Ingrese '+str(cantNum)+' numeros:')
for i in range(cantNum):
	lista.append(int(input('Ingrese numero:')))
print(lista)
listaMayorMenor = [] + lista
listaMenorMayor = [] + lista

listaMayorMenor.sort(reverse=True)
listaMenorMayor.sort()


#  Otra manera usan booleanos ej. 1.2.3
'''
creciente = True
decreciente = True
for i in range(1,len(lista)):
	if lista[i] > lista[i-1]: SI 1 ES MAYOR A 3, ES DECRECIENTE
		decreciente = False
	if lista[i] < lista[i-1]: SI 1 ES MENOR A 3, ES CRECIENTE
		creciente = False
'''

if lista == listaMayorMenor: #COMPARA LAS 2 LISTAS
	print('El orden es decreciente')
elif lista == listaMenorMayor:
	print('El orden es creciente')
else:
	print('Los numeros estan desordenados')