## QUE EL USUARIO INGRESE SU NOMBRE, SU APELLLIDO, SU AÑO DE NACIMIENTO Y QUE EL PROGRAMA LE DE UNA BIENVENIDA Y LE DIGA CUANTOS AÑOS CUMPLIRA

print ('ingrese su nombre')
nombre =input ()

print ('ingrese su apellido')
apellido = input ()

print ('ingrese su año de nacimiento')
nacimiento = int (input ())

edad = (2022- nacimiento)

print ('bienvenido ' + (nombre) + ' ' + apellido)
print ('el año que viene cumpliras ' + str (edad + 1) + ' años')