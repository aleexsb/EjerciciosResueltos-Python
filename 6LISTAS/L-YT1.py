#SI HAY IGUAL PARA UNIR 2 PALABRAS HAY QUE USAR STR, SI HAY SOLO PRINT SE PUEDE USAR COMA
#EJ: 
hello='Hola' + str(teclado)

print('Hola', hello)


#A) COMO USAR LA FUNCION LEN

hello='Hola'
print(len(hello)) #--> CANTIDAD DE LETRAS

'-----------'
print('Celular tiene',len('celular'),'caracteres' )

'-----------'
longitud=len('microfono')
print('Microfono tiene ',longitud,' caracteres')

print('-----------')

#LISTAS

numeros=[1,2,3,4,5] 

print(len(numeros)) #--> CANTIDAD DE ELEMENTOS

print(numeros[4])

print(numeros[-1])

print(numeros[0:4]) #-->TODOS LOS ELEMENTOS QUE ESTAN ENTRE EL INDICE 0 Y EL 4 SIN CONTAR EL 4

print(numeros[0:4:2]) #--> CON SALTOS DE 2 EN 2

lista1=[4,5,6]
lista2=[7,8,9]

print(lista1+lista2)

print(len(lista1)) #--> TIENE 3 ELEMENTOS

print(4 in lista1) #--> PREGUNTA SI EL 4 ESTA EN LA LISTA 1
print(85 in lista2)
