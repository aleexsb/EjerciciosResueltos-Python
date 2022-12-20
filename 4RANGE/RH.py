#pide un numero y mostrar la tabla de multiplicar de ese numero

print('Escriba un numero')
num=int(input())

for i in range (1,10+1,1):
  print(str(num) + ' x ' + str(i) + ' = ' + str(i*num))