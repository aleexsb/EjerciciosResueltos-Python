#PEDIR 10 NUMEROS, HASTA QUE SE INGRESE UNO NEGATIVO Y MOSTRAR LA SUMA DE TODOS LOS INGRESADOS, RESTANDO TAMBIEN EL NEGATIVO

sumanum=0

while True:
  num=int(input('Escriba un numero: '))
  if num >=0:
    sumanum=sumanum+num
    
  else:
    if num <0:
      sumanum=sumanum+num  
      break
      
print('La suma total es ' + str (sumanum))

