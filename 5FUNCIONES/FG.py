#Ejercicio8.Definir una función que devuelva si un número es primo o no. 
#Numeros primos son aquellos con solo 2 divisores, 1 y el mismo número.
#7 es primo porque solo es divisible por 1 y 7.
#2,3,4,5,6
# 7 % 2 != 0
# 7 % 3 != 0
# 7 % 6 != 0
#4
#4 % 2 == 0
def primo(num):
  numprimo = 0
  for i in range(1,num+1):
    if num%i==0:
      numprimo+=1      
  if numprimo ==2:
    return 'Es primo'
  else:
    return 'No es primo'

num=int(input('Escriba un numero: '))
print (primo(num))