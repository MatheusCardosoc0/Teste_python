listaCompras = []
preco = 0

while True:
  print('\nLista de compras\n0-finalizar\n1-brocolis R$6.00\n2-Beterraba 5.70\n3-leite R$1500.00\n4-gás R$200.50\n')
  try:
     x = int(input('Digite qul você quer acrescentar a lista '))
  except:
    print('tente novamente')
    continue
  if(x < 0 or x > 4):
    print('opçao invalida')
    continue
  elif(x == 1):
    listaCompras.append(['brocolis',6.00])
    continue
  elif(x == 2):
    listaCompras.append(['beterraba',5.70])
    continue
  elif(x == 3):
    listaCompras.append(['leite',1500.00])
    continue
  elif(x == 4):
    listaCompras.append(['gás',200.50])
    continue
  else:
    break

for i in listaCompras:
  preco += i[:][1]

print('\nLista:')

for i in listaCompras:
  print(i[:][0])

print('\nValor a ser pago R${}'.format(preco))
  