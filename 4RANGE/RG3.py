#EJERCICIO SIN IMPORT RANDOM

promedad=0
sumedad=0

sumaestatura=0
promedioest=0

mayores18=0
altos=0
sumaestatura=0


for i in range(5):
  dato1 = int (input('Ingrese la altura: '))
  promedioest+=1
  sumaestatura=sumaestatura+dato1

  if dato1>175:
    altos+=1
            
  dato2 = int (input('Ingrese la edad: '))
  sumedad=sumedad+dato2
  promedad+=1
  if dato2 >18:
    mayores18+=1

print('Promedio de edad = ' + str(sumedad/promedad))
print('Promedio de estatura = ' + str(sumaestatura/promedioest))
print('Alumnos que miden mas de 175 cm = ' + str(altos))
print('Alumnos mayores a 18 años = ' + str(mayores18))