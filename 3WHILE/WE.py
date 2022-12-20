while True: #MIENTRAS QUE TODO DE TRUE, VA A SER ACCESO PERMITIDO
    print('Quién eres?')
    nombre=input()
    if nombre!='pepe':
        continue #SI EL NOMBRE ES DIFERENTE A PEPE, CONTINUA DE 0
    print('Hola, Pepe. Cuál es la contraseña?')
    password=input()
    if password!='pez':
        continue
    print('Cuantos años tenes?')
    anios=int (input())
    if anios != 20:
        continue
    print('Cuantos hijos tenes?')
    hijos=int (input())
    if hijos == 2:
        break #SI LOS HIJOS ES IGUAL A 2, SE ROMPE EL BUCLE
    print('Error')
print('Acceso Permitido')