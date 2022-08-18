number = int(input('Digite um número inteiro, impar e positivo: '))
while(number < 0 or number % 2 == 0):
  number = int(input('Digite um número inteiro, impar e positivo: '))
print('O número {} serve, Parabens'.format(number))