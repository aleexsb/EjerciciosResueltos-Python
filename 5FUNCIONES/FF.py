#ESCRIBIR UN NUMERO Y QUE EL PROGRAMA RESPONDA SI ES PAR O NO

def esPar(numero):
  if numero % 2 == 0:
    return True
  else:
    return False

numero = int(input('Ingrese un numero: '))
if esPar(numero):
    print('Es par')
else:
    print('Es impar')