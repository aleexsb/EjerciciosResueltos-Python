def calCilindro(radio,altura,operacion):
    pi = 3.14
    if operacion == 'a':
        area = 2 * pi * radio * altura
        return area
    if operacion == 'v':
        volumen = pi * radio**2 * altura
        return volumen
    print('OPCION INCORRECTA')
    
radCilindro = int(input('Ingrese el radio del cilindro: '))
altCilindro = int(input('Ingrese la altura: '))
opcion = input('Desea calcular el (a)rea o el (v)olumen: ')

resultado = calCilindro(radCilindro,altCilindro,opcion)
print('Resultado: '+str(resultado))