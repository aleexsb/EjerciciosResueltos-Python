#Ejercicio11. Pedir 10 sueldos. Mostrar su suma y cuantos hay mayores de $60.000 

total=0
mayoresnum=0

from random import randint

for i in range (10):
  num=randint(10000,100000)
  print('Ingrese un sueldo: $ ' + str(num))
  if num>60000:
    mayoresnum+=1
    total=total+num
  else:
    if num <60000:
      total=total+num

print('La suma total es de $ ' + str(total))
print('Hay ' + str(mayoresnum) + ' sueldos mayores a $60.000')
