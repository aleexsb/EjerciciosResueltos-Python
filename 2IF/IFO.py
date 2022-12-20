#EJERCICIO N RESUELTO DE OTRA MANERA

print ('FECHA 1')
print('Escriba el dia')
dia= int(input ())
print('Escriba el mes')
mes= int(input ())
print('Escriba el año')
anio= int(input ())
print ('La fecha ingresada es '+ str (dia)+'/'+ str(mes)+'/'+ str (anio))
if (1 <= dia <= 30) and (1 <= mes <= 30) and (anio >=1):
    print('Fecha valida')
print(' ')
print ('FECHA 2')
print('Escriba el dia')
dia2= int(input ())
print('Escriba el mes')
mes2= int(input ())
print('Escriba el año')
anio2= int(input ())
print ('La fecha ingresada es '+ str (dia2)+'/'+ str(mes2)+'/'+ str (anio2))
if (dia2 >= 1 and dia2 <=30) and (mes2 >=1 and mes2 <=12) and (anio2 >=1):
    print('Fecha valida')
  
result = (dia2 - dia) + (mes2 - mes)*30 + (anio2 - anio)*360

if result < 0:
	result = result * (-1)
#result = abs(result)
print('Eso representa '+str(result)+' dias')
