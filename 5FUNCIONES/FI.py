#Ejercicio9.Programar una función que muestre en binario un número entre 0 y 255.

#Por ejemplo:
#Se ingresa el numero 28
#La función devuelve 11100

def enBinario(num):
	binario = ''
	while num >= 1:
		resto = num % 2
		binario =  str(resto) + binario #ACA HACE QUE LO ORDENE AL REVEZ
		num = num // 2 # num//= 2
	return binario

numIng = int(input('Ingrese un numero: '))
resultado = enBinario(numIng)
print('En Binario: '+resultado)


