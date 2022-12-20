#PEDIR EL DIA, MES, AÑO DE UNA FECHA VALIDA Y MOSTRAR LA FECHA DEL DIA SIGUIENTE. SUPONIENDO MES DE 30 DIAS

print('escriba el dia')
dia= int(input ())
print('escriba el mes')
mes= int(input ())
print('escriba el año')
anio= int(input ())
print ('la fecha ingresada es '+ str (dia)+'/'+ str(mes)+'/'+ str (anio))
if (dia >= 1 and dia <=30) and (mes >=1 and mes <=12) and (anio >=1):
    print('Fecha valida')
    if dia!=30:#Caso cambio solo el dia
        print ('La fecha de mañana sera ' + str (dia + 1) + '/' + str(mes )+ '/' + str(anio))
    elif mes != 12:#(dia >= 30): Caso cambio dia y mes
        print ('La fecha de mañana sera ' + str (1) + '/' + str(mes+1)+ '/' + str(anio))
    else:#Caso cambio dia, mes y año.
        print ('La fecha de mañana sera ' + str(1) + '/' + str(1)+ '/' + str(anio+1))
else:
    print('Fecha invalida')

  

  