#PEDIR UNA NOTA ENTRE 1 Y 10 Y MOSTRARLA DE MANERA INSUFICIENTE (1 A 3), REGULAR (4 A 5), BIEN (6 A 7), MUY BIEN (7 A 9)Y SOBRESALIENTE (10), SEGUN CORRESPONDA

print ('escriba su nota')
nota = int (input ())

if nota <= 3:
  print ('Insuficiente')

else:
  if 3 < nota < 6:
    print ("Regular")

  else:
    if nota > 5 and nota < 7:
      print ("Bien")

    else:
      if nota > 6 and nota <= 9:
        print ("Muy bien")
      else:
        if nota == 10:
          print ("Sobresaliente")
    


# OTRA SOLUCION --> if 3 < nota <6: EJEMPLO 3 ES MENOR QUE 5 Y 5 ES MENOR QUE 6
                    #print ('regular')