#LEER NUMEROS HASTA QUE SE INTRODUZCA UN 0. PARA CADA UNO INDICAR SI ES PAR O IMPAR

print('Escriba un numero')
numero=int(input())
while (numero != 0):
  if (numero%2) == 0:
    print('Numero par')
    print('Ingrese otro numero')
    numero=int(input())

  else:
    print('Numero impar')
    print('Ingrese otro numero')
    numero=int(input())
print('Fin del programa')