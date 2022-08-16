quant = 0
soma = 0

for i in range(1,31,1):
  if(i % 5 == 0):
    soma += i
    quant += 1
print('A média é {}'.format(soma / quant))