print('Calculadora')


n1 = float(input('Escreva um número: '))
n2 = float(input('Escreva um número: '))
operacao = input('Escreva qual operação voçe deseja realizar: ')

if(operacao == 'adição'):
  print(n1 + n2)
elif(operacao == 'divisão'):
  print(n1 / n2)
elif(operacao == 'multiplicaçaõ'):
  print(n1 * n2)
elif(operacao == 'suntração'):
  print(n1 - n2)
else:
  print('Não existe essa operação')