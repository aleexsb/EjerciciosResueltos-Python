#LEER 12 NUMEROS PARA 2 LISTAS Y MEZCLARLAS EN UNA TERCERA LISTA DE FORMA: 3 DE LA LISTA 1, 3 DE LA LISTA 2 Y ASI..

from random import randint

lista_a=[]
lista_b=[]
lista_c=[]

for i in range(12):
    lista_a.append(randint(1,10))
    lista_b.append(randint(1,10))

print('La lista A contiene :' + str(lista_a))
print('La lista B contiene :' + str(lista_b))

'''
for i in range(0,12,3):
    lista_c.append(lista_a[i])
    lista_c.append(lista_a[i+1])
    lista_c.append(lista_a[i+2])
'''
for i in range(0,12,3):
    for j in range(3):  
      lista_c.append(lista_a[i+j])
    for j in range(3):
      lista_c.append(lista_b[i+j])


print('lista C='+ str(lista_c))