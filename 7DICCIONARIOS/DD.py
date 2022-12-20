#Ejercicio3.Escribir un programa que lea una cadena y devuelva un diccionario con la cantidad de veces que aparece cada carácter en la cadena.

#Ejemplo
#cadenaEntrada = 'casa'
#diccSalida = {'a':2,'c':1,'s':1}

#Utilizando Try, Except.
cadenaEntrada= input('Ingrese una palabra: ') #'casa'
diccSalida = {}
for caracter in cadenaEntrada:
	try:
		diccSalida[caracter] = diccSalida[caracter] + 1
	except:
		diccSalida[caracter] = 1
print(diccSalida)


#Utilizando operador de Pertenencia
cadenaEntrada= input('Ingrese una palabra: ') #'casa'
diccSalida = {}
for caracter in cadenaEntrada:
	if caracter in diccSalida:#.keys():
		diccSalida[caracter] = diccSalida[caracter] + 1
	else:
		diccSalida[caracter] = 1

print(diccSalida)

