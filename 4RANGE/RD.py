
#PEDIR UN NUMERO Y MOSTRAR SU FACTORIAL
#EJ. 5 = 1*2*3*4*5 = 120

factorial=1

print('Escriba un numero')
num=int (input())


for i in range(1,num+1,):

  factorial=factorial*i #AL PONER LA PALABRA FACTORIAL EL RESULTADO SE VA ACTUALIZANDO

  print(factorial)

print('El factorial es ' + str(factorial))

'''
1*1=1
1*2=2
2*3=6
6*4=24


1*1 1*1
1*2 2*2
1*3 3*6
1*4 4*24



'''