'''
Escribir un programa que implemente una agenda. 
En la agenda se podrán guardar nombres y números de teléfono. 
El programa nos dará el siguiente menú:
Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. 
Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
Listar: Nos muestra todos los contactos de la agenda.
Implementar el programa con un diccionario

'''

agenda={}

def limpiarPantalla():
	print("\033c", end="")

def añadir():
    nombre=input('Escriba el nombre que desea AÑADIR: ')
    telefono=input('Escriba el telefono del contacto: ')
    agenda[nombre]=telefono
    print('Contacto añadido!'.center(40,'*')+'\n\n')

def modificar():
    modificar=input('Escriba el contacto que desea MODIFICAR: ')
    if modificar in agenda.keys():
        agenda[modificar]=input('Escriba el nuevo numero:')
        print('Contacto modificado!')
    else:
        print('Contacto inexistente!'.center(40,'*')+'\n\n')

def buscar():
    buscar=input('Escriba el contacto que desea BUSCAR: ')
    for busqueda in agenda.keys():
        if busqueda.startswith(buscar):
            print(f'Nombre: {busqueda} / Telefono: {agenda[busqueda]}'+'\n\n')
        else:
            print('Contacto inexistente!'.center(40,'*')+'\n\n')
            
def borrar():
    borrar=input('Escriba el contacto que desea BORRAR: ')
    if borrar in agenda.keys():
        del agenda[borrar]
        print('Contacto Borrado!'.center(40,'*')+'\n\n')

def listar():
    print(f'{agenda}')
    print('Lista de contactos!'.center(40,'*')+'\n\n')

def principal():
    opcion='0'
    while opcion!='6':
        print('AGENDA'.center(40,'='))
        print('1.Añadir')
        print('2.Modificar nombre')
        print('3. Buscar nombre')
        print('4. Borrar nombre')
        print('5. Listar')
        print('6. Finalizar')
        print('2022'.center(40,'='))
        opcion=input()
        limpiarPantalla()
        if opcion=='1':
            añadir()
        elif opcion=='2':
            modificar()
        elif opcion=='3':
            buscar()
        elif opcion=='4':
            borrar()
        elif opcion=='5':
            listar()
    print('Fin del programa')


principal()


#OTRA MANERA DE HACERLO CON WHILE

agenda = {}
while True:
    print("\n")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    
    opcion = int(input("Dime opción:"))
    if opcion == 1:
        nombre = input("Nombre del contacto:")    
        if nombre in agenda:
            print("%s ya existe su número de teléfono es %s" % (nombre,agenda[nombre]))
            opcion = input("Pulsa 's' si quieres modificarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                numero = input("Dame el nuevo número de teléfono:")
                agenda[nombre]=numero
        else:
            numero = input("Dame el número de teléfono:")
            agenda[nombre]=numero
    elif opcion == 2:
        cadena = input("Nombre del contacto a buscar:")    
        for nombre, numero in agenda.items():
            if nombre.startswith(cadena):
                print("El número de teléfono de %s es el %s" % (nombre,agenda[nombre]))
    elif opcion == 3:
        nombre = input("Nombre del contacto para borrar:")    
        if nombre in agenda:
            opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                del agenda[nombre]
        else:
            print("No existe el contacto")
    elif opcion == 4:
        for nombre, numero in agenda.items():
            print(nombre,"->",numero)
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")