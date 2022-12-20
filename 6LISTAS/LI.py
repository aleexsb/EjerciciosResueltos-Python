#Crear un programa que lea por teclado una lista de 10 números enteros y la desplace una posición hacia abajo/la derecha, manteniendo la misma cantidad de posiciones: el primero pasa a ser el segundo, el segundo pasa a ser el tercero y así sucesivamente. El último pasa a ser el primero.

#Modulo Time
#Como limpiar la pantalla de REPL
#print("\033c", end="")

import time
from random import randint

lista = []
for i in range(10):
	lista.append(randint(1,10))
while True:
	print(lista)
	lista.insert(0,lista[-1])
	del lista[-1]
	print("\033c", end="") #COMANDO PARA BORRAR PANTALLA REPL
	time.sleep(1) #TIEMPO QUE VA HACIENDO LA TRANSICION ES DE 1 SEGUNDO