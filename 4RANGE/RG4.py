from random import randint

print('Ingresa la Altura de 5 alumnos:')
sumaAlt=0
sumaEdad=0
alum18=0
alum175=0
for i in range (5):
  alt=randint(150,200)
  print(alt)
  sumaAlt=sumaAlt+alt
  if alt>175:
    alum175+=1
print('Ingresa la Edad de 5 alumnos:')
for i in range (5):
  edad=randint(15,25)
  print(edad)
  sumaEdad=sumaEdad+edad
  if edad>18:
    alum18+=1
print('Media de Altura: ' +str(round(sumaAlt/5,2)))
print('Media de Edad: ' +str(round(sumaEdad/5,2)))
print('Mayores de 1.75(175cm): ' +str(alum175))
print('Mayores de 18 años: ' +str(alum18))