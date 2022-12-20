#INGRESA UNA HORA, PIDIENDO LA HORA, MINUTO Y SEGUNDO POR SEPARADO Y MOSTRAR LA HORA CON EL SIGUIENTE SEGUNDO

print ('Escriba la hora actual')
print ('Hora')
hora = int(input())
print('Minutos')
minutos=int(input())
print('Segundos')
segundos=int(input())

if (0 <= hora <= 23) and (0 <= minutos <= 59) and (0 <= segundos <= 59):
  print('Hora valida')
  print('La hora ingresada mas 1 segundo es:')

  if (hora<=23) and (minutos<=59) and (segundos<59):
    print(str(hora)+':'+str(minutos)+':'+str(segundos+1))
  
  elif (hora==23) and (minutos==59) and (segundos==59):
    print(str(0)+':'+str(0)+':'+str(0))
  
  elif(hora<23) and (minutos==59) and (segundos ==59):
    print(str(hora+1)+':'+str(0)+':'+str(0))
  
  elif(hora<=23) and (minutos < 59) and (segundos == 59):
    print(str(hora)+':'+str(minutos+1)+':'+str(0))

else:
  print('HORA INVALIDA, PARA QUE EL PROGRAMA RESPONDA, DEBE INGRESAR UNA HORA VALIDA')