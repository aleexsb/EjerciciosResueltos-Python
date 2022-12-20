# Escribir un programa que contenga en un diccionario los precios de una verdulería. El programa pedirá el nombre de la verdura y la cantidad que se ha vendido y nos mostrará el precio final de la venta a partir de los datos guardados en el diccionario. Si la verdura no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

verdu = {'tomate':150,'pepino':100,'limon':250, 'pera': 180, 'naranja':120}

while True:
	nombreVerd = input('Ingrese la verdura: ')
	cantVend = int(input('Ingrese cantidad vendida(grs): '))
	try: 
		precioFinal = cantVend * verdu[nombreVerd]
		print('Precio Final: '+str(precioFinal))
	except:
		print('No vendemos esa verdura.')
	opcion = input('Desea hacer otra consulta? (s)i o (n)o: ')
	if opcion == 'n':
		print('Hasta luego 👋')
		break
		
#OTRA MANERA

verdu={'ajo':200, 'kaki':120}

while True:
    nombre=input('Escriba una verdura: ')
    while nombre not in verdu:
        nombre=input('Escriba un producto que exista: ')
    kilos=int(input('Cuantos kilos desea comprar ? '))
    precio=kilos*verdu[nombre]
    print(f'el precio total es {precio} ')
    opcion=input('Desea continuar? si o no? ').lower()
    if opcion=='si':
        continue
    else:
        break
print('Hasta luego!')