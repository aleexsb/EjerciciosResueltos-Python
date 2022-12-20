# Escribir un programa que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.
from random import randint
numIngr = int(input('Ingrese un numero: '))
print(numIngr)
nuevoDic = {}
for i in range(1,numIngr+1):#1,2,3
	nuevoDic[i] = i ** 2
print(nuevoDic)