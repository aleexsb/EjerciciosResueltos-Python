#PEDIR UN NUMERO ENTRE 0 Y 9999 Y DECIR CUANTAS CIFRAS TIENE

print ('escriba un numero entre 0 y 9999')
numero = int (input ())

if numero <= 9:
  print ('tiene una cifra')
else:
    if numero >=10 and numero <=99:
      print ('tiene dos cifras')
    else:
      if numero >=100 and numero <=999:
        print ('tiene tres cifras')
      else:
          if numero >=1000 and numero <=9999:
            print ('tiene cuatro cifras')