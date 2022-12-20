'''
spam = {'color': 'rojo', 'edad': 42}

for v in spam.values(): #-->ROJO Y 42
    print(v)

for k in spam.keys(): #-->COLOR Y EDAD
    print(k)

    
for i in spam.items(): #--> 'color': 'rojo', 'edad': 42
    print(i)

spam = {'color': 'rojo', 'edad': 42}
for k, v in spam.items():
    print('Clave: ' + k + ' Valor: ' + str(v))
'''

JOIN CONVIERTE LISTA A CADENA
SPLIT CONVIERTE CADENA A LISTA

nombre='alex'
edad=10
notas=[5,4,7,9]
suma=sum(notas)

print('mi nombre es'.ljust(15,'.')+(f'{nombre}'))