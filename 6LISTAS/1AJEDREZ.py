'''
Crear un programa que genere tableros de ajedrez aleatorios como se ve en la imagen de ejemplo.

 a) Un tablero de ajedrez debe tener en cada equipo (blancas y negras): 

     Entre 0 y 8 Peones
     Entre 0 y 2 Caballos
     Entre 0 y 2 Alfiles
     Entre 0 y 2 Torres
     Entre 0 y 1 Reina
     1 Rey

b) El programa debe poder calcular el puntaje de cada jugador dependiendo de qué piezas poseen en el tablero: 

     Peones valen 1 punto
     Caballos valen 3 puntos 
     Alfiles valen 3 puntos 
     Torres valen 5 puntos 
     Reinas valen 9 puntos 
     Reyes valen 4 puntos

c) El programa debe poder reconocer cuando un Rey está en jaque. Como no todo el mundo conoce las reglas de Ajedrez, en este ejercicio diremos que el Rey está en jaque cuando 2 piezas del otro equipo se encuentran adyacentes al Rey.

'''

from random import randint

from random import sample

peones_n=0
caballos_n=0
alfiles_n=0
torres_n=0
reinas_n=0
reyes_n=0

peones_b=0
caballos_b=0
alfiles_b=0
torres_b=0
reinas_b=0
reyes_b=0

tablero=[' ',' ',' ',' ',' ',' ',' ',' ',
        ' ',' ',' ',' ',' ',' ',' ',' ',
        ' ',' ',' ',' ',' ',' ',' ',' ',
        ' ',' ',' ',' ',' ',' ',' ',' ',
        ' ',' ',' ',' ',' ',' ',' ',' ',
        ' ',' ',' ',' ',' ',' ',' ',' ',
        ' ',' ',' ',' ',' ',' ',' ',' ',
        ' ',' ',' ',' ',' ',' ',' ',' ']

piezas=['tN','cN','aN','reinaN','aN','cN','tN','pN','pN','pN','pN','pN','pN','pN','pN',
        'tB','cB','aB','reinaB','aB','cB','tB','pB','pB','pB','pB','pB','pB','pB','pB'] 

print('Comienza el juego del ajedrez!')
print('Se generara un tablero aleatorio y el jugador con mas puntos, ganara la partida!')

azar_piezas = randint(0,29) 

azar_rey=randint(0,63)
azar_rey2=randint(0,63)

for i in range(1):
    tablero[azar_rey]='rN'
    reyes_n+=4
    tablero[azar_rey2]='rB'
    reyes_b+=4

fichas_opcion = sample(piezas, azar_piezas)

for piezas in fichas_opcion:
    while True:
        total_tablero = randint(0,63)
        if tablero[total_tablero] == ' ':
            tablero[total_tablero]=piezas
        if piezas=='tN':
            torres_n+=5
        elif piezas=='cN':
            caballos_n+=3
        elif piezas=='aN':
            alfiles_n+=3
        elif piezas=='reinaN':
            reinas_n+=9
        elif piezas=='pN':
            peones_n+=1    
            
        if piezas=='tB':
            torres_b+=5
        elif piezas=='cB':
            caballos_b+=3
        elif piezas=='aB':
            alfiles_b+=3
        elif piezas=='reinaB':
            reinas_b+=9
        elif piezas=='pB':
            peones_b+=1  
        break

print(tablero)

piezas_b=['tB','cB','aB','reinaB','pB','rB']
jaque_b=0

if (azar_rey>8 and azar_rey<15) or (azar_rey>16 and azar_rey<23) or (azar_rey>24 and azar_rey<31) or (azar_rey>32 and azar_rey<39) or (azar_rey>40 and azar_rey<47) or (azar_rey>48 and azar_rey<55) :
    for i in range(6):
        if tablero[azar_rey+1]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+7]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+8]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+9]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-1]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-7]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-8]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-9]==piezas_b[i]:
            jaque_b+=1 

elif azar_rey==8 or azar_rey==16 or azar_rey==24 or azar_rey==32 or azar_rey==40 or azar_rey==48:
    for i in range(6):
        if tablero[azar_rey+1]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+8]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+9]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-7]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-8]==piezas_b[i]:
            jaque_b+=1 

elif azar_rey==7:
    for i in range(6):
        if tablero[azar_rey+7]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+8]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-1]==piezas_b[i]:
            jaque_b+=1
         
elif azar_rey>=1 and azar_rey<7: 
    for i in range(6):
        if tablero[azar_rey+1]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+7]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+8]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+9]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-1]==piezas_b[i]:
            jaque_b+=1
            
elif azar_rey==0:
    for i in range(6):
        if tablero[azar_rey+1]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+8]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+9]==piezas_b[i]:
            jaque_b+=1

elif (azar_rey==55) or (azar_rey==47) or (azar_rey==39) or (azar_rey==31) or (azar_rey==23) or (azar_rey==15): 
    for i in range(6):
        if tablero[azar_rey+7]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey+8]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-1]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-8]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-9]==piezas_b[i]:
            jaque_b+=1 

elif azar_rey==56:
    for i in range(6):
        if tablero[azar_rey+1]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-7]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-8]==piezas_b[i]:
            jaque_b+=1

elif azar_rey>=57 and azar_rey<=62: 
    for i in range(6):
        if tablero[azar_rey+1]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-1]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-7]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-8]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-9]==piezas_b[i]:
            jaque_b+=1 

elif azar_rey==63:
    for i in range(6):
        if tablero[azar_rey-1]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-8]==piezas_b[i]:
            jaque_b+=1
        if tablero[azar_rey-9]==piezas_b[i]:
            jaque_b+=1 

if jaque_b>=2:
    print('El Rey Negro esta en JAQUE!')

piezas_n=['tN','cN','aN','reinaN','pN','rN']
jaque_n=0

if (azar_rey2>8 and azar_rey2<15) or (azar_rey2>16 and azar_rey2<23) or (azar_rey2>24 and azar_rey2<31) or (azar_rey2>32 and azar_rey2<39) or (azar_rey2>40 and azar_rey2<47) or (azar_rey2>48 and azar_rey2<55):
    for i in range(6):
        if tablero[azar_rey2+1]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+7]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+8]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+9]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-1]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-7]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-8]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-9]==piezas_n[i]:
            jaque_n+=1 

elif azar_rey2==8 or azar_rey2==16 or azar_rey2==24 or azar_rey2==32 or azar_rey2==40 or azar_rey2==48:
    for i in range(6):
        if tablero[azar_rey2+1]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+8]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+9]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-7]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-8]==piezas_n[i]:
            jaque_n+=1 

elif azar_rey2==7:
    for i in range(6):
        if tablero[azar_rey2+7]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+8]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-1]==piezas_n[i]:
            jaque_n+=1
            
elif azar_rey2>=1 and azar_rey2<7:
    for i in range(6):
        if tablero[azar_rey2+1]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+7]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+8]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+9]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-1]==piezas_n[i]:
            jaque_n+=1
            
elif azar_rey2==0:
    for i in range(6):
        if tablero[azar_rey2+1]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+8]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+9]==piezas_n[i]:
            jaque_n+=1

elif (azar_rey2==55) or (azar_rey2==47) or (azar_rey2==39) or (azar_rey2==31) or (azar_rey2==23) or (azar_rey2==15):
    for i in range(6):
        if tablero[azar_rey2+7]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2+8]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-1]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-8]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-9]==piezas_n[i]:
            jaque_n+=1 

elif azar_rey2==56:
    for i in range(6):
        if tablero[azar_rey2+1]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-7]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-8]==piezas_n[i]:
            jaque_n+=1

elif azar_rey2>=57 and azar_rey2<=62:
    for i in range(6):
        if tablero[azar_rey2+1]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-1]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-7]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-8]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-9]==piezas_n[i]:
            jaque_n+=1 

elif azar_rey2==63:
    for i in range(6):
        if tablero[azar_rey2-1]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-8]==piezas_n[i]:
            jaque_n+=1
        if tablero[azar_rey2-9]==piezas_n[i]:
            jaque_n+=1 

if jaque_n>=2:
    print('El Rey Blanco esta en JAQUE!')

total_negro=peones_n+caballos_n+alfiles_n+torres_n+reinas_n+reyes_n
total_blanco=peones_b+caballos_b+alfiles_b+torres_b+reinas_b+reyes_b

print('Puntos fichas negras= ' +str(total_negro))
print('Puntos fichas blancas= ' +str(total_blanco))

if total_negro>total_blanco:
    print('Felicidades gano el jugador con fichas NEGRAS!')
elif total_negro<total_blanco:
    print('Felicidades gano el jugador con fichas BLANCAS!')
else:
    print('EMPATE!')

