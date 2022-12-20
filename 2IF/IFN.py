#Pedir 2 fechas (por separado) y mostrar la cantidad de días que hay de diferencia entre ambas.Suponer meses de 30 dias.

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

if (dia >= 1 and dia <=30) and (mes >=1 and mes <=12) and (anio >=1):
    print('Fecha valida')
  
resultado1 = (dia2 - dia)
resultado2 = (mes2 - mes)
resultado3 = (anio2 - anio)

resultado4 = (dia - dia2)
resultado5 = (mes - mes2)
resultado6 = (anio - anio2)

if (dia2 >= dia) and (mes2 >= mes) and (anio2 >= anio):
  print('Hay ' + str(resultado1) + ' dias,' + ' ' + str(resultado2) + ' meses,' +  ' y ' +str(resultado3) + ' años de diferencia')

elif (dia2 <= dia) and (mes2 <= mes) and (anio2 <= anio):
  print('Hay ' + str(resultado4) + ' dias,' + ' ' + str(resultado5) + ' meses,' +  ' y ' +str(resultado6) + ' años de diferencia')

elif (dia2 >= dia) and (mes2 <= mes) and (anio2 <= anio):
  print('Hay ' + str(resultado1) + ' dias,' + ' ' + str(resultado5) + ' meses,' +  ' y ' +str(resultado6) + ' años de diferencia')

elif (dia2 <= dia) and (mes2 >= mes) and (anio2 >= anio):
  print('Hay ' + str(resultado4) + ' dias,' + ' ' + str(resultado2) + ' meses,' +  ' y ' +str(resultado3) + ' años de diferencia')

elif (dia2 >= dia) and (mes2 <= mes) and (anio2 >= anio):
  print('Hay ' + str(resultado1) + ' dias,' + ' ' + str(resultado5) + ' meses,' +  ' y ' +str(resultado3) + ' años de diferencia')

elif (dia2 <= dia) and (mes2 >= mes) and (anio2 <= anio):
  print('Hay ' + str(resultado4) + ' dias,' + ' ' + str(resultado2) + ' meses,' +  ' y ' +str(resultado6) + ' años de diferencia')

elif (dia2 <= dia) and (mes2 <= mes) and (anio2 >= anio):
  print('Hay ' + str(resultado4) + ' dias,' + ' ' + str(resultado5) + ' meses,' +  ' y ' +str(resultado3) + ' años de diferencia')

elif (dia2 >= dia) and (mes2 >= mes) and (anio2 <= anio):
  print('Hay ' + str(resultado1) + ' dias,' + ' ' + str(resultado2) + ' meses,' +  ' y ' +str(resultado6) + ' años de diferencia')


resultado2 = resultado2*30
resultado3 = resultado3*365
resultado5 = resultado5*30
resultado6 = resultado6*365


if (dia2 >= dia) and (mes2 >= mes) and (anio2 >= anio):
  print('Eso representa ' + str (resultado1 + resultado2 + resultado3) + ' dias')

elif (dia2 <= dia) and (mes2 <= mes) and (anio2 <= anio):
  print('Eso representa ' + str (resultado4 + resultado5 + resultado6) + ' dias')

elif (dia2 >= dia) and (mes2 <= mes) and (anio2 <= anio):
  print('Eso representa ' + str (resultado1 + resultado5 + resultado6) + ' dias')

elif (dia2 <= dia) and (mes2 >= mes) and (anio2 >= anio):
  print('Eso representa ' + str (resultado4 + resultado2 + resultado3) + ' dias')

elif (dia2 >= dia) and (mes2 <= mes) and (anio2 >= anio):
  print('Eso representa ' + str (resultado1 + resultado5 + resultado3) + ' dias')

elif (dia2 <= dia) and (mes2 >= mes) and (anio2 <= anio):
  print('Eso representa ' + str (resultado4 + resultado2 + resultado6) + ' dias')

elif (dia2 <= dia) and (mes2 <= mes) and (anio2 >= anio):
  print('Eso representa ' + str (resultado4 + resultado5 + resultado3) + ' dias')

elif (dia2 >= dia) and (mes2 >= mes) and (anio2 <= anio):
  print('Eso representa ' + str (resultado1 + resultado2 + resultado6) + ' dias')
  