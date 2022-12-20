#INGRESE 6 NOTAS Y MOSTRAR LA CANTIDAD DE APROBADAS(>=4 AL 7), PROMOCIONADOS(>=8) Y REPITENTES(<4)

from random import randint

repitentes=0
aprobados=0
promocionados=0


for i in range(1,7):
  print('Nota ' + str(i))
  nota=randint(1,10)
  print('Escriba la nota: ' + str(nota)) #SIN RANDINT nota=int(input('Escriba la nota: '))
  if 1<=nota<4:
    repitentes +=1
  elif 4<=nota<=7:
    aprobados+=1
  elif nota>=8:
    promocionados+=1
print('Reprobados = ' + str(repitentes))
print('Aprobados = ' + str(aprobados))
print('Promocionados = ' + str(promocionados))