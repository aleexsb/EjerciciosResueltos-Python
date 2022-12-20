#CON SLICE

from random import randint

lista_a=[]
lista_b=[]
lista_c=[]

for i in range(12):
    lista_a.append(randint(1,10))
    lista_b.append(randint(1,10))

print('La lista A contiene :' + str(lista_a))
print('La lista B contiene :' + str(lista_b))


for i in range(0,12,3):
    lista_c=lista_c+(lista_a[i:i+3])
    lista_c=lista_c+(lista_b[i:i+3])      

print('lista C='+ str(lista_c))