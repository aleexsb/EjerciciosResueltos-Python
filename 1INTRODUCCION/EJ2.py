## INGRESE DOS LADOS DE UN RECTANGULO Y QUE EL PROGRAMA CALCULE EL AREA Y EL PERIMETRO DEL RECTANGULO

print ('escriba un lado del rectangulo')
lado1 = int (input ())

print ('escriba otro lado del rectangulo')
lado2 = int (input ())

area = lado1 * lado2

print ('el area del rectangulo es ' + str (area))

perimetro =lado1*2 + lado2*2

print ('el perimetro del rectangulo es ' + str (perimetro))