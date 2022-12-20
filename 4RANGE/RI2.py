#SIN RANDOM

sumatotal=0
mayor6000=0
art1=0

for i in range (1,6,1):
  print('Factura ' + str(i))
  print('Escriba el codigo del producto: ')
  cod=int(input())
  print('Cantidad de litros vendidos: ')
  litros=int(input())
  print('Precio x litro: ')
  precio=int(input())

  if cod==123456:
    art1=litros+art1
    
  sumatotal=sumatotal+(precio*litros)

if sumatotal >6000:
  mayor6000+=1

print('Cantidad de litros vendidos del articulo 1 = ' + str(art1))
print(str(mayor6000)+ ' facturas se emitieron x mas de $6000')
print('Facturacion total= ' + '$' + str(sumatotal))
  
