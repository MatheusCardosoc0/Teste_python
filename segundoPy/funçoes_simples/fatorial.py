
fat = 1


def validident(n, min, max):
  x = int(input(n))
  while(x > max or x < min):
     x = int(input(n))
  return x

def fatorial(x):
  global fat
  for i in range(1,x + 1, 1):
    fat *= i
  return fat

x = validident('Digite um número: ',0,1000)
print(fatorial(x))