#PEDIR 10 NUMEROS. MOSTRAR LA MEDIA DE NUMEROS POSITIVOS, LA MEDIA DE NUMEROS NEGATIVOS Y CUANTOS CEROS
from random import randint

ceros = 0
sumapos=0
sumaneg=0
cantpos=0
cantneg=0

for i in range (10):
  num=randint(-5,5)
  print(num)
  if num==0:
    ceros+=1 #CERO=CERO+1
  
  elif num > 0:
    cantpos +=1
    sumapos=sumapos+num
  
  else:
    cantneg+=1
    sumaneg=sumaneg+num
  
print('Cantidad de ceros ' + str(ceros))
print('Media positivos ' + str(sumapos/cantpos))
print('Media negativos ' + str(sumaneg/cantneg))
