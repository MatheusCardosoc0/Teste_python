animais = []
animal = {}

for i in range(3):
  animal['nome'] = input('Nome do animal ')
  animal['reino'] = input('Reino do animal ')
  animais.append(animal.copy())

for x in animais:
  for i,j in x.items():
    print('{} = {}'.format(i,j))