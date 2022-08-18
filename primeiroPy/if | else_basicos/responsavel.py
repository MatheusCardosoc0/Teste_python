YourName = input('Qual é seu nome?  ')
print('Seja bem vindo {}'.format(YourName))


idade = 'legal'

YourAge = int(input('Qual sua idade? '))


if(YourAge > 18):
  idade = 'velho'
if(YourAge < 18):
  idade = 'novo'

print('Sua idade +6 é {}, voçê é {}' .format(YourAge + 6, idade))