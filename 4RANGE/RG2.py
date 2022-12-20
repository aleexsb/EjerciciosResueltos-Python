from random import randint

cantedad=0
sumedad=0

sumaestatura=0
cantestatura=0

mayores18=0
altos=0

for i in range(5): #ES COMO PONER (0,5,1)
  dato1 = randint(130,200)
  print('Ingrese la altura: '+str(dato1) + ' cm')
  cantestatura+=1
  sumaestatura=sumaestatura+dato1

  if dato1>175:
    altos+=1
            
  dato2 = randint(15,30)
  print('Ingrese la edad: '+str(dato2) + ' años')
  sumedad=sumedad+dato2
  cantedad+=1
  if dato2 >18:
    mayores18+=1

promedad=sumedad/cantedad
promestatura=sumaestatura/cantestatura

print('Promedio de edad = ' + str(promedad))
print('Promedio de estatura = ' + str(promestatura) + ' cm')
print('Alumnos que miden mas de 175 cm = ' + str(altos))
print('Alumnos mayores de 18 años = ' + str(mayores18))