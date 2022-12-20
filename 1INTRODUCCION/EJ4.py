##INGRESE UN MONTO Y EL PROGRAMA CONVERTIRA EL IMPORTE EN EL DOLAR OFICIAL, DOLAR BLUE Y EURO

print ('ingrese el monto')
monto = float (input ())

dolarOficial= monto/100
dolarBlue= monto/199
euro= monto/220

print ('dolar oficial = ' + str (dolarOficial))
print ('dolar blue = ' + str (round (dolarBlue,2)))
print ('euro = ' + str (round (euro,2)))

monto = (input ()) 

##ROUND SIRVE PARA REDONDEAR DECIMALES

