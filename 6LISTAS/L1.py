>>> ['gato','perro','raton','elefante']

>>> spam=['gato','perro','raton','elefante']
>>> [2,4,6,8][1]

>>> spam[3]
'elefante'

'El' + spam[1] + 'se comio al' + spam[0]
'El perro se comio al gato'

spam[0]='cerdo' -->#REEMPLAZA AL GATO

--------------------

spam=['gato','perro','raton']
spam.append('gallo') -->#AGREGA GALLO A LA LISTA, SIEMPRE AL FINAL
>>> spam

#OTRA MANERA
>>> spam.insert(1,'leon')  -->#SE ASIGNA UNA UBICACION Y UN NOMBRE
>>> spam

-----------------------

>>> len(spam)
5  --> #5 ELEMENTOS

---------------------------
>>> huevos=[]
>>> len(huevos)
0

>>> huevos.insert(len(huevos),'hola')

>>> huevos
['hola']

-------------------------

#SLICES

spam = ['gato', 'perro', 'ratón', 'elefante']

print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])


print(spam[:2]) -->#Si no escribimos el primer entero de un rango es lo mismo que escribir 0.
print(spam[1:])
print(spam[:])


spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C'] -->#CONCATENACION
print(spam)