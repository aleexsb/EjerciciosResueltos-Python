#PEDIR UN NUMERO HASTA QUE SE INGRESE UN 0, MOSTRAR LA SUMA DE LOS NUMEROS INGRESADOS

total=0

while True:
  num=int(input('Ingrese un numero: '))
  if num == 0:
    break
  else:
        total=num+total

print ('La suma total de todos los numeros ingresados es igual a ' + str(total)) 
