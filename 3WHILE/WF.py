#PEDIR NUMEROS HASTA QUE SE INGRESE UNO NEGATIVO Y MOSTRAR CUANTOS NUMEROS SE INTRODUJERON

cantnum=0

while True:
  num=int(input('Ingrese un numero: '))
  if num < 0:
    break
  else:
    cantnum=cantnum+1

print('La cantidad de numeros ingresados fue ' + str (cantnum))
  