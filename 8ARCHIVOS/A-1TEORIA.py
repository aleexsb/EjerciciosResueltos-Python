import os
rutaArchivo = os.path.join('.','soneto29.txt')
#Escribimos el archivo
sonetoFile = open(rutaArchivo,'w')
sonetoFile.write('''Cuando siento el rechazo y la obcecación de mi sociedad
y en soledad me duelo de mi posición marginal
y sueño y deseo y sé entonces que el esfuerzo no sirve
y me contemplo y lamento de ser quien soy
deseando tener más fuerza para ser otra
deseando ser mejor compañía para disfrutar de amistad
deseando el talento que no tengo, la libertad que me falta
nada de lo que me ocupaba con contento logra consolarme.
Pero si con estos pensamientos casi de desprecio por mí misma
ocurre por fortuna que pienso en ti, entonces mi tristeza plomada
se alza al alba como en la emoción de un primer vuelo
dejando atrás la tierra oscura, cantando libre en el espacio que acoge
pues pensar en tu amor es conocer tal alegría
que no podría nunca cambiar mi vida por ninguna otra.''')
sonetoFile.close()

sonetoFile = open(rutaArchivo,'a')
for i in range(1,11):
	sonetoFile.write(f'\n{i}')
sonetoFile.write('\n'+input('Texto a añadir: '))
sonetoFile.close()

#Leemos y mostramos el archivo
if os.path.exists(rutaArchivo):
	sonetoFile = open(rutaArchivo)
	sonetoContenido = sonetoFile.readlines()	
	sonetoFile.close()
else:
	print('Archivo no encontrado')
print(sonetoContenido)