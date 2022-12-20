#Ejercicio7. Escribir un programa que lea los datos de un archivo de texto, se llama agenda.txt , que transforme cada línea en un diccionario y los añada a una lista.
#Hacer un menu para borrar un contacto.
#Hacer un menu para agregar contactos.
#Para modificar contactos.

#Ejemplo:
'''
1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
'''
# lista = [{'id':1,'nombre':Carlos,'apellido':Pérez,'nacimiento':'05/01/1989'},{}]

import os
from pprint import pprint
#Mostrar Agenda
def mostrarAgenda(listaContactos):
	contador = 0
	for contacto in listaContactos:
		print(('Entrada: '+str(contador)).center(20,'='))
		contador +=1
		print(f"ID: {contacto['id']}")
		print(f"Nombre: {contacto['nombre']}")
		print(f"Apellido: {contacto['apellido']}")
		print(f"Nacimiento: {contacto['nacimiento']}")
		print('')

listaContactos=[]
#Abrimos el archivo y lo leemos
if os.path.exists('./agenda.txt'):
	agendaFile = open('./agenda.txt')
	agendaContenido = agendaFile.readlines()
	agendaFile.close()
#Descomponemos el contenido en una lista con diccionarios
for linea in agendaContenido:
	valoresLista = linea.split(';')
	dicContacto = {}
	dicContacto['id'] = valoresLista[0]
	dicContacto['nombre'] = valoresLista[1]
	dicContacto['apellido'] = valoresLista[2]
	dicContacto['nacimiento'] = valoresLista[3].strip('\n')
	listaContactos.append(dicContacto)
#Mostrar Agenda
mostrarAgenda(listaContactos)
#Borrar contacto
print(f'Qué entrada vamos a borrar: ')
queContacto = int(input(''))
del listaContactos[queContacto]
print('Se borró el contacto posición:'+str(queContacto))
mostrarAgenda(listaContactos)

#Agregar un contacto
print('Vamos a agregar un contacto. Ingrese los datos')
dicContacto = {}
dicContacto['id'] = input('ID: ')
dicContacto['nombre'] = input('Nombre: ')
dicContacto['apellido'] = input('Apellido: ')
dicContacto['nacimiento'] = input('Nacimiento (formato dd/mm/aaaa): ')
listaContactos.append(dicContacto)
mostrarAgenda(listaContactos)

#Modificando un contacto
print(f'Qué entrada vamos a modificar: ')
queContacto = int(input(''))
listaContactos[queContacto]['nombre'] = input('Nombre: ')
listaContactos[queContacto]['apellido'] = input('Apellido: ')
listaContactos[queContacto]['nacimiento'] = input('Nacimiento (formato dd/mm/aaaa): ')
mostrarAgenda(listaContactos)

#Reconstruimos la cadena original a partir de nuestra lista de contactos.
cadenaSalida = ''
for contacto in listaContactos:
	cadenaSalida += contacto['id'] + ';'
	cadenaSalida += contacto['nombre'] + ';'
	cadenaSalida += contacto['apellido'] +';'
	cadenaSalida += contacto['nacimiento'] +'\n'
cadenaSalida = cadenaSalida.strip('\n')
#Abrimos el archivo nuevamente y escribimos los cambios.
if os.path.exists('./agenda.txt'):
	agendaFile = open('./agenda.txt','w')
	agendaContenido = agendaFile.write(cadenaSalida)
	agendaFile.close()

