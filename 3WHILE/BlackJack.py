'''
Objetivo del juego: Ganarle al Croupier (la computadora)

Para generar cartas, generar al azar un número entre 1 y 13.

El 1, 11, 12 y 13, valen 10.

Cuando empieza la ronda generar 1 carta para cada jugador.

El croupier debe pedir otra carta si suma 16 o menos.
El croupier debe plantarse si suma 17 o más.

El jugador puede pedir otra carta o plantarse.
Gana el jugador que se acerque más al 21 sin pasarse.

Pierde el jugador que se pase de 21. Si ambos se pasan o llegan al mismo número, hay empate.

'''
from random import randint

pc=0
jugador=0

print('Empieza el juego!')

azarpc=randint(1,13)
azarjugador=randint(1,13)

print('Primera carta generada para el croupier: ' + str(azarpc))
if azarpc >0:
  pc+=azarpc

print('-------')

print('Primera carta generada para el jugador: ' + str(azarjugador))
if azarjugador >0:
  jugador+=azarjugador
  
print('-------')

while True:
  print('El croupier debe solicitar una carta!')
  print('Salio la carta ---> ' + str(azarpc))
  if 2 <= azarpc <=10:
    pc+=azarpc
  else:
    pc+=10  
  if pc <= 16:
    continue
    
  if pc >=17:
    break
    
print('El croupier tiene una suma de ' + str(pc))
if pc ==21:
  print('BLACKJACK!')
if pc>21:
  print('Se ha pasado de 21')

print('-------')

print('Ahora es turno del Jugador!')
print('El Jugador debe solicitar una carta!')
while True:  
  print('Salio la carta ---> ' + str(azarjugador))
  if 2 <= azarjugador <=10:
    jugador+=azarjugador
  else:
    jugador+=10
  print('El jugador tiene una suma de ' + str(jugador))

  if jugador == 21:
    print('BLACKJACK!')
    break
  else:
    if jugador>21:
      print('Se ha pasado de 21')
      break

  print('Si escribe el numero 1, solicita otra carta, si escribe el numero 2, se planta')
  num=int(input())
  if num==1:
    continue
  else:
    if num == 2:
      break
    
if (pc > jugador and pc<=21) or (pc<jugador and jugador >21):
  print('Felicitaciones! Ha ganado el CROUPIER!')
  
elif (pc ==jugador) or (pc > 21 and jugador>21):
  print('Empate!')

else:
  print('Felicitaciones! Ha ganado el JUGADOR!')