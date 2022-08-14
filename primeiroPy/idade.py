nome = input('Digite seu nome ')
if(nome == 'Matheus'):
  print('Pode pasar meu rei!')
else:
  idade = int(input('Digite sua idade '))
  if(idade < 18):
    print('você é de menor')
  elif(idade > 100):
    print('Impossivel!')
  else:
    print('pode passar')