#Leer 5 numeros, guardarlos en una lista y a continuación realizar la media de los números positivos, la media de los negativos y la cantidad de ceros, en la lista.

from random import randint

positivos=0
cantpos=0
negativos=0
cantneg=0
ceros=0
lista1=[]

for i in range(5):
  num=randint(-3,3)#int(input('Escriba un numero: '))
  lista1.insert(i,num)
  if num >0:
    positivos+=num
    cantpos+=1
  elif num<0:
    negativos+=num
    cantneg+=1
  elif num==0:
    ceros+=1
print(lista1)

if cantpos>0:
  prompos=positivos/cantpos
  print('media de positivos= ' +str(prompos))
else:
  print('la media de positivos es 0')
  
if cantneg>0:
  promneg=negativos/cantneg
  print('media de negativos= ' + str(promneg))
else:
  print('la media de negativos es 0')
  
print('cantidad de ceros= ' + str(ceros))


