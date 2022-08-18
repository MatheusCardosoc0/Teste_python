while True:
  try:
    per = int(input('Digite um número '))
    break
  except ValueError:
    print('Ouve um erro')
    continue
print('e')