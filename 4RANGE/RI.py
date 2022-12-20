#Ejercicio14. Una empresa que se dedica a la venta de desinfectantes necesita un programa para gestionar las facturas.

#En cada factura figura:
#el código del artículo,
#la cantidad vendida en litros
#y el precio por litro. 

#Se pide de 5 facturas introducidas:
#Facturación total,
#cantidad en litros vendidos del artículo 1
#y cuantas facturas se emitieron de más de $6000. 

from random import randint

sumatotal=0
mayor6000=0
art1=0

for i in range (1,6):
	print('Factura ' + str(i))
	print('Escriba el codigo del producto: ',end='')
	cod=randint(1,5)#int(input())
	print(cod)
	print('Cantidad de litros vendidos: ',end='')
	litros=randint(10,50)#int(input())
	print(litros)
	print('Precio x litro: ',end='') 
	precio=randint(5,10) * 100#int(input())
	print(precio)
  
	if cod==1:
		art1=litros+art1
	sumatotal+=(precio*litros)
  
if sumatotal >6000:
	mayor6000+=1

print('Cantidad de litros vendidos del articulo 1 = ' + str(art1))
print('Facturas emitidas x mas de $6000 = ' + str(mayor6000))
print('Facturacion total= ' + '$' + str(sumatotal))