#Ejercicio8. Armar un programa que muestre el producto de los primeros 10 números impares.
#Arrancando desde 0.
#Ejemplo:
#1,3,5,7,

producto=1

for i in range(1,10,2):
  print(i*i)
  producto=producto*i #SE LE DICE PRODUCTO A LA MULTIPLICACION DE TODO
print('El producto es ' + str(producto))

#PRODUCTO= 1*3*5*7*9 = 945