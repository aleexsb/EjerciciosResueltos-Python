#Ta-te-ti con listas.
#Programar un juego de Ta-Te-TI / La vieja:
#El tablero son 9 casilleros en un 3x3.
#Jugador1 y Jugador2 se toman turnos para poner una X o un O, respectivamente.
#Checkear luego de cada turno si hay un ganador.

#JUEGO DE TA TE TI

tablero =['-', '-', '-','-', '-', '-','-', '-', '-']

def limpiarPantalla():
	print("\033c", end="")

def juego():
	ver_tablero()
	print('Arranca el juego del Ta te ti!')
	print('El jugador debe seleccionar la posicion en donde quiera jugar')

def ver_tablero():
	limpiarPantalla()
	#for i in range(0,9,3):
	#	print(tablero[i] + ' | ' + tablero[i+1] + ' | ' +  tablero[i+2] )
	print(tablero[0] + ' | ' + tablero[1] + ' | ' +  tablero[2]  +'\t1 | 2 | 3')
	print(tablero[3] + ' | ' + tablero[4] + ' | ' +  tablero[5]  +'\t4 | 5 | 6')
	print(tablero[6] + ' | ' + tablero[7] + ' | ' +  tablero[8]  +'\t7 | 8 | 9')

def jugador1():
	while True:
		print('Turno del jugador 1 - Elija un numero del 1 al 9 y sera marcado con una X')
		num = int(input()) - 1 
		if num > 8 or num < 0:
			print('Posición invalida')
			continue
		if tablero[num] == '-':
			tablero[num] = 'X'
			break
		else:
			print('Esa posición está ocupada. Elija otra.')
			continue
	ver_tablero()

def jugador2():
	while True:
		print('Turno del jugador 2 - Elija un numero del 1 al 9 y sera marcado con una O')
		num = int(input()) - 1 
		if num > 8 or num < 0:
			print('Posición invalida')
			continue
		if tablero[num] == '-':
			tablero[num] = 'O'
			break
		else:
			print('Esa posición está ocupada. Elija otra.')
			continue
	ver_tablero()

def ganador(turno):
	victoria = False
	for i in range(0,9,3):
		if tablero[i] == tablero[i+1] == tablero[i+2] and tablero[i] != '-':
			victoria = True
	for i in range(0,3,1):
		if tablero[i] == tablero[i+3] == tablero[i+6] and tablero[i] != '-':
			victoria = True
	if tablero[0] ==  tablero[4] == tablero[8] and tablero[0] != '-':
		victoria = True
	elif tablero[2] ==  tablero[4] == tablero[6] and tablero[2] != '-':
		victoria = True
	if victoria:
		if turno % 2 != 0:
			print('Ganó el jugador 1.')
		else:
			print('Ganó el jugador 2.')
		return True
	return False

limpiarPantalla()
juego()

turno = 1
while True:
	jugador1()
	if ganador(turno):
		print('Terminó la partida')
		break
	turno += 1
	if turno == 10:
		print('Empate')
		break
	jugador2()
	if ganador(turno):
		print('Terminó la partida')
		break
	turno += 1

