#DEFINIR UNA FUNCION CON 2 PARAMETROS, QUE SON NUMEROS QUE SE LE PASAN POR ARGUMENTO Y NOS DICEN CUAL ES EL MAS GRANDE

def numeros(num,num2): #PARAMETRO
  num=int(input('Ingrese un num: '))
  num2=int(input('Ingrese otro num: '))
  if num > num2:
    print(num)
  else:
    print(num2)
    
numeros('a', 'b') #ARGUMENTO