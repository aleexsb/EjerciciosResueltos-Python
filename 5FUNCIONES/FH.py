#Mostrando todos los primos del 1 al 100


def esPrimo(num):
  for i in range(2,num):
    if num%i==0:
      return False
  return True

for i in range (101):
	if esPrimo(i):
		print(i)



def numeroPrimo(num,n=2):
    if n<=num:
        print(end='')
        return True
    if num % n !=0:
        return numeroPrimo(num, n+1)
    else:
        return False
num=int(input('Ingrese un numero: '))

if numeroPrimo(num):
    print('Es número primo.')
else:
    print('No es número primo.')