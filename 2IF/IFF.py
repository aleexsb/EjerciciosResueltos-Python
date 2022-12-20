##ESCRIBA 3 NUMEROS Y QUE EL PROGRAMA LO ORDENE DE MENOR A MAYOR

print ('escriba 3 numeros')
num1= int (input ())
num2= int (input ())
num3= int (input ())

if num1 < num2 and num1 < num3 :
  print (num1) 
  if num2 < num3 :
    print (num2)
    print (num3)
  else:
    print (num3)
    print (num2)

else:
  if num2 < num1 and num2 < num3:
    print (num2)
    if num1 < num3:
      print (num1)
      print (num3)
    else:
      print (num3)
      print (num1)
  else:
      ##if num3 < num2 and num3 < num1:
      print (num3)
      if num2 < num1:
        print (num2)
        print (num1)
      else:
        print (num1)
        print (num2)
