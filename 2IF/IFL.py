#PEDIR EL DIA, EL MES Y EL AÑO DE UNA FECHA E INDICAR SI ES VALIDA

print('escriba el dia')
dia= int(input ())

print('escriba el mes')
mes= int(input ())

print('escriba el año')
anio= int(input ())

   
print ('la fecha ingresada es '+ str (dia)+'/'+ str(mes)+'/'+ str (anio))

if (dia >= 1 and dia <=30) and (mes >=1 and mes <=12) and (anio >=1 and anio <=2022):
  print('Fecha valida')
  
else:
 print('Fecha invalida')