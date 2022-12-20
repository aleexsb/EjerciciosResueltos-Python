#Ejercicio10. Pedir un número entre 0 y 9999. Y mostrarlo por pantalla al reves.
#1956 -> 6591

print('Ingrese un numero entre 0 y 9999')
num = int(input())
if num < 10 :
	print(num)
elif num < 100:
	decena = num // 10
	unidad = num - decena * 10
	print(str(unidad)+str(decena))
elif num < 1000:
  centena = num // 100
  decena = num // 10
  unidad = num - decena *10
  print(str(unidad)+str(decena-centena*10)+str(centena))
elif num < 10000:
  millar = num // 1000
  centena = num // 100
  decena = num // 10
  unidad = num - decena *10
  print(str(unidad)+str(decena-centena*10)+str(centena-millar*10)+str(millar))