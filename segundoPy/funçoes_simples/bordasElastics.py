def border(a):
  print('+','-'* len(a), '+')
  print('|' ,a, '|')
  print('+','-'* len(a), '+')

palavra = input('Digite uma palavra para ser bordeada ')
border(palavra)