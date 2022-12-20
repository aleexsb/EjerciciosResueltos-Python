#PEDIR UN NUMERO Y MOSTRAR SU CUADRADO/ REPETIR ESTO HASTA QUE SE INTRODUCE UN NUMERO NEGATIVO

print('Escriba un numero')
numero=int(input())

while numero >= 0:
  print(numero**2)
  print('Ingrese otro numero')
  numero=int(input())
print('Fin del programa')
