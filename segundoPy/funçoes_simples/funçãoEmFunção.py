def PosiNeg(number, func):
  if (func(number)):
    print(' Esse número serve')
  else:
    print(' Esse número não serve')

def positivo(n):
  return n > 0

def negativo(n):
  return n < 0

PosiNeg(-410, negativo)