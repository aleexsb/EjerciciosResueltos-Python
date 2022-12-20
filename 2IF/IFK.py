#EJERCICIO J RESUELTO DE OTRA MANERA
#PEDIR UN NUMERO DEL 0 AL 99 Y MOSTRARLO ESCRITO 
#EJ --> 75 -- SETENTA Y CINCO

print('Escriba un numero del 0 al 99')
num= int (input ()) #35

#CASOS PARTICULARES

if num == 0:
  print ('cero')
elif num == 1:
  print('uno')
elif num == 2:
  print ('dos')
elif num == 3:
  print ('tres')
elif num == 4:
  print ('cuatro')
elif num == 5:
  print ('cinco')
elif num == 6:
  print ('seis')
elif num == 7:
  print ('siete')
elif num == 8:
  print ('ocho')
elif num == 9:
  print ('nueve')
elif num == 10:
  print ('diez')
elif num == 11:
  print ('once')
elif num == 12:
  print ('doce')
elif num == 13:
  print ('trece')
elif num == 14:
  print ('catorce')
elif num == 15:
  print ('quince')
elif num == 20:
  print ('veinte')

else:

#CASOS PARA ARMAR
  
  decena = num // 10 #LA DECENA ES EL 3
  unidad = num - decena * 10 # 35 - 3 * 10 == 5

  if decena == 1:
    print('Dieci', end='')
  elif decena == 2:
    print('Veinti', end ='')
  elif decena == 3:
    print ('Treinta', end='')
  elif decena == 4:
    print('Cuarenta', end='')
  elif decena == 5:
    print('Cincuenta', end='')
  elif decena == 6:
    print('Sesenta', end='')
  elif decena == 7:
    print('Setenta', end='')
  elif decena == 8:
    print('Ochenta y ', end ='')
  elif decena == 9:
    print('Noventa y ', end='')
    
    
  if unidad != 0 and decena > 2: #SI HAY UNIDAD, IMPRIME EL Y // NUMEROS ANTES DE 30
    print (' y ', end ='')
  if unidad == 0 and decena == 0:
    print('cero')
  elif unidad == 1:
    print ('uno')
  elif unidad == 2:
    print ('dos')
  elif unidad == 3:
    print ('tres')
  elif unidad == 4:
    print ('cuatro')
  elif unidad == 5:
    print ('cinco')
  elif unidad == 6:
    print ('seis')
  elif unidad == 7:
    print ('siete')
  elif unidad == 8:
    print ('ocho')
  elif unidad == 9:
    print ('nueve')



