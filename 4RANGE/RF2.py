from random import randint
sumaSueldos = 0
masDe60 = 0

for i in range(10):
	#sueldo = int(input('Ingrese un sueldo:'))
	sueldo = randint(50,100)*1000
	print('Ingrese un sueldo: $'+str(sueldo))
	sumaSueldos += sueldo
	if sueldo > 60000:
		masDe60 +=1

print('La suma de los sueldos es: $ '+str(sumaSueldos))
print('Cantidad sueldos mayores de 60mil: '+str(masDe60))
