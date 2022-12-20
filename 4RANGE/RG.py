#Ejercicio12.Ingresar las alturas y edades de 5 alumnos. Mostrar la edad y estatura promedio, la cantidad de alumnos mayores de 18 años, y la cantidad de alumnos que miden más de 1.75m.

from random import randint

promedad=0
sumedad=0

sumaestatura=0
promedioest=0

mayores18=0
altos=0
sumaestatura=0


for i in range(5):
  dato1 = randint(130,200)
  print('Ingrese la altura: '+str(dato1) + ' cm')
    
  if dato1>175:
    altos+=1
    sumaestatura=sumaestatura+dato1
    promedioest+=1
  else:
    if dato1<175:
      promedioest+=1
      sumaestatura=sumaestatura+dato1
            
  dato2 = randint(15,30)
  print('Ingrese la edad: '+str(dato2) + ' años')
  if dato2 >18:
    mayores18+=1
    sumedad=sumedad+dato2
    promedad+=1
  else:
    if dato2<18:
      promedad+=1
      sumedad=sumedad+dato2

print('Promedio de edad = ' + str(sumedad/promedad))
print('Promedio de estatura = ' + str(sumaestatura/promedioest))
print('Alumnos que miden mas de 175 cm = ' + str(altos))
print('Alumnos mayores a 18 años = ' + str(mayores18))
