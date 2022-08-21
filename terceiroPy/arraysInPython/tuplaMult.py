def TuplaMult(*num):
  mult = 1
  for i in num:
    mult *= i
  return mult

print('{}'.format(TuplaMult(8,8)))

x = int(input('Digite um número '))

