#LEER 5 NUMEROS, GUARDARLOS EN UNA LISTA Y MOSTRARLOS EN EL MISMO ORDEN INTRODUCIDO


#Soluciona Profe


from random import randint
listaA = []

for i in range(5):
	listaA.append(randint(1,10))#int(input('ingresar un numero:'))
print(listaA)

for elemento in listaA :
	print(elemento, end=' ')


-------------------------


lista=[5,4,3,2,1]

print(numeros)

-----------------

lista=[]
for i in range(5):
  lista.insert(len(lista),i)

print(lista)

------------------------

lista=[]
for i in range(5):
  lista.insert(i,i)

print(lista)


--------------------------

lista=[]
for i in range(5):
  numero=int(input('Ingrese un numero '))
  lista.insert(i,numero)
  
print(lista)