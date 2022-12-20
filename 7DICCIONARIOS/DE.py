# Crear un programa que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guardar la información en un diccionario cuyas claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. 
#El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo.
# Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

dicNotas = {}

cantAlumno = int(input('Ingrese la cantidad de alumnos a registrar:' ))

for i in range(cantAlumno):
	while True:
		nombre = input('Ingrese el nombre del alumno a registrar: ').lower()
		if nombre not in dicNotas.keys():
			break
		print('Ese alumno ya está cargado')  
	dicNotas[nombre] = []
    
	while True:
		nota = int(input('Ingrese las notas de ese alumno (ingrese -1 para finalizar):'))
		if nota >= 0:
			dicNotas[nombre].append(nota)
		else:
			break

dicNotas

for alumno,listaNotas in dicNotas.items():
	print(f'Nombre: {alumno}'.ljust(20,'.'))
	suma = sum(listaNotas)
	if len(listaNotas) > 0:
		promedio = suma / len(listaNotas)
		print(f'Promedio: {promedio}'.ljust(20,'.'))

	

#Otra manera

alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guradar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    alumnos[alumno] = notas.copy()


print(alumnos)
for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))
