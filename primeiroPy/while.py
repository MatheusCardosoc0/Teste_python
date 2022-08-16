print('Números impares')
n1 = float(input('Digite o número inicial:'))
n2 = float(input('Digite o número final: '))

while(n1 < n2):
  if(n1 % 2 != 0):
    print(n1)
  n1 = n1 + 1