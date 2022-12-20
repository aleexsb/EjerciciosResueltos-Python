#Funciones.
#Definir una función que calcule y muestre por pantalla, el área o el volumen de un cilindro, según se especifique en el parámetro de la misma. Para distinguir entre un caso y otro se le pasará el caracter 'a' (para área) o 'v' (para volumen). Además, hay que pasar el radio y la altura del cilindro.
#Volumen = Pi * Radio^2 * altura
#Area = 2 * Pi * Radio * Altura
#Pi = 3.14

def calCilindro(radio,altura,operacion):
	pi = 3.14
	if operacion == 'a':
		area = 2 * pi * radio * altura
		print('Area: '+str(area))
	if operacion == 'v':
		volumen = pi * radio**2 * altura
		print('Volumen: '+str(volumen))

radCilindro = int(input('Ingrese el radio del cilindro: '))
altCilindro = int(input('Ingrese la altura: '))
opcion = input('Desea calcular el (a)rea o el (v)olumen: ')
calCilindro(radCilindro,altCilindro,opcion)

'''
Si queremos volvor a usar la funcion copiamos y pegamos nuevamente--->
'''

radCilindro = int(input('Ingrese el radio del cilindro: '))
altCilindro = int(input('Ingrese la altura: '))
opcion = input('Desea calcular el (a)rea o el (v)olumen: ')
calCilindro(radCilindro,altCilindro,opcion)