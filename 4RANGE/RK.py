#PEDIR 10 NUMEROS Y MOSTRAR AL FINAL SI SE HA INTRODUCIDO ALGUNO NEGATIVO

from random import randint 

negativos=False

for i in range(1,11):
  num=randint(-5,5)
  print('Escriba un numero: ' + str(num))
  if num < 0:
    negativos=True

if negativos:
  print('Hay negativos')
else:
  print('No hay negativos')