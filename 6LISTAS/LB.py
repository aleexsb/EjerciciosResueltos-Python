#ORDEN INVERSO

#Soluciona profe

from random import randint
listaA = []
for i in range(5):
	listaA.append(randint(1,10))#int(input('ingresar un numero:'))
print(listaA)
for i in range(4,-1,-1):
	print(listaA[i],end=' ')
print()
for i in range(-1,-6,-1):
	print(listaA[i],end=' ')
print()

------------------
lista=['I','O','E','M']

print(lista[-1],lista[-2],lista[-3],lista[-4])

---------------------------------

numeros=[]
for i in range(5):
  numeros.insert(len(numeros),i)

print(numeros[-1],numeros[-2],numeros[-3],numeros[-4])

----------

numeros=[]
for i in range(5):
  numeros.insert(len(numeros),i)

print(numeros[::-1])

------------

numeros=[]
for i in range(5):
  numeros.insert(len(numeros),i)

numeros.reverse()

print(numeros)

