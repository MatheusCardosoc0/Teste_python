#é uma tupla
mochila = ('pasta de dente', 'garfo', 'chiclete', 'chocolate')

for item in mochila:
  print('{}'.format(item))

print('')

for i in range(1, len(mochila),1):
  print('{}'.format(mochila[i]))

melhoria = ('queijo', 'mangericão', 'alface')
print(mochila + melhoria)