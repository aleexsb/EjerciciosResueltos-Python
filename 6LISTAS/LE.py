#Leer por teclado 2 listas(ListaA y ListaB) de 10 números enteros, mezclarlas en una tercera lista(ListaC) de la forma:
#1 de A, 1 de B, 1 de A, 1 de B, y así.

from random import randint
listaA=[]
listaB=[]
listaC=[]

for i in range(10):
	  listaA.append(randint(1,10))
	  listaB.append(randint(1,10))
  
print('La lista A contiene :' + str(listaA))
print('La lista B contiene :' + str(listaB))

for i in range(10):
    listaC.append(listaA[i])
    listaC.append(listaB[i])

print(listaC)

