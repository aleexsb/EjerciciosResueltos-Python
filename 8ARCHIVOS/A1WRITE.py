#SI EL ARCHIVO NO EXISTE CON LA w O CON LA a CREA UNO NUEVO.

direcc='./jamon.txt'
jamon_file=open(direcc,'w') 
#--> SI CAMBIAMOS LA w POR LA a AGREGAMOS TODO LO Q QUEREMOS 
texto=input('Escribe cualquier texto: ')
jamon_file.write(texto) #('\n'+texto)
jamon_file.close()