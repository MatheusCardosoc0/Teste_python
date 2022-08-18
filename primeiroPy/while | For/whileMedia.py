inicial = 0
soma = 0
while(inicial <= 4):
  valor = float(input('Digite a nota da matéria: '))
  inicial = inicial + 1
  soma = soma + valor
print('Sua media é {}'.format(soma / 5))

