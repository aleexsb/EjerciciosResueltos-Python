def spam(divisor):
  try:
    return 42/divisor
  except:
    return ('Se trato de dividir por cero')

while True:
  num=int(input('Ingrese un numero: '))
  print(spam(num))
