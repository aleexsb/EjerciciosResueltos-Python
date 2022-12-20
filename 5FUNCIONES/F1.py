import random
def divinacion(numRespuesta):
  if numRespuesta == 1:
    return 'Probablemente'
  elif numRespuesta == 2:
    return 'Tal vez'
  elif numRespuesta == 3:
    return 'Si'
  elif numRespuesta == 4:
    return 'Pregunta de nuevo más tarde'
  elif numRespuesta == 5:
    return 'No entendí la pregunta'
  elif numRespuesta == 6:
    return 'No'
  elif numRespuesta == 7:
    return 'Lo dudo mucho'
    
r = random.randint(1, 7)
fortuna = divinacion(r)
print(fortuna)