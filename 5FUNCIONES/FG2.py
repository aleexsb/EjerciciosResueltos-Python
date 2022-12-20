#SIN EL CONTADOR
def primo(num):
  for i in range(2,num):#2,3,4,5,6
    if num%i==0:
      return 'No es primo'      
  return 'Es primo'

num=int(input('Escriba un numero: '))
print (primo(num))