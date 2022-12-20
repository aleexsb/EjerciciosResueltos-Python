from random import randint
cantCeros = 0
sumaPos = 0
cantPos = 0
sumaNeg = 0
cantNeg = 0
for i in range(10):
	numIngresado = randint(-5,5)#int(input('Ingrese un número: '))
	print('Ingrese un número: '+str(numIngresado))
	if numIngresado == 0:
		cantCeros += 1 # cantCeros = cantCeros + 1
	elif numIngresado > 0:
		cantPos += 1
		sumaPos += numIngresado
	else:
		cantNeg += 1
		sumaNeg += numIngresado
    
if cantPos > 0:
	promPos = sumaPos / cantPos
else:
	promPos = 0

if cantNeg > 0:
	promNeg = sumaNeg / cantNeg
else:
	promNeg = 0
  
print('Promedio de positivos: '+str(round(promPos,3)))
print('Promedio de negativos: '+str(round(promNeg,3)))
print('Cantidad de ceros: '+str(cantCeros))
