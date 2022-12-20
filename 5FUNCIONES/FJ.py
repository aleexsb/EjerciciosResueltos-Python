#Escriba una función que sume los n primeros números impares y lo devuelva.

#Se introduce 20, entonces:
#Del 1 al 20, sumar los impares y mostrar el resultado.

def impares(num):
  suma=0
  for i in range(1,num,2): 
      suma+=i
  print(suma)

num=int(input('Escriba un numero: '))
impares(num) #PORQUE SI PONGO PRINT SALE NONE
#COMO HAGO PARA QUE SOLO APAREZCA EL RESULTADO FINAL
