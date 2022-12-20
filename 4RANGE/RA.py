#Ejercicio6.Pedir un número N, y mostrar todos los números del 1 al N.
#Ejemplo:
#5
#Muestra 1,2,3,4,5

num=int(input('Ingrese un numero: '))
print('Tus numeros son:')
for i in range(num):
  print(i+1)

#Otra solucion
num=int(input('Ingrese un numero: '))
print('Tus numeros son:')
for i in range(1,num+1):
  print(i)

#Otra solucion reutilizando la primera variable
#Resuelve: Nicolas Ayala
print('ingrese un Numero')
j=int(input())
for j in range (1,j+1):
	print(j)