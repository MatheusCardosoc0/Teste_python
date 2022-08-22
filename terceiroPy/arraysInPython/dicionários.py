pessoas = {'nome': 'João', 'profissão': 'policial', 'idade' : 30}

print(pessoas)
print(pessoas.values())

for i in pessoas.values():
  print(i)

for i in pessoas.keys():
  print(i)

for i,j in pessoas.items():
  print('{} = {}'.format(i,j))
