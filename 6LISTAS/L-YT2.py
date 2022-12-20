'''
Manipulacion de una lista:
1. Capturar lista
2. mostrar lista
3. Agregar un elemento a la lista
4. Eliminar un elemento a la lista
5. Modificar un elemento en la lista
6. Salir
'''

def capturar():
  global lista
  lista=[]
  n=int(input('Cuantos elementos tendra la lista? '))
  for i in range(0,n):
    elemento=(input('Ingrese el elemento del indice '+ str(i) + ': '))
    lista.insert(i,elemento)

def mostrar():
  print(lista)

def agregar():
  elemento=(input('Ingrese el elemento del indice: '))
  indice=int(input('Ingrese el indice donde desea agregar'))
  longitud=len(lista)
  longitud=int(longitud)
  if(indice>longitud or indice<0):
    print('El indice debe estar entre el 0 y ' + str(longitud))
  else:
    lista.insert(indice,elemento)
    print('Elemento agregado')

def eliminar():
  indice=int(input('Ingrese el indice del elemento que desea eliminar: '))
  longitud=len(lista)
  longitud=int(longitud)
  if(indice>longitud or indice<0):
    print('El indice debe estar entre el 0 y ' + str(longitud))
  else:
    del lista[indice]
    print('Elemento eliminado')

def modificar():
  indice=int(input('Ingrese el indice del elemento que desea modificar: '))
  elemento=input('Ingrese el nuevo valor del elemento: ')
  longitud=len(lista)
  longitud=int(longitud)
  if(indice>longitud or indice<0):
    print('El indice debe estar entre el 0 y ' + str(longitud))
  else:
    lista[indice]=elemento
    print('Elemento modificado')

def principal():
  opcion='1'
  while(opcion!=6):
    print('1. Capturar lista')
    print('2. mostrar lista')
    print('3. Agregar un elemento a la lista')
    print('4. Eliminar un elemento a la lista')
    print('5. Modificar un elemento en la lista')
    print('6. Salir')
    print('Que deseas hacer?')
    opcion=input()
    if opcion=='1':
      capturar()
    elif opcion=='2':
      mostrar()
    elif opcion=='3':
      agregar()
    elif opcion=='4':
      eliminar()
    elif opcion=='5':
      modificar()
    elif opcion=='6':
      print('Programa terminado!')
    else:
      print('Opcion incorrecta')
  
principal()

'''
capturar()
mostrar()  
agregar()
mostrar()
eliminar()
mostrar()
modificar()
mostrar()
'''