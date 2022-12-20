#PEDIR 2 FECHAS, VERIFICAR QUE SEAN VALIDOS, MOSTRAR EL DIA SIGUIENTE DE LA PRIMERA FECHA Y CUANTOS DIAS HAY DE DIFERENCIA ENTRE LAS DOS. CON MESES DE 28, 30 Y 31 DIAS SEGUN CORRESPONDA, SIN AÑOS BISIESTOS

print ('FECHA 1')
print('Escriba el dia')
dia= int(input ())
print('Escriba el mes')
mes= int(input ())
print('Escriba el año')
anio= int(input ())
print ('La fecha ingresada es '+ str (dia)+'/'+ str(mes)+'/'+ str (anio))

if ((dia >= 1 and dia <=31) and ((mes == 1) or (mes == 3) or (mes ==5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes ==12))) or ((dia >= 1 and dia <=30) and ((mes == 4) or (mes == 6) or (mes ==9) or (mes == 11)) and (anio >=1)) or ((dia >=1 and dia <=28) and (mes == 2) and (anio >=1)):
  print ('Fecha valida')

  if (dia!=31) and ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)):
    print ('La fecha de mañana sera ' + str (dia+1) + '/' + str(mes)+ '/' + str(anio))
    
  elif (dia == 31) and (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10):
    print ('La fecha de mañana sera ' + str (1) + '/' + str(mes+1)+ '/' + str(anio))
    
  elif (dia!=30) and (mes == 4) or (mes == 6) or (mes ==9) or (mes == 11):
    print ('La fecha de mañana sera ' + str (dia + 1) + '/' + str(mes)+ '/' + str(anio))
  
  elif (dia == 30) and (mes == 4) or (mes == 6) or (mes ==9) or (mes == 11):
    print ('La fecha de mañana sera ' + str (1) + '/' + str(mes+1)+ '/' + str(anio))
  
  elif (dia!=28) and (mes == 2):
    print ('La fecha de mañana sera ' + str (1) + '/' + str(mes+1 )+ '/' + str(anio))
    
  elif mes != 12:
    print ('La fecha de mañana sera ' + str (1) + '/' + str(mes+1)+ '/' + str(anio))
  
  elif (dia == 31) and (mes == 12):
    print ('La fecha de mañana sera ' + str(1) + '/' + str(1)+ '/' + str(anio+1))
  
  print(' ')
  
  print ('FECHA 2')
  print('Escriba el dia')
  dia2= int(input ())
  print('Escriba el mes')
  mes2= int(input ())
  print('Escriba el año')
  anio2= int(input ())
  
  print ('La fecha ingresada es '+ str (dia2)+'/'+ str(mes2)+'/'+ str (anio2))
  
  if ((dia2 >= 1 and dia2 <=31) and ((mes2 == 1) or (mes2 == 3) or (mes2 ==5) or (mes2 == 7) or (mes2 == 8) or (mes2 == 10) or (mes2 ==12))) or ((dia2 >= 1 and dia2 <=30) and ((mes2 == 4) or (mes2 == 6) or (mes2 ==9) or (mes2 == 11)) and (anio2 >=1)) or ((dia >=1 and dia <=28) and (mes2 == 2) and (anio2 >=1)):
    print ('Fecha valida')
  
    result = (dia2 - dia) + (mes2 - mes)*30 + (anio2 - anio)*365
  
    if result < 0:
  	  result = result * (-1)
  
    print('Eso representa '+str(result)+' dias')
    
  else:
    print('FECHA INVALIDA')
    
else:
  print('FECHA INVALIDA')