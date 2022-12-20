#EJEMPLO G CON RANDOM

from random import randint
suma = 0

while True:
	#num = int(input('Ingrese un numero: '))
	num = randint(-5,5)
	print(num)
	suma = suma + num
	if num == 0:
		break
print('Fin del programa')
print('La suma de los numeros ingresados es: '+str(suma))