#PEDIR UN NUMERO Y DECIR SI ES POSITIVO O NEGATIVO. SEGUIR PIDIENDO NUMEROS HASTA QUE SE INTRODUCE UN 0

print('Escriba un numero')
numero=int(input())

while (numero > 0) or (numero < 0):
  if numero >= 0:
    print('Numero positivo')
    print('Ingrese otro numero')  
  else:
    print('Numero negativo')
    print('Ingrese otro numero')  
  numero=int(input())
print('Fin del programa')