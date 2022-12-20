#PEDIR NUMEROS HASTA QUE SE INGRESE UNO NEGATIVO Y MOSTRAR CUANTOS NUMEROS SE INTRODUJERON

cantnum=0

print('escriba un numero')
num=int(input())

while num >=0:
  cantnum=cantnum+1
  num=int(input())

print('La cantidad de numeros ingresados fueron ' + str(cantnum))