#PEDIR UN NUMERO N, INTRODUCIR N SUELDOS Y MOSTRAR EL SUELDO MAXIMO

from random import randint

numero=randint(1,10)
print('Escriba un numero: ' + str(numero))

sueldomax=0

for i in range(1,numero+1):
  print('Sueldo ' + str(i))
  sueldo=randint(5000,15000)
  print('Escriba el sueldo: ' + str(sueldo))
  if sueldo > sueldomax:
    sueldomax=sueldo
    
print('Sueldo mas alto = ' + str(sueldomax))
