#Leer mediante el teclado 8 números. Después se debe pedir un número y una posición, insertarlo en la posición indicada, desplazando  hacia la derecha las posiciones que le siguen.

from random import randint

lista_a=[]

for i in range(8):
  num=randint(10,50)
  lista_a.append(num)

print(lista_a)

deseo=int(input('Cuantos numeros desea agregar? '))

for i in range(deseo):             
  agregar=int(input('Ingrese el numero que desea agregar: '))
  posicion=int(input('Ingrese la posicion donde desea agregar: '))
  lista_a.insert(posicion,agregar)
  print('Tabla actualizada= ' +str(lista_a))

print(lista_a)

