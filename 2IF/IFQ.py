#PEDIR UN NUMERO DEL 0 AL 9999 Y DECIR SI ES CAPICUA O NO

print ('Escriba un numero del 0 al 9999')
numero = int(input ())

millar = numero // 1000
centena = numero // 100
decena = numero // 10
unidad = numero - decena * 10

if numero < 1000:
  print ('No es capicua')

else:
  if numero > 1000 and millar == unidad and (centena-millar*10) == (decena-centena*10):
    print ('Es capicua')
  else:
    print ('No es capicua')