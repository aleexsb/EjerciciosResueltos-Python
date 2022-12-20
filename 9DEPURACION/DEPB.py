#Programar o modificar este codigo para simular un par de semaforos de 4 tiempos.

'''

Programar un par de semáforos de 3 tiempos:

calleRivadavia = {'eo': 'rojo'}
calleJujuy = {'ns': 'verde'}
Estas 2 variables son para la intersección de Rivadavia y Jujuy. Para empezar necesitamos una
función cambiarLuces(), que tomará una intersección y cambiará las luces. Y para probar las
aserciones que acabamos de ver pondremos en el código algo que no queremos que ocurra
nunca.
Para este ejercicio pueden utilizar la función time.sleep(t) donde t es el número de segundos
que queremos detener el programa. Tendrán que importar el módulo time para poder usarla
'''
import logging,time
logging.basicConfig(filename='mensajesLog2.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')
#logging.disable(logging.DEBUG)

def cambiarColor(color):#Toggle
	logging.info('Arranca cambiarColor')
	logging.debug(f'Entrada color:{color}')
	if color == 'rojo':
		color = 'rojo/amarillo'
	elif color == 'rojo/amarillo':
		color = 'verde'
	elif color == 'verde':
		color = 'amarillo'
	elif color == 'amarillo':
		color = 'rojo'
	logging.debug(f'Salida color:{color}')
	logging.info('Termina cambiarColor')
	return color

def cambiarLuces(calle1,calle2):
	logging.info('Arranca cambiarLuces')
	logging.debug(f'Entrada calle1: {calle1}')
	logging.debug(f'Entrada calle2: {calle2}')
	if calle2['ns'] == 'verde':
		calle2['ns'] = cambiarColor(calle2['ns'])#pasa a amarillo
		mostrarSemaforo(calle1['eo'],calle2['ns'])
		calle2['ns'] = cambiarColor(calle2['ns'])#pasa a rojo
		mostrarSemaforo(calle1['eo'],calle2['ns'])
		calle1['eo'] = cambiarColor(calle1['eo'])#pasa a rojo/amarillo
		mostrarSemaforo(calle1['eo'],calle2['ns'])
		calle1['eo'] = cambiarColor(calle1['eo'])#pasa a verde
		mostrarSemaforo(calle1['eo'],calle2['ns'])
	elif calle1['eo'] == 'verde':
		calle1['eo'] = cambiarColor(calle1['eo'])#pasa a amarillo
		mostrarSemaforo(calle1['eo'],calle2['ns'])
		time.sleep(1)
		calle1['eo'] = cambiarColor(calle1['eo'])#pasa a rojo
		mostrarSemaforo(calle1['eo'],calle2['ns'])
		time.sleep(1)
		calle2['ns'] = cambiarColor(calle2['ns'])#pasa a rojo/amarillo
		mostrarSemaforo(calle1['eo'],calle2['ns'])
		time.sleep(1)
		calle2['ns'] = cambiarColor(calle2['ns'])#pasa a verde
		mostrarSemaforo(calle1['eo'],calle2['ns'])
	logging.debug(f'Salida calle1: {calle1}')
	logging.debug(f'Salida calle2: {calle2}')
	assert not (calle1['eo'] =='verde' and calle2['ns'] =='verde'),'Error ambos semaforos estan en verde'
	logging.info('Termina cambiarLuces')
	return calle1,calle2

def mostrarSemaforo(colorCalle1,colorCalle2):
	time.sleep(1)
	print("\033c", end="")
	print(f'Semaforo Santa Fe: {colorCalle1}')
	print(f'Semaforo Laprida: {colorCalle2}')	

logging.info('Arranca mi programa')
calleLaprida = {'eo': 'rojo'}
calleSantaFe = {'ns': 'verde'}
logging.debug(f'Calle Rivadavia: {calleLaprida}')
logging.debug(f'Calle Jujuy: {calleSantaFe}')
mostrarSemaforo(calleLaprida['eo'],calleSantaFe['ns'])

while True:
	calleLaprida, calleSantaFe = cambiarLuces(calleLaprida,calleSantaFe)
	logging.debug(f'Calle Rivadavia: {calleLaprida}')
	logging.debug(f'Calle Jujuy: {calleSantaFe}')
	time.sleep(10)
print(calleLaprida)
print(calleSantaFe)

logging.info('Termina mi programa')