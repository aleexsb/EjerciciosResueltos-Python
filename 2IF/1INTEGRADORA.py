'''
Programar un juego para adivinar un número entre 1 y 10:

El jugador tiene 3 intentos para adivinar.
Luego de cada intento se dará una pista del estilo "el número es más bajo" o "más alto"
Para generar un número aleatorio pueden utilizar el siguiente código:
'''

import random
numAleatorio = random.randint(1,10)

print('Adivine el numero del 1 al 10')
numero=int(input ())

if numero==numAleatorio:
  print('Ganaste!')
else:
  if numero < numAleatorio:
    print('Mas alto') 

  if numero > numAleatorio:
    print ('Mas bajo')

  print('Te quedan 2 oportunidades')
  numero=int(input ())

  if numero==numAleatorio:
    print('Ganaste!')
  else:
    if numero < numAleatorio:
      print('Mas alto') 
  
    if numero > numAleatorio:
      print ('Mas bajo')
  
    print('Te queda 1 oportunidad')
    numero=int(input ())
  
    if numero==numAleatorio:
      print('Ganaste!')
    else:
      if numero < numAleatorio:
        print('Perdiste!, el numero es ' + str(numAleatorio)) 
    
      if numero > numAleatorio:
        print('Perdiste!, el numero es ' + str(numAleatorio)) 
