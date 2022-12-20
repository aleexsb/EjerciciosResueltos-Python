# Queremos desarrollar una aplicación que nos ayude a gestionar las notas de un centro educativo. Cada grupo (o clase) está compuesto por 5 alumnos. Se pide leer las notas del primer, segundo y tercer trimestre de un grupo. Debemos mostrar al final: la nota media del grupo en cada trimestre, y la media del alumno que se encuentra en la posición N (N se lee por teclado).

from random import randint
PrimerTrimestre = [] 
SegundoTrimestre = []
TercerTrimestre =[]
suma1=0
suma2=0
suma3=0

for i in range(5):
    PrimerTrimestre.append(randint(1,10))
    SegundoTrimestre.append(randint(1,10))
    TercerTrimestre.append(randint(1,10))
print('Primer Trimestre= ' + str(PrimerTrimestre))
print('Segundo Trimestre= ' + str(SegundoTrimestre))
print('Tercer Trimestre= ' + str(TercerTrimestre))

for i in range(5):
    suma1+=PrimerTrimestre[i]
    suma2+=SegundoTrimestre[i]
    suma3+=TercerTrimestre[i]

'''
Otra forma

promedioPrimTrim=(PrimTrim[0]+PrimTrim[1]+PrimTrim[2]+PrimTrim[3]+PrimTrim[4])//5
promedioSegTrim=(SegTrim[0]+SegTrim[1]+SegTrim[2]+SegTrim[3]+SegTrim[4])//5
promedioUltTrim=(UltTrim[0]+UltTrim[1]+UltTrim[2]+UltTrim[3]+UltTrim[4])//5
'''

'''
Otra forma

for i in PrimerTrimestre:
    suma1+=i
for i in SegundoTrimestre:
    suma2+=i
for i in TercerTrimestre:
    suma3+=i
'''

prom_1=suma1/5
prom_2=suma2/5
prom_3=suma3/5

print('El promedio total del primer trimestre es ' + str(prom_1))
print('El promedio total del segundo trimestre es ' + str(prom_2))
print('El promedio total del tercer trimestre es ' + str(prom_3))

alumno = int(input('Para buscar el promedio de un alumno, ingrese su ubicacion: '))
prom_alumno=(PrimerTrimestre[alumno]) + (SegundoTrimestre[alumno]) + (TercerTrimestre[alumno])
prom_alumno/=3

print('El promedio del alumno es ' + str(round(prom_alumno,2)))